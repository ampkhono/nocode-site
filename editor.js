// ゲームデータ構造
let gameData = {
    startNode: null,
    questions: [],
    results: []
};

let selectedNodeId = null;
let nodeIdCounter = 0;

// カスタム画像を保存（localStorage）
function saveCustomImage(name, base64Data) {
    try {
        const customImages = JSON.parse(localStorage.getItem('customBackgroundImages') || '{}');
        customImages[name] = base64Data;
        localStorage.setItem('customBackgroundImages', JSON.stringify(customImages));
        return true;
    } catch (e) {
        console.error('画像の保存に失敗しました:', e);
        return false;
    }
}

// カスタム画像を取得
function getCustomImages() {
    try {
        return JSON.parse(localStorage.getItem('customBackgroundImages') || '{}');
    } catch (e) {
        return {};
    }
}

// カスタム画像のオプションを生成
function getCustomImageOptions(currentValue) {
    const customImages = getCustomImages();
    let options = '';
    for (const [name, data] of Object.entries(customImages)) {
        const value = `custom:${name}`;
        options += `<option value="${escapeHtml(value)}" ${currentValue === value ? 'selected' : ''}>${escapeHtml(name)}</option>`;
    }
    return options;
}

// カスタム画像のURLを取得
function getCustomImageUrl(value) {
    if (value && value.startsWith('custom:')) {
        const name = value.substring(7);
        const customImages = getCustomImages();
        return customImages[name] || '';
    }
    return value || '';
}

// 画像ファイルを処理
function handleImageFiles(event, questionId) {
    const files = Array.from(event.target.files);
    if (files.length === 0) return;
    
    files.forEach(file => {
        if (file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const base64Data = e.target.result;
                const fileName = file.name;
                if (saveCustomImage(fileName, base64Data)) {
                    // 選択肢を更新
                    updateBackgroundImageSelect(questionId);
                    // 自動的に選択
                    const select = document.getElementById('backgroundImage');
                    if (select) {
                        select.value = `custom:${fileName}`;
                        updateBackgroundImagePreview(questionId);
                    }
                    alert(`画像「${fileName}」を追加しました！`);
                } else {
                    alert('画像の保存に失敗しました。');
                }
            };
            reader.readAsDataURL(file);
        } else {
            alert(`「${file.name}」は画像ファイルではありません。`);
        }
    });
    
    // 入力値をリセット（同じファイルを再度選択できるように）
    event.target.value = '';
}

// ドラッグ&ドロップで画像を処理
function handleImageDrop(event, questionId) {
    event.preventDefault();
    event.stopPropagation();
    
    const dropZone = event.currentTarget;
    dropZone.style.borderColor = '#cbd5e0';
    dropZone.style.background = 'white';
    
    const files = Array.from(event.dataTransfer.files);
    if (files.length === 0) return;
    
    files.forEach(file => {
        if (file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const base64Data = e.target.result;
                const fileName = file.name;
                if (saveCustomImage(fileName, base64Data)) {
                    // 選択肢を更新
                    updateBackgroundImageSelect(questionId);
                    // 自動的に選択
                    const select = document.getElementById('backgroundImage');
                    if (select) {
                        select.value = `custom:${fileName}`;
                        updateBackgroundImagePreview(questionId);
                    }
                    alert(`画像「${fileName}」を追加しました！`);
                } else {
                    alert('画像の保存に失敗しました。');
                }
            };
            reader.readAsDataURL(file);
        } else {
            alert(`「${file.name}」は画像ファイルではありません。`);
        }
    });
}

// 背景画像の選択肢を更新
function updateBackgroundImageSelect(questionId) {
    const select = document.getElementById('backgroundImage');
    if (!select) return;
    
    const currentValue = select.value || '';
    
    // デフォルトオプションを定義
    const defaultOptions = [
        { value: '', text: '画像を選択...' },
        { value: 'data/game_back_forest.jpg', text: '森の背景' },
        { value: 'data/game_back_mountain.jpg', text: '山の背景' },
        { value: 'data/game_back_space.jpg', text: '宇宙の背景' },
        { value: 'data/game_back_stars.jpg', text: '星空の背景' }
    ];
    
    // 選択肢を再構築
    select.innerHTML = '';
    
    // デフォルトオプションを追加
    defaultOptions.forEach(opt => {
        const option = document.createElement('option');
        option.value = opt.value;
        option.textContent = opt.text;
        if (opt.value === currentValue) option.selected = true;
        select.appendChild(option);
    });
    
    // カスタム画像を追加
    const customImages = getCustomImages();
    for (const [name, data] of Object.entries(customImages)) {
        const value = `custom:${name}`;
        const option = document.createElement('option');
        option.value = value;
        option.textContent = name;
        if (value === currentValue) option.selected = true;
        select.appendChild(option);
    }
}

// ドロップゾーンのクリックでファイル選択
document.addEventListener('DOMContentLoaded', function() {
    // ドロップゾーンのクリックイベントは動的に追加する必要があるため、
    // showQuestionEditor内で設定する
});

// 質問ノードを追加
function addQuestion() {
    const questionId = `q_${nodeIdCounter++}`;
    const question = {
        id: questionId,
        type: 'question',
        title: `質問 ${gameData.questions.length + 1}`,
        text: '',
        questionFont: '',
        choiceFont: '',
        customCSS: '',
        // GUI設定
        backgroundType: 'color', // 'color', 'image', 'gradient'
        backgroundColor: '#ffffff',
        backgroundImage: '',
        gradientColor1: '#667eea',
        gradientColor2: '#764ba2',
        questionFontSize: '1.3em',
        questionTextColor: '#2d3748',
        choiceFontSize: '1.2em',
        choiceButtonColor: '#667eea',
        choiceButtonTextColor: '#ffffff',
        choices: [
            { text: '選択肢1', value: 0, nextId: null },
            { text: '選択肢2', value: 1, nextId: null }
        ]
    };
    
    gameData.questions.push(question);
    
    // 最初の質問の場合はスタートノードに設定
    if (gameData.questions.length === 1 && !gameData.startNode) {
        gameData.startNode = questionId;
    }
    
    updateUI();
    selectNode(questionId);
}

// 結果ノードを追加
function addResult() {
    const resultId = `r_${nodeIdCounter++}`;
    const result = {
        id: resultId,
        type: 'result',
        title: `結果 ${gameData.results.length + 1}`,
        text: '',
        image: '',
        url: '',
        buttonText: ''
    };
    
    gameData.results.push(result);
    updateUI();
    selectNode(resultId);
}

// ノードを選択
function selectNode(nodeId) {
    selectedNodeId = nodeId;
    updateUI();
    showEditor();
    showPreview();
}

// UIを更新
function updateUI() {
    updateNodeList();
    updateEditor();
}

// ノードリストを更新
function updateNodeList() {
    const nodeList = document.getElementById('nodeList');
    nodeList.innerHTML = '';
    
    // スタートノード
    if (gameData.startNode) {
        const startNode = gameData.questions.find(q => q.id === gameData.startNode);
        if (startNode) {
            const node = createListNode(startNode, 'start');
            nodeList.appendChild(node);
        }
    }
    
    // 質問ノード
    gameData.questions.forEach(question => {
        const node = createListNode(question, 'question');
        nodeList.appendChild(node);
    });
    
    // 結果ノード
    gameData.results.forEach(result => {
        const node = createListNode(result, 'result');
        nodeList.appendChild(node);
    });
}

// リスト表示用のノード要素を作成
function createListNode(data, type) {
    const div = document.createElement('div');
    div.className = `node ${selectedNodeId === data.id ? 'selected' : ''}`;
    
    const typeLabels = {
        'start': '🚀 スタート',
        'question': '❓ 質問',
        'result': '✅ 結果'
    };
    
    div.innerHTML = `
        <div class="node-title">${data.title || data.text || '無題'}</div>
        <div class="node-type">${typeLabels[type] || type}</div>
    `;
    
    div.onclick = () => selectNode(data.id);
    
    return div;
}

// エディタを表示
function updateEditor() {
    if (!selectedNodeId) {
        document.getElementById('editorContent').innerHTML = `
            <div class="empty-state">
                <h2>👋 ノードを選択</h2>
                <p style="margin-top: 20px;">左側のノードをクリックして編集してください。</p>
            </div>
        `;
        return;
    }
    
    const question = gameData.questions.find(q => q.id === selectedNodeId);
    const result = gameData.results.find(r => r.id === selectedNodeId);
    
    if (question) {
        showQuestionEditor(question);
    } else if (result) {
        showResultEditor(result);
    }
}

// 質問エディタを表示
function showQuestionEditor(question) {
    const editorContent = document.getElementById('editorContent');
    editorContent.innerHTML = `
        <div class="form-group">
            <label>タイトル</label>
            <input type="text" id="questionTitle" value="${escapeHtml(question.title)}" 
                   onchange="updateQuestionProperty('${question.id}', 'title', this.value)">
        </div>
        
        <div class="form-group">
            <label>質問文</label>
            <textarea id="questionText" 
                      onchange="updateQuestionProperty('${question.id}', 'text', this.value)">${escapeHtml(question.text)}</textarea>
        </div>
        
        <div class="form-group" style="border-top: 2px solid #e2e8f0; padding-top: 20px; margin-top: 20px;">
            <h3 style="color: #2d3748; margin-bottom: 15px;">🎨 デザイン設定</h3>
            
            <div style="background: #f7fafc; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <label style="font-weight: 600; margin-bottom: 10px; display: block;">背景の種類</label>
                <select id="backgroundType" onchange="updateQuestionStyle('${question.id}')" 
                        style="width: 100%; padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px;">
                    <option value="color" ${(question.backgroundType || 'color') === 'color' ? 'selected' : ''}>単色</option>
                    <option value="image" ${question.backgroundType === 'image' ? 'selected' : ''}>画像</option>
                    <option value="gradient" ${question.backgroundType === 'gradient' ? 'selected' : ''}>グラデーション</option>
                </select>
            </div>
            
            <div id="backgroundColorGroup" style="display: ${(question.backgroundType || 'color') === 'color' ? 'block' : 'none'}; margin-bottom: 15px;">
                <label style="font-weight: 600; margin-bottom: 8px; display: block;">背景色</label>
                <div style="display: flex; gap: 10px; align-items: center;">
                    <input type="color" id="backgroundColor" value="${question.backgroundColor || '#ffffff'}" 
                           onchange="document.getElementById('backgroundColorText').value = this.value; updateQuestionStyle('${question.id}')"
                           style="width: 60px; height: 40px; border: 2px solid #e2e8f0; border-radius: 5px; cursor: pointer;">
                    <input type="text" id="backgroundColorText" value="${question.backgroundColor || '#ffffff'}" 
                           onchange="document.getElementById('backgroundColor').value = this.value; updateQuestionStyle('${question.id}')"
                           style="flex: 1; padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px;">
                </div>
            </div>
            
            <div id="backgroundImageGroup" style="display: ${question.backgroundType === 'image' ? 'block' : 'none'}; margin-bottom: 15px;">
                <label style="font-weight: 600; margin-bottom: 8px; display: block;">背景画像</label>
                
                <div style="margin-bottom: 15px; padding: 15px; background: #f7fafc; border-radius: 8px; border: 2px dashed #cbd5e0;">
                    <label style="font-weight: 600; margin-bottom: 10px; display: block; font-size: 0.9em;">📁 画像を追加</label>
                    <div style="display: flex; gap: 10px; margin-bottom: 10px;">
                        <button type="button" onclick="document.getElementById('imageFileInput').click()" 
                                style="flex: 1; padding: 10px; background: #667eea; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: 600;">
                            📂 ファイルを選択
                        </button>
                        <input type="file" id="imageFileInput" accept="image/*" multiple 
                               style="display: none;" onchange="handleImageFiles(event, '${question.id}')">
                    </div>
                    <div id="imageDropZone" 
                         style="padding: 20px; text-align: center; border: 2px dashed #cbd5e0; border-radius: 5px; background: white; cursor: pointer; transition: all 0.3s;"
                         ondrop="handleImageDrop(event, '${question.id}')" 
                         ondragover="event.preventDefault(); event.currentTarget.style.borderColor='#667eea'; event.currentTarget.style.background='#edf2f7';" 
                         ondragleave="event.currentTarget.style.borderColor='#cbd5e0'; event.currentTarget.style.background='white';">
                        <div style="color: #718096; font-size: 0.9em;">
                            🖼️ 画像をここにドラッグ&ドロップ<br>
                            <small>またはクリックしてファイルを選択</small>
                        </div>
                    </div>
                    <small style="color: #718096; display: block; margin-top: 8px;">JPEG、PNG、GIF形式の画像に対応</small>
                </div>
                
                <select id="backgroundImage" onchange="updateBackgroundImagePreview('${question.id}')" 
                        style="width: 100%; padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px; margin-bottom: 10px;">
                    <option value="">画像を選択...</option>
                    <option value="data/game_back_forest.jpg" ${question.backgroundImage === 'data/game_back_forest.jpg' ? 'selected' : ''}>森の背景</option>
                    <option value="data/game_back_mountain.jpg" ${question.backgroundImage === 'data/game_back_mountain.jpg' ? 'selected' : ''}>山の背景</option>
                    <option value="data/game_back_space.jpg" ${question.backgroundImage === 'data/game_back_space.jpg' ? 'selected' : ''}>宇宙の背景</option>
                    <option value="data/game_back_stars.jpg" ${question.backgroundImage === 'data/game_back_stars.jpg' ? 'selected' : ''}>星空の背景</option>
                    ${getCustomImageOptions(question.backgroundImage)}
                </select>
                
                <div id="backgroundImagePreview" style="margin-top: 10px; ${question.backgroundImage ? '' : 'display: none;'}">
                    <label style="font-weight: 600; margin-bottom: 8px; display: block; font-size: 0.9em;">プレビュー:</label>
                    <img id="backgroundImagePreviewImg" 
                         src="${getCustomImageUrl(question.backgroundImage || '')}" 
                         alt="背景画像プレビュー"
                         style="width: 100%; max-height: 200px; object-fit: cover; border-radius: 8px; border: 2px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"
                         onerror="this.style.display='none'; document.getElementById('backgroundImagePreview').style.display='none';">
                </div>
                <small style="color: #718096; display: block; margin-top: 5px;">dataフォルダ内の画像、または追加した画像を選択できます</small>
            </div>
            
            <div id="gradientGroup" style="display: ${question.backgroundType === 'gradient' ? 'block' : 'none'}; margin-bottom: 15px;">
                <label style="font-weight: 600; margin-bottom: 8px; display: block;">グラデーション色1</label>
                <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 10px;">
                    <input type="color" id="gradientColor1" value="${question.gradientColor1 || '#667eea'}" 
                           onchange="document.getElementById('gradientColor1Text').value = this.value; updateQuestionStyle('${question.id}')"
                           style="width: 60px; height: 40px; border: 2px solid #e2e8f0; border-radius: 5px; cursor: pointer;">
                    <input type="text" id="gradientColor1Text" value="${question.gradientColor1 || '#667eea'}" 
                           onchange="document.getElementById('gradientColor1').value = this.value; updateQuestionStyle('${question.id}')"
                           style="flex: 1; padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px;">
                </div>
                <label style="font-weight: 600; margin-bottom: 8px; display: block;">グラデーション色2</label>
                <div style="display: flex; gap: 10px; align-items: center;">
                    <input type="color" id="gradientColor2" value="${question.gradientColor2 || '#764ba2'}" 
                           onchange="document.getElementById('gradientColor2Text').value = this.value; updateQuestionStyle('${question.id}')"
                           style="width: 60px; height: 40px; border: 2px solid #e2e8f0; border-radius: 5px; cursor: pointer;">
                    <input type="text" id="gradientColor2Text" value="${question.gradientColor2 || '#764ba2'}" 
                           onchange="document.getElementById('gradientColor2').value = this.value; updateQuestionStyle('${question.id}')"
                           style="flex: 1; padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px;">
                </div>
            </div>
            
            <div style="background: #f7fafc; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <label style="font-weight: 600; margin-bottom: 10px; display: block;">質問文のフォント</label>
                <select id="questionFont" onchange="updateQuestionStyle('${question.id}')" 
                        style="width: 100%; padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px; margin-bottom: 10px;">
                    <option value="">デフォルト</option>
                    <option value="Arial, sans-serif" ${question.questionFont === 'Arial, sans-serif' ? 'selected' : ''}>Arial</option>
                    <option value="メイリオ, Meiryo, sans-serif" ${question.questionFont === 'メイリオ, Meiryo, sans-serif' ? 'selected' : ''}>メイリオ</option>
                    <option value="游ゴシック, Yu Gothic, sans-serif" ${question.questionFont === '游ゴシック, Yu Gothic, sans-serif' ? 'selected' : ''}>游ゴシック</option>
                    <option value="MS ゴシック, MS Gothic, monospace" ${question.questionFont === 'MS ゴシック, MS Gothic, monospace' ? 'selected' : ''}>MS ゴシック</option>
                    <option value="Times New Roman, serif" ${question.questionFont === 'Times New Roman, serif' ? 'selected' : ''}>Times New Roman</option>
                </select>
                <label style="font-weight: 600; margin-bottom: 8px; display: block; margin-top: 10px;">フォントサイズ</label>
                <input type="range" id="questionFontSize" min="0.8" max="2.5" step="0.1" 
                       value="${parseFloat(question.questionFontSize || '1.3')}" 
                       oninput="document.getElementById('questionFontSizeValue').textContent = this.value + 'em'; updateQuestionStyle('${question.id}')"
                       style="width: 100%;">
                <div style="display: flex; justify-content: space-between; margin-top: 5px;">
                    <span style="color: #718096; font-size: 0.9em;">0.8em</span>
                    <span id="questionFontSizeValue" style="color: #2d3748; font-weight: 600;">${question.questionFontSize || '1.3em'}</span>
                    <span style="color: #718096; font-size: 0.9em;">2.5em</span>
                </div>
                <label style="font-weight: 600; margin-bottom: 8px; display: block; margin-top: 10px;">文字色</label>
                <div style="display: flex; gap: 10px; align-items: center;">
                    <input type="color" id="questionTextColor" value="${question.questionTextColor || '#2d3748'}" 
                           onchange="document.getElementById('questionTextColorText').value = this.value; updateQuestionStyle('${question.id}')"
                           style="width: 60px; height: 40px; border: 2px solid #e2e8f0; border-radius: 5px; cursor: pointer;">
                    <input type="text" id="questionTextColorText" value="${question.questionTextColor || '#2d3748'}" 
                           onchange="document.getElementById('questionTextColor').value = this.value; updateQuestionStyle('${question.id}')"
                           style="flex: 1; padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px;">
                </div>
            </div>
            
            <div style="background: #f7fafc; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <label style="font-weight: 600; margin-bottom: 10px; display: block;">選択肢ボタンのフォント</label>
                <select id="choiceFont" onchange="updateQuestionStyle('${question.id}')" 
                        style="width: 100%; padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px; margin-bottom: 10px;">
                    <option value="">デフォルト</option>
                    <option value="Arial, sans-serif" ${question.choiceFont === 'Arial, sans-serif' ? 'selected' : ''}>Arial</option>
                    <option value="メイリオ, Meiryo, sans-serif" ${question.choiceFont === 'メイリオ, Meiryo, sans-serif' ? 'selected' : ''}>メイリオ</option>
                    <option value="游ゴシック, Yu Gothic, sans-serif" ${question.choiceFont === '游ゴシック, Yu Gothic, sans-serif' ? 'selected' : ''}>游ゴシック</option>
                    <option value="MS ゴシック, MS Gothic, monospace" ${question.choiceFont === 'MS ゴシック, MS Gothic, monospace' ? 'selected' : ''}>MS ゴシック</option>
                    <option value="Times New Roman, serif" ${question.choiceFont === 'Times New Roman, serif' ? 'selected' : ''}>Times New Roman</option>
                </select>
                <label style="font-weight: 600; margin-bottom: 8px; display: block; margin-top: 10px;">フォントサイズ</label>
                <input type="range" id="choiceFontSize" min="0.8" max="2.0" step="0.1" 
                       value="${parseFloat(question.choiceFontSize || '1.2')}" 
                       oninput="document.getElementById('choiceFontSizeValue').textContent = this.value + 'em'; updateQuestionStyle('${question.id}')"
                       style="width: 100%;">
                <div style="display: flex; justify-content: space-between; margin-top: 5px;">
                    <span style="color: #718096; font-size: 0.9em;">0.8em</span>
                    <span id="choiceFontSizeValue" style="color: #2d3748; font-weight: 600;">${question.choiceFontSize || '1.2em'}</span>
                    <span style="color: #718096; font-size: 0.9em;">2.0em</span>
                </div>
                <label style="font-weight: 600; margin-bottom: 8px; display: block; margin-top: 10px;">ボタンの背景色</label>
                <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 10px;">
                    <input type="color" id="choiceButtonColor" value="${question.choiceButtonColor || '#667eea'}" 
                           onchange="document.getElementById('choiceButtonColorText').value = this.value; updateQuestionStyle('${question.id}')"
                           style="width: 60px; height: 40px; border: 2px solid #e2e8f0; border-radius: 5px; cursor: pointer;">
                    <input type="text" id="choiceButtonColorText" value="${question.choiceButtonColor || '#667eea'}" 
                           onchange="document.getElementById('choiceButtonColor').value = this.value; updateQuestionStyle('${question.id}')"
                           style="flex: 1; padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px;">
                </div>
                <label style="font-weight: 600; margin-bottom: 8px; display: block;">ボタンの文字色</label>
                <div style="display: flex; gap: 10px; align-items: center;">
                    <input type="color" id="choiceButtonTextColor" value="${question.choiceButtonTextColor || '#ffffff'}" 
                           onchange="document.getElementById('choiceButtonTextColorText').value = this.value; updateQuestionStyle('${question.id}')"
                           style="width: 60px; height: 40px; border: 2px solid #e2e8f0; border-radius: 5px; cursor: pointer;">
                    <input type="text" id="choiceButtonTextColorText" value="${question.choiceButtonTextColor || '#ffffff'}" 
                           onchange="document.getElementById('choiceButtonTextColor').value = this.value; updateQuestionStyle('${question.id}')"
                           style="flex: 1; padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px;">
                </div>
            </div>
            
            <details style="margin-top: 15px;">
                <summary style="cursor: pointer; color: #667eea; font-weight: 600; padding: 10px; background: #f7fafc; border-radius: 5px;">
                    ⚙️ 上級者向け: カスタムCSSを直接編集
                </summary>
                <div style="margin-top: 10px;">
                    <textarea id="customCSS" 
                              placeholder="例: .container { border: 3px solid #ff0000; }"
                              onchange="updateQuestionProperty('${question.id}', 'customCSS', this.value)"
                              style="font-family: monospace; min-height: 100px; width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 5px;">${escapeHtml(question.customCSS || '')}</textarea>
                    <small style="color: #718096; display: block; margin-top: 5px;">.container クラスに対してスタイルを適用できます</small>
                </div>
            </details>
        </div>
        
        <div class="form-group">
            <label>選択肢</label>
            <div id="choicesList" class="choices-list"></div>
            <button class="btn" onclick="addChoice('${question.id}')" style="margin-top: 10px;">+ 選択肢を追加</button>
        </div>
        
        <div class="form-group">
            <button class="btn btn-danger" onclick="deleteNode('${question.id}')">🗑️ この質問を削除</button>
        </div>
    `;
    
    // 選択肢を表示
    updateChoicesList(question);
    
    // 背景タイプの変更時に表示を切り替える
    setTimeout(() => {
        const backgroundTypeSelect = document.getElementById('backgroundType');
        if (backgroundTypeSelect) {
            backgroundTypeSelect.addEventListener('change', function() {
                const type = this.value;
                document.getElementById('backgroundColorGroup').style.display = type === 'color' ? 'block' : 'none';
                document.getElementById('backgroundImageGroup').style.display = type === 'image' ? 'block' : 'none';
                document.getElementById('gradientGroup').style.display = type === 'gradient' ? 'block' : 'none';
                updateQuestionStyle(question.id);
            });
        }
        
        // ドロップゾーンのクリックでファイル選択
        const dropZone = document.getElementById('imageDropZone');
        const fileInput = document.getElementById('imageFileInput');
        if (dropZone && fileInput) {
            dropZone.addEventListener('click', function() {
                fileInput.click();
            });
        }
        
        // 背景画像の選択肢を更新
        updateBackgroundImageSelect(question.id);
    }, 100);
}

// 結果エディタを表示
function showResultEditor(result) {
    const editorContent = document.getElementById('editorContent');
    editorContent.innerHTML = `
        <div class="form-group">
            <label>タイトル</label>
            <input type="text" id="resultTitle" value="${escapeHtml(result.title)}" 
                   onchange="updateResultProperty('${result.id}', 'title', this.value)">
        </div>
        
        <div class="form-group">
            <label>結果テキスト</label>
            <textarea id="resultText" 
                      onchange="updateResultProperty('${result.id}', 'text', this.value)">${escapeHtml(result.text)}</textarea>
        </div>
        
        <div class="form-group">
            <label>画像ファイル名（オプション）</label>
            <input type="text" id="resultImage" value="${escapeHtml(result.image)}" 
                   placeholder="例: attention_type.png"
                   onchange="updateResultProperty('${result.id}', 'image', this.value)">
        </div>
        
        <div class="form-group">
            <label>URL（オプション）</label>
            <input type="text" id="resultUrl" value="${escapeHtml(result.url)}" 
                   placeholder="例: https://example.com"
                   onchange="updateResultProperty('${result.id}', 'url', this.value)">
        </div>
        
        <div class="form-group">
            <label>ボタンテキスト（URLがある場合）</label>
            <input type="text" id="resultButtonText" value="${escapeHtml(result.buttonText)}" 
                   placeholder="例: 公式サイトを見る"
                   onchange="updateResultProperty('${result.id}', 'buttonText', this.value)">
        </div>
        
        <div class="form-group">
            <button class="btn btn-danger" onclick="deleteNode('${result.id}')">🗑️ この結果を削除</button>
        </div>
    `;
}

// 選択肢リストを更新
function updateChoicesList(question) {
    const choicesList = document.getElementById('choicesList');
    choicesList.innerHTML = '';
    
    question.choices.forEach((choice, index) => {
        const choiceDiv = document.createElement('div');
        choiceDiv.className = 'choice-item';
        choiceDiv.innerHTML = `
            <input type="text" value="${escapeHtml(choice.text)}" 
                   placeholder="選択肢 ${index + 1}"
                   onchange="updateChoice('${question.id}', ${index}, 'text', this.value)">
            <select onchange="updateChoiceNext('${question.id}', ${index}, this.value)" 
                    style="padding: 8px; border: 2px solid #e2e8f0; border-radius: 5px; flex: 1;">
                ${getNextNodeOptions(choice.nextId)}
            </select>
            <button onclick="removeChoice('${question.id}', ${index})">削除</button>
        `;
        choicesList.appendChild(choiceDiv);
    });
}

// 次のノードオプションを取得
function getNextNodeOptions(currentNextId) {
    let options = '';
    
    // 「なし」オプションを最初に追加
    options += `<option value="" ${!currentNextId ? 'selected' : ''}>（なし）</option>`;
    
    // 質問ノード（現在のノードは除外）
    gameData.questions.forEach(q => {
        if (q.id === selectedNodeId) return; // 現在編集中のノードは除外
        const selected = q.id === currentNextId ? 'selected' : '';
        const displayText = q.text || q.title || '無題';
        options += `<option value="${q.id}" ${selected}>❓ 質問: ${escapeHtml(displayText.substring(0, 30))}</option>`;
    });
    
    // 結果ノード
    gameData.results.forEach(r => {
        const selected = r.id === currentNextId ? 'selected' : '';
        const displayText = r.text || r.title || '無題';
        options += `<option value="${r.id}" ${selected}>✅ 結果: ${escapeHtml(displayText.substring(0, 30))}</option>`;
    });
    
    return options;
}

// 質問プロパティを更新
function updateQuestionProperty(questionId, property, value) {
    const question = gameData.questions.find(q => q.id === questionId);
    if (question) {
        question[property] = value;
        updateUI();
    }
}

// 背景画像プレビューを更新
function updateBackgroundImagePreview(questionId) {
    const question = gameData.questions.find(q => q.id === questionId);
    if (!question) return;
    
    const select = document.getElementById('backgroundImage');
    const previewDiv = document.getElementById('backgroundImagePreview');
    const previewImg = document.getElementById('backgroundImagePreviewImg');
    
    if (select && select.value) {
        question.backgroundImage = select.value;
        const imageUrl = getCustomImageUrl(select.value);
        if (previewImg) {
            previewImg.src = imageUrl;
            previewImg.onerror = function() {
                this.style.display = 'none';
                if (previewDiv) previewDiv.style.display = 'none';
            };
            previewImg.onload = function() {
                this.style.display = 'block';
                if (previewDiv) previewDiv.style.display = 'block';
            };
        }
        if (previewDiv) previewDiv.style.display = 'block';
    } else {
        question.backgroundImage = '';
        if (previewDiv) previewDiv.style.display = 'none';
    }
    
    updateQuestionStyle(questionId);
}

// 質問スタイルを更新（GUI設定から自動的にCSSを生成）
function updateQuestionStyle(questionId) {
    const question = gameData.questions.find(q => q.id === questionId);
    if (!question) return;
    
    // 背景タイプの表示切り替え
    const backgroundTypeEl = document.getElementById('backgroundType');
    if (backgroundTypeEl) {
        const backgroundType = backgroundTypeEl.value;
        question.backgroundType = backgroundType;
        
        const backgroundColorGroup = document.getElementById('backgroundColorGroup');
        const backgroundImageGroup = document.getElementById('backgroundImageGroup');
        const gradientGroup = document.getElementById('gradientGroup');
        
        if (backgroundColorGroup) backgroundColorGroup.style.display = backgroundType === 'color' ? 'block' : 'none';
        if (backgroundImageGroup) backgroundImageGroup.style.display = backgroundType === 'image' ? 'block' : 'none';
        if (gradientGroup) gradientGroup.style.display = backgroundType === 'gradient' ? 'block' : 'none';
    }
    
    // 各設定値を取得
    const backgroundColorEl = document.getElementById('backgroundColor');
    if (backgroundColorEl) {
        question.backgroundColor = backgroundColorEl.value || question.backgroundColor || '#ffffff';
        const backgroundColorTextEl = document.getElementById('backgroundColorText');
        if (backgroundColorTextEl) backgroundColorTextEl.value = question.backgroundColor;
    }
    
    const backgroundImageEl = document.getElementById('backgroundImage');
    if (backgroundImageEl && !question.backgroundImage) {
        question.backgroundImage = backgroundImageEl.value || '';
    }
    
    const gradientColor1El = document.getElementById('gradientColor1');
    if (gradientColor1El) {
        question.gradientColor1 = gradientColor1El.value || question.gradientColor1 || '#667eea';
        const gradientColor1TextEl = document.getElementById('gradientColor1Text');
        if (gradientColor1TextEl) gradientColor1TextEl.value = question.gradientColor1;
    }
    
    const gradientColor2El = document.getElementById('gradientColor2');
    if (gradientColor2El) {
        question.gradientColor2 = gradientColor2El.value || question.gradientColor2 || '#764ba2';
        const gradientColor2TextEl = document.getElementById('gradientColor2Text');
        if (gradientColor2TextEl) gradientColor2TextEl.value = question.gradientColor2;
    }
    
    question.questionFont = document.getElementById('questionFont').value || '';
    question.questionFontSize = document.getElementById('questionFontSize').value + 'em';
    question.questionTextColor = document.getElementById('questionTextColor').value || question.questionTextColor || '#2d3748';
    document.getElementById('questionTextColorText').value = question.questionTextColor;
    document.getElementById('questionTextColor').value = question.questionTextColor;
    
    question.choiceFont = document.getElementById('choiceFont').value || '';
    question.choiceFontSize = document.getElementById('choiceFontSize').value + 'em';
    question.choiceButtonColor = document.getElementById('choiceButtonColor').value || question.choiceButtonColor || '#667eea';
    document.getElementById('choiceButtonColorText').value = question.choiceButtonColor;
    document.getElementById('choiceButtonColor').value = question.choiceButtonColor;
    
    question.choiceButtonTextColor = document.getElementById('choiceButtonTextColor').value || question.choiceButtonTextColor || '#ffffff';
    document.getElementById('choiceButtonTextColorText').value = question.choiceButtonTextColor;
    document.getElementById('choiceButtonTextColor').value = question.choiceButtonTextColor;
    
    // CSSを自動生成
    let css = '';
    
    // 背景設定
    if (backgroundType === 'color') {
        css += `.container { background: ${question.backgroundColor}; }\n`;
    } else if (backgroundType === 'image' && question.backgroundImage) {
        const imageUrl = getCustomImageUrl(question.backgroundImage);
        css += `.container { background-image: url('${imageUrl}'); background-size: cover; background-position: center; background-repeat: no-repeat; }\n`;
    } else if (backgroundType === 'gradient') {
        css += `.container { background: linear-gradient(135deg, ${question.gradientColor1} 0%, ${question.gradientColor2} 100%); }\n`;
    }
    
    // 質問文のスタイル
    if (question.questionFont || question.questionFontSize || question.questionTextColor) {
        css += `.question-text { `;
        if (question.questionFont) css += `font-family: ${question.questionFont}; `;
        if (question.questionFontSize) css += `font-size: ${question.questionFontSize}; `;
        if (question.questionTextColor) css += `color: ${question.questionTextColor}; `;
        css += `}\n`;
    }
    
    // 選択肢ボタンのスタイル
    if (question.choiceFont || question.choiceFontSize || question.choiceButtonColor || question.choiceButtonTextColor) {
        css += `button { `;
        if (question.choiceFont) css += `font-family: ${question.choiceFont}; `;
        if (question.choiceFontSize) css += `font-size: ${question.choiceFontSize}; `;
        if (question.choiceButtonColor) css += `background: ${question.choiceButtonColor}; `;
        if (question.choiceButtonTextColor) css += `color: ${question.choiceButtonTextColor}; `;
        css += `}\n`;
    }
    
    question.customCSS = css;
    
    updateUI();
    showPreview();
}

// 結果プロパティを更新
function updateResultProperty(resultId, property, value) {
    const result = gameData.results.find(r => r.id === resultId);
    if (result) {
        result[property] = value;
        updateUI();
    }
}

// 選択肢を追加
function addChoice(questionId) {
    const question = gameData.questions.find(q => q.id === questionId);
    if (question) {
        const nextValue = question.choices.length;
        question.choices.push({
            text: `選択肢${nextValue + 1}`,
            value: nextValue,
            nextId: null
        });
        updateUI();
    }
}

// 選択肢を更新
function updateChoice(questionId, choiceIndex, property, value) {
    const question = gameData.questions.find(q => q.id === questionId);
    if (question && question.choices[choiceIndex]) {
        question.choices[choiceIndex][property] = value;
        updateUI();
    }
}

// 選択肢の次ノードを更新
function updateChoiceNext(questionId, choiceIndex, nextId) {
    const question = gameData.questions.find(q => q.id === questionId);
    if (question && question.choices[choiceIndex]) {
        question.choices[choiceIndex].nextId = nextId || null;
        updateUI();
    }
}

// 選択肢を削除
function removeChoice(questionId, choiceIndex) {
    const question = gameData.questions.find(q => q.id === questionId);
    if (question && question.choices[choiceIndex]) {
        question.choices.splice(choiceIndex, 1);
        // 値を再割り当て
        question.choices.forEach((choice, index) => {
            choice.value = index;
        });
        updateUI();
    }
}

// ノードを削除
function deleteNode(nodeId) {
    if (!confirm('このノードを削除してもよろしいですか？')) {
        return;
    }
    
    // 質問ノードを削除
    const questionIndex = gameData.questions.findIndex(q => q.id === nodeId);
    if (questionIndex !== -1) {
        // スタートノードの場合はnullに
        if (gameData.startNode === nodeId) {
            gameData.startNode = gameData.questions.length > 1 ? gameData.questions[0].id : null;
        }
        gameData.questions.splice(questionIndex, 1);
    }
    
    // 結果ノードを削除
    const resultIndex = gameData.results.findIndex(r => r.id === nodeId);
    if (resultIndex !== -1) {
        gameData.results.splice(resultIndex, 1);
    }
    
    // 他のノードからの参照を削除
    gameData.questions.forEach(q => {
        q.choices.forEach(choice => {
            if (choice.nextId === nodeId) {
                choice.nextId = null;
            }
        });
    });
    
    selectedNodeId = null;
    updateUI();
}

// プレビューを表示
function showPreview() {
    const previewContent = document.getElementById('previewContent');
    
    if (!selectedNodeId) {
        previewContent.innerHTML = '<div class="empty-state" style="color: #718096;"><p>ノードを選択するとプレビューが表示されます</p></div>';
        return;
    }
    
    const question = gameData.questions.find(q => q.id === selectedNodeId);
    const result = gameData.results.find(r => r.id === selectedNodeId);
    
    if (question) {
        // 背景画像のプレビューを生成
        let backgroundPreview = '';
        if (question.backgroundImage) {
            const imageUrl = getCustomImageUrl(question.backgroundImage);
            backgroundPreview = `
                <div style="margin-top: 15px; margin-bottom: 15px;">
                    <strong style="display: block; margin-bottom: 8px; font-size: 0.9em;">背景画像:</strong>
                    <img src="${escapeHtml(imageUrl)}" 
                         alt="背景画像プレビュー"
                         style="width: 100%; max-height: 150px; object-fit: cover; border-radius: 8px; border: 2px solid #4a5568; box-shadow: 0 2px 8px rgba(0,0,0,0.3);"
                         onerror="this.style.display='none';">
                </div>
            `;
        }
        
        previewContent.innerHTML = `
            <div class="question-node">
                <div class="node-title">質問プレビュー</div>
                <div style="margin-top: 15px;">
                    <strong>${question.title || '無題'}</strong>
                    <p style="margin: 10px 0;">${question.text || '(質問文が未入力)'}</p>
                    ${backgroundPreview}
                    <div style="margin-top: 15px;">
                        <strong>選択肢と分岐:</strong>
                        <ul style="margin-top: 10px; padding-left: 20px; list-style: none;">
                            ${question.choices.map((choice, i) => {
                            const nextNode = choice.nextId ? 
                                (gameData.questions.find(q => q.id === choice.nextId) || 
                                 gameData.results.find(r => r.id === choice.nextId)) : null;
                            const nextType = nextNode ? (nextNode.type === 'question' ? '❓ 質問' : '✅ 結果') : '';
                            const nextText = nextNode ? (nextNode.text || nextNode.title || '無題').substring(0, 25) : '';
                            
                            return `
                                <li style="margin: 8px 0; padding: 10px; background: #f7fafc; border-radius: 8px; border-left: 3px solid ${choice.nextId ? '#48bb78' : '#e53e3e'};">
                                    <strong>${escapeHtml(choice.text || `選択肢${i+1}`)}</strong>
                                    ${choice.nextId ? 
                                        `<div style="margin-top: 5px; font-size: 0.9em; color: #48bb78;">
                                            → ${nextType}: ${escapeHtml(nextText)}
                                        </div>` : 
                                        '<div style="margin-top: 5px; font-size: 0.9em; color: #e53e3e;">⚠️ 次のノードが設定されていません</div>'
                                    }
                                </li>
                            `;
                        }).join('')}
                        </ul>
                    </div>
                </div>
            </div>
        `;
    } else if (result) {
        previewContent.innerHTML = `
            <div class="result-node">
                <div class="node-title">結果プレビュー</div>
                <div style="margin-top: 15px;">
                    <strong>${result.title || '無題'}</strong>
                    <p style="margin: 10px 0;">${result.text || '(結果テキストが未入力)'}</p>
                    ${result.image ? `<p style="margin-top: 10px;">🖼️ 画像: ${result.image}</p>` : ''}
                    ${result.url ? `<p style="margin-top: 10px;">🔗 URL: ${result.url}</p>` : ''}
                    ${result.buttonText ? `<p style="margin-top: 10px;">ボタン: ${result.buttonText}</p>` : ''}
                </div>
            </div>
        `;
    }
}

// プロジェクトを保存
function saveProject() {
    const dataStr = JSON.stringify(gameData, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'game_project.json';
    link.click();
    URL.revokeObjectURL(url);
}

// プロジェクトを読み込み
function loadProject() {
    document.getElementById('fileInput').click();
}

function handleFileLoad(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            gameData = JSON.parse(e.target.result);
            selectedNodeId = null;
            updateUI();
            alert('プロジェクトを読み込みました！');
        } catch (error) {
            alert('エラー: ファイルの読み込みに失敗しました。');
            console.error(error);
        }
    };
    reader.readAsText(file);
}

// CSV形式でエクスポート
function exportCSV() {
    let csv = '';
    
    // スタートノードがあればStart行を追加
    if (gameData.startNode) {
        const startQuestion = gameData.questions.find(q => q.id === gameData.startNode);
        if (startQuestion) {
            csv += `Start,"${startQuestion.title || startQuestion.text || '開始'}"\n`;
        }
    }
    
    // 質問を出力
    gameData.questions.forEach((question, index) => {
        if (question.id === gameData.startNode && index === 0) {
            // スタートノードは既に出力済み
            return;
        }
        
        csv += `Selection,"${question.text || question.title}","`;
        csv += question.choices.map(c => c.text).join('","');
        csv += '"\n';
    });
    
    // 結果を出力
    gameData.results.forEach(result => {
        if (result.url && result.buttonText) {
            csv += `Result_URL,0,"${result.text || result.title}","${result.buttonText}","${result.url}"\n`;
        } else if (result.image) {
            csv += `Result,0,"${result.text || result.title}","${result.image}"\n`;
        } else {
            csv += `Result,0,"${result.text || result.title}",""\n`;
        }
    });
    
    csv += 'End\n';
    
    // ダウンロード
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'game_data.csv';
    link.click();
    URL.revokeObjectURL(link.href);
}

// HTML形式でエクスポート
function exportHTML() {
    alert('HTMLエクスポート機能は準備中です。\n現在はCSVをエクスポートして、908.pyのCtrl+H機能を使用してください。');
}

// プレビューを表示
function previewGame() {
    if (gameData.questions.length === 0 && gameData.results.length === 0) {
        alert('プレビューするためには、少なくとも1つの質問または結果が必要です。');
        return;
    }
    
    if (!gameData.startNode) {
        alert('スタートノードが設定されていません。最初の質問を追加してください。');
        return;
    }
    
    // プレビューページを開く
    const previewWindow = window.open('', '_blank');
    generatePreviewHTML(previewWindow);
}

// プレビューHTMLを生成（実際にゲームを実行できる）
function generatePreviewHTML(window) {
    // ゲームデータをJSON形式で埋め込む
    const gameDataJson = JSON.stringify(gameData);
    // カスタム画像データも埋め込む
    const customImagesJson = JSON.stringify(getCustomImages());
    
    window.document.write(`
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>ゲームプレビュー</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }
                .container { 
                    background: white; 
                    padding: 40px; 
                    border-radius: 20px; 
                    max-width: 700px;
                    width: 100%;
                    text-align: center;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                }
                h1 { 
                    color: #2d3748; 
                    margin-bottom: 30px;
                    font-size: 2em;
                }
                .question-text {
                    font-size: 1.3em;
                    margin-bottom: 30px;
                    color: #2d3748;
                    line-height: 1.6;
                }
                .buttons { 
                    display: flex; 
                    flex-direction: column;
                    gap: 15px;
                    margin-top: 30px;
                }
                button { 
                    padding: 18px 30px; 
                    font-size: 1.2em; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white; 
                    border: none; 
                    border-radius: 12px; 
                    cursor: pointer;
                    transition: all 0.3s ease;
                    font-weight: 600;
                }
                button:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
                }
                .result-text {
                    font-size: 1.4em;
                    margin: 20px 0;
                    color: #2d3748;
                    line-height: 1.6;
                }
                .result-image {
                    max-width: 100%;
                    border-radius: 15px;
                    margin: 20px 0;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                }
                .back-button {
                    margin-top: 30px;
                    background: #4a5568;
                }
                .progress {
                    color: #718096;
                    margin-bottom: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container" id="gameContainer">
                <h1>ゲームを読み込んでいます...</h1>
            </div>
            <script>
                const gameData = ${gameDataJson};
                const customImages = ${customImagesJson};
                let currentQuestionId = gameData.startNode;
                let history = [];
                
                function applyCustomCSS(css) {
                    if (!css) return;
                    let styleEl = document.getElementById('custom-question-style');
                    if (!styleEl) {
                        styleEl = document.createElement('style');
                        styleEl.id = 'custom-question-style';
                        document.head.appendChild(styleEl);
                    }
                    styleEl.textContent = css;
                }
                
                function showQuestion(questionId) {
                    const question = gameData.questions.find(q => q.id === questionId);
                    if (!question) {
                        showError('質問が見つかりません');
                        return;
                    }
                    
                    currentQuestionId = questionId;
                    history.push(questionId);
                    
                    const container = document.getElementById('gameContainer');
                    const progress = history.length > 0 ? \`質問 \${history.length}\` : '開始';
                    
                    // フォントスタイルを適用
                    let questionFontStyle = '';
                    if (question.questionFont) questionFontStyle += \`font-family: \${escapeHtml(question.questionFont)}; \`;
                    if (question.questionFontSize) questionFontStyle += \`font-size: \${escapeHtml(question.questionFontSize)}; \`;
                    if (question.questionTextColor) questionFontStyle += \`color: \${escapeHtml(question.questionTextColor)}; \`;
                    
                    let choiceFontStyle = '';
                    if (question.choiceFont) choiceFontStyle += \`font-family: \${escapeHtml(question.choiceFont)}; \`;
                    if (question.choiceFontSize) choiceFontStyle += \`font-size: \${escapeHtml(question.choiceFontSize)}; \`;
                    if (question.choiceButtonColor) choiceFontStyle += \`background: \${escapeHtml(question.choiceButtonColor)}; \`;
                    if (question.choiceButtonTextColor) choiceFontStyle += \`color: \${escapeHtml(question.choiceButtonTextColor)}; \`;
                    
                    // カスタムCSSを適用
                    applyCustomCSS(question.customCSS || '');
                    
                    container.innerHTML = \`
                        <div class="progress">\${progress}</div>
                        <h1>\${escapeHtml(question.title || '質問')}</h1>
                        <div class="question-text" style="\${questionFontStyle}">\${escapeHtml(question.text || '質問文が未入力です')}</div>
                        <div class="buttons">
                            \${question.choices.map((choice, index) => \`
                                <button onclick="selectChoice('\${choice.nextId}', '\${escapeHtml(choice.text)}')" style="\${choiceFontStyle}">
                                    \${escapeHtml(choice.text || \`選択肢\${index + 1}\`)}
                                </button>
                            \`).join('')}
                        </div>
                        <button class="back-button" onclick="goBack()">← 戻る</button>
                    \`;
                }
                
                function getCustomImageUrl(value) {
                    if (value && value.startsWith('custom:')) {
                        const name = value.substring(7);
                        return customImages[name] || '';
                    }
                    return value || '';
                }
                
                function selectChoice(nextId, choiceText) {
                    if (!nextId) {
                        alert('この選択肢には次のノードが設定されていません。');
                        return;
                    }
                    
                    // 質問ノードか結果ノードかを判定
                    const question = gameData.questions.find(q => q.id === nextId);
                    const result = gameData.results.find(r => r.id === nextId);
                    
                    if (question) {
                        // 次の質問へ
                        showQuestion(nextId);
                    } else if (result) {
                        // 結果を表示
                        showResult(result);
                    } else {
                        alert('次のノードが見つかりません。');
                    }
                }
                
                function showResult(result) {
                    const container = document.getElementById('gameContainer');
                    history.push(result.id);
                    
                    let imageHtml = '';
                    if (result.image) {
                        imageHtml = \`<img src="data/\${escapeHtml(result.image)}" alt="結果画像" class="result-image" onerror="this.style.display='none'">\`;
                    }
                    
                    let urlButton = '';
                    if (result.url && result.buttonText) {
                        urlButton = \`<button onclick="window.open('\${escapeHtml(result.url)}', '_blank')">\${escapeHtml(result.buttonText)}</button>\`;
                    }
                    
                    container.innerHTML = \`
                        <h1>診断結果</h1>
                        \${imageHtml}
                        <div class="result-text">\${escapeHtml(result.text || result.title || '結果が未入力です')}</div>
                        \${urlButton}
                        <button class="back-button" onclick="restartGame()">最初からやり直す</button>
                    \`;
                }
                
                function goBack() {
                    if (history.length <= 1) {
                        restartGame();
                        return;
                    }
                    
                    history.pop(); // 現在のノードを削除
                    const prevId = history[history.length - 1];
                    const question = gameData.questions.find(q => q.id === prevId);
                    
                    if (question) {
                        showQuestion(prevId);
                    } else {
                        restartGame();
                    }
                }
                
                function restartGame() {
                    history = [];
                    currentQuestionId = gameData.startNode;
                    showQuestion(gameData.startNode);
                }
                
                function showError(message) {
                    document.getElementById('gameContainer').innerHTML = \`
                        <h1>エラー</h1>
                        <p>\${escapeHtml(message)}</p>
                        <button onclick="restartGame()">最初からやり直す</button>
                    \`;
                }
                
                function escapeHtml(text) {
                    if (!text) return '';
                    const div = document.createElement('div');
                    div.textContent = text;
                    return div.innerHTML;
                }
                
                // ゲーム開始
                if (gameData.startNode) {
                    showQuestion(gameData.startNode);
                } else {
                    showError('スタートノードが設定されていません。');
                }
            </script>
        </body>
        </html>
    `);
    window.document.close();
}

// HTMLエスケープ
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// 初期化
document.addEventListener('DOMContentLoaded', function() {
    updateUI();
});




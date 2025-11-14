// ゲームデータ構造
let gameData = {
    startNode: null,
    questions: [],
    results: []
};

let selectedNodeId = null;
let nodeIdCounter = 0;

// 質問ノードを追加
function addQuestion() {
    const questionId = `q_${nodeIdCounter++}`;
    const question = {
        id: questionId,
        type: 'question',
        title: `質問 ${gameData.questions.length + 1}`,
        text: '',
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
        previewContent.innerHTML = `
            <div class="question-node">
                <div class="node-title">質問プレビュー</div>
                <div style="margin-top: 15px;">
                    <strong>${question.title || '無題'}</strong>
                    <p style="margin: 10px 0;">${question.text || '(質問文が未入力)'}</p>
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
                let currentQuestionId = gameData.startNode;
                let history = [];
                
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
                    
                    container.innerHTML = \`
                        <div class="progress">\${progress}</div>
                        <h1>\${escapeHtml(question.title || '質問')}</h1>
                        <div class="question-text">\${escapeHtml(question.text || '質問文が未入力です')}</div>
                        <div class="buttons">
                            \${question.choices.map((choice, index) => \`
                                <button onclick="selectChoice('\${choice.nextId}', '\${escapeHtml(choice.text)}')">
                                    \${escapeHtml(choice.text || \`選択肢\${index + 1}\`)}
                                </button>
                            \`).join('')}
                        </div>
                        <button class="back-button" onclick="goBack()">← 戻る</button>
                    \`;
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




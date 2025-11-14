# アクティブフレーム:ここに各グループのコンポーネントを設置する

# 実行時
# Componentをmove_inhibit_Falseにすると、画像やボタンのように、アクティブフレームに移動できる
# Componentをmove_inhibit_Trueにすると、要素は動かない

# Ctrl+z 元に戻す（Undo）
# Ctrl+Shift+z やり直し（Redo）
# Ctrl+e 設計モードと実行モードを交換する
# Ctrl+d ダンプ出力
# Ctrl+c ルート域のみプリント
# Ctrl+t 全ツリー情報をプリント
# Ctrl+h htmlファイルを作成


# max_page_no  :RGB値決定／キャンセル
# max_page_no-1:画像ファイル 決定／キャンセル
# max_page_no-2:Copyright OK

# Selection
# Result
# Resul_URL
# Result_3_image


# COmponent_Button の draw_component で、True/Falseに応じてボタンを描画している



# 0022 タイトルを指定できるようにする
# 0138 コンポーネント画像移動を、設計時もできるようにする
# 0146 EXCLUSIVE_で、設計のとき、エラー
# 0247 全くの更の画面から作成できるようにする
# 0248 新ページを作成できるようする
# 0262 パラメタの一覧（グリッド、余白、フォルダ）を作る
# 0268 新たな機能「タイトルとデータ」のようなものを追加できるようにする
# 0270 インタフェースのように線でつないで動く
# 0271 PCの画像などを自由における
# 0291 inhibit（移動可能）を変えられるようにする
# 0292 exclusive（排他）を変えられるようにする
# 0294 「次に進む」ボタンをすぐ作れるようにする（そのとき、mouse_upでコマンドを受け入れるようにする）
# 0297 Active_Frameを設定できるようにする
# 0304 設計で変更したデータを抽出し、ソースに反映できる
# 0315 (08)上とか左に大きくできるようにしてほしい
# 0380 まだ上下左右はダメ
# 0453 同じ選択肢があったときの対処をする
# 0479 「ページの追加」を作成
# 0480 新規のページの名前を付ける
# 0481 ページ追加時、CSV_listは更新し、保存で、新しいシナリオテキストを作成
# 0484 01と02の間に04を入れる、NからたどりN-00の内容(N-01)をSave、N-00に04を代入、N-04にSave(00)を代入
# 0485 01と02の間に04を入れる、PからP-03、P-02、P-01をたどりP-01の内容(P-00)をSave、P-01に04を代入、P-04にSave(00)を代入
# 0486 ページを削除できるようにする 
# 0495 新ページを作ったあと、その結果をcsvに正確に反映する仕組みを考える
# 0499 CSVファイルを作る
# 0530 「データを保存」時に数字を設定
# 0531 「データを読込」時に数字を設定
# 0532　Resultで長い文章のとき、位置を真ん中に
# 0533





# ＜改修済＞
# 〇0515 （D01）トグルボタンで、透明な部分をクリックすると落ちる
# 〇0516 （D02）シナリオが並んでいるところで、要素が動かないようにする
# 〇0517 （D03）「実行」ボタンはいらない
# 〇0518 （D04）「スライダーは、マウスで持って移動するようにする
# 〇0519 （D05）チェックボックスも落ちる
# 〇0520 （D06）フレームも落ちる
# 〇0529 MOUSEMOTIONで、スライダーを引っ張れるか？
# 〇0525 設計の「次に進む」でRGBに行き、キャンセルするとファイルがないエラー
# 〇0526 RGBで、データが０～１になっている
# 〇0527 RGBで、257になると落ちる
# 〇0528 スライダーの表示が、値でなく９０％で表現
# 〇0413 いきなり左ボタンで、少し右ボタンが見える
# 〇0414 問題ラベルをサポート
# 〇0379 高さの高い右メニューが下で見にくいので上にずらす
# 〇0514 生成のときの右メニューの位置を合わせる
# 〇0523 （D07）右メニューの位置を上に行かないようにする
# 〇0524 ３イメージも動かないようにする
# 〇0483 22133125土井可蓮さんの作品「５問２択」「３２通りのおすすめページ」「ページに画像」「さらに３冊から１冊をランダムでおすすめ」
# 〇0521 左１画像、右上下２画像をサポート
# 〇0522 乱数で３つのうち２つの画像を選ぶ
# 〇0489 （C01）「次に進む」で、最後に落ちる
# 〇0490 （C02）「新項目」で、文字変更すると落ちる
# 〇0491 （C03）「グループの画像変更」で、落ちる
# 〇0492 （C04）ExcelからCSVを書き換えるときに、文字化けする
# 〇0493 （C05）「pip install pygbag」で、pyソースをHPで見れる
# 〇0494 （C06）「右クリック」で、最後に落ちる
# 〇0412 縦２ボタン最小文字で、さらに右棒で左に行くとFont決めでエラー
# 〇0502 新規で、種類を選べるようにする
# 〇0512 「新しいページを作る」を止めておく
# 〇0513 画像を横に追加して、項目を追加するとalphaでエラー
# 〇0504 htmlのページの名前を考える
# 〇0505 htmlで、０／２、０／１を自動で作る
# 〇0506 Resultの結果を出す
# 〇0507 Resultのサイズを大きくする
# 〇0508 Selectionなどを見てhtmlを作る
# 〇0509 html作成ボタンを作る
# 〇0510 選択肢を２から３に増やす
# 〇0511 Resultのときのhtmlを作る
# 〇0503 html作成時、index.htmlを起動できるようにする
# 〇0500 「新項目」の直後「新項目」でエラー
# 〇0501 テキストで「項目の追加」でエラー
# 〇0497 ページのタイプ（Selection、Result等）を、ページ情報域に格納
# 〇0498 実行ボタンをもとに戻す
# 〇0496 CSVファイルをutf-8にしない
# 〇0487 ページの双方向リストを作成 
# 〇0488 実行時「前に戻る」もサポート 
# 〇0415（B01）「実行」ボタンを押したとき、キャプションが変わらない
# 〇0416（B02）RGBの色見本を枠で囲む
# 〇0417（B03）画像と色変更で落ちる
# 〇0418（B04）トグルの後ろも不透明の画像にする
# 〇0419（B05）項目の背景色変更を、項目ごとにする
# 〇0420（B06）グループの背景色変更もできるようにする
# 〇0421（B07）全体一括で、背景を表示し、チェックボタンで変えられるようにしたい
# 〇0422（B08）全体一括で、フォントの色を表示し、チェックボタンで変えられるようにしたい
# 〇0423（B09）全体一括で、フォントの種類を表示し、チェックボタンで変えられるようにしたい
# 〇0424（B10）前面にグループを移動
# 〇0425（B11）背面にグループを移動
# 〇0426（B12）「次に移動」で、RGBで落ちる
# 〇0427（B13）「前に戻る」で、RGBで落ちる
# 〇0428（B14）CSVで、構造を変えられるようにする
# 〇0429（B15）ページを増やす機能を作る
# 〇0430（B16）ページを増やし、そこで問題文とか作りたい
# 〇0431（B17）左下にコピーライトボタンを作る
# 〇0468 最初の画面で、「NEW」を作る（初めての）
# 〇0475 何もないページを作る 
# 〇0476 新規がSTARTだと、新たな選択肢が表示される
# 〇0477 新規に変えてもroot変わらない
# 〇0478 新規のページ（"次に進む"）
# 〇0482 シナリオテキストで、選択肢の後の数字はなくす
# 〇0469 選択したら、それに移る
# 〇0472 左下のクリックを得るとprint
# 〇0473 データの読込で、最大ページ３になっているが、本当は８
# 〇0474 データの読込で読んだ先にcopyright（P.6)がない 
# 〇0442 最初からシステムの２ページを０，１にするか
# 〇0456 複数のファイルから必要な状態を読み込む 
# 〇0458 LOAD読込で、複数のファイルを選択できる
# 〇0465 最初のページ
# 〇0466 「使用する画像を選んでください」のように開始ページを作る 
# 〇0467 「使用する画像を選んでください」で、引数にワイルドカードを指定できるようにする
# 〇0470 コンポーネントの予約領域を３つずつ作る
# 〇0471 グループの予約領域を３つずつ作る
# 〇0457 背景の色変更で、即座に色が変わらない（ページ０で「背景の色変更を行ったとき」）
# 〇0459 即座に背景画像が変わる # 0460 
# 〇0460 全ページの背景の色を変更できる 
# 〇0461 全ページの文字色を変更できる 
# 〇0462 全ページの背景の画像を変更できる 
# 〇0463 ページでフォントを変更できる 
# 〇0464 全ページでフォントを変更できる 
# 〇0444 ３つの選択肢をサポート 
# 〇0452 候補を、リストの長さから判断
# 〇0454 実行時にRGB値の決定、キャンセルが効かない 
# 〇0455 修正はTEXTではなくTOGGLE 
# 〇0447 Mouse_button_upで、設計時と実行時を分ける 
# 〇0449 ３つの選択
# 〇0450 URLをクリックしても飛ばない
# 〇0451 URLボタンをクリックすると、次のページに移動している （動かないのがよさそう）
# 〇0440 項目の追加ができない
# 〇0441 CSVをリストに入れる
# 〇0443 flag_0、flag_1をリスト化 
# 〇0445 神楽と洋楽で、ボタンを押しても進まない 
# 〇0446 Selectionの選択肢は、２次元リスト化 
# 〇0448 ２つの選択
# 〇0343 表示順番を変更できるようにする
# 〇0267 「機能」を実現する部分を、動的にする
# 〇0438 ページ０で、グループ３が選べない
# 〇0432 項目の背景色は、グループの背景色
# 〇0433 グループの背景色を廃止
# 〇0435 グループの文字色変更は、すべてのコンポーネントの色を変更
# 〇0436 font_light_colorも、componentに移す
# 〇0437 グループから、font_color,font_light_color,back_colorを消す
# 〇0439 RGB色が枠に出ない
# 〇0434 グループの背景色変更は、すべてのコンポーネントの色を変更
# 〇0383 (A01)右メニューで、画像に変化しない
# 〇0384 (A02)全画面をサポート
# 〇0385 (A03)グループ全体でなく、項目ごとにフォントを変えたい
# 〇0386 (A04)グループ全体でなく、項目ごとに色を変えたい
# 〇0387 (A05)フォントの色をRGBや丸い環で選べるようにする
# 〇0388 (A06)右ボタンの効きが、〇は確実だが他はぼけている
# 〇0389 (A07)youtubeやHPに飛べるようにする
# 〇0390 (A08)背景の色を変えられるようにする
# 〇0391 (A09)背景に画像を貼れるようにする　
# 〇0411 横のボタンの項目の文字変更で、右メニューが薄くなる
# 〇0410 ファイル選択で、トグルの幅が短い
# 〇0341 選択したグループ番号を表示できるようにする
# 〇0348 グループ番号を出すか？
# 〇0409 グループに番号を出す
# 〇0405 common_data_0は、データのやりとりには使うべきでない
# 〇0406 RGBの色見本四角を作る
# 〇0407 URL領域をボタンに作る
# 〇0408 URLを入れる
# 〇0403 トグル画面で連続のとき、一つ前の選択をオフっておく
# 〇0404 ページ番号を入れる
# 〇0378 画像をリストから選べる
# 〇0396 背景の画像を選ぶメニューを作る
# 〇0398 背景の画像を、game_back背景の画像を選ぶメニューを作る
# 〇0401 「決定」でトグルの値を得るとき、グループ番号が１なのに２になる
# 〇0402 トグル画面は実行にし、決定したら設計にする
# 〇0242 グループ作成のときに、種類を選べる
# 〇0300 もし実行時に表示したくなければ、そう指定できる
# 〇0301 ボタンに従って、結果の絵を表示できる
# 〇0302 ボタンの文字を使ってページジャンプできる
# 〇0400 ０１２３４５ページ遷移後、次に進むでエラー
# 〇0394 ２ページ目から３ページ目に行くときの「次に進む」でエラー
# 〇0399 「制御ボタン」として「次に進む」「前に戻る」「データの読込」「データの保存」「開始」「終了」を作成し、常に全ページに出す
# 〇0395 右メニューの幅の範囲を調べる
# 〇0397 背景の色を変える度に保存する
# 〇0382 データを保存すると、０番目のグループが消える
# 〇0393 画面をRESIZABLEにすると、マウスmx,myを再計算する必要がある
# 〇0395 データの読込で、画面がなくなる
# 〇0396 全画面や大きさを限界以上にしたら、原寸に戻す
# 〇0397 データの読込、保存でデータが消える
# 〇0397 グループのフォントの色変更が動かない
# 〇0398 グループのフォントの種類変更が動かない
# 〇0395 コンポーネントのフォント色を使う
# 〇0396 コンポーネントのフォントの種類を使う
# 〇0399 右メニューの高さを４０→３０にする
# 〇0397 項目の追加で、fontの色とタイプとNoneを追加
# 〇0394 コンポーネントにフォント領域を２つつくる
# 〇0381 制御ボタンは、設計時のみ動くようにする
# 〇0319 (12)画像の濃度を変えられる
# 〇0335 設計で画像のとき、濃度を設定するパラメタを作る
# 〇0336 設計で画像のとき、濃度を設定できるようにする
# 〇0296 制御ボタンを追加
# 〇0310 (03)フラグで分岐するようにする
# 〇0322 選択モードを作る
# 〇0299 文字の色をあとから指定できる
# 〇0381 フォントの変更メニュー
# 〇0377 フォントを変えられる
# 〇0380 上棒のとき、正しくdiffを設定
# 〇0381 上棒のとき、２つ要素があって最小高さにしたとき、幅が小さすぎる
# 〇0320 (13)新項目で青はおかしいので、文字の色を変えられる
# 〇0376 新規グループの色は黒にしておく
# 〇0378 デフォルトのフォント色を黒にする
# 〇0001 枠を２重にする 
# 〇0002 0,1,2がコンポーネント、3が枠にする dfbnm
# 〇0003 Mouse_Controlで、mouse_componentが-1にされる
# 〇0004 componentの表示が、０番がおかしい
# 〇0005 枠のみを、明確に指定する
# 〇0006 移動した後のコンポーネントを移動できない
# 〇0007 コンポーネント移動後の色を変える
# 〇0008 横並べの枠がない
# 〇0009 画像を薄くする
# 〇0010 ５か６のときスライダー決め打ちになっている
# 〇0011 スライダーを表示する
# 〇0012 ７か８のときトグルボタン決め打ちになっている
# 〇0013 ９か１０のときチェックボックス決め打ちになっている
# 〇0014 Columnをグループに変える
# 〇0015 横スライダーのデータ位置が、移動後にずれる
# 〇0016 対象となるフレームをどこに持つか
# 〇0017 横スライダーの幻影を出しておく
# 〇0018 文字を枠に入れる
# 〇0019 排他をサポートする
# 〇0020 排他のフラグを作る
# 〇0021 ColumnとRowをパラメタで１つにする
# 〇0023 ページで背景の色を指定できるようにする
# 〇0024 テキストを指定できるようにする
# 〇0025 音楽、ボタンも排他可能にする
# 〇0026 移動しないボタンをサポートする
# 〇0027 移動しないボタンは、押すと意味があるようにする
# 〇0028 フレームの背景色を指定
# 〇0029 テキストの背景色を指定
# 〇0030 ボタンクリックでグラフィックスを変える
# 〇0031 「次に進む」ボタンクリックでページを変える
# 〇0032 ページごとにデータを保存
# 〇0033 優先順位をつける（select_frame）
# 〇0034 ステージ２，３でFrameをクリックすると、前に戻る
# 〇0035 全ステージを作る
# 〇0036 データ書き出し、読込処理を作成
# 〇0037 o_designから復元
# 〇0038 imageがずれる
# 〇0039 stage_defaultが出ない
# 〇0040 文字の内側に白が出ない
# 〇0041 グループ全体のx,yが保存されていない
# 〇0042 pリストから再現する
# 〇0043 マウスクリック時pを変える
# 〇0044 マウス移動時pを変える
# 〇0045 マウスアップ時pを変える
# 〇0046 マウス関数を移動する
# 〇0047 ページ番号の絶対化
# 〇0048 ページ番号で、pを読む
# 〇0049 マウス移動を別に分ける
# 〇0050 check_posを、再利用のときどうすればよいか
# 〇0051 ０ページ、１ページ、０ページのとき、再利用なのに、再度pにappendしている
# 〇0052 check_frame_posを再利用時に使えるようにする
# 〇0053 最終的には、新ページをなくし、いきなりpで行けるようにする
# 〇0054 ボタンのページの先に行き、前に戻ると、空の画面になる
# 〇0055 ボタンをクリックすると、太さが大きくなる
# 〇0056 ボタンをクリックしたとき、その番号をpushに覚えさせる
# 〇0057 ボタンを移動させる 
# 〇0058 スライダーの移動途中が異常
# 〇0059 チェックボックスをまとめて移動させる 
# 〇0060 トグルボタンをまとめて移動させる 
# 〇0061 スライダーが２つあるとき、同じ値で反映される 
# 〇0062 スライダーは、コンポーネントごとにValueを作る 
# 〇0063 新のとき、表示をせずに旧に移行
# 〇0064 保存する 
# 〇0065 初期化・データを保存ではなく、データを読込にする 
# 〇0066 COM___active_frameを生かす
# 〇0067 ０番のactive_frameをグループ０だと思ってみてしまうので、１足す（mouse系）
# 〇0068 CHeckBoxで、今クリックすると、値がない
# 〇0069 同じフレームへの排他が効かない
# 〇0070 実枠、仮想枠の作成
# 〇0071 コンテナにチェックボックスを入れる
# 〇0072 コンテナにトグルを入れる
# 〇0073 コンテナ上は、相対アドレスにする
# 〇0074 コンテナ上は、コンポーネントも相対アドレスにする
# 〇0075 トグルで、丸をつける
# 〇0076 ボタンをクリックした後に、押した状態が残る
# 〇0077 toggleで縦のとき、左に寄せたい
# 〇0078 単独の位置確認
# 〇0079 ボタンプッシュを、個別に持ち込む
# 〇0080 ボタンをコンテナと同期して相対アドレス
# 〇0081 ボタンをクリック時、最初のコンポーネントしか選ばれない
# 〇0082 スライダーでクリック時値が大きすぎる
# 〇0083 画像枠移動後、移動が大きすぎる
# 〇0084 画像枠移動せず、画像を移動すると、move、up時ともにずれている
# 〇0085 枠を一切動かさないモードを作る
# 〇0086 移動した画像を戻せない
# 〇0087 tempも得られるようにする
# 〇0088 スライダーでクリックしても値が変わらない
# 〇0089 defaultの左の縦画像が反応しない
# 〇0090 スライダーも影がいるかも
# 〇0091 スライダーのグループを作成
# 〇0092 テキスト移動時の位置がずれている
# 〇0093 テキストの元の表示が、塗りつぶしで消えている
# 〇0094 スライダーの最大・最小を指定する
# 〇0095 グループ枠を出すか出さないかフラグ作成
# 〇0096 フレーム枠表示フラグを一括でできるようにする
# 〇0097 フレームが移動できない
# 〇0098 フレームのtempありなしの色が同じ
# 〇0099 共通フラグで、設計モードと実行モードを作成
# 〇0100 ０ぺージ削除は成功、ページを調整して１減らす
# 〇0101 Modeが設計のときは、Frame関係なく移動できるべき
# 〇0102 Modeが実行のときは、Frame上へ置けるだけ
# 〇0103 トグルボタンの初期値を置けるようにする
# 〇0104 トグルボタンの文字を小さくしたら、丸の半径も小さくする
# 〇0105 設計のとき、フレームの大きさを変更できるべき
# 〇0106 設計のとき、新グループを追加できるべき
# 〇0107 設計のとき、グループを削除できるべき
# 〇0108 設計のとき、グループに新要素を追加できるべき
# 〇0109 設計のとき、グループから要素を削除できるべき
# 〇0110 設計のとき、要素の名前を変更できるべき
# 〇0111 設計と実行は、赤で表示
# 〇0112 実行のときは、フレームは動かない
# 〇0113 実行時、コンポーネントを動かしたくないときのフラグを作る
# 〇0114 保存時、page_noが大きくなりすぎてしまう
# 〇0115 controlに機能を移す
# 〇0116 ２ページのSliderが移動できてしまう 
# 〇0117 ６ページ表示後、７ページを表示、戻って６ページの「保存」で、表示が７ページに行ってしまう
# 〇0118 Page_0に、右ボタン対応のボックスを作る
# 〇0119 Page_1～7にも、右ボタン対応のボックスを作る
# 〇0120 プロジェクトに、右ボタンフラグを設ける
# 〇0121 ページ部分の１に、右ボタンデータを設ける
# 〇0122 ページ検索の番号を１増やす
# 〇0123 右クリック処理時に再度右クリックで位置をずらす
# 〇0124 showを再設計
# 〇0125 何もない場所の右クリックは「グループの作成」、すでにグループがある場所の右クリックは「コンポーネントの追加」「コンポーネントの更新」「コンポーネントの削除「グループの削除」
# 〇0126 右クリックでメニューがあるとき、メニュー以外をクリックしたら右クリック解除
# 〇0127 すでにデータがあるので、add_componentを廃止
# 〇0128 設計モードで、画像を移動させるとき、mousemotion中が表示されない
# 〇0129 スライダーでコンポーネント個々にcomponent_valueを指定できるようにする
# 〇0130 表示順は、双方向リストを用いる
# 〇0131 Pageに、前、次を入れる
# 〇0132 Singleを、１つアップにする
# 〇0133 Create_group_Directで、グループの情報を付加
# 〇0134 グループの総エントリ数を作成
# 〇0135 page_0で、設計／実行モードを削除しても、クリックすると機能が生きている
# 〇0136 page_3で、フレームを削除しても、active_frameがそのままなので、機能が生きてしまう
# 〇0137 コンポーネント上、グループ上、それ以外をシンプルにする
# 〇0139 MUSICで、２回目クリックしても音楽が止まらない
# 〇0140 音楽ボタンを移動して、そこをクリックしてもMOU_CLICK_COMPONENTにならない
# 〇0141 ボタンを移動して、そこをクリックしてもMOU_CLICK_COMPONENTにならない
# 〇0142 右ボタンが停止されている
# 〇0143 マウスダウンのときは、サーチを逆順にすべき
# 〇0144 画像クリックのとき、tempで見ていない
# 〇0145 敵選択で、複数選択できない
# 〇0147 Page_0で、設計のとき、なにも移動できない
# 〇0148 Bottomでグループを移動させると、0を動かしたとき表示されない
# 〇0149 右ボタンで新規作成に入る
# 〇0150 Page_0で、３のボタングループのコンポーネント以外を選べない
# 〇0151 右マウスでRECTANGLEモードのとき、マウスのmxmyを入手する
# 〇0152 右マウスでDOWNMOVEUP後、矩形を新エントリとしてInsertする
# 〇0153 右マウスでDOWN時、一瞬大きな矩形ができる
# 〇0154 そもそもPage_0で1->2->3->0の順番はおかしくないか
# 〇0155 設計・実行の切り替えができない
# 〇0156 フレーム作成後、それが表示されない
# 〇0157 設計時のみ、右ボタンでグループが追加できる
# 〇0158 設計時でコンポーネントを選んでいるとき、追加か更新か削除が選べる
# 〇0159 設計時でグループを選んでいるとき、コンポーネントに対し追加か更新か削除が選べる
# 〇0160 設計時のみ、右ボタンでグループが追加でき、それをどのタイプか変更できる
# 〇0160 設計時のみ、範囲外で右クリックでグループが作成でき、その後、範囲外で再度グループが作成できる
# 〇0161 Bottomで移動した後、Page_0で、正しく新しいエントリが挿入できるか確認
# 〇0162 メモ帳形式で文字入力ができる
# 〇0163 単純に、右クリックのメニューで削除が選べる
# 〇0164 グループの大きさ変更ができる
# 〇0165 削除してから追加ができることを確認する
# 〇0166 生成位置をグリッドで縛れるようにする
# 〇0167 ２つ目の右クリック生成で、widthheightがリセットされていない
# 〇0168 追加更新削除を動的に作成
# 〇0169 メ１２３（Component中）で、右ボタンをはずしたとき、その位置で処理を行う
# 〇0170 メ１（Component中）「削除」で、右ボタンをはずしたとき、そのグループを削除する
# 〇0172 削除で順番が変わらないか確認
# 〇0173 ７追加６削除６追加でフルのとき、追加で最初のエントリが消えてしまう
# 〇0174 Page_0で全削除のとき、エラーになる
# 〇0175 すべてのグループを消した時、処理を加える
# 〇0176 delete_listで、存在しないエントリを削除しても逃げる
# 〇0177 Page_0で、[0]テキストを消した後、右クリックでエントリを作ると、[0]テキストが復活する
# 〇0178 Page_0で、[0]テキストを消した後、右クリックでボタンエントリを作り、その後右クリックで画像を作ると、ボタンの同じところに画像が作られる
# 〇0179 最後のグループは消せないようにする
# 〇0180 右クリックで、削除の文字がずれる
# 〇0181 右クリックのときは、一時は出さない
# 〇0182 右クリックのとき、最小サイズを作る
# 〇0183 複数コンポーネントの再利用のとき、前のエントリが出てしまう
# 〇0184 再利用では、エントリは１個に絞る
# 〇0185 前コンポーネントの消去を完璧にする関数
# 〇0186 画像を再利用でスライダーにすると、項目が足りない
# 〇0187 コンポーネント上で、２つのメニューを出せるようにする
# 〇0188 項目の追加で、新たにコンポーネントを追加
# 〇0189 ８１８行で、新たな項目を追加したとき、もとの情報から高さを引っ張ってきて、それを全高に加え、幅も第０項と同じに修正
# 〇0190 画像を右クリックで削除するとエラー
# 〇0191 ０ページは項目の追加できるが、１ページ目以降できない
# 〇0192 ０ページで項目の追加をした後、項目の追加がエラー
# 〇0193 新しいグループ作成時の文字は「新」でなく変更可能にする
# 〇0194 ２項目に＋１できるようにする
# 〇0195 グループのTYPEを変えられる
# 〇0196 グループの項目の削除ができる（コンポーネント上では項目の追加・項目の更新・項目の削除・グループの削除）
# 〇0197 画像の追加は、何かデフォルトの画像が必要
# 〇0198 スライダーの追加はできていない
# 〇0199 全要素を消した後、グループを削除できない
# 〇0200 削除したエントリは詰める
# 〇0201 項目の更新を実現する（メモ帳か？）
# 〇0202 フォルダをデータにして保存
# 〇0203 音楽を判断して、音楽でないときはdefaultを流す
# 〇0204 複数のタイプ変更を可能にする
# 〇0205 チェックボックスのボタンの大きさを、可変にする
# 〇0206 日本語入力ができるか
# 〇0207 日本語入力したら、クリアする
# 〇0208 日本語入力で、TABキーを無視
# 〇0209 日本語入力で、連続しても大丈夫にする
# 〇0210 日本語入力で、確定しても、もう一度「Enter」を求める
# 〇0211 項目の文字変更で、正しい位置を見つける
# 〇0212 項目の文字変更で、複数のコンポーネントの中の何番目かを指定
# 〇0213 もし、右クリックメニューで全体を表示できないときは、上にずらす
# 〇0214 設計で、グループのタイプ変更がエラーになる
# 〇0215 左上で移動できるようにする
# 〇0216 右棒で拡大できるようにする
# 〇0217 右棒で縮小できるようにする
# 〇0218 下棒で拡大できるようにする
# 〇0219 下棒で縮小できるようにする
# 〇0220 左上に移動画像を出す
# 〇0221 右棒に移動画像を出す
# 〇0222 右棒に移動画像を出す
# 〇0223 Groupをクリックしているのに、Rectangleになってしまう
# 〇0224 追加した戦闘機でグループのタイプ変更を行い、項目の追加をすると画像になる
# 〇0225 追加した戦闘機でグループのタイプ変更を行うと、エラーになる
# 〇0226 左ボタンで移動するときに、右クリックメニューが出る
# 〇0227 右棒で拡大し、コンポーネントも拡大
# 〇0228 右棒で縮小し、コンポーネントも縮小
# 〇0229 下棒で拡大し、コンポーネントも拡大
# 〇0230 下棒で縮小し、コンポーネントも縮小
# 〇0231 小さくしたボタンをクリックしても押した描画が元に戻らない
# 〇0232 グループ枠変更に応じて、ボタンの文字を小さくする
# 〇0233 グループ枠変更に応じて、最低限以上枠を小さくしない
# 〇0234 縦のフィットだけでなく、横のフィットも導入
# 〇0235 ボタンで、項目の追加ができない 
# 〇0236 拡大縮小で、フォントサイズが縦と横と両方見て行う
# 〇0237 ROWのときに、要素の追加が未サポート
# 〇0238 ROWのときに、要素の更新が未サポート
# 〇0239 ROWのときに、要素の削除が未サポート
# 〇0240 ROWのときに、グループの削除が未サポート
# 〇0241 ROWのときに、項目の文字変更が未サポート
# 〇0243 グループ作成で要素を追加するときに、縦か横か選べる
# 〇0244 グループ作成で要素を追加するときに、間隔が正しいかを確認
# 〇0245 間隔をどこかに変数で持っておく
# 〇0246 グリッドをどこかに変数で持っておく
# 〇0249 項目の追加ができない
# 〇0250 下棒や右棒で、右クリックが表示される 
# 〇0251 スライダーの新規時の初期値をちゃんとする
# 〇0252 間隔を変数化
# 〇0253 グリッドを変数化
# 〇0254 グリッド10－＞20のとき、確認
# 〇0255 2319行で、fontのサイズを計算
# 〇0256 新しい項目で、間隔を調整
# 〇0257 戦闘機を作りスライダーに変換しエントリを追加するとエラー
# 〇0258 スライダー追加でも、Textと表記されている
# 〇0259 小さすぎる戦闘機でエラー（余白が大きいときは、それで画像がつぶれる）
# 〇0260 大グリッドで、移動のマウスアップのときに利かす
# 〇0261 複数のグループが重なったとき、移動できるグループを選んでそれだけ移動できるようにする
# 〇0263 右クリックのメニューを変えられるようにする
# 〇0264 右クリックのメニューの背景を不透明にできるようにする
# 〇0265 下で右クリックのメニューが見えなくなる時は、位置を上にずらす
# 〇0266 設計時と実行時に、両方とも同じ機能が使える（実行時は、新たなエントリはできないようにする）
# 〇0269 入力がないとき、エラーになる（ERROR002）
# 〇0272 届かない場所をgetする関数を作る（[タイプ＝Slider][CheckBox]など）
# 〇0273 右メニューを枠内に入れる
# 〇0274 グループのタイプ変更で、自由にメニューが選べる
# 〇0275 新規作成のときも、change_typeを使う
# 〇0276 文字の入力で半角空白がエラー
# 〇0277 文字の入力で未入力がエラー
# 〇0278 ダイレクトに設計モードに入れる
# 〇0279 ほぼ背景が出るが、途中５個のとき出ない
# 〇0280 Escで１つ戻る
# 〇0281 コンポーネントのtextが空白のとき、拡大するとゼロ割り
# 〇0282 重大な処理の直前にSaveする
# 〇0283 永続的なSaveと分ける
# 〇0284 ２つ目のメニューでそれを使わないと、次回が２つ目のメニューになってしまう
# 〇0285 メニューの折り返しがうまくいかない
# 〇0286 page_0をshowしたときに、最初のpage_noが１　<< Page_no = 1 , Group Information >>
# 〇0287 何もないページから作る
# 〇0288 項目の削除で、pが保存されていない
# 〇0289 すべて削除し、その後つくるボタンで「次に進む」を作っても、次にいけない
# 〇0290 page_5のハイスコアをinhibit=Trueにすると、設計のとき、移動は見えないが、最後には移動している
# 〇0293 「設計」「実行」トグルをすぐ作れるようにする
# 〇0295 キャプションをもとに戻す
# 〇0298 設計・実行トグルの追加
# 〇0303 ページを自由に行き来できるようにする
# 〇0305 「データの保存」でエラーになる
# 〇0306 新ページで飛ばせるようにする、または、一気に作れるようにする
# 〇0307 最大ページを使っているか確認
# 〇0308 (01)右ボタンを離しても大丈夫にする
# 〇0309 (02)グループのタイプ変更を先頭にし、削除系は下にする
# 〇0311 (04)「Esc」でなく「Ctrl＋Z」で戻るようにする
# 〇0312 (05)２つ３つと戻れる
# 〇0313 (06)下の項目が押されたとき、かぶって扱えない
# 〇0314 (07)要素の追加で、グループのサイズを変えないでほしい
# 〇0316 (09)グループの移動は、グループを選んだら、どこを持ってもいいようにする
# 〇0317 (10)グループの作成で、すぐメニュー
# 〇0318 (11)グループを処理するために、固定できるようにしたい
# 〇0321 なんとか、設計と実行を切り替えできるようする（交換）
# 〇0323 右メニューを専用の関数で行い、他の左は受け付けない
# 〇0324 pxxx.pklを、適当なところで消去
# 〇0325 _BOTTOMで下からサイズを変えるとき、ファイル保存するのを止めている
# 〇0326 _BOTTOMで下からサイズを変えるとき、MOUSEBUTTONDOWNでファイル保存する
# 〇0327 Ctrl+Shift+z やり直し（Redo）をサポート
# 〇0328 MOU_CLICK_RIGHTもファイル保存タイミングを変える
# 〇0329 MOU_CLICK_MOVABLEもファイル保存タイミングを変える
# 〇0330 設計／実行トグルは不要
# 〇0331 設計時、重なった下のバーが動かせるようにする
# 〇0332 設計時、重なった下の要素が動かせるか確認
# 〇0333 ctrl+dで消せるのがグループ２だけという制約
# 〇0334 ./data/のtemp_で始まるファイルを削除
# 〇0337 選んだグループのみ、移動バーを出す
# 〇0338 Rectangleを作るとき、どこでpを保存するかを考える
# 〇0339 コンポーネントでも、設計時クリックしたらそこを設計の選択グループにする
# 〇0340 グループが重なって下になっていても、アウトラインは最後に描画
# 〇0342 移動バーは、押されている判定を最初にする
# 〇0344 設計モードでは、グループ内すべて左クリックはグループクリック、右クリックは要素クリック
# 〇0345 グループ選択後、そのグループの移動は、グループ全体できる
# 〇0346 左上、右下棒ができない
# 〇0347 まず右棒・下棒・残り全体で横拡大・縦拡大・移動をこなす
# 〇0349 下棒で、少し下をクリックするとgroup_noがー１になってしまう
# 〇0350 左上の表示を止める
# 〇0351 他のグループでも、移動バーのときは座標だけで考える
# 〇0352 すでにselect_group_noが決まっていて、座標が下棒のときは、select_group_noの変更をしない
# 〇0353 設計でグループを選択中削除されたら、選択グループを-1にする
# 〇0354 設計で１つのコンポーネントを選択中削除されたら、選択グループの表示を-1にする
# 〇0355 関係ないボタン上での右クリックは無視
# 〇0356 ２つあるボタンを設計モードで１つ項目の削除をして、右棒（少し外）を持つとエラー
# 〇0357 長方形を作るきっかけがおかしくなっている（空の上右下左が表示されてしまう）ので、グループの右メニューでグループの作成を作る
# 〇0358 右メニューで完全な外のときはマウスUPでメニューが残るが、中のときは消えてしまう
# 〇0359 右メニューで完全な外をクリックされたときは、リセットする
# 〇0360 右クリックで出たメニューが、MOUSEBUTTONUPで消える
# 〇0361 実行モードでボタンを押す処理が行かない
# 〇0362 右メニューで、項目の削除でエラー
# 〇0363 右メニューで、グループのタイプ変更でエラー
# 〇0364 右メニューで、グループのタイプ変更でリストが出ない
# 〇0365 delete_componentは、設計のときなので、指定がコンポーネントではなくグループになっている
# 〇0366 右メニューを押すときは、一応、コンポーネントの何番目かを入れておく
# 〇0367 単体のright_page_noは、グループ番号ではないのか？
# 〇0368 コンポーネントで右クリックのとき、self.mouse_componentとself.mouse_posは生きている
# 〇0369 右メニューの名前を「グループの削除」を一番下に
# 〇0370 右メニューの名前を「項目の削除」を下に
# 〇0371 右メニューの名前を「項目の文字変更」を「項目の文字変更」に
# 〇0372 右メニューの名前を「グループのタイプ変更」を「グループのタイプ変更」に
# 〇0373 右メニューの名前を「項目の追加」を先頭に
# 〇0374 右メニューの箱が小さい
# 〇0375 新項目のグループを、優先にする

import csv
import os
import pickle
import pygame
import random
import subprocess
import sys
from pygame.locals import *
from text import Text
import unicodedata
import glob
import webbrowser

COL_RED = (255, 0, 0)
COL_BLUE = (0, 0, 255)
COL_GREEN = (0, 255, 0)
COL_YELLOW = (255, 255, 0)
COL_WHITE = (255, 255, 255)
COL_BLACK = (0, 0, 0)
COL_GRAY = (128, 128, 128)
COL_PINK = (212, 143, 150)
COL_PURPLE = (128, 0, 128)
COL_LIGHT_BLUE = (175, 223, 228)
COL_ORANGE = (255, 165, 0)
COL_LIGHT_ORANGE = (255, 224, 0)
COL_DARK_GREEN = (1, 50, 32)
COL_LIGHT_GREEN = (208, 226, 190)
COL_LIGHT_PURPLE = (189, 154, 205)
COL_LIGHT_YELLOW = (255, 241, 171)
COL_SLIDER_LIGHT_BLUE = (0, 198, 255)
COL_SLIDER_BLUE = (0, 160, 255)

COM_WIDTH = 800
COM_HEIGHT = 600

# ルートの引数
COM____name = 0
COM____version = 1
COM____mode = 2
COM____right_mouse = 3
COM____data_path = 4
COM____margin = 5
COM____grid = 6
COM____page_no_save = 7
COM____cur_page_no = 8
COM____page_next_top = 9
COM____page_previous_top = 10
COM____CSV_file_name = 11
# COM____reserve_0 = 12
COM____reserve_1 = 12
COM____reserve_2 = 13

# ページの引数
COM___page_no = 0
COM___page_next = 1
COM___page_previous = 2
COM___page_type = 3
COM___active_frame = 4
COM___back_color = 5
COM___group_next_top = 6
COM___group_previous_top = 7
COM___group_entry_no = 8
COM___reserve_0 = 9
COM___reserve_1 = 10
COM___reserve_2 = 11

# グループの引数
COM__current_group = 0
COM__group_next = 1
COM__group_previous = 2
COM__type = 3
COM__dir = 4
COM__group_x = 5
COM__group_y = 6
COM__group_width = 7
COM__group_height = 8
COM__font_size = 9
COM__font_type = 10
COM__frame_color = 11
COM__draw_frame = 12
COM__move_exclusive = 13
COM__move_inhibit = 14
COM__move_control = 15
COM__reserve_0 = 16
COM__reserve_1 = 17
COM__reserve_2 = 18
COM__push = 19
COM__music_push = 19
COM__toggle_value = 19
COM__music_value = 20

# コンポーネントの引数
COM_text = 0
COM_x = 1
COM_y = 2
COM_width = 3
COM_height = 4
COM_temp_x = 5
COM_temp_y = 6
COM_click_offset_x = 7
COM_click_offset_y = 8
COM_font_color = 9
COM_font_light_color = 11
COM_back_color = 11
COM_font_type = 12
COM_reserve_0 = 13
COM_reserve_1 = 14
COM_reserve_2 = 15
COM_value = 16
COM_button_url = 16
COM_slider_value = 16
COM_checkbox_value = 16
COM_image_brightness = 16
COM_slider_min = 17
COM_slider_max = 18

DIR_NONE = 0
DIR_COLUMN = 1
DIR_ROW = 2

FIL_LIST_PAGE = 0
FIL_LIST_ALL = 1

FNT_GOTHIC = 0
FNT_MINCHO = 1

# グループタイプ変更の種類            
GTY_FIRST = 0
GTY_CHANGE = 1
GTY_COLUMN = 2
GTY_ROW = 3

MNU_MAIN = 0
MNU_GROUP_TYPE = 1
MNU_NEW_GROUP = 2
MNU_NUMBER = 3

# 設計／実行モード
MOD_DESIGN = 0
MOD_EXECUTE = 1

MOU_CLICK_FALSE = 0 
MOU_CLICK_CONTROL = 1
MOU_CLICK_RECTANGLE = 2 
MOU_CLICK_MOVABLE = 3 
MOU_CLICK_RIGHT = 4 
MOU_CLICK_LEFT = 5 
MOU_CLICK_BOTTOM = 6 
MOU_CLICK_TOP = 7 
MOU_CLICK_GROUP_LEFT = 8
MOU_CLICK_GROUP_RIGHT = 9
MOU_CLICK_COMPONENT_LEFT = 10 
MOU_CLICK_COMPONENT_RIGHT = 11 
MOU_CLICK_SLIDER = 12 

POS_LEFT = 0
POS_CENTER = 1
POS_CHECKBOX = 2
POS_SLIDER = 3

RGB_NONE = 0
RGB_ALL_BACK = 1
RGB_ALL_FONT = 2
RGB_PAGE_BACK = 3
RGB_PAGE_FONT = 4
RGB_GROUP_BACK = 5
RGB_GROUP_FONT = 6
RGB_COMPONENT_BACK = 7
RGB_COMPONENT_FONT = 8

TYP_FRAME = 0
TYP_BUTTON = 1
TYP_IMAGE = 2
TYP_SLIDER = 3
TYP_TOGGLE = 4
TYP_CHECKBOX = 5
TYP_MUSIC = 6
TYP_TEXT = 7
TYP_MAX = 7

component_value_None = None
draw_frame_False = False
draw_frame_True = True
group_value_None = None
move_exclusive_False = False
move_exclusive_True = True
move_inhibit_False = False
move_inhibit_True = True
move_control_False = False
move_control_True = True

RES_COMPONENT_FALSE = -7
RES_GROUP_FALSE = -77
RES_PAGE_FALSE = -777
RES_ROOT_FALSE = -7777

class Fonts:
    ###########################
    # フォントクラス    
    ###########################
    def __init__(self, size, font_type):
        ###########################
        # フォントのサイズを設定
        ###########################
        self.size = int(size)
        if font_type == FNT_GOTHIC:
            self.font = pygame.font.Font("C:/Windows/Fonts/msgothic.ttc", int(size))
        else:
            self.font = pygame.font.Font("C:/Windows/Fonts/msmincho.ttc", int(size))

    def font_size(self):
        ###########################
        # フォントのサイズを返す
        ###########################
        return self.size

class c_Input_Japanese():
    ###########################
    # 日本語入力クラス    
    ###########################
    def __init__(self, text, screen, o_Mouse_Control):
        self.mode = True
        self.text = text
        self.input_text = ""
        self.screen = screen
        self.text_surface = ""
        # self.center_w = 0
        # self.center_h = 0
        self.save_input_text = ""
        self.o_Mouse_Control = o_Mouse_Control

    def draw_in_text(self):
        ###########################
        # 中の文字を描画
        ###########################
        screen.blit(self.text_surface, (self.o_Mouse_Control.input_x+8, self.o_Mouse_Control.input_y+8))

    def draw_out_frame(self, b_fill):
        ###########################
        # 外の枠を描く
        ###########################
        if b_fill == True:
            # 塗りつぶす    
            pygame.draw.rect(self.screen, COL_WHITE, (self.o_Mouse_Control.input_x, self.o_Mouse_Control.input_y, COM_WIDTH-20, 50))
        else:
            # 赤枠を描く    
            pygame.draw.rect(self.screen, COL_RED, (self.o_Mouse_Control.input_x, self.o_Mouse_Control.input_y, COM_WIDTH-20, 50), 2)
        
    def draw_text(self, text: str, o_font) -> None:
        ###########################
        # 入力文字を描画
        ###########################
        if self.mode == True:
            # テキストの色
            self.text_surface = o_font.font.render(text, True, COL_BLACK)

            # テキストに応じて上下左右中央揃えにする
            self.draw_in_text()

            # 外の枠を描く
            self.draw_out_frame(False)

            # 更新する
            pygame.display.update()

    def decide(self):
        ###########################
        # 入力文字が確定
        ###########################
        
        if self.input_text == "":
            # 文字が存在しない            
            self.input_text = self.save_input_text
            s = self.input_text.rstrip("|")

        else:
            # 文字が存在            
            # 確定した文字列を表示
            s = self.input_text
        
        # テキストボックスに"|"を表示
        o_J.draw_text(format(self.text), o_font)  
        
        # "|"に戻す
        self.input_text = format(self.text)  

        self.input_text = ""

        return s

    def input_2(self):
        ###########################
        # ２バイト入力
        ###########################
        self.input_text = self.text.edit(event.text, event.start)

    def input_1(self):
        ###########################
        # １バイト入力
        ###########################
        self.input_text = self.text.input(event.text)

    def redraw(self):
        # 描画しなおす必要があるとき
        if "|" in self.input_text:
            # 縦棒がある
            if event.type in [KEYDOWN, TEXTEDITING, TEXTINPUT]:
                self.draw_text(self.input_text, o_font)
            self.save_input_text = self.save_input_text.rstrip("|")

        else:
            # 縦棒はない
            if self.input_text=="":
                # 入力が空白になってしまったので、前を活用
                self.input_text = self.save_input_text + "|"
                self.save_input_text = self.input_text
            else:                 
                # 今を使う"
                self.input_text = self.input_text + "|"
                self.save_input_text = self.input_text

class Mouse_Control:
    ###########################
    # マウスコントロールクラス    
    ###########################
    def __init__(self, o_page):
        ###########################
        # マウスの初期化
        ###########################
        self.o_page = o_page
        self.mouse_x = -1
        self.mouse_y = -1
        self.mouse_pos = -1
        self.mouse_component = -1
        self.mouse_temp = False
        self.mouse_mx = -1
        self.mouse_my = -1
        self.mouse_click = MOU_CLICK_FALSE
        self.button_click = False
        self.group_offset_x = 0
        self.group_offset_y = 0
        self.b_found = False
        self.select_group_when_right = -1
        self.select_component_when_right = -1
        self.border_group_width = -1
        self.margin = self.o_page.get_root_information(COM____margin)
        self.input_x = -1
        self.input_y = -1
        # Ctrl+zで戻る場所
        self.log_new = -1
        self.log_top = -1
        self.log_bottom = 0
        # 展開方向（縦がデフォルト）
        self.new_dir = DIR_COLUMN

        # ここで、タイプメニューに変更            
        # GTY_CHANGE/COLUMN/ROWでright_menuの処理を変える
        self.group_type_mode = GTY_CHANGE

    def button_push_off(self, mouse_component):
        ################################
        # ボタンプッシュオフ
        ################################
        self.o_page.set_group(mouse_component, COM__push, -1)

    def button_push_on(self, mouse_component, mouse_pos):
        ################################
        # ボタンプッシュオン
        ################################
        if self.o_page.get_group(mouse_component, COM__move_control) == True:
            # 移動できないボタンがオンなら、ボタンクリックボタンをオンにする
            self.button_click = True
        # プッシュフラグに、番号を設定する
        self.o_page.set_group(mouse_component, COM__push, mouse_pos)

    def checkbox_change_value(self, i_groups, mouse_pos):    
        ################################
        # チェックボックスの値を変更        
        ################################
        if self.o_page.get_component(i_groups, mouse_pos, COM_checkbox_value) == 1:
            self.o_page.set_component(i_groups, mouse_pos, COM_checkbox_value, -1)
        else:
            self.o_page.set_component(i_groups, mouse_pos, COM_checkbox_value, 1)

    def exclusive_reset(self, type, mouse_component, mouse_pos):
        ################################
        # 排他制御をリセット
        ################################
        if mouse_component < 0:
            # 排他の引数エラーをひっかける
            print("ERROR 001:exclusive_resetのmouse_component", mouse_component, mouse_pos)
            exit(0)
        if type in (TYP_IMAGE, TYP_BUTTON, TYP_MUSIC):
            # 画像
            if self.o_page.get_group(mouse_component, COM__move_exclusive) == True:
                # 排他的

                for i in range(self.o_page.len_component(mouse_component)):
                    if mouse_pos != i:
                        # 戻す
                        self.o_page.set_component(mouse_component, i, COM_temp_x, self.o_page.get_component(mouse_component, i, COM_x))
                        self.o_page.set_component(mouse_component, i, COM_temp_y, self.o_page.get_component(mouse_component, i, COM_y))
                        self.o_page.set_component(mouse_component, i, COM_click_offset_x, 0)
                        self.o_page.set_component(mouse_component, i, COM_click_offset_y, 0)
            else:
                pass    

    def event_key_scan(self):
        ################################
        # キーボードイベントをスキャン
        ################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # ファイルを書き出す
                # 終わる
                return False

            elif event.type == KEYDOWN:    # キー押下
                if event.key == pygame.K_ESCAPE:
                    # 一つ戻す
                    # ESC
                    self.escape_undo()

                elif event.key == pygame.K_y and event.mod & pygame.KMOD_CTRL:
                    # "Ctrl+Shift+Z が押されました！"
                    # やり直す（Redo）
                    self.escape_redo()
                    
                elif event.key == pygame.K_z and event.mod & pygame.KMOD_CTRL:
                    # "Ctrl+Z が押されました！"
                    # 元に戻す（Undo）
                    self.escape_undo()
                    
                elif event.key == pygame.K_e and event.mod & pygame.KMOD_CTRL:
                    # "Ctrl+e が押されました！"
                    # 設計モードと実行モードを交換する
                    self.o_page.switch_root_information(COM____mode)
                    # キャプションに書き出す
                    self.o_page.draw_window_title()
                    
                elif event.key == pygame.K_d and event.mod & pygame.KMOD_CTRL:
                    # "Ctrl+d が押されました！"
                    # 「ダンプ」をする
                    print(self.o_page.o_design.p)
                    print("ページ番号＝", self.o_page.page_no)
                    print(self.o_page.CSV_list)
                    print("CSV_list_selection:", self.o_page.CSV_list_selection)
                    print("CSV_list_result_by_CSV:", self.o_page.CSV_list_result_by_CSV)
                    print("CSV_list_result:", self.o_page.CSV_list_result)
                    exit(0)
                    
                elif event.key == pygame.K_c and event.mod & pygame.KMOD_CTRL:
                    # "Ctrl+c が押されました！"
                    # 「root」を一瞬プリントする
                    print(self.o_page.o_design.p[0])
                    print("ページ番号＝", self.o_page.page_no)
                    print(self.o_page.CSV_list)
                    print("CSV_list_selection:", self.o_page.CSV_list_selection)
                    print("CSV_list_result_by_CSV:", self.o_page.CSV_list_result_by_CSV)
                    print("CSV_list_result:", self.o_page.CSV_list_result)
                    # exit(0)
                    
                elif event.key == pygame.K_t and event.mod & pygame.KMOD_CTRL:
                    # "Ctrl+t が押されました！"
                    # ツリーをプリントする
                    self.draw_tree()
                    
                elif event.key == pygame.K_h and event.mod & pygame.KMOD_CTRL:
                    # "Ctrl+h が押されました！"
                    # htmlファイルをCSVから作成する
                    self.o_page.write_html_by_CSV(self.o_page.CSV_list)
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ################################
                # マウスダウン
                ################################
                # マージンを計算
                # self.margin = self.o_page.get_root_information(COM____margin)
                # クリック時に、マウスの位置情報を初期化
                self.mouse_pos = -1
                self.mouse_component = -1

                # マウスクリックの場所
                mx, my = pygame.mouse.get_pos()
                mx = mx * rate_x
                my = my * rate_y    

                y_debug("　＋＋＋　マウスダウン時の状態", self.o_page.get_root_information(COM____right_mouse))

                #77777777
                # 左下でコピーライト
                if (10 <= mx <= 30 and self.o_page.screen_height - 30 <= my <= self.o_page.screen_height - 10):
                    # コピーライト
                    print("CopyRight", self.o_page.screen_width, self.o_page.screen_height)
                    # exit(0)

                    # 項目の文字色の変更
                    self.o_page.page_no_save = self.o_page.page_no

                    # ファイルの選択のためのファイル名データを返す
                    print("COPYRIGHT CLICKED self.o_page.copyright_page_no" , self.o_page.copyright_page_no)
                    # ファイルリストページを選択
                    self.o_page.set_page_no(self.o_page.copyright_page_no)
                    
                    # 実行モードに移す
                    self.o_page.set_root_information(COM____mode, MOD_EXECUTE)

                # MOUSEBUTTONDOWN                
                # CLICK_FALSEのとき、ふつうにクリックされた位置を確認し、グループ内、コンポーネント内の処理を行う
                # CLICK_COMPONENT_RIGHTのとき、右メニューでクリックされた位置を確認し、右メニューの処理を行う（メニュー範囲外クリックならメニュー表示を削除）

                ###########################################
                ###########################################
                # 画面のどこをクリックされたかチェック            
                ###########################################
                ###########################################
                if self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_FALSE:
                    ###########################################
                    ###########################################
                    # 右メニューではない通常時のクリックチェック            
                    ###########################################
                    ###########################################
    
                    # 優先グループの処理                            
                    # もし設計モードで選択グループがあり左ボタンのときは、座標を調べて先に処理
                    if self.o_page.get_root_information(COM____mode) == MOD_DESIGN and self.o_page.select_group_no_on_design != -1 and\
                        event.button != 3:

                        # 選択されたグループ番号にする
                        i_groups = self.o_page.select_group_no_on_design

                        # 右棒内にいるかチェック
                        b_found_group = self.check_click_on_right_rectangle(i_groups, mx, my)
                        if b_found_group == True:
                            # 右棒内にいた
                            break 

                        # 左棒内にいるかチェック
                        #222
                        # b_found_group = self.check_click_on_left_rectangle(i_groups, mx, my)
                        # if b_found_group == True:
                        #     # 左棒内にいた
                        #     break 

                        # 下棒内にいるかチェック
                        b_found_group = self.check_click_on_bottom_rectangle(i_groups, mx, my)
                        if b_found_group == True:
                            # 下棒内にいた
                            break 

                        #222                
                        # # 上棒内にいるかチェック
                        # b_found_group = self.check_click_on_top_rectangle(i_groups, mx, my)
                        # if b_found_group == True:
                        #     # 上棒内にいた
                        #     break 


                        b_found_group = self.check_click_on_extended_group(i_groups, mx, my)

                        if b_found_group == True:

                            # 優先グループに制御ボタンがあるかチェック
                            self.search_control_button(i_groups, mx, my)
                            
                    # 優先グループ以外の処理                            
                    if self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_CONTROL:
                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_CONTROL)
                        y_debug("　＋・＋　「制御ボタン」処理", self.o_page.get_root_information(COM____right_mouse))

                    else:
                        #「制御ボタン以外」
                        
                        # コンポーネント内にあるか確認
                        self.b_found = False

                        y_debug("　＋・＋　リスト探索前の状態", self.o_page.get_root_information(COM____right_mouse))

                        # ここに、グループ双方向リストを入れる
                        f_start = True
                        while True:
                            # グループがないなら即作成
                            if self.o_page.get_page_information(COM___group_entry_no) == 0:
                                # 既存のグループなし
                                self.b_found = False
                                # グループでもコンポーネントでもない    
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
                                i_groups = -1
                                break

                            else:
                                # 既存のグループあり    
                                #################################################
                                # グループを双方向リスト探索：前処理
                                #################################################
                                if f_start == True:
                                    # グループ終了を設定
                                    i_groups = self.o_page.get_page_information(COM___group_previous_top)
                                    f_start = False
                                else:
                                    # 前のグループを表示
                                    i_groups = self.o_page.get_group(i_groups, COM__group_previous)                       

                                #################################################
                                # グループを双方向リストで移りわたるときの主処理
                                #################################################
                                
                                # print("グループ", i_groups,"でループする")
                                for i in range(self.o_page.len_component(i_groups)):

                                    # コンポーネントにいるかチェック
                                    b_found_component = self.check_click_on_component(i_groups, i, mx, my)

                                    if b_found_component == True:
                                        # コンポーネント内にいた

                                        # ここで、コンポーネント上ならその番号をself.o_page.select_component_no_on_designに設定
                                        # これによって、他の画面（RGB）で
                                        self.o_page.select_component_no_on_design = i
                                        print("select_component_no_on_design =", self.o_page.select_component_no_on_design)
                                        
                                        break 
    
                                #################################################
                                # グループを双方向リスト探索：後処理
                                #################################################
                                # グループ開始を判断
                                if  self.o_page.get_group(i_groups, COM__group_previous) == -1:
                                    # print("グループ開始に着いたので終わる")
                                    break
                                
                                if self.b_found == True:
                                    # print("コンポーネントを見つけた")
                                    break

                        if self.b_found == True:
                            # コンポーネントがクリックされた
        
                            y_debug("　＋・＋　コンポーネント発見", self.o_page.get_root_information(COM____right_mouse))
        
                            # コンポーネント
                            if event.button == 3:
                                # 右クリック
                                # もし設計モードなら右メニュー表示、選択されたグループでないときは何もしない
                                if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                                    # 設計モード
                                    if self.mouse_component == self.o_page.select_group_no_on_design:
                                        # 選択しているグループ上で右クリック
                                        
                                        # print("？？？選択しているグループ上で右クリック group_no=", self.mouse_component)
                                        
                                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_COMPONENT_RIGHT)
                                        self.mouse_click = MOU_CLICK_COMPONENT_RIGHT
                                    
                                    else:
                                        # 選択していないグループ上で右クリック
                                        # 戻す
                                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
                                        self.mouse_click = MOU_CLICK_FALSE
                                y_debug("　＋・＋　コンポーネント発見右クリック", self.o_page.get_root_information(COM____right_mouse))
                                    
                            else:
                                # 左クリック
                                # もし設計モードならグループ選択、実行ならコンポーネント選択    
                                if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                                    # 設計モード
                                    self.mouse_click = MOU_CLICK_GROUP_RIGHT

                                else:
                                    # 実行モード    
                                    self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_COMPONENT_LEFT)
                                    #222    
                                    self.mouse_click = MOU_CLICK_COMPONENT_LEFT

                                y_debug("　＋・＋　コンポーネント発見左クリック", self.o_page.get_root_information(COM____right_mouse))

                        else:
                            # コンポーネントではなかったので、グループかを判定
                            # ここに、グループ双方向リストを入れる
                            f_start = True
                            b_found_group = False
                            while True:
                                # コンポーネントがクリックされなかった
                                #################################################
                                # グループを双方向リスト探索：前処理
                                #################################################
                                if f_start == True:
                                    # グループ終了を設定
                                    i_groups = self.o_page.get_page_information(COM___group_previous_top)
                                    f_start = False
                                else:
                                    # 前のグループを表示
                                    i_groups = self.o_page.get_group(i_groups, COM__group_previous)                       

                                # 次にグループ内について調べる
                                if i_groups == -1:
                                    # グループが存在しない
                                    # グループでもコンポーネントでもない
                                    self.mouse_click == MOU_CLICK_FALSE

                                else:
                                    # グループが存在する                            

                                    # 上下左右４づつ増やしたエリアをグループ内と判定
                                    if (self.o_page.get_group(i_groups, COM__group_x)-4 <= mx \
                                        <= self.o_page.get_group(i_groups, COM__group_x) +\
                                        self.o_page.get_group(i_groups, COM__group_width)+4\
                                        and\
                                        self.o_page.get_group(i_groups, COM__group_y)-4 <= my \
                                        <= self.o_page.get_group(i_groups, COM__group_y) +\
                                        self.o_page.get_group(i_groups, COM__group_height)+4):
                                        # グループ内にある
                                        self.mouse_component = i_groups

                                        self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
                                        self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

                                        self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
                                        self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)
                                        # グループに属している    
                                        b_found_group = True

                                        if event.button == 3:
                                            # 右クリックでグループ
                                            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_GROUP_RIGHT)
                                        else:
                                            # 左クリックでグループ
                                            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_GROUP_LEFT)
                                            self.o_page.select_group_no_on_design = self.mouse_component
                                            self.o_page.select_component_no_on_design = self.mouse_pos

                                        # フォントサイズ８のときの境界グループ幅設定
                                        char_number = get_east_asian_width_count(self.o_page.get_component(self.mouse_component, i, COM_text))
                                        cur_group_width = self.o_page.get_group(self.mouse_component, COM__group_width) 
                                        cur_component_width = self.o_page.get_component(self.mouse_component, 0, COM_width) 
                                        self.border_group_width = self.margin * char_number / 2 + (cur_group_width - cur_component_width)
                                        break

                                    else:
                                        # グループでもコンポーネントでも左上・右棒・下棒でもない
                                        pass    
                                        print("マウスダウン（何もなし） 状態＝", self.o_page.get_root_information(COM____right_mouse), "選択グループ＝", self.o_page.select_group_no_on_design)

                                #################################################
                                # グループを双方向リスト探索：後処理
                                #################################################
                                # グループ開始を判断
                                if i_groups == -1:
                                    # どのグループでもなかった
                                    self.mouse_click = MOU_CLICK_FALSE
                                    break

                                else:
                                    if self.o_page.get_group(i_groups, COM__group_previous) == -1:
                                        break

                            # ループから出て、それ以外の付加情報を設定
                            if b_found_group == False:
                                # グループに存在しない

                                y_debug("　＋・＋　グループにない", self.o_page.get_root_information(COM____right_mouse))

                                # 左クリックで、左上のグループ移動部
                                if event.button == 3:
                                    if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                                        # 設計のとき
                                        
                                        y_debug("　＋・＋　右メニュー（NEW__GROUP）を作る", self.o_page.get_root_information(COM____right_mouse))

                                        ########################
                                        # ここで矩形を作っている
                                        ########################
                                        # グループの追加
                                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_RIGHT)
                                        # 左上の座標を設定
                                        self.o_page.set_group_right(COM__group_x, mx)
                                        self.o_page.set_group_right(COM__group_y, my)
                                        self.o_page.set_group_right(COM__group_width, self.margin * 2 + 4)
                                        self.o_page.set_group_right(COM__group_height, self.margin * 2 + 4)

                                        # グループ作成メニューを出す
                                        self.make_right_menu(MNU_NEW_GROUP, mx, my)

                                        self.mouse_click = MOU_CLICK_RIGHT

                                        self.group_type_mode = GTY_FIRST

                                        break
                                    else:
                                        # 実行のとき
                                        # 何もしない    
                                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
                                        self.mouse_click = MOU_CLICK_FALSE
                                        self.mouse_component = -1
                                        self.mouse_pos = -1
                                
                                else:
                                    self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
                                    self.mouse_click = MOU_CLICK_FALSE
                                    self.mouse_component = -1
                                    self.mouse_pos = -1

                                y_debug("　＋・＋　グループ発見できず左クリック", self.o_page.get_root_information(COM____right_mouse))

                            else:
                                # コンポーネントにないことが分かったうえでグループに存在する
                                self.mouse_component = i_groups
                                self.mouse_pos = -1
                                y_debug("　＋・＋　グループに存在", self.o_page.get_root_information(COM____right_mouse))

                        if self.mouse_click == MOU_CLICK_COMPONENT_LEFT:
                            # グループの種類を得て、その結果で値を変える
                            type = self.o_page.get_group(self.mouse_component, COM__type)

                            y_debug("　＋・＋　コンポーネント左の処理", self.o_page.get_root_information(COM____right_mouse))

                            if type == TYP_SLIDER:
                                # スライダーの値を変更
                                self.slider_change_value(self.mouse_component, self.mouse_pos, mx)    
                            
                                # 色見本の表示
                                if self.o_page.page_no == self.o_page.RGB_page_no:
                                    # 最終ページの場合、frameの色を変える
                                    frame_group_no = 2
                                    slider_group_no = 1    
                                    color_list = list(self.o_page.get_group(frame_group_no, COM__frame_color))
                                    print("最終ページの場合、frame2の更新前：", color_list)
                                    if self.mouse_pos == 0:
                                        # 赤
                                        red_data = int(self.o_page.get_component(slider_group_no, 0, COM_slider_value) * 255)  
                                        color_list[0] = red_data
                                        color_tuple = tuple(color_list)                    
                                        self.o_page.set_group(frame_group_no, COM__frame_color, color_tuple)                
                                    elif self.mouse_pos == 1:
                                        # 緑
                                        green_data = int(self.o_page.get_component(slider_group_no, 1, COM_slider_value) * 255)  
                                        color_list[1] = green_data
                                        color_tuple = tuple(color_list)                    
                                        self.o_page.set_group(frame_group_no, COM__frame_color, color_tuple)                
                                    elif self.mouse_pos == 2:
                                        # 青
                                        blue_data = int(self.o_page.get_component(slider_group_no, 2, COM_slider_value) * 255)  
                                        color_list[2] = blue_data
                                        color_tuple = tuple(color_list)                    
                                        self.o_page.set_group(frame_group_no, COM__frame_color, color_tuple)                
                                    print("最終ページの場合、frame2の更新後：", color_tuple)

                                self.mouse_click = MOU_CLICK_SLIDER
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_SLIDER)

                                print("スライダークリック時、mouse_click = MOU_CLICK_SLIDERに変えた", self.mouse_click)
                                break
                                                           
                            elif type == TYP_TOGGLE:
                                # トグルボタンの値を変更
                                self.toggle_change_value(self.mouse_component, self.mouse_pos)    

                            elif type == TYP_CHECKBOX:
                                # チェックボックスの値を変更        
                                self.checkbox_change_value(self.mouse_component, self.mouse_pos)    

                            elif type == TYP_MUSIC:
                                # 音楽のフラグの値を変更        
                                # ボタンプッシュオン
                                self.button_push_on(self.mouse_component, self.mouse_pos)
                                # MUSICのフラグ値を変更
                                self.music_change_value(self.mouse_component, self.mouse_pos)    

                            elif type == TYP_BUTTON:
                                # ボタンプッシュオン
                                self.button_push_on(self.mouse_component, self.mouse_pos)

                            elif type == TYP_TEXT:
                                # テキストの値を変更
                                pass
                                                                                        
                            else:
                                # それ以外は、何もしない
                                pass
                            
                        elif self.mouse_click == MOU_CLICK_COMPONENT_RIGHT:

                            y_debug("　＋・＋　コンポーネント右の処理", self.o_page.get_root_information(COM____right_mouse))
                            if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                                # 設計時のみ
                                # 右ボタン
                                # 右クリック時に、どのコンポーネントが選ばれたか
                                self.select_group_when_right = self.mouse_component

                                self.select_component_when_right = self.mouse_pos

                                self.right_click(mx, my, self.mouse_component)                    

                        elif self.mouse_click == MOU_CLICK_COMPONENT_RIGHT:
                            # 矩形
                            pass
                            
                        elif self.mouse_click == MOU_CLICK_CONTROL:
                            # 制御ボタン
                            print("MOU_CLICK_CONTROL")
                            exit(0)
                            
                        else:
                            # 左コンポーネントか右コンポーネント    
                            y_debug("　＋・＋　何もなし処理", self.o_page.get_root_information(COM____right_mouse))
                            # 見つかっていないかもしれない
                            # 左ボタン(右ボタンではない)
                            # 左上でグループ移動
                            if event.button == 3:
                                # 右クリックなので、そのまま
                                self.o_page.set_root_information(COM____right_mouse, self.mouse_click)                            
                                y_debug("　＋・＋　コンポーネント右の処理", self.o_page.get_root_information(COM____right_mouse))
                            else:    
                                # 左クリックで、もし設計モードならグループ選択に変更 
                                if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                                    y_debug("　＋・＋　コンポーネント左の処理（設計）", self.o_page.get_root_information(COM____right_mouse))
                                    if self.mouse_component != -1:
                                        # グループ番号がある
                                        # print("マウスダウン（コンポ選択→グループ） 状態１＝", self.o_page.get_root_information(COM____right_mouse), "選択グループ＝", self.o_page.select_group_no_on_design)
                                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_GROUP_LEFT)                            
                                        self.o_page.select_group_no_on_design = self.mouse_component
                                        self.o_page.select_component_no_on_design = self.mouse_pos
                                        self.mouse_pos = -1                   
                                                
                                    else:
                                        # グループ番号がない
                                        # print("マウスダウン（コンポ選択→グループ） 状態２＝", self.o_page.get_root_information(COM____right_mouse), "選択グループ＝", self.o_page.select_group_no_on_design)
                                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)                            


                                        y_debug("　＋＋＋　グループではない", self.o_page.get_root_information(COM____right_mouse))

                                        # 右メニュー（グループの追加）
                                        if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                                            if self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_FALSE:

                                                print("右メニュー（グループの追加）")

                                                self.make_right_menu(MNU_NEW_GROUP, mx, my)

                                else: 
                                    # 実行       
                                    self.o_page.set_root_information(COM____right_mouse, self.mouse_click)                            

                            y_debug("　＋・＋　コンポーネント左か左の処理", self.o_page.get_root_information(COM____right_mouse))

                elif self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_COMPONENT_RIGHT:
                    ###########################################
                    ###########################################
                    # 右メニューのどこをクリックされたかチェック            
                    ###########################################
                    ###########################################
                    # 右クリックでメニューが出ているときの処理
                    y_debug("　＋・＋　コンポーネント右クリックメニューの処理", self.o_page.get_root_information(COM____right_mouse))
                    
                    # メニューの上オフセットを得る
                    menu_offset_y = self.o_page.get_right_menu_offset_y()
                    
                    self.b_found = False
                    # print("右クリックでメニューが出ているときの処理開始", status)
                    
                    # 幅を大きくとる
                    right_menu_width = self.o_page.get_group_right(COM__group_width)# 7番目　COM__group_width = 7

                    for i in range(self.o_page.len_component_right()):
                        # mx,myがコンポーネント上にあるかチェック
                        if (self.o_page.get_component_right(i, COM_temp_x) <= mx 
                            <= self.o_page.get_component_right(i, COM_temp_x) + right_menu_width\
                            and\
                            self.o_page.get_component_right(i, COM_temp_y) - menu_offset_y <= my\
                            <= self.o_page.get_component_right(i, COM_temp_y)  - menu_offset_y+ self.o_page.get_component_right(i, COM_height)):

                            # コンポーネント内にマウスがある
                            self.mouse_pos = i

                            # 見つかった
                            self.b_found = True

                            break

                    if self.b_found == True:

                        print("＊＊＊＊ select_component_when_right=", self.select_component_when_right)

                        y_debug("　＋・＋　コンポーネント右メニューあり", self.o_page.get_root_information(COM____right_mouse))
                        if event.button != 3:
                            # 左クリックのときのみ

                            if self.o_page.get_component_right(i, COM_text) == "グループの削除":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # そのグループを削除する
                                self.o_page.delete_list(self.o_page.select_group_no_on_design)

                                # そのグループ番号を選択から外す
                                self.o_page.select_group_no_on_design = -1
                                self.o_page.select_component_no_on_design = -1
                                
                            elif self.o_page.get_component_right(i, COM_text) == "項目の追加":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                print("Save後 Esc new=", self.log_new, " top=", self.log_top, "bottom=", self.log_bottom)
                                # そのグループに項目を追加する

                                g_no = self.o_page.select_group_no_on_design
                                
                                # サイズの再計算

                                if self.o_page.get_group(g_no, COM__dir) == DIR_COLUMN:
                                    # 下に伸ばす
                                    # g_noがグループ番号
                                    # 現在のグループの高さを保存しておく
                                    save_group_height = self.o_page.get_group(g_no, COM__group_height)

                                    # 現在のグループの幅を保存しておく
                                    save_group_width = self.o_page.get_group(g_no, COM__group_width)

                                    # 今のコンポーネントエントリ数
                                    component_entry_no = self.o_page.len_component(g_no)    

                                    # 種類を得る
                                    type_data = self.o_page.o_design.p[self.o_page.page_no+2][g_no+1][1][3]

                                    unit_x = self.o_page.get_component(g_no, 0, COM_x) - self.o_page.get_group(g_no, COM__group_x)
                                    unit_y = self.o_page.get_component(g_no, component_entry_no - 1, COM_y) - self.o_page.get_group(g_no, COM__group_y)
                                    unit_width = self.o_page.get_component(g_no, 0, COM_width)
                                    unit_height = self.o_page.get_component(g_no, 0, COM_height)
                                    group_height = self.o_page.get_group(g_no, COM__group_height)
                                    unit_offset_x = self.o_page.get_component(g_no, 0, COM_click_offset_x)
                                    unit_offset_y = self.o_page.get_component(g_no, 0, COM_click_offset_y)
                                    self.o_page.set_group(g_no, COM__group_height, group_height + unit_height + self.margin)

                                    if type_data == "Slider":
                                        # スライダーは項目を３つ増やす
                                        slider_value = self.o_page.get_component(g_no, 0, COM_slider_value)
                                        slider_min = self.o_page.get_component(g_no, 0, COM_slider_min)
                                        slider_max = self.o_page.get_component(g_no, 0, COM_slider_max)
                                        self.o_page.o_design.p[self.o_page.page_no+2][g_no+1].append(\
                                            [self.o_page.page_no, g_no, component_entry_no, type_data, [self.o_page.get_component(g_no, 0, COM_text)+\
                                                "_" + str(component_entry_no+1),\
                                                unit_x, unit_y+unit_height + self.margin,\
                                                unit_width, unit_height, unit_x, unit_y+unit_height + self.margin, unit_offset_x, unit_offset_y,\
                                                self.o_page.get_component(g_no, 0, COM_font_color), self.o_page.get_component(g_no, 0, COM_font_light_color),\
                                                self.o_page.get_component(g_no, 0, COM_back_color),\
                                                self.o_page.get_component(g_no, 0, COM_font_type),\
                                                RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, slider_value, slider_min, slider_max]])

                                    elif type_data == "CheckBox":
                                        # チェックボックスは項目を１つ増やす
                                        checkbox_value = self.o_page.get_component(g_no, 0, COM_checkbox_value)
                                        self.o_page.o_design.p[self.o_page.page_no+2][g_no+1].append(\
                                            [self.o_page.page_no, g_no, component_entry_no, type_data, [self.o_page.get_component(g_no, 0, COM_text)+\
                                                "_" + str(component_entry_no+1),\
                                                unit_x, unit_y+unit_height + self.margin,\
                                                unit_width, unit_height, unit_x, unit_y+unit_height + self.margin, unit_offset_x, unit_offset_y,\
                                                self.o_page.get_component(g_no, 0, COM_font_color), self.o_page.get_component(g_no, 0, COM_font_light_color),\
                                                self.o_page.get_component(g_no, 0, COM_back_color),\
                                                self.o_page.get_component(g_no, 0, COM_font_type),\
                                                RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, checkbox_value]])

                                    elif type_data == "Button":
                                        # ボタンはURLを入れる
                                        self.o_page.o_design.p[self.o_page.page_no+2][g_no+1].append(\
                                            [self.o_page.page_no, g_no, component_entry_no, type_data, [self.o_page.get_component(g_no, 0, COM_text)+\
                                                "_" + str(component_entry_no+1),\
                                                unit_x, unit_y+unit_height + self.margin,\
                                                unit_width, unit_height, unit_x, unit_y+unit_height + self.margin, unit_offset_x, unit_offset_y,\
                                                self.o_page.get_component(g_no, 0, COM_font_color), self.o_page.get_component(g_no, 0, COM_font_light_color),\
                                                self.o_page.get_component(g_no, 0, COM_back_color),\
                                                self.o_page.get_component(g_no, 0, COM_font_type),\
                                                RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, "URL"]])

                                    elif type_data == "Image":
                                        # 画像は255を入れる
                                        self.o_page.o_design.p[self.o_page.page_no+2][g_no+1].append(\
                                            [self.o_page.page_no, g_no, component_entry_no, type_data, [self.o_page.get_component(g_no, 0, COM_text)+\
                                                "_" + str(component_entry_no+1),\
                                                unit_x, unit_y+unit_height + self.margin,\
                                                unit_width, unit_height, unit_x, unit_y+unit_height + self.margin, unit_offset_x, unit_offset_y,\
                                                self.o_page.get_component(g_no, 0, COM_font_color), self.o_page.get_component(g_no, 0, COM_font_light_color),\
                                                self.o_page.get_component(g_no, 0, COM_back_color),\
                                                self.o_page.get_component(g_no, 0, COM_font_type),\
                                                RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, 255]])

                                    else:
                                        # スライダー以外は項目を増やさない
                                        self.o_page.o_design.p[self.o_page.page_no+2][g_no+1].append(\
                                            [self.o_page.page_no, g_no, component_entry_no, type_data, [self.o_page.get_component(g_no, 0, COM_text)+\
                                                "_" + str(component_entry_no+1),\
                                                unit_x, unit_y+unit_height + self.margin,\
                                                unit_width, unit_height, unit_x, unit_y+unit_height + self.margin, unit_offset_x, unit_offset_y,\
                                                self.o_page.get_component(g_no, 0, COM_font_color), self.o_page.get_component(g_no, 0, COM_font_light_color),\
                                                self.o_page.get_component(g_no, 0, COM_back_color),\
                                                self.o_page.get_component(g_no, 0, COM_font_type),\
                                                RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, -1]])

                                    self.o_page.set_component_root(g_no, component_entry_no, 3, type_data)

                                    # 保存しておいたグループ高さを設定
                                    self.o_page.set_group(g_no, COM__group_height, save_group_height)
                                    
                                    # 保存しておいたグループ幅を設定
                                    self.o_page.set_group(g_no, COM__group_width, save_group_width)

                                    # ※全コンポーネントの最大幅を獲得（項目の追加：DIR_COLUMN）
                                    char_number = self.calc_longest_width_of_component(g_no)

                                    # ※コンポーネント数の設定（項目の追加で１増やす：DIR_COLUMN）
                                    component_entry_no += 1

                                    # ※限界のグループの高さを得る（項目の追加：DIR_COLUMN）
                                    self.border_group_height = self.margin * (component_entry_no + 1) + 20 * component_entry_no

                                    # ※コンポーネントの高さを再計算（項目の追加：DIR_COLUMN）
                                    component_height = (save_group_height - (component_entry_no + 1) * self.margin) // component_entry_no

                                    # ※コンポーネントの幅を再計算（項目の追加：DIR_COLUMN）
                                    component_width = save_group_width - 2 * self.margin 

                                    # コンポーネントの高さの再設定
                                    for i in range(component_entry_no):
                                        self.o_page.set_component_direct(g_no, i, COM_y, self.margin * (i + 1) + component_height * i)
                                        self.o_page.set_component_direct(g_no, i, COM_temp_y, self.margin * (i + 1) + component_height * i)
                                        self.o_page.set_component_direct(g_no, i, COM_height, component_height)
                                        self.o_page.set_component_direct(g_no, i, COM_width, component_width)
                    
                                    # diffを計算する                            
                                    diff = self.calc_diff_x(mx, char_number, g_no)

                                    # コンポーネント幅から文字サイズを計算し設定
                                    self.calc_font_size(component_width, char_number, g_no)

                                elif self.o_page.get_group(g_no, COM__dir) == DIR_ROW:
                                    # 右に伸ばす
                                    component_entry_no = self.o_page.len_component(g_no)    

                                    # 現在のグループの高さを保存しておく
                                    save_group_height = self.o_page.get_group(g_no, COM__group_height)

                                    # 現在のグループの幅を保存しておく
                                    save_group_width = self.o_page.get_group(g_no, COM__group_width)

                                    # 種類を得る
                                    type_data = self.o_page.o_design.p[self.o_page.page_no+2][g_no+1][1][3]

                                    unit_x = self.o_page.get_component(g_no, component_entry_no - 1, COM_x) - self.o_page.get_group(g_no, COM__group_x)
                                    unit_y = self.o_page.get_component(g_no, 0, COM_y) - self.o_page.get_group(g_no, COM__group_y)
                                    unit_width = self.o_page.get_component(g_no, 0, COM_width)
                                    unit_height = self.o_page.get_component(g_no, 0, COM_height)
                                    group_width = self.o_page.get_group(g_no, COM__group_width)
                                    group_height = self.o_page.get_group(g_no, COM__group_height)
                                    unit_offset_x = self.o_page.get_component(g_no, 0, COM_click_offset_x)
                                    unit_offset_y = self.o_page.get_component(g_no, 0, COM_click_offset_y)
                                    # font_color = self.o_page.get_group(g_no, COM__font_color)
                                    font_color = self.o_page.get_component(g_no, 0, COM_font_color)
                                    font_light_color = self.o_page.get_component(g_no, 0, COM_font_light_color)
                                    back_color = self.o_page.get_component(g_no, 0, COM_back_color)
                                    font_type = self.o_page.get_group(g_no, COM__font_type)
                                    self.o_page.set_group(g_no, COM__group_width, group_width + unit_width + self.margin)

                                    if type_data == "Slider":
                                        # スライダーは項目を３つ増やす
                                        slider_value = self.o_page.get_component(g_no, 0, COM_slider_value)
                                        slider_min = self.o_page.get_component(g_no, 0, COM_slider_min)
                                        slider_max = self.o_page.get_component(g_no, 0, COM_slider_max)
                                        self.o_page.o_design.p[self.o_page.page_no+2][g_no+1].append(\
                                            [self.o_page.page_no, g_no, component_entry_no, type_data, [self.o_page.get_component(g_no, 0, COM_text)+\
                                                "_" + str(component_entry_no+1),\
                                                unit_x+unit_width + self.margin, unit_y,\
                                                unit_width, unit_height, unit_x+ unit_width + self.margin, unit_y, unit_offset_x, unit_offset_y,\
                                                font_color, font_light_color, back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                                                    slider_value, slider_min, slider_max]])

                                    elif type_data == "CheckBox":
                                        # チェックボックスは項目を１つ増やす
                                        checkbox_value = self.o_page.get_component(g_no, 0, COM_checkbox_value)
                                        self.o_page.o_design.p[self.o_page.page_no+2][g_no+1].append(\
                                            [self.o_page.page_no, g_no, component_entry_no, type_data, [self.o_page.get_component(g_no, 0, COM_text)+\
                                                "_" + str(component_entry_no+1),\
                                                unit_x+unit_width + self.margin, unit_y,\
                                                unit_width, unit_height, unit_x+ unit_width + self.margin, unit_y, unit_offset_x, unit_offset_y,\
                                                font_color, font_light_color, back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                                                    checkbox_value]])

                                    elif type_data == "Button":
                                        # ボタンはURLを入れる
                                        self.o_page.o_design.p[self.o_page.page_no+2][g_no+1].append(\
                                            [self.o_page.page_no, g_no, component_entry_no, type_data, [self.o_page.get_component(g_no, 0, COM_text)+\
                                                "_" + str(component_entry_no+1),\
                                                unit_x+unit_width + self.margin, unit_y,\
                                                unit_width, unit_height, unit_x+ unit_width + self.margin, unit_y, unit_offset_x, unit_offset_y,\
                                                font_color, font_light_color, back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                                                    "URL"]])

                                    else:
                                        # スライダー以外は項目を増やさない
                                        self.o_page.o_design.p[self.o_page.page_no+2][g_no+1].append(\
                                            [self.o_page.page_no, g_no, component_entry_no, type_data, [self.o_page.get_component(g_no, 0, COM_text)+\
                                                "_" + str(component_entry_no+1),\
                                                unit_x+unit_width + self.margin, unit_y,\
                                                unit_width, unit_height, unit_x+ unit_width + self.margin, unit_y, unit_offset_x, unit_offset_y,\
                                                font_color, font_light_color, back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                                                    None]])

                                    # 保存しておいたグループ高さを設定
                                    self.o_page.set_group(g_no, COM__group_height, save_group_height)
                                    
                                    # 保存しておいたグループ幅を設定
                                    self.o_page.set_group(g_no, COM__group_width, save_group_width)
                                    
                                    # ※全コンポーネントの最大幅を獲得（項目の追加：DIR_ROW）
                                    char_number = self.calc_longest_width_of_component(g_no)

                                    # ※コンポーネント数の設定（項目の追加で１増やす：DIR_ROW）
                                    component_entry_no += 1

                                    # ※コンポーネントの幅を再計算（項目の追加：DIR_ROW）
                                    component_width = (save_group_width - (component_entry_no + 1) * self.margin) // component_entry_no

                                    # コンポーネントの幅の再設定
                                    for i in range(component_entry_no):
                                        self.o_page.set_component_direct(g_no, i, COM_x, self.margin * (i + 1) + component_width * i)
                                        self.o_page.set_component_direct(g_no, i, COM_temp_x, self.margin * (i + 1) + component_width * i)
                                        # self.o_page.set_component_direct(g_no, i, COM_height, component_height)
                                        self.o_page.set_component_direct(g_no, i, COM_width, component_width)
                    
                                    # コンポーネント幅から文字サイズを計算し設定
                                    self.calc_font_size(component_width, char_number, g_no)
                                    
                                y_debug("　＋・＋　コンポーネント右に伸ばした", self.o_page.get_root_information(COM____right_mouse))
                                    
                            elif self.o_page.get_component_right(i, COM_text) == "項目のフォント変更":
                            
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                g_no = self.o_page.select_group_no_on_design

                                # 項目フォントタイプの変更
                                if self.o_page.get_component(g_no, self.select_component_when_right, COM_font_type) == FNT_MINCHO:
                                    # 明朝からゴシックへ
                                    self.o_page.set_component(g_no, self.select_component_when_right, COM_font_type, FNT_GOTHIC)
                                else:
                                    # ゴシックから明朝へ
                                    self.o_page.set_component(g_no, self.select_component_when_right, COM_font_type, FNT_MINCHO)
                                        
                                break
                                
                            elif self.o_page.get_component_right(i, COM_text) == "項目の文字色変更":
                            
                                #66666666
                                print("＊＊項目の文字色変更　self.o_page.RGB_page_no＝",self.o_page.RGB_page_no,"self.o_page.common_data_0=", self.o_page.common_data_0)
                                #66666666

                                print("＄＄＄select_group_when_right =", self.select_group_when_right)
                                print("＄＄＄select_component_when_right =", self.select_component_when_right)
                                print("＄＄＄select_component_no_on_design =", self.o_page.select_component_no_on_design)

                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 項目の文字色の変更
                                self.o_page.page_no_save = self.o_page.page_no

                                # グループ画像の変更のためグループ番号を変更
                                print(" *** 項目の文字色変更　Group_no = ", self.o_page.select_group_no_on_design)
                                self.o_page.group_no_save = self.o_page.select_group_no_on_design

                                # 右メニューの消去
                                self.finish_right_menu()

                                # RGBタイプの設定
                                self.o_page.RGB_type = RGB_COMPONENT_FONT

                                # RGB指定のためのページ番号を入れる
                                self.o_page.set_page_no(self.o_page.RGB_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)

                                print("＊＊＊項目の文字色変更　self.o_page.RGB_page_no＝",self.o_page.RGB_page_no,"self.o_page.common_data_0=", self.o_page.common_data_0)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "項目の背景色変更":
                            
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 項目の背景色の変更
                                self.o_page.page_no_save = self.o_page.page_no

                                # グループ画像の変更のためグループ番号を変更
                                print(" *** 項目の背景色変更　Group_no = ", self.o_page.select_group_no_on_design)
                                self.o_page.group_no_save = self.o_page.select_group_no_on_design

                                # 右メニューの消去
                                self.finish_right_menu()

                                # RGBタイプの設定
                                self.o_page.RGB_type = RGB_COMPONENT_BACK

                                # RGB指定のためのページ番号を入れる
                                self.o_page.set_page_no(self.o_page.RGB_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)
                                print("項目の背景色変更　self.o_page.RGB_page_no＝",self.o_page.RGB_page_no,"self.o_page.common_data_0=", self.o_page.common_data_0)
                                #66666666
                                break

                            elif self.o_page.get_component_right(i, COM_text) == "グループのタイプ変更":
                            
                                # 元に戻した
                                
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # ここで、タイプメニューに変更            
                                self.group_type_mode = GTY_CHANGE

                                # そのグループに項目を変更する
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_COMPONENT_RIGHT)                            

                                # グループタイプの変更
                                self.make_right_menu(MNU_GROUP_TYPE, mx, my)

                                break
                                
                            elif self.o_page.get_component_right(i, COM_text) == "グループのフォント変更":
                            
                                # 元に戻した
                                
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                g_no = self.o_page.select_group_no_on_design

                                # グループフォントタイプの変更
                                if self.o_page.get_component(g_no, 0, COM_font_type) == FNT_MINCHO:
                                    # 明朝からゴシックへ
                                    for j in range(self.o_page.len_component(g_no)):
                                        self.o_page.set_component(g_no, j, COM_font_type, FNT_GOTHIC)
                                else:
                                    # ゴシックから明朝へ
                                    for j in range(self.o_page.len_component(g_no)):
                                        self.o_page.set_component(g_no, j, COM_font_type, FNT_MINCHO)
                                        
                                break
                                
                            elif self.o_page.get_component_right(i, COM_text) == "このページのフォント変更":
                            
                                # 元に戻した
                                
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                for g_no in range(self.o_page.len_group()-1):
                                    # グループフォントタイプの変更
                                    if self.o_page.get_component(g_no, 0, COM_font_type) == FNT_MINCHO:
                                        # 明朝からゴシックへ
                                        for j in range(self.o_page.len_component(g_no)):
                                            self.o_page.set_component(g_no, j, COM_font_type, FNT_GOTHIC)
                                    else:
                                        # ゴシックから明朝へ
                                        for j in range(self.o_page.len_component(g_no)):
                                            self.o_page.set_component(g_no, j, COM_font_type, FNT_MINCHO)
                                        
                                break
                                
                            elif self.o_page.get_component_right(i, COM_text) == "グループの文字色変更":
                            
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 項目の文字色の変更
                                self.o_page.page_no_save = self.o_page.page_no

                                # グループ画像の変更のためグループ番号を変更
                                print(" *** グループの文字色変更　Group_no = ", self.o_page.select_group_no_on_design)
                                self.o_page.group_no_save = self.o_page.select_group_no_on_design

                                # 右メニューの消去
                                self.finish_right_menu()

                                # RGBタイプの設定
                                self.o_page.RGB_type = RGB_GROUP_FONT

                                # RGB指定のためのページ番号を入れる
                                self.o_page.set_page_no(self.o_page.RGB_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)
                                print("項目の文字色変更　self.o_page.RGB_page_no＝",self.o_page.RGB_page_no,"self.o_page.common_data_0=", self.o_page.common_data_0)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "このページの文字色変更":
                            
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 項目の文字色の変更
                                self.o_page.page_no_save = self.o_page.page_no

                                # グループ画像の変更のためグループ番号を変更
                                self.o_page.group_no_save = self.o_page.select_group_no_on_design

                                # 右メニューの消去
                                self.finish_right_menu()

                                # RGBタイプの設定
                                self.o_page.RGB_type = RGB_PAGE_FONT

                                # RGB指定のためのページ番号を入れる
                                self.o_page.set_page_no(self.o_page.RGB_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)
                                print("項目の文字色変更　self.o_page.RGB_page_no＝",self.o_page.RGB_page_no,"self.o_page.common_data_0=", self.o_page.common_data_0)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "全ページの文字色変更":
                            
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 項目の文字色の変更
                                self.o_page.page_no_save = self.o_page.page_no

                                # グループ画像の変更のためグループ番号を変更
                                self.o_page.group_no_save = self.o_page.select_group_no_on_design

                                # 右メニューの消去
                                self.finish_right_menu()

                                # RGBタイプの設定
                                self.o_page.RGB_type = RGB_ALL_FONT

                                # RGB指定のためのページ番号を入れる
                                self.o_page.set_page_no(self.o_page.RGB_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)
                                print("項目の文字色変更　self.o_page.RGB_page_no＝",self.o_page.RGB_page_no,"self.o_page.common_data_0=", self.o_page.common_data_0)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "グループの背景色変更":
                            
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 背景色の変更
                                self.o_page.page_no_save = self.o_page.page_no

                                # グループ画像の変更のためグループ番号を変更
                                print(" *** グループの背景色変更　Group_no = ", self.o_page.select_group_no_on_design)
                                self.o_page.group_no_save = self.o_page.select_group_no_on_design

                                # 右メニューの消去
                                self.finish_right_menu()

                                # RGBタイプの設定
                                self.o_page.RGB_type = RGB_GROUP_BACK

                                # RGB指定のためのページ番号を入れる
                                # self.o_page.set_page_no(self.o_page.max_page_no)
                                self.o_page.set_page_no(self.o_page.RGB_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)
                                print("グループの背景色変更　self.o_page.RGB_page_no＝",self.o_page.RGB_page_no,"self.o_page.common_data_0=", self.o_page.common_data_0)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "最背面へ移動":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 最背面へ移動のためグループ番号を表示
                                print(" *** 最背面へ移動 group_no = ", self.o_page.select_group_no_on_design)
                                
                                # リストの表示
                                print("移動前")
                                print("Next:", self.o_page.get_page_information(COM___group_next_top))
                                print("Prev:", self.o_page.get_page_information(COM___group_previous_top))
                                self.o_page.display_list()

                                # トップに移動（選択グループ）
                                self.o_page.top_list(self.o_page.select_group_no_on_design)
                                # リストの表示
                                print("移動後")
                                print("Next:", self.o_page.get_page_information(COM___group_next_top))
                                print("Prev:", self.o_page.get_page_information(COM___group_previous_top))
                                self.o_page.display_list()

                                # 右メニューの消去
                                self.finish_right_menu()

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "最前面へ移動":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 最背面へ移動のためグループ番号を表示
                                print(" *** 最前面へ移動 group_no = ", self.o_page.select_group_no_on_design)
                                
                                # リストの表示
                                print("移動前")
                                print("Next:", self.o_page.get_page_information(COM___group_next_top))
                                print("Prev:", self.o_page.get_page_information(COM___group_previous_top))
                                self.o_page.display_list()

                                # ボトムに移動（選択グループ）
                                self.o_page.bottom_list(self.o_page.select_group_no_on_design)
                                # リストの表示
                                print("移動後")
                                print("Next:", self.o_page.get_page_information(COM___group_next_top))
                                print("Prev:", self.o_page.get_page_information(COM___group_previous_top))
                                self.o_page.display_list()

                                # 右メニューの消去
                                self.finish_right_menu()

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "画像の濃度変更":
                            
                                # 元に戻した
                                
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                g_no = self.o_page.select_group_no_on_design

                                # 画像のときだけ濃度の変更
                                if self.o_page.get_group(g_no, COM__type) == TYP_IMAGE:

                                    if self.o_page.get_component(g_no, self.select_component_when_right, COM_image_brightness) == 64:
                                        # 64->128
                                        self.o_page.set_component(g_no, self.select_component_when_right, COM_image_brightness, 128)
                                    elif self.o_page.get_component(g_no, self.select_component_when_right, COM_image_brightness) == 128:
                                        # 128->192
                                        self.o_page.set_component(g_no, self.select_component_when_right, COM_image_brightness, 192)
                                    elif self.o_page.get_component(g_no, self.select_component_when_right, COM_image_brightness) == 192:
                                        # 192->255
                                        self.o_page.set_component(g_no, self.select_component_when_right, COM_image_brightness, 255)
                                    elif self.o_page.get_component(g_no, self.select_component_when_right, COM_image_brightness) == 255:
                                        # 255->64
                                        self.o_page.set_component(g_no, self.select_component_when_right, COM_image_brightness, 64)
                                        
                                break
                                
                            elif self.o_page.get_component_right(i, COM_text) == "項目の削除":
                                # # そのグループから項目を削除する
                                
                                g_no = self.o_page.select_group_no_on_design
                                                                
                                print("コンポーネントを削除するグループ番号＝", g_no, " pos=", self.mouse_pos)
                                self.delete_component(g_no)
                                
                                y_debug("　＋・＋　項目の削除", self.o_page.get_root_information(COM____right_mouse))

                            elif self.o_page.get_component_right(i, COM_text) == "項目の文字変更":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # そのグループに項目を変更する

                                g_no = self.o_page.select_group_no_on_design
                                
                                # 日本語入力モードをオンにする
                                self.o_page.input_mode = True
                                self.o_page.input_group_no = g_no
                                self.o_page.input_component_no = self.select_component_when_right

                                # 右メニューを初期化
                                self.init_right_menu()

                                # クリック処理を止める
                                self.o_page.set_group_right(COM__group_x, -300)
                                self.o_page.set_group_right(COM__group_y, -200)

                                # コンポーネントを描画
                                self.o_page.draw(self.o_page.draw_mode)    

                                # 開始位置を設定
                                self.input_x = self.o_page.get_group(g_no, COM__group_x) + 20
                                if my < 510:
                                    # 下の場合は上に向ける    
                                    self.input_y = self.o_page.get_group(g_no, COM__group_y) + 50
                                else:
                                    # 上の場合は下に向ける    
                                    self.input_y = self.o_page.get_group(g_no, COM__group_y) - 50
                                # y_debug("　＋・＋　項目の文字変更", self.o_page.get_root_information(COM____right_mouse))

                                return True

                            elif self.o_page.get_component_right(i, COM_text) == "フレーム":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 「フレームに設定」
                                # 右メニューを初期化
                                self.init_right_menu()

                                # 旧タイプからボタンに変更・または新規でグループ作成
                                new_type = TYP_FRAME
                                g_no = self.o_page.select_group_no_on_design
                                self.change_type_or_new_group(self.o_page.page_no, self.o_page.select_group_no_on_design,\
                                    self.o_page.get_group(g_no, COM__type), new_type, mx ,my)

                            elif self.o_page.get_component_right(i, COM_text) == "ボタン":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 「ボタンに設定」
                                # 右メニューを初期化
                                self.init_right_menu()

                                # 旧タイプからボタンに変更・または新規でグループ作成
                                new_type = TYP_BUTTON
                                g_no = self.o_page.select_group_no_on_design
                                self.change_type_or_new_group(self.o_page.page_no, self.o_page.select_group_no_on_design,\
                                    self.o_page.get_group(g_no, COM__type), new_type, mx ,my)

                            elif self.o_page.get_component_right(i, COM_text) == "画像":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 「画像に設定」
                                # 右メニューを初期化
                                self.init_right_menu()

                                # 旧タイプからボタンに変更・または新規でグループ作成
                                new_type = TYP_IMAGE
                                g_no = self.o_page.select_group_no_on_design
                                self.change_type_or_new_group(self.o_page.page_no, self.o_page.select_group_no_on_design,\
                                    self.o_page.get_group(g_no, COM__type), new_type, mx ,my)

                            elif self.o_page.get_component_right(i, COM_text) == "スライダー":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 「スライダーに設定」
                                # 右メニューを初期化
                                self.init_right_menu()

                                # 旧タイプからボタンに変更・または新規でグループ作成
                                new_type = TYP_SLIDER
                                g_no = self.o_page.select_group_no_on_design
                                self.change_type_or_new_group(self.o_page.page_no, self.o_page.select_group_no_on_design,\
                                    self.o_page.get_group(g_no, COM__type), new_type, mx ,my)

                            elif self.o_page.get_component_right(i, COM_text) == "トグルボタン":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 「トグルボタンに設定」
                                # 右メニューを初期化
                                self.init_right_menu()

                                # 旧タイプからボタンに変更・または新規でグループ作成
                                new_type = TYP_TOGGLE
                                g_no = self.o_page.select_group_no_on_design
                                self.change_type_or_new_group(self.o_page.page_no, self.o_page.select_group_no_on_design,\
                                    self.o_page.get_group(g_no, COM__type), new_type, mx ,my)

                            elif self.o_page.get_component_right(i, COM_text) == "チェックボックス":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 「チェックボックスに設定」
                                # 右メニューを初期化
                                self.init_right_menu()

                                # 旧タイプからボタンに変更・または新規でグループ作成
                                new_type = TYP_CHECKBOX
                                g_no = self.o_page.select_group_no_on_design
                                self.change_type_or_new_group(self.o_page.page_no, self.o_page.select_group_no_on_design,\
                                    self.o_page.get_group(g_no, COM__type), new_type, mx ,my)

                            elif self.o_page.get_component_right(i, COM_text) == "音楽":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 「音楽に設定」
                                # 右メニューを初期化
                                self.init_right_menu()

                                # 旧タイプからボタンに変更・または新規でグループ作成
                                new_type = TYP_MUSIC
                                g_no = self.o_page.select_group_no_on_design
                                self.change_type_or_new_group(self.o_page.page_no, self.o_page.select_group_no_on_design,\
                                    self.o_page.get_group(g_no, COM__type), new_type, mx ,my)

                            elif self.o_page.get_component_right(i, COM_text) == "テキスト":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 「テキストに設定」
                                # 右メニューを初期化
                                self.init_right_menu()

                                # 旧タイプからボタンに変更・または新規でグループ作成
                                new_type = TYP_TEXT
                                g_no = self.o_page.select_group_no_on_design
                                self.change_type_or_new_group(self.o_page.page_no, self.o_page.select_group_no_on_design,\
                                    self.o_page.get_group(g_no, COM__type), new_type, mx ,my)

                            elif self.o_page.get_component_right(i, COM_text) == "グループの追加（横）":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 右メニューを初期化
                                self.init_right_menu()
                                # 旧タイプからボタンに変更

                                g_no = self.o_page.select_group_no_on_design
                                #「グループの追加（横）」に設定

                                # ここで、タイプメニューに変更            
                                self.group_type_mode = GTY_ROW

                                # そのグループに項目を変更する
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_COMPONENT_RIGHT)                            

                                # グループタイプの変更
                                self.make_right_menu(MNU_GROUP_TYPE, mx, my)

                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_RECTANGLE)
                                # 左上の座標を設定
                                self.o_page.set_group_right(COM__group_x, mx)
                                self.o_page.set_group_right(COM__group_y, my)
                                self.o_page.set_group_right(COM__group_width, self.margin * 2 + 120)
                                self.o_page.set_group_right(COM__group_height, self.margin * 2 + 90)
                                
                                # 横に展開
                                self.new_dir = DIR_ROW

                                self.mouse_click = MOU_CLICK_RECTANGLE
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_RECTANGLE)
                                break

                            elif self.o_page.get_component_right(i, COM_text) == "このページの背景の色変更":
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 背景色の変更
                                self.o_page.page_no_save = self.o_page.page_no
                                
                                # 右メニューの消去
                                self.finish_right_menu()
                                
                                # RGBタイプの設定
                                self.o_page.RGB_type = RGB_PAGE_BACK
                                
                                # ファイルの選択のためのファイル名データを返す
                                self.o_page.set_page_no(self.o_page.RGB_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)

                                self.o_page.set_page_information(COM___back_color, self.o_page.common_data_0)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "このページの背景の画像変更":
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 背景色の変更
                                self.o_page.page_no_save = self.o_page.page_no
                                
                                # 右メニューの消去
                                self.finish_right_menu()
                                
                                # ファイルリストタイプの設定
                                self.o_page.file_list_type = FIL_LIST_PAGE

                                # トグル保存場所をリセット
                                self.o_page.set_group(1, COM__toggle_value, -1)

                                # ファイルの選択のためのファイル名データを返す
                                # ファイルリストページを選択
                                self.o_page.set_page_no(self.o_page.file_list_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "全ページの背景の色変更":
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 背景色の変更
                                self.o_page.page_no_save = self.o_page.page_no
                                
                                # 右メニューの消去
                                self.finish_right_menu()
                                
                                # RGBタイプの設定
                                self.o_page.RGB_type = RGB_ALL_BACK
                                
                                # ファイルの選択のためのファイル名データを返す
                                self.o_page.set_page_no(self.o_page.RGB_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "全ページの文字色変更":
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 背景色の変更
                                self.o_page.page_no_save = self.o_page.page_no
                                
                                # 右メニューの消去
                                self.finish_right_menu()
                                
                                # ファイルリストタイプの設定
                                self.o_page.file_list_type = FIL_LIST_ALL

                                # トグル保存場所をリセット
                                self.o_page.set_group(1, COM__toggle_value, -1)

                                # ファイルの選択のためのファイル名データを返す
                                # ファイルリストページを選択
                                self.o_page.set_page_no(self.o_page.file_list_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "全ページの背景の画像変更":
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 背景色の変更
                                self.o_page.page_no_save = self.o_page.page_no
                                
                                # 右メニューの消去
                                self.finish_right_menu()
                                
                                # ファイルリストタイプの設定
                                self.o_page.file_list_type = FIL_LIST_ALL

                                # トグル保存場所をリセット
                                self.o_page.set_group(1, COM__toggle_value, -1)

                                # ファイルの選択のためのファイル名データを返す
                                # ファイルリストページを選択
                                self.o_page.set_page_no(self.o_page.file_list_page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "新しいページの追加":
                                # 直前にpを保存する
                                self.save_for_escape_undo()

                                # 右メニューの消去
                                self.finish_right_menu()

                                print("新しいページの追加前")

                                self.draw_tree()

                                #「New」を使う
                                work_CSV = 'New,"新規のページ"'
                                self.o_page.create_page_new_by_CSV(work_CSV)

                                # print(self.o_page.o_design.p)
                                
                                # ページ番号の増加
                                self.o_page.page_no += 1
                                                                
                                # 最大ページ番号の更新
                                self.o_page.max_page_no = self.o_page.page_no - 3
                                
                                self.o_page.CSV_list_selection += 1

                                print("新しいページの追加後")
                                self.draw_tree()

                                # ファイルの選択のためのファイル名データを返す
                                # ファイルリストページを選択
                                self.o_page.set_page_no(self.o_page.page_no)
                                
                                # 実行モードに移す
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)

                                break

                            elif self.o_page.get_component_right(i, COM_text) == "グループの追加（縦）":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 右メニューを初期化
                                self.init_right_menu()
                                # 旧タイプからボタンに変更

                                g_no = self.o_page.select_group_no_on_design
                                #「グループの追加（縦）」に設定

                                # ここで、タイプメニューに変更            
                                self.group_type_mode = GTY_COLUMN

                                # そのグループに項目を変更する
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_COMPONENT_RIGHT)                            

                                # グループタイプの変更
                                self.make_right_menu(MNU_GROUP_TYPE, mx, my)

                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_RECTANGLE)
                                # 左上の座標を設定
                                self.o_page.set_group_right(COM__group_x, mx)
                                self.o_page.set_group_right(COM__group_y, my)
                                self.o_page.set_group_right(COM__group_width, self.margin * 2 + 120)
                                self.o_page.set_group_right(COM__group_height, self.margin * 2 + 90)
                                
                                # 縦に展開
                                self.new_dir = DIR_COLUMN

                                self.mouse_click = MOU_CLICK_RECTANGLE
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_RECTANGLE)
                                break

                            elif self.o_page.get_component_right(i, COM_text) == "グループの追加（横）":
                                # 直前にpを保存する
                                self.save_for_escape_undo()
                                # 右メニューを初期化
                                self.init_right_menu()
                                # 旧タイプからボタンに変更

                                g_no = self.o_page.select_group_no_on_design
                                #「グループの追加（縦）」に設定

                                # ここで、タイプメニューに変更            
                                self.group_type_mode = GTY_ROW

                                # そのグループに項目を変更する
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_COMPONENT_RIGHT)                            

                                # グループタイプの変更
                                self.make_right_menu(MNU_GROUP_TYPE, mx, my)

                                #######################
                                # ここで矩形を作っている
                                #######################
                                
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_RECTANGLE)
                                # 左上の座標を設定
                                self.o_page.set_group_right(COM__group_x, mx)
                                self.o_page.set_group_right(COM__group_y, my)
                                self.o_page.set_group_right(COM__group_width, self.margin * 2 + 120)
                                self.o_page.set_group_right(COM__group_height, self.margin * 2 + 90)
                                
                                # 縦に展開
                                self.new_dir = DIR_ROW

                                self.mouse_click = MOU_CLICK_RECTANGLE
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_RECTANGLE)
                                break

                        else:
                            # 右ボタンなので、ここは何もしない
                            y_debug("　＋・＋　右ボタンなにもしない", self.o_page.get_root_information(COM____right_mouse))

                        # クリック処理を止める
                        self.finish_right_menu()
                        print("finish_right_menu")

                        break

                    else:
                        print("なにもみつからなかった")

                        y_debug("　＋・＋　右メニューを消す", self.o_page.get_root_information(COM____right_mouse))
                        # クリック処理を止める

                        self.finish_right_menu()
                        break

                    # 最後にリセットしてみた
                    self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
                    y_debug("　＋・＋　リセット", self.o_page.get_root_information(COM____right_mouse))
                    exit(0)

                else:
                    #999999
                    print("きっと、矩形ならここに来る")
                    y_debug("　＋・＋　FALSEとCOMPONENT_RIGHTのいずれでもない", self.o_page.get_root_information(COM____right_mouse))
                
                    y_debug("　＋・＋　FALSE", self.o_page.get_root_information(COM____right_mouse))
                
                y_debug("＊＊＊ self.o_page.get_root_information(COM____right_mouse)", self.o_page.get_root_information(COM____right_mouse))
                # print(self.o_page.get_page_information(COM___group_next_top),"!")
                
                ############################################
                ############################################
                # 以下、最初から右メニューがなかった時の処理
                ############################################
                ############################################

                # 設計時選択されたグループで右棒下棒移動
                if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                    if self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_GROUP_LEFT:
                        # 選択されたグループ番号にする
                        i_groups = self.o_page.select_group_no_on_design
                        y_debug("　＋・＋　最初から右メニューなし", self.o_page.get_root_information(COM____right_mouse))

                        if (self.o_page.get_group(i_groups, COM__group_x)-4 <= mx 
                            <= self.o_page.get_group(i_groups, COM__group_x)+4\
                            and\
                            self.o_page.get_group(i_groups, COM__group_y)+4 <= my\
                            <= self.o_page.get_group(i_groups, COM__group_y) + self.o_page.get_group(i_groups, COM__group_height)-4):
                            # グループ内右棒にある
                            self.mouse_component = i_groups
                            y_debug("　＋・＋　グループ内左棒にある", self.o_page.get_root_information(COM____right_mouse))

                            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
                            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

                            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
                            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)
                            # グループに属している    
                            b_found_group = True

                            # 左クリックで、左棒のグループ移動部
                            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_LEFT)

                            self.mouse_click = MOU_CLICK_LEFT

                            # 直前にpを保存する
                            self.save_for_escape_undo()

                        elif (self.o_page.get_group(i_groups, COM__group_x)+self.o_page.get_group(i_groups, COM__group_width)-4 <= mx 
                            <= self.o_page.get_group(i_groups, COM__group_x)+self.o_page.get_group(i_groups, COM__group_width)+4\
                            and\
                            self.o_page.get_group(i_groups, COM__group_y)+4 <= my\
                            <= self.o_page.get_group(i_groups, COM__group_y) + self.o_page.get_group(i_groups, COM__group_height)-4):
                            # グループ内右棒にある
                            self.mouse_component = i_groups
                            y_debug("　＋・＋　グループ内右棒にある", self.o_page.get_root_information(COM____right_mouse))

                            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
                            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

                            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
                            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)
                            # グループに属している    
                            b_found_group = True

                            # 左クリックで、右のグループ移動部
                            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_RIGHT)

                            self.mouse_click = MOU_CLICK_RIGHT

                            # 直前にpを保存する
                            self.save_for_escape_undo()

                        elif (self.o_page.get_group(i_groups, COM__group_x)+4 <= mx 
                            <= self.o_page.get_group(i_groups, COM__group_x) + self.o_page.get_group(i_groups, COM__group_width)-4\
                            and\
                            self.o_page.get_group(i_groups, COM__group_y)-4 <= my\
                            <= self.o_page.get_group(i_groups, COM__group_y)+4):
                            # グループ内上棒にある
                            self.mouse_component = i_groups
                            y_debug("　＋・＋　グループ内上棒にある", self.o_page.get_root_information(COM____right_mouse))

                            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
                            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

                            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
                            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)
                            # グループに属している    
                            b_found_group = True
                            self.mouse_click = MOU_CLICK_TOP

                            # 左クリックで、下のグループ移動部
                            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_TOP)

                            # フォントサイズ８のときの境界グループ幅設定
                            char_number = get_east_asian_width_count(self.o_page.get_component(self.mouse_component, 0, COM_text))
                            cur_group_width = self.o_page.get_group(self.mouse_component, COM__group_width) 
                            cur_component_width = self.o_page.get_component(self.mouse_component, 0, COM_width) 
                            self.border_group_width = self.margin * char_number / 2 + (cur_group_width - cur_component_width)

                            # 直前にpを保存する
                            self.save_for_escape_undo()

                        elif (self.o_page.get_group(i_groups, COM__group_x)+4 <= mx 
                            <= self.o_page.get_group(i_groups, COM__group_x) + self.o_page.get_group(i_groups, COM__group_width)-4\
                            and\
                            self.o_page.get_group(i_groups, COM__group_y) + self.o_page.get_group(i_groups, COM__group_height)-4 <= my\
                            <= self.o_page.get_group(i_groups, COM__group_y) + self.o_page.get_group(i_groups, COM__group_height)+4):
                            # グループ内下棒にある
                            self.mouse_component = i_groups
                            y_debug("　＋・＋　グループ内下棒にある", self.o_page.get_root_information(COM____right_mouse))

                            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
                            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

                            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
                            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)
                            # グループに属している    
                            b_found_group = True
                            self.mouse_click = MOU_CLICK_BOTTOM

                            # 左クリックで、下のグループ移動部
                            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_BOTTOM)

                            # フォントサイズ８のときの境界グループ幅設定
                            char_number = get_east_asian_width_count(self.o_page.get_component(self.mouse_component, 0, COM_text))
                            cur_group_width = self.o_page.get_group(self.mouse_component, COM__group_width) 
                            cur_component_width = self.o_page.get_component(self.mouse_component, 0, COM_width) 
                            self.border_group_width = self.margin * char_number / 2 + (cur_group_width - cur_component_width)

                            # 直前にpを保存する
                            self.save_for_escape_undo()

                        # 上下左右４づつ増やしたエリアをグループ内と判定
                        elif (self.o_page.get_group(i_groups, COM__group_x) <= mx \
                            <= self.o_page.get_group(i_groups, COM__group_x) +\
                                self.o_page.get_group(i_groups, COM__group_width)\
                            and\
                            self.o_page.get_group(i_groups, COM__group_y) <= my \
                            <= self.o_page.get_group(i_groups, COM__group_y) +\
                                self.o_page.get_group(i_groups, COM__group_height)):
                            # グループ内全体（旧左上）
                            y_debug("　＋・＋　グループ内（移動用）にいる", self.o_page.get_root_information(COM____right_mouse))
                            # グループ内にある
                            i_groups = self.o_page.select_group_no_on_design
                            self.mouse_component = i_groups

                            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
                            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

                            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
                            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)
                            # グループに属している    
                            b_found_group = True
                            if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                                # 設計なので移動可能    
                                self.mouse_click = MOU_CLICK_MOVABLE
                                # 左クリックで、左上のグループ移動部
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_MOVABLE)

                            else:
                                self.mouse_click = MOU_CLICK_FALSE
                                # 左クリックで、左上のグループ移動部
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
                                
                            print("マウスダウン（グループ発見） 状態＝", self.o_page.get_root_information(COM____right_mouse), "選択グループ＝", self.o_page.select_group_no_on_design)

                            # 直前にpを保存する
                            self.save_for_escape_undo()

                        else:
                            # 左右棒でも上下棒でもない
                            y_debug("　＋・＋　上下左右棒でないのでリセット", self.o_page.get_root_information(COM____right_mouse))

                            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
                           
                    elif self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_COMPONENT_RIGHT:
                        # 右メニューがあったときに、次回の左クリック

                        y_debug("　＋・＋　右メニューがあったときに、次回の左クリック", self.o_page.get_root_information(COM____right_mouse))
                    
                    else:
                        # 制御のときは、ここを通過
                        pass       
                           
            elif event.type == pygame.MOUSEBUTTONUP:
                ################################
                # マウスアップ
                ################################
                # マウスクリックの場所
                mx, my = pygame.mouse.get_pos()
                mx = mx * rate_x
                my = my * rate_y    

                status = self.o_page.get_root_information(COM____right_mouse)
                y_debug("　ーーー　マウスアップ最初", status)          

                if status == MOU_CLICK_COMPONENT_LEFT:
                    # print("MOU_CLICK_COMPONENT_LEFT")    
                    y_debug("　ー・ー　MOUSEUP コンポーネント左", status)          
                    type = self.o_page.get_group(self.mouse_component, COM__type)

                    if type in (TYP_BUTTON, TYP_MUSIC):
                        # ボタン解放
                        # ボタンプッシュオン
                        self.button_push_off(self.mouse_component)

                    if type == TYP_BUTTON:
                        # ボタンがcontrolのとき、何もしない
                        if self.mouse_pos == -1:
                            # 指定されていない
                            self.mouse_click = MOU_CLICK_FALSE
                            return True
                        name = self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_text)

                        if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                            # 設計時
                            if name == "終了":
                                # ページ番号を増やす    
                                sys.exit(0)
                    
                            else:
                                # 何もしない
                                y_debug("　ー・ー　MOUSEUP 「命令」何もしない", status)          
                        
                        else:
                            # 実行時
                            if name == "最初に戻る":
                                # ページ番号を増やす    
                                # 最後にリセット    
                                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)

                                self.o_page.set_page_no(0)

                                # CSV制御フラグを-1にする
                                for i in range(8):
                                    self.o_page.CSV_control[i] = -1

                            elif name == "OK":
                                # コピーライトから戻る    

                                # 設計モードに戻す
                                self.o_page.set_root_information(COM____mode, MOD_DESIGN)

                                self.o_page.page_no = self.o_page.page_no_save
                                
                                # キャプション
                                self.o_page.draw_window_title()

                            elif name == "終了":
                                # ページ番号を増やす    
                                sys.exit(0)
                        
                            elif name == "RGB値の決定":
                                # ページ番号を変える
                                # 設計モードに戻す
                                self.o_page.set_root_information(COM____mode, MOD_DESIGN)

                                print("RGB値=", (int(self.o_page.get_component(1, 0, COM_slider_value)*255),\
                                                    int(self.o_page.get_component(1, 1, COM_slider_value)*255),\
                                                    int(self.o_page.get_component(1, 2, COM_slider_value)*255)))
                                self.o_page.common_data_0 = (int(self.o_page.get_component(1, 0, COM_slider_value)*255),\
                                                    int(self.o_page.get_component(1, 1, COM_slider_value)*255),\
                                                    int(self.o_page.get_component(1, 2, COM_slider_value)*255))
                                print("RGB common_data_0 =", self.o_page.common_data_0)
                                
                                print("page_no=", self.o_page.page_no, "save_page_no=", self.o_page.page_no_save,\
                                    "select_group_no_on_design=", self.o_page.select_group_no_on_design,\
                                    "select_component_when_right=", self.select_component_when_right)
                                
                                if self.o_page.RGB_type == RGB_ALL_FONT:
                                    # ページフォントへのRGBタイプの設定

                                    self.o_page.page_no = self.o_page.page_no_save

                                    page_no = self.o_page.page_no

                                    for i in range(self.o_page.len_page()):
                                        self.o_page.page_no = i
                                        # 全グループをめぐる
                                        for g_no in range(self.o_page.len_group()-1):
                                            # 全コンポーネントをめぐる    
                                            for i_component in range(self.o_page.len_component(g_no)):
                                                self.o_page.set_component(g_no, i_component, COM_font_color, self.o_page.common_data_0)

                                    self.o_page.page_no = page_no

                                elif self.o_page.RGB_type == RGB_ALL_BACK:
                                    # 全ページの背景色
                                    print("！！！全ページ色", self.o_page.common_data_0)

                                    page_no = self.o_page.page_no
                                    for i in range(self.o_page.len_page()):
                                        self.o_page.page_no = i
                                        self.o_page.set_page_information(COM___back_color, self.o_page.common_data_0)
                                    self.o_page.page_no = page_no

                                elif self.o_page.RGB_type == RGB_PAGE_FONT:
                                    # ページフォントへのRGBタイプの設定
                                    self.o_page.page_no = self.o_page.page_no_save
                                    # 全グループをめぐる
                                    for g_no in range(self.o_page.len_group()-1):
                                        # 全コンポーネントをめぐる    
                                        for i_component in range(self.o_page.len_component(g_no)):
                                            self.o_page.set_component(g_no, i_component, COM_font_color, self.o_page.common_data_0)

                                elif self.o_page.RGB_type == RGB_PAGE_BACK:
                                    # ページ背景へのRGBタイプの設定
                                    self.o_page.page_no = self.o_page.page_no_save
                                    self.o_page.set_page_information(COM___back_color, self.o_page.common_data_0)

                                elif self.o_page.RGB_type == RGB_GROUP_FONT:
                                    # グループフォントへのRGBタイプの設定
                                    self.o_page.page_no = self.o_page.page_no_save
                                    for i_component in range(self.o_page.len_component(self.o_page.select_group_no_on_design)):
                                        self.o_page.set_component(self.o_page.select_group_no_on_design, i_component, COM_font_color, self.o_page.common_data_0)

                                elif self.o_page.RGB_type == RGB_GROUP_BACK:
                                    # グループ背景へのRGBタイプの設定
                                    self.o_page.page_no = self.o_page.page_no_save
                                    for i_component in range(self.o_page.len_component(self.o_page.select_group_no_on_design)):
                                        self.o_page.set_component(self.o_page.select_group_no_on_design, i_component, COM_back_color, self.o_page.common_data_0)

                                elif self.o_page.RGB_type == RGB_COMPONENT_FONT:
                                    # コンポーネントフォントへのRGBタイプの設定
                                    self.o_page.page_no = self.o_page.page_no_save
                                    i_component = self.select_component_when_right
                                    self.o_page.set_component(self.select_group_when_right, i_component, COM_font_color, self.o_page.common_data_0)

                                elif self.o_page.RGB_type == RGB_COMPONENT_BACK:
                                    # コンポーネント背景へのRGBタイプの設定
                                    self.o_page.page_no = self.o_page.page_no_save
                                    i_component = self.select_component_when_right
                                    self.o_page.set_component(self.select_group_when_right, i_component, COM_back_color, self.o_page.common_data_0)

                                else:
                                    print("ERROR06:RGBタイプが存在しない", self.o_page.RGB_type)
                                # self.o_page.page_no = self.o_page.page_no_save

                            elif name == "ファイルの決定":
                                # ページ番号を変える
                                # 設計モードに戻す
                                self.o_page.set_root_information(COM____mode, MOD_DESIGN)
                                # トグルから、ファイル名と、選択されたコンポーネント番号を返す
                                self.o_page.common_data_0, component_no = self.get_select_toggle_file_name()

                                self.o_page.page_no = self.o_page.page_no_save
                                
                                # 背景の変更を選ぶ
                                if self.o_page.file_list_type == FIL_LIST_PAGE:
                                    # ページの背景の変更
                                    self.o_page.set_page_information(COM___back_color, self.o_page.common_data_0)
                                elif self.o_page.file_list_type == FIL_LIST_ALL:
                                    # 全ページの背景の変更
                                    page_no = self.o_page.page_no
                                    for i in range(self.o_page.len_page()):
                                        self.o_page.page_no = i
                                        self.o_page.set_page_information(COM___back_color, self.o_page.common_data_0)
                                    self.o_page.page_no = page_no
                                
                            elif name == "シナリオの決定":
                                # ページ番号を変える
                                # 設計モードに戻す
                                self.o_page.set_root_information(COM____mode, MOD_DESIGN)
                                # シナリオを得る
                                self.o_page.common_data_0, component_no = self.get_select_toggle_file_scenario()

                                if component_no == -1:
                                    # シナリオは開始
                                    s_file_name = "page_start_program"

                                elif self.o_page.common_data_0 == "":
                                    # トグルで何も指定されなかった
                                    print("トグルで何も指定されなかった「",self.o_page.common_data_0, "」" )
                                    s_file_name = "page_start_program"

                                else:
                                    # トグルで指定された

                                    # ここで、シナリオを変更する
                                    print("シナリオ変更", self.o_page.common_data_0)
                                    s_file_name = self.o_page.common_data_0
                                    s_file_name = s_file_name[:len(s_file_name)-4]    


                                #888
                                # ルートに、CSVファイル名を保存しておく
                                self.o_page.set_root_information(COM____CSV_file_name, s_file_name)    
                                
                                print("シナリオ変更ファイル名", s_file_name)
                                # また、ここで、STARTの代わりに新シナリオに変更
                                # ページ開始を作る

                                # ページの作成
                                o_page = Page(o_design)

                                # ページ番号
                                o_page.page_no = 0

                                # 共通部を作成する
                                o_page.create_root_information()

                                # データパスを設定する
                                o_design.data_path = o_page.get_root_information(COM____data_path)

                                # CSVデータからページ作成
                                self.o_page.create_page_by_CSV(s_file_name)

                                # 実行モードに変更
                                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)

                            elif name == "キャンセル":
                                # ページ番号を変えない    
                                self.o_page.common_data_0 = -1

                                # 設計モードに戻す
                                self.o_page.set_root_information(COM____mode, MOD_DESIGN)

                                self.o_page.page_no = self.o_page.page_no_save

                            elif name == "次に進む":
                                # 実行時、次に進む
                                self.o_page.select_group_no_on_design = 0
                                
                                self.o_page.next_page_no() 

                            elif name == "前に戻る":
                                # 実行時、前に戻る
                                self.o_page.select_group_no_on_design = 0
                                
                                self.o_page.previous_page_no() 

                            else:
                                # まずSelectionを処理
                                self.calc_selection_step_size(name)
                                
                        # 最後にリセット    
                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
                        y_debug("　ーーー　MOUSEUP 「命令」リセット", status)          

                    elif status in (MOU_CLICK_GROUP_LEFT, MOU_CLICK_COMPONENT_LEFT):
                        active_frame = self.o_page.get_page_information(COM___active_frame)
                        # print("Active frame=", active_frame, "Page=", self.o_page.page_no, "mouse=", self.mouse_component, self.mouse_pos)
                        
                        if active_frame != -1:
                            # アクティブフレームがある
                            # check_frame_pos
                            if self.o_page.get_group(active_frame, COM__group_x) <= mx <=\
                                self.o_page.get_group(active_frame, COM__group_x) +\
                                self.o_page.get_group(active_frame, COM__group_width) and\
                                self.o_page.get_group(active_frame, COM__group_y) <= my <=\
                                self.o_page.get_group(active_frame, COM__group_y) +\
                                self.o_page.get_group(active_frame, COM__group_height):
                                # フレーム内にマウスがある
                                if self.o_page.get_group(self.mouse_component, COM__type)==TYP_SLIDER:
                                    y_debug("　ー・ー　MOUSEUP フレーム内マウス", status)          
                                    pass
                                else:    
                                    # マウスの位置を更新
                                    
                                    # print("inhibitでここへ来た")
                                    if  self.o_page.get_group(self.mouse_component, COM__move_inhibit) == True:
                                        # 移動禁止なので、何もしない
                                        self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_temp_x,\
                                            self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_temp_x))
                                        self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_temp_y,\
                                            self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_temp_y))
                                    else:
                                        #　移動を認める
                                        self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_temp_x, mx -\
                                            self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_click_offset_x))
                                        self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_temp_y, my -\
                                            self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_click_offset_y))
                            else:
                                # フレーム外にマウスがあるので、戻す
                                self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_temp_x ,\
                                    self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_x))
                                self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_temp_y,\
                                    self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_y))
                            # オフセットを消す
                            self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_click_offset_x, 0)
                            self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_click_offset_y, 0)
                            y_debug("　ー・ー　MOUSEUP フレーム外でリセット", status)          

                        # グループの種類を得る
                        self.o_page.set_group(self.mouse_component, COM__type, type)

                        # 排他制御をリセット
                        self.exclusive_reset(type, self.mouse_component, self.mouse_pos)

                        self.mouse_click = MOU_CLICK_FALSE
                        # リセット
                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)

                elif status == MOU_CLICK_CONTROL:
                    #######################
                    # 制御ボタン
                    #######################
                    name = self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_text)

                    print("制御ボタン「",name, "」", self.mouse_component, self.mouse_pos)

                    if name == "終了":
                        exit(0)

                    elif name == "実行":
                        # 設計モードから実行モードに移す    
                        # 設計モードと実行モードを交換する
                        self.o_page.switch_root_information(COM____mode)
                        self.o_page.draw_window_title()
                        
                    elif name == "表示":
                        # 背景を黄色で塗りつぶす
                        screen.fill(COL_WHITE)  
                        # pの表示
                        self.o_page.show_all()
                        # print("表示shwoall")
                        print(self.o_page.o_design.p)
                        exit(0)

                    elif name == "ログ":
                        # 背景を黄色で塗りつぶす
                        screen.fill(COL_WHITE)  
                        # pの表示
                        # ログのテキストを並べて表示
                        self.dump_log()
                
                    elif name == "次に進む":
                        # 設計で次に進む

                        # ページ番号を増やす
                        self.o_page.select_group_no_on_design = 0

                        if self.o_page.page_no >= self.o_page.RGB_page_no:
                            # 上限    
                            self.o_page.set_page_no(0) 
                        else:
                            # 上限ではない    
                            self.o_page.set_page_no(self.o_page.page_no+1) 

                        self.button_click = False
                        
                    elif name == "データの読込":

                        # グループ作成メニューを出す
                        self.make_right_menu(MNU_NUMBER, mx, my)

                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_GROUP_RIGHT)
                        # 左上の座標を設定
                        self.o_page.set_group_right(COM__group_x, mx)
                        self.o_page.set_group_right(COM__group_y, my)
                        self.o_page.set_group_right(COM__group_width, self.margin * 2 + 120)
                        self.o_page.set_group_right(COM__group_height, self.margin * 2 + 90)
                                
                        self.o_page.o_design.p = self.o_page.load_design("long")
                        
                        self.o_page.page_no = self.o_page.get_root_information(COM____cur_page_no)
                        self.o_page.set_page_no(self.o_page.page_no)

                        #888888

                        # CSVファイル名を読む    
                        s_file_name = self.o_page.get_root_information(COM____CSV_file_name)
                        # if type(s_file_name) is str:
                        if s_file_name != -7777:
                            # 入っている
                            print(s_file_name)
                            print(self.o_page.o_design.p[0])
                            
                            #888888
                            self.o_page.CSV_list = self.o_page.load_CSV(s_file_name)
                            if self.o_page.CSV_list == []:
                                print("空CSV")
                                exit(0)
                                
                            # CSVファイル名を読んでみる    
                            print(self.o_page.get_root_information(COM____CSV_file_name))
                            # CSVを読み込む

                            # CSVが空でないので、self.CSV_listに読み込んだ    
                            for i in range(len(self.o_page.CSV_list)):
                                for j in range(len(self.o_page.CSV_list[i])):
                                    print(self.o_page.CSV_list[i][j])

                            # CSVリストの内訳
                            self.o_page.CSV_list_selection = 0
                            self.o_page.CSV_list_result_by_CSV = 0
                            self.o_page.CSV_list_result = 0

                        #88888
                        print("データの読込　CSV_list_selection=", self.o_page.CSV_list_selection, " list_result_by_CSV",\
                            self.o_page.CSV_list_result_by_CSV ," list_result=", self.o_page.CSV_list_result)

                        # CSVデータを作成
                        print("＋＋＋＋＋＋新たにデータを読み込む１")
                        self.o_page.construct_CSV_data(s_file_name)

                        self.o_page.set_root_information(COM____CSV_file_name, s_file_name)

                        print("＋＋＋＋＋＋新たにデータを読み込む２")

                        # キャプション
                        self.o_page.draw_window_title()
                        
                        self.button_click = False

                    elif name == "データを保存":

                        print("＋＋＋＋＋＋新たにデータを書き込む１")
                        # 保存時にCSVファイル名をルートに確保    
                            
                        # グループ作成メニューを出す
                        self.make_right_menu(MNU_NUMBER, mx, my)

                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_GROUP_RIGHT)
                        # 左上の座標を設定
                        self.o_page.set_group_right(COM__group_x, mx)
                        self.o_page.set_group_right(COM__group_y, my)
                        self.o_page.set_group_right(COM__group_width, self.margin * 2 + 120)
                        self.o_page.set_group_right(COM__group_height, self.margin * 2 + 90)
                        self.o_page.save_design("long")

                        # 移動できないボタンクリック解除
                        self.button_click = False

                    elif name == "htmlを作成":
                        # htmlを作成
                        self.o_page.write_html_by_CSV(self.o_page.CSV_list)

                        # 移動できないボタンクリック解除
                        self.button_click = False

                    elif name in ("前に戻る", "ゲームを開始"):
                        # 設計で前に戻る

                        # ページ番号を減らす
                        self.o_page.select_group_no_on_design = 0

                        if self.o_page.page_no <= 0:
                            # 下限    
                            self.o_page.set_page_no(self.o_page.RGB_page_no) 
                        else:
                            # 下限ではない    
                            self.o_page.set_page_no(self.o_page.page_no-1) 

                        self.button_click = False
                        
                    else:
                        # 何もしない
                        # print("Error", name, "is not defined in mouse_control")    
                        y_debug("　ー・ー　MOUSEUP 「命令」何もしない", status)          
                    
                    # 最後にリセット    
                    self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
                    y_debug("　ーーー　MOUSEUP 「命令」リセット", status)          

                elif status == MOU_CLICK_GROUP_RIGHT:
                    # print("MOU_CLICK_GROUP_RIGHT")    
                    y_debug("　ー・ー　MOUSEUP グループ右クリック", status)          
                        # elif self.mouse_click == MOU_CLICK_GROUP:
                    # ここは、マウスアップのときに矩形なので、今は来ない    
                    pass      

                elif status == MOU_CLICK_RECTANGLE:
                    # 右クリック時の矩形作成
                    y_debug("　ー・ー　MOUSEUP 矩形 MOU_CLICK_RECTANGLE", status)          

                    # 新グループを作成
                    # ここは、新しいグループを縦か横か決めるところ
                    print("新しいグループを縦か横か決める、あえてここでグループを選ぶ右メニューを出す")          

                    # あえてここはパスし、あらたにメニューを出す                    
                    print("縦にしてみる右メニューを出す（横にしたら機能しない）")          
                    
                    self.make_right_menu(MNU_GROUP_TYPE, mx, my)
                    break                

                elif status == MOU_CLICK_COMPONENT_RIGHT:
                    # 右メニュー表示
                    y_debug("　ー・ー　MOUSEUP 矩形 MOU_CLICK_COMPONENT_RIGHT", status)          

                    #11111111
                    print("＠右メニューの座標：",self.o_page.get_group_right(COM__group_x),\
                        self.o_page.get_group_right(COM__group_y),\
                        self.o_page.get_group_right(COM__group_width),\
                        self.o_page.get_group_right(COM__group_height))
                        

                    break
                            
                # クリック処理を止める
                self.o_page.set_group_right(COM__group_x, -300)
                self.o_page.set_group_right(COM__group_y, -200)
                self.o_page.set_group_right(COM__group_width, 4)
                self.o_page.set_group_right(COM__group_height, 4)

                self.mouse_click = MOU_CLICK_FALSE
                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)

                # 右メニューをリセット
                self.init_right_menu()
                            
            elif event.type == pygame.MOUSEMOTION:
                ################################
                # マウス移動
                ################################
                
                #2222
                # print(self.o_page.get_root_information(COM____right_mouse))
                
                # 右ボタンではない通常の処理
                if self.button_click == False:
                    # マウスの位置を移動
                    self.move_mouse(self.mouse_component, self.mouse_pos)

                if self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_COMPONENT_LEFT:
                    # 画像などを左ボタンで移動する
                    if self.button_click == False:
                        # マウスの位置を移動
                        self.move_mouse(self.mouse_component, self.mouse_pos)

                elif self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_RECTANGLE:
                    # 直前にpを保存する
                    self.save_for_escape_undo()
                    # 四角を描くために、幅。高さを設定（クリック場所から現在の）
                    mx, my = pygame.mouse.get_pos()
                    mx = mx * rate_x
                    my = my * rate_y    

                    self.o_page.set_group_right(COM__group_width, mx - self.o_page.get_group_right(COM__group_x))                    
                    self.o_page.set_group_right(COM__group_height, my - self.o_page.get_group_right(COM__group_y))                    
                 
                elif self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_SLIDER:
                    # 直前にpを保存する
                    self.save_for_escape_undo()
                    # スライダーの矩形を移動する
                    # print("スライダーの矩形を移動する group=", self.mouse_component, "c_no=", self.mouse_pos)
                    mx, my = pygame.mouse.get_pos()
                    mx = mx * rate_x
                    my = my * rate_y    

                    # スライダーの矩形の位置を変える
                    self.calc_slider_pos(mx)
                 
                elif self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_MOVABLE:
                    # 直前にpを保存する
                    # グループの移動
                    if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                        # 動かせるグループ（実行時は動かせない）
                        mx, my = pygame.mouse.get_pos()
                        mx = mx * rate_x
                        my = my * rate_y    

                        # グリッドを利かす
                        grid = self.o_page.get_root_information(COM____grid)

                        self.o_page.set_group(self.mouse_component, COM__group_x,\
                            ((mx - self.group_offset_x) // grid) * grid)
                        self.o_page.set_group(self.mouse_component, COM__group_y,\
                            ((my - self.group_offset_y) // grid) * grid)

                elif self.o_page.get_root_information(COM____right_mouse) in (MOU_CLICK_RIGHT, MOU_CLICK_LEFT):
                    # グループの幅の変更

                    if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                        if self.o_page.get_group(self.mouse_component, COM__dir) == DIR_COLUMN:
                            # 横のときは、すべてのコンポーネントを伸ばす
                            mx, my = pygame.mouse.get_pos()
                            mx = mx * rate_x
                            my = my * rate_y    

                            # ※全コンポーネントの最大幅を獲得（グループの幅の変更：DIR_COLUMN）
                            char_number = self.calc_longest_width_of_component(self.mouse_component)

                            # diffを計算する                            
                            diff = self.calc_diff_x(mx, char_number, self.mouse_component)

                            # グループ幅からスペースを引いてコンポーネント幅にする                                                     
                            cur_component_width = diff - self.margin * 2
                            
                            # diffをグループの幅にする
                            self.o_page.set_group(self.mouse_component, COM__group_width, diff)

                            # 全コンポーネントの幅を変更
                            self.change_all_component_width(cur_component_width)

                            # コンポーネント幅から文字サイズを計算し設定
                            self.calc_font_size(cur_component_width, char_number, self.mouse_component)

                            # コンポーネントの幅の最小（グループの幅の変更：DIR_COLUMN）
                            # 限界の幅を得る
                            cur_group_width = self.o_page.get_group(self.mouse_component, COM__group_width) 
                            cur_component_width = self.o_page.get_component(self.mouse_component, 0, COM_width) 
                            self.border_group_width = 10 * char_number / 2 + (cur_group_width - cur_component_width)
                            print("char_number=", char_number,"コンポーネントの幅の最小:", cur_component_width, "border=",self.border_group_width)
                        
                        elif self.o_page.get_group(self.mouse_component, COM__dir) == DIR_ROW:
                            # 横のときは、高さは一緒
                            mx, my = pygame.mouse.get_pos()
                            mx = mx * rate_x
                            my = my * rate_y    

                            # 全コンポーネントの最大高を獲得
                            char_number = -1    
                            for i in range(self.o_page.len_component(self.mouse_component)):
                                # 各コンポーネントを拡大
                                # 文字数を、i番目のエントリから得る
                                l = get_east_asian_width_count(self.o_page.get_component(self.mouse_component, i, COM_text))
                                if char_number < l:
                                    char_number = l    

                            # コンポーネント数
                            component_entry_no = self.o_page.len_component(self.mouse_component)

                            # 限界の幅を得る
                            cur_group_width = self.o_page.get_group(self.mouse_component, COM__group_width) 
                            cur_component_width = self.o_page.get_component(self.mouse_component, 0, COM_width) 
                            self.border_group_width = 10 * char_number / 2 + (cur_group_width - cur_component_width)

                            # diffの設定（限界との関係による）
                            if cur_group_width == self.border_group_width:
                                # 同じなので、増やす方しか動かさない
                                diff = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
                            elif cur_group_width > self.border_group_width:
                                # ボーダー幅以上のどこでも、増やす方も減らす方も動かす（最小は、ボーダー）
                                diff = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
                            else:
                                diff = self.border_group_width
        
                            # diffの限界による修正
                            if diff < self.border_group_width:
                                # 限界を設定
                                diff = self.border_group_width

                            # グループ幅からスペースを引いてコンポーネント幅にする                                                     
                            cur_component_width = (diff - self.margin * 2 - self.margin *\
                                (component_entry_no - 1)) // component_entry_no
                            
                            # diffをグループの幅にする
                            self.o_page.set_group(self.mouse_component, COM__group_width, diff)
                            i = 0

                            # 全コンポーネントの幅を変更
                            char_number = -1    
                            for i in range(self.o_page.len_component(self.mouse_component)):
                                # 各コンポーネントを拡大
                                self.o_page.set_component(self.mouse_component, i, COM_x, self.o_page.get_group(self.mouse_component, COM__group_x)+self.margin+(cur_component_width+self.margin)*(i))
                                self.o_page.set_component(self.mouse_component, i, COM_temp_x, self.o_page.get_group(self.mouse_component, COM__group_x)+self.margin+(cur_component_width+self.margin)*(i))
                                self.o_page.set_component(self.mouse_component, i, COM_width, cur_component_width)
                                # 文字数を、i番目のエントリから得る
                                l = get_east_asian_width_count(self.o_page.get_component(self.mouse_component, i, COM_text))
                                if char_number < l:
                                    char_number = l    
                                # y座標を変更
                                self.o_page.set_component(self.mouse_component, i, COM_y, self.margin + self.o_page.get_group(self.mouse_component, COM__group_y))
                                self.o_page.set_component(self.mouse_component, i, COM_temp_y, self.margin + self.o_page.get_group(self.mouse_component, COM__group_y))

                            # コンポーネント幅から文字サイズを計算し設定
                            cur_component_width = self.o_page.get_component(self.mouse_component, i, COM_width)
                            cur_component_height = self.o_page.get_component(self.mouse_component, i, COM_height)
                            font_size_by_right = int((cur_component_width - 22) / char_number * 2)
                            font_size_by_bottom = cur_component_height - 14
                            font_size = min(font_size_by_right, font_size_by_bottom)
                            if font_size < 8:
                                font_size = 8
                            self.o_page.set_group(self.mouse_component, COM__font_size, font_size)

                            print("char_number=", char_number,"　コンポーネントの幅の最小:", cur_component_width, "border=",self.border_group_width)

                elif self.o_page.get_root_information(COM____right_mouse) in (MOU_CLICK_BOTTOM, MOU_CLICK_TOP):
                    # グループの幅の変更
                    if self.o_page.get_root_information(COM____mode) == MOD_DESIGN:
                        if self.o_page.get_group(self.mouse_component, COM__dir) == DIR_COLUMN:
                            ###########################    
                            # 縦に並ぶ項目で縦に拡大縮小
                            ###########################    
                            # 縦のときは、幅は一緒
                            mx, my = pygame.mouse.get_pos()
                            mx = mx * rate_x
                            my = my * rate_y    

                            # ※全コンポーネントの最大幅を獲得（グループの幅の変更：DIR_COLUMN）
                            char_number = self.calc_longest_width_of_component(self.mouse_component)

                            # ※コンポーネント数の設定（グループの幅の変更：DIR_COLUMN）
                            component_entry_no = self.o_page.len_component(self.mouse_component)
            
                            # ※限界のグループの高さを得る（グループの幅の変更：DIR_COLUMN）
                            self.border_group_height = self.margin * (component_entry_no + 1) + 20 * component_entry_no

                            # 現在の高さと限界値で分類
                            cur_group_height = self.o_page.get_group(self.mouse_component, COM__group_height)
                            
                            # diffの設定（限界との関係による）
                            if self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_BOTTOM:
                                ##########################
                                # 下棒（縦）
                                ##########################
                                if cur_group_height >= self.border_group_height:
                                    # ボーダー高以上のどこでも、増やす方も減らす方も動かす（最小は、ボーダー）
                                    # 同じのとき、増やす方しか動かさない
                                    diff = my - self.o_page.get_group(self.mouse_component, COM__group_y)
                                else:
                                    diff = self.border_group_height
                                # diffの限界による修正
                                if diff < self.border_group_height:
                                    # 限界を設定
                                    diff = self.border_group_height

                                # グループ高からスペースを引いてコンポーネント高にする                                                     
                                cur_component_height = (diff - self.margin * 2 - self.margin * (component_entry_no - 1)) // component_entry_no
                                
                                # diffをグループの高さにする
                                self.o_page.set_group(self.mouse_component, COM__group_height, diff)

                            # diffの設定（限界との関係による）
                            elif self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_TOP:
                                ##########################
                                # 上棒（縦）    
                                ##########################
                                pass

                            # 全コンポーネントの高さを変更
                            char_number = -1    
                            for i in range(self.o_page.len_component(self.mouse_component)):
                                # 各コンポーネントを拡大
                                self.o_page.set_component(self.mouse_component, i, COM_y, self.o_page.get_group(self.mouse_component, COM__group_y)+self.margin+(cur_component_height+self.margin)*(i))
                                self.o_page.set_component(self.mouse_component, i, COM_temp_y, self.o_page.get_group(self.mouse_component, COM__group_y)+self.margin+(cur_component_height+self.margin)*(i))
                                self.o_page.set_component(self.mouse_component, i, COM_height, cur_component_height)
                                # 文字数を、i番目のエントリから得る
                                l = get_east_asian_width_count(self.o_page.get_component(self.mouse_component, i, COM_text))
                                if char_number < l:
                                    char_number = l    
                                # ｘ座標を変更
                                self.o_page.set_component(self.mouse_component, i, COM_x, self.margin + self.o_page.get_group(self.mouse_component, COM__group_x))
                                self.o_page.set_component(self.mouse_component, i, COM_temp_x, self.margin + self.o_page.get_group(self.mouse_component, COM__group_x))

                            # コンポーネント幅から文字サイズを計算し設定
                            cur_component_width = self.o_page.get_component(self.mouse_component, i, COM_width)
                            font_size_by_right = int((cur_component_width - 22) / char_number * 2)
                            font_size_by_bottom = cur_component_height - 14
                            font_size = min(font_size_by_right, font_size_by_bottom)
                            if font_size < 8:
                                font_size = 8
                            self.o_page.set_group(self.mouse_component, COM__font_size, font_size)

                        elif self.o_page.get_group(self.mouse_component, COM__dir) == DIR_ROW:
                            ###########################    
                            # 横に並ぶ項目で縦に拡大縮小
                            ###########################    
                            # 縦のときは、すべてのコンポーネントを伸ばす
                            mx, my = pygame.mouse.get_pos()
                            mx = mx * rate_x
                            my = my * rate_y    

                            # 全コンポーネントの最大高を獲得
                            char_number = -1    
                            for i in range(self.o_page.len_component(self.mouse_component)):
                                # 各コンポーネントを拡大
                                # 文字数を、i番目のエントリから得る
                                l = get_east_asian_width_count(self.o_page.get_component(self.mouse_component, i, COM_text))
                                if char_number < l:
                                    char_number = l    

                            # コンポーネント数
                            entry_no = 1
            
                            # 限界の高さを得る
                            cur_group_height = self.o_page.get_group(self.mouse_component, COM__group_height) 
                            cur_component_height = self.o_page.get_component(self.mouse_component, 0, COM_height) 

                            self.border_group_height = self.margin * (entry_no + 1) + 20 * entry_no

                            # diffの設定（限界との関係による）
                            if cur_group_height == self.border_group_height:
                                # 同じなので、増やす方しか動かさない
                                diff = my - self.o_page.get_group(self.mouse_component, COM__group_y)
                            elif cur_group_height > self.border_group_height:
                                # ボーダー高以上のどこでも、増やす方も減らす方も動かす（最小は、ボーダー）
                                diff = my - self.o_page.get_group(self.mouse_component, COM__group_y)
                            else:
                                diff = self.border_group_height
        
                            # diffの限界による修正
                            if diff < self.border_group_height:
                                # 限界を設定
                                diff = self.border_group_height

                            # グループ高からスペースを引いてコンポーネント高にする                                                     
                            cur_component_height = diff - self.margin * 2
                            
                            # diffをグループの高にする
                            self.o_page.set_group(self.mouse_component, COM__group_height, diff)

                            # 全コンポーネントの高を変更
                            for i in range(self.o_page.len_component(self.mouse_component)):
                                # 各コンポーネントを拡大
                                self.o_page.set_component(self.mouse_component, i, COM_height, cur_component_height)
                                # 文字数を、i番目のエントリから得る
                                l = 1
                                # y座標を変更
                                self.o_page.set_component(self.mouse_component, i, COM_y, self.margin + self.o_page.get_group(self.mouse_component, COM__group_y))
                                self.o_page.set_component(self.mouse_component, i, COM_temp_y, self.margin + self.o_page.get_group(self.mouse_component, COM__group_y))

                            # コンポーネント高から文字サイズを計算し設定
                            cur_component_width = self.o_page.get_component(self.mouse_component, 0, COM_width)
                            cur_font_size = self.o_page.get_group(self.mouse_component, COM__font_size) 
                            # この下は、そのまま使っている
                            font_size_by_right = int((cur_component_width - 22) / char_number * 2)
                            font_size_by_bottom = cur_component_height - 14
                            font_size = min(font_size_by_right, font_size_by_bottom)
                            
                            if font_size < 8:
                                font_size = 8
                            self.o_page.set_group(self.mouse_component, COM__font_size, font_size)
                        
        # 回り続ける
        return True 

    def calc_diff_x(self, mx, char_number, g_no):
        ################################
        #   縦のdiffを計算する                            
        ################################
                            
        cur_group_width = self.o_page.get_group(g_no, COM__group_width) 
        cur_component_width = self.o_page.get_component(g_no, 0, COM_width) 
        self.border_group_width = 10 * char_number / 2 + (cur_group_width - cur_component_width)

        # diffの設定（限界との関係による）
        if cur_group_width == self.border_group_width:
            # 同じなので、増やす方しか動かさない
            diff = mx - self.o_page.get_group(g_no, COM__group_x)
        elif cur_group_width > self.border_group_width:
            # ボーダー幅以上のどこでも、増やす方も減らす方も動かす（最小は、ボーダー）
            diff = mx - self.o_page.get_group(g_no, COM__group_x)
        else:
            diff = self.border_group_width

        # diffの限界による修正
        if diff < self.border_group_width:
            # 限界を設定
            diff = self.border_group_width

        return diff

    def calc_diff_y(self, my, char_number):
        ################################
        #   横のdiffを計算する                            
        ################################
                            
        cur_group_width = self.o_page.get_group(self.mouse_component, COM__group_width) 
        cur_component_width = self.o_page.get_component(self.mouse_component, 0, COM_width) 
        self.border_group_width = 10 * char_number / 2 + (cur_group_width - cur_component_width)

        # diffの設定（限界との関係による）
        if cur_group_width == self.border_group_width:
            # 同じなので、増やす方しか動かさない
            diff = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
        elif cur_group_width > self.border_group_width:
            # ボーダー幅以上のどこでも、増やす方も減らす方も動かす（最小は、ボーダー）
            diff = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
        else:
            diff = self.border_group_width

        # diffの限界による修正
        if diff < self.border_group_width:
            # 限界を設定
            diff = self.border_group_width

        return diff

    def calc_font_size(self, cur_component_width, char_number, g_no):
        ################################
        # コンポーネント幅から文字サイズを計算し設定
        ################################
        cur_component_height = self.o_page.get_component(g_no, 0, COM_height)
        cur_font_size = self.o_page.get_group(g_no, COM__font_size) 
        font_size_by_right = int((cur_component_width - 22) / char_number * 2)
        font_size_by_bottom = cur_component_height - 14
        font_size = min(font_size_by_right, font_size_by_bottom)
        if font_size < 8:
            font_size = 8
        self.o_page.set_group(g_no, COM__font_size, font_size)

    def calc_longest_width_of_component(self, g_no):
        ################################
        # コンポーネントで最長幅を返す
        ################################

        char_number = -1    
        for i in range(self.o_page.len_component(g_no)):
            # 各コンポーネントを拡大
            # 文字数を、i番目のエントリから得る
            l = get_east_asian_width_count(self.o_page.get_component(g_no, i, COM_text))
            if char_number < l:
                char_number = l    
                
        return char_number        

    def calc_slider_pos(self, mx):
        ################################
        # スライダーの位置を計算（端付）
        ################################
        left_pos = mx - self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_x)
        # 255を求める
        virtual_width = self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_slider_max) -\
            self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_slider_min)
        # 400
        real_width = self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_width)

        # 0.6->0.5
        value_data = self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_slider_value)
        slider_length = int(0.05 * real_width + value_data * (real_width * 0.9))
        print("@@@ left_pos = ", left_pos, " slider_length=", slider_length, "value_data=", value_data, "real_width=", real_width, "virtyal_width=", virtual_width)

        #1111111
        # 最小、最大のときは、左端、右端に寄せる
        if value_data == 0:
            slider_length = 0
        elif value_data == 1:
            slider_length = real_width

        # left_posを生かす
        # クリックされたところが、left_pos（real_width上）
        if left_pos < (real_width * 0.05):
            new_value_data = 0
        elif left_pos > (real_width * 0.95):
            new_value_data = 1
        else:
            new_value_data = left_pos / real_width
                        
        self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_slider_value, new_value_data)
        print("mx=", mx, " New_value_data=", new_value_data)
        print("slider_length=", slider_length, " 保存スライダー値：", self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_slider_value))

    def calc_selection_step_size(self, name):
        ################################
        # Selctionでstep_sizeを返す
        ################################
                                
        # CSVリストの内訳
        add_page_no = 0
        b_selection = False

        # ステップサイズを計算
        branch_len = []
        for i_page in range(0, self.o_page.CSV_list_selection):
            list_len = len(self.o_page.CSV_list[i_page])-2
            branch_len.append(list_len)
        # step 1,2,6
        branch_len.reverse()
        step_size = []
        for i_page in range(self.o_page.CSV_list_selection):
            if i_page == 0:
                # ０のとき特別
                step_size.append(1)
            else:
                # ０以外のとき
                x = branch_len[0]
                for j in range(1, i_page):
                    x *= branch_len[j]
                # print(i_page, x)    
                step_size.append(x)    
        # これで、各ページのステップ
        step_size.reverse()        
        print("   @@@　step_size", step_size)

        for i_page in range(0, self.o_page.CSV_list_selection):
            # list_len = (len(self.o_page.CSV_list[i_page])-2) // 2
            list_len = len(self.o_page.CSV_list[i_page])-2
            for i_component in range(list_len):
                # if name == self.o_page.CSV_list[i_page][i_component * 2 + 2]:
                if name == self.o_page.CSV_list[i_page][i_component + 2]:
                    # 選択肢（i_component番目）
                    self.o_page.CSV_control[i_page] = i_component * step_size[i_page]
                    print("＊＊＊　selectionが見つかった　i_component=", i_component, " CSV_control=", self.o_page.CSV_control, " i_page=",i_page, " step_size=",step_size)
                    # ページ番号を増やす    
                    add_page_no = 1
                    # self.o_page.set_page_no(self.o_page.page_no+1)
                    b_selection = True
                    # print("<<0>> i_page=",i_page)            
                    break
                else:
                    pass

            if b_selection == True:
                # 外側のforも処理を止める
                break

        if b_selection == True:
            # selectionで該当の文字があった
            # print("<<2>> i_page=",i_page)            
            # CSV_controlにしたがって移動するページを設定            
            # 最終質問でページ番号を増やす    
            if i_page == self.o_page.CSV_list_selection - 1:
                data = 0        
                # フラグをすべて足す
                for i in range(self.o_page.CSV_list_selection):
                    data += self.o_page.CSV_control[i]    
                print("selectionの最後：次は", self.o_page.page_no + data + 1, "ページ", i_page, self.o_page.CSV_control)
                self.o_page.set_page_no(self.o_page.page_no+data+1)
            else:
                # 単純に１ページ先に行く
                print("selectionの通常：次は", self.o_page.page_no+1, "ページ", i_page, self.o_page.CSV_control)
                self.o_page.set_page_no(self.o_page.page_no+1)

        if b_selection == False:
            # selectionの処理
            # Result_CSVの処理    
            # b_result_by_CSV = False
            # Result_by_CSVを処理
            for i_page in range(self.o_page.CSV_list_selection, self.o_page.CSV_list_selection+self.o_page.CSV_list_result_by_CSV):
                if name == self.o_page.CSV_list[i_page][3]:
                    # URLに飛ぶ
                    webbrowser.open(self.o_page.CSV_list[i_page][4])

                    break

    def change_all_component_width(self, cur_component_width):
        ################################
        # タイプ変更
        ################################
        char_number = -1    
        for i in range(self.o_page.len_component(self.mouse_component)):
            # 各コンポーネントを拡大
            self.o_page.set_component(self.mouse_component, i, COM_width, cur_component_width)
            # 文字数を、i番目のエントリから得る
            l = get_east_asian_width_count(self.o_page.get_component(self.mouse_component, i, COM_text))
            if char_number < l:
                char_number = l    
            # ｘ座標を変更
            self.o_page.set_component(self.mouse_component, i, COM_x, self.margin + self.o_page.get_group(self.mouse_component, COM__group_x))
            self.o_page.set_component(self.mouse_component, i, COM_temp_x, self.margin + self.o_page.get_group(self.mouse_component, COM__group_x))

    def change_type_or_new_group(self, p_no, g_no, old_type, new_type, mx, my):
        ################################
        # タイプ変更
        ################################
        # 旧タイプからボタンに変更・または新規でグループ作成
        if self.group_type_mode == GTY_CHANGE:
            # タイプ変更
            g_no = self.o_page.select_group_no_on_design

            old_type = self.o_page.get_group(g_no, COM__type)
            self.change_type(self.o_page.page_no, g_no, old_type, new_type)

        else:
            # 新規作成タイプグループ（横）か 新規作成タイプグループ（縦）    
            # 新グループを作成
            empty_group = self.make_new_group(mx, my)                    

            print("新グループ", self.o_page.o_design.p[2])

            # 右クリア
            self.o_page.set_group_right(COM__group_x, -300)
            self.o_page.set_group_right(COM__group_y, -200)
            self.o_page.set_group_right(COM__group_width, 4)
            self.o_page.set_group_right(COM__group_height, 4)

            # 最後にリセット    
            # 選択グループにする
            self.o_page.select_group_no_on_design = empty_group
            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_GROUP_LEFT)
            self.o_page.set_group(empty_group, COM__group_x, mx - 10)
            self.o_page.set_group(empty_group, COM__group_y, my - 10)

            old_type = self.o_page.get_group(empty_group, COM__type)
            self.change_type(self.o_page.page_no, empty_group, old_type, new_type)

    def change_type(self, p_no, g_no, old_type, new_type):
        ################################
        # タイプ変更
        ################################
        type_text = ""    

        ########################################
        # 古いほうのタイプ
        ########################################
        if old_type == TYP_FRAME:
            # Frame 何もしない
            pass
        elif old_type == TYP_BUTTON:
            # Button 何もしない
            pass
        elif old_type == TYP_IMAGE:
            # Image なにもしない
            pass
        elif old_type == TYP_SLIDER:
            # Slider コンポーネント２つ削除
            for i in range(self.o_page.len_component(g_no)):
                self.o_page.delete_component_element(g_no, i)
                self.o_page.delete_component_element(g_no, i)
        elif old_type == TYP_TOGGLE:
            # Toggle 何もしない
            pass
        elif old_type == TYP_CHECKBOX:
            # Checkbox 何もしない
            pass
        elif old_type == TYP_MUSIC:
            # グループ１つ削除
            self.o_page.delete_group_element(g_no)

        ########################################
        # 新しいほうのタイプ
        ########################################
        if new_type == TYP_BUTTON:
            # Button グループ１つ削除　コンポーネント１つ削除
            self.o_page.delete_group_element(g_no)
            self.o_page.add_group_element(g_no, -1)
            for i in range(self.o_page.len_component(g_no)):
                self.o_page.delete_component_element(g_no, i)
                self.o_page.add_component_element(g_no, i, "URL")
            type_text = "Button"

        elif new_type == TYP_IMAGE:
            # Image グループ１つ交換　コンポーネント１つ交換
            self.o_page.delete_group_element(g_no)
            self.o_page.add_group_element(g_no, None)

            print("change_type：", self.o_page.o_design.p[2])
            print("length=", self.o_page.len_component(g_no))

            type_text = "Image"
            for i in range(self.o_page.len_component(g_no)):
                self.o_page.delete_component_element(g_no, i)
                self.o_page.add_component_element(g_no, i, 255)
                #999
                print("画像の明るさ：", g_no, i, self.o_page.get_component(g_no, i, COM_image_brightness))

            print("change_type：", self.o_page.o_design.p[2])


        elif new_type == TYP_SLIDER:
            # Slider グループ１つ交換　コンポーネント１つ削除３つ追加
            self.o_page.delete_group_element(g_no)
            self.o_page.add_group_element(g_no, None)
            type_text = "Slider"
            for i in range(self.o_page.len_component(g_no)):
                self.o_page.delete_component_element(g_no, i)
                self.o_page.add_component_element(g_no, i, 0.6)
                self.o_page.add_component_element(g_no, i, 0)
                self.o_page.add_component_element(g_no, i, 9)

        elif new_type == TYP_TOGGLE:
            # Toggle グループ１つ交換
            self.o_page.delete_group_element(g_no)
            self.o_page.add_group_element(g_no, -1)
            type_text = "Toggle"

        elif new_type == TYP_CHECKBOX:
            # Checkbox グループ１つ交換　コンポーネント１つ交換
            self.o_page.delete_group_element(g_no)
            self.o_page.add_group_element(g_no, None)
            type_text = "CheckBox"
            for i in range(self.o_page.len_component(g_no)):
                self.o_page.delete_component_element(g_no, i)
                self.o_page.add_component_element(g_no, i, -1)

        elif new_type == TYP_MUSIC:
            # Music グループ１つ削除２つ追加
            self.o_page.delete_group_element(g_no)
            self.o_page.add_group_element(g_no, -1)
            self.o_page.add_group_element(g_no, -1)
            type_text = "Music"

        elif new_type == TYP_TEXT:
            #  グループ１つ交換
            self.o_page.delete_group_element(g_no)
            self.o_page.add_group_element(g_no, None)
            type_text = "Text"
            
        # 全コンポーネントのタイプを書き換える    
        for i in range(self.o_page.len_component(g_no)):
            self.o_page.set_component_root(g_no, i, 3, type_text)

        # コンポーネントの種類を変更
        self.o_page.set_group(g_no, COM__type, new_type)

        return type_text

    def check_click_on_right_rectangle(self, i_groups, mx, my):
        ################################
        # 右棒内にいるかチェック
        ################################
        b_break = False

        if (self.o_page.get_group(i_groups, COM__group_x)+self.o_page.get_group(i_groups, COM__group_width)-4 <= mx 
            <= self.o_page.get_group(i_groups, COM__group_x)+self.o_page.get_group(i_groups, COM__group_width)+4\
            and\
            self.o_page.get_group(i_groups, COM__group_y)+4 <= my\
            <= self.o_page.get_group(i_groups, COM__group_y) + self.o_page.get_group(i_groups, COM__group_height)-4):
            # グループ内右棒にある
            self.mouse_component = i_groups
            self.mouse_pos = -1

            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)

            # 左クリックで、右のグループ移動部
            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_RIGHT)

            self.mouse_click = MOU_CLICK_RIGHT
            y_debug("　＋＋＋　右棒マウスクリック", self.o_page.get_root_information(COM____right_mouse))

            # 直前にpを保存する
            self.save_for_escape_undo()
            # この後breakする
            b_break = True

        return b_break

    def check_click_on_left_rectangle(self, i_groups, mx, my):
        ################################
        # 左棒内にいるかチェック
        ################################
        b_break = False

        if (self.o_page.get_group(i_groups, COM__group_x) - 4 <= mx 
            <= self.o_page.get_group(i_groups, COM__group_x) + 4\
            and\
            self.o_page.get_group(i_groups, COM__group_y)+4 <= my\
            <= self.o_page.get_group(i_groups, COM__group_y) + self.o_page.get_group(i_groups, COM__group_height)-4):
            # グループ内右棒にある
            self.mouse_component = i_groups
            self.mouse_pos = -1

            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)
            # グループに属している    
            # b_found_group = True

            # 左クリックで、左のグループ移動部
            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_LEFT)

            self.mouse_click = MOU_CLICK_LEFT
            y_debug("　＋＋＋　左棒マウスクリック", self.o_page.get_root_information(COM____right_mouse))

            # 直前にpを保存する
            self.save_for_escape_undo()
            # この後breakする
            b_break = True

        return b_break

    def check_click_on_bottom_rectangle(self, i_groups, mx, my):
        ################################
        # 下棒内にいるかチェック
        ################################
        b_break = False
        
        if (self.o_page.get_group(i_groups, COM__group_x)+4 <= mx 
            <= self.o_page.get_group(i_groups, COM__group_x) + self.o_page.get_group(i_groups, COM__group_width)-4\
            and\
            self.o_page.get_group(i_groups, COM__group_y) + self.o_page.get_group(i_groups, COM__group_height)-4 <= my\
            <= self.o_page.get_group(i_groups, COM__group_y) + self.o_page.get_group(i_groups, COM__group_height)+4):
            # グループ内下棒にある
            self.mouse_component = i_groups
            self.mouse_pos = -1

            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)

            # グループに属している    
            self.mouse_click = MOU_CLICK_BOTTOM

            # 左クリックで、下のグループ移動部
            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_BOTTOM)

            # フォントサイズ８のときの境界グループ幅設定
            char_number = get_east_asian_width_count(self.o_page.get_component(self.mouse_component, 0, COM_text))
            cur_group_width = self.o_page.get_group(self.mouse_component, COM__group_width) 
            cur_component_width = self.o_page.get_component(self.mouse_component, 0, COM_width) 
            self.border_group_width = self.margin * char_number / 2 + (cur_group_width - cur_component_width)

            y_debug("　＋＋＋　下棒マウスクリック", self.o_page.get_root_information(COM____right_mouse))
            # 直前にpを保存する
            self.save_for_escape_undo()
            # この後breakする
            b_break = True

        return b_break

    def check_click_on_top_rectangle(self, i_groups, mx, my):
        ################################
        # 上棒内にいるかチェック
        ################################
        b_break = False
        
        if (self.o_page.get_group(i_groups, COM__group_x)+4 <= mx 
            <= self.o_page.get_group(i_groups, COM__group_x) + self.o_page.get_group(i_groups, COM__group_width)-4\
            and\
            self.o_page.get_group(i_groups, COM__group_y) - 4 <= my\
            <= self.o_page.get_group(i_groups, COM__group_y) + 4):
            # グループ内下棒にある
            self.mouse_component = i_groups
            self.mouse_pos = -1

            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)
            # グループに属している    
            # b_found_group = True
            self.mouse_click = MOU_CLICK_TOP

            # 左クリックで、下のグループ移動部
            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_TOP)

            # フォントサイズ８のときの境界グループ幅設定
            char_number = get_east_asian_width_count(self.o_page.get_component(self.mouse_component, 0, COM_text))
            cur_group_width = self.o_page.get_group(self.mouse_component, COM__group_width) 
            cur_component_width = self.o_page.get_component(self.mouse_component, 0, COM_width) 
            self.border_group_width = self.margin * char_number / 2 + (cur_group_width - cur_component_width)

            y_debug("　＋＋＋　上棒マウスクリック", self.o_page.get_root_information(COM____right_mouse))
            # 直前にpを保存する
            self.save_for_escape_undo()
            # この後breakする
            b_break = True

        return b_break

    def check_click_on_extended_group(self, i_groups, mx, my):
        ################################
        # 拡大したグループ域にいるかチェック
        ################################
        b_break = False

        # 上下左右４づつ増やしたエリアをグループ内と判定
        if (self.o_page.get_group(i_groups, COM__group_x) <= mx \
            <= self.o_page.get_group(i_groups, COM__group_x) +\
                self.o_page.get_group(i_groups, COM__group_width)\
            and\
            self.o_page.get_group(i_groups, COM__group_y) <= my \
            <= self.o_page.get_group(i_groups, COM__group_y) +\
                self.o_page.get_group(i_groups, COM__group_height)):
            # グループ内全体（旧左上）
            # グループ内にある
            i_groups = self.o_page.select_group_no_on_design
            self.mouse_component = i_groups
            self.mouse_pos = -1

            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)
            # グループに属している    
            self.mouse_click = MOU_CLICK_MOVABLE

            # 左クリックで、左上のグループ移動部
            self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_MOVABLE)

            y_debug("　＋＋＋　グループ（移動用）クリック", self.o_page.get_root_information(COM____right_mouse))
            # print("マウスダウン（グループ発見） 状態＝", self.o_page.get_root_information(COM____right_mouse), "選択グループ＝", self.o_page.select_group_no_on_design)

            # 直前にpを保存する
            self.save_for_escape_undo()
            # この後breakする
            print("check_click_on_extended_groupで見つけた。グループ番号＝",self.mouse_component)
            b_break = True

        # breakするかを返す
        return b_break

    def check_click_on_component(self, i_groups, i, mx, my):
        ################################
        # コンポーネントにいるかチェック
        ################################
        b_break = False

        if (self.o_page.get_component(i_groups, i, COM_temp_x) <= mx 
            <= self.o_page.get_component(i_groups, i, COM_temp_x) + self.o_page.get_component(i_groups, i, COM_width)\
            and\
            self.o_page.get_component(i_groups, i, COM_temp_y) <= my\
            <= self.o_page.get_component(i_groups, i, COM_temp_y) + self.o_page.get_component(i_groups, i, COM_height)):
            # コンポーネント内にマウスがある
            self.mouse_component = i_groups
            self.mouse_pos = i

            # その時の双方向リスト  
            # print("Check マウスボタンダウン　グループ内コンポーネント内にマウスがある", self.mouse_component,self.mouse_pos)    
            self.group_offset_x = mx - self.o_page.get_group(self.mouse_component, COM__group_x)
            self.group_offset_y = my - self.o_page.get_group(self.mouse_component, COM__group_y)

            self.o_page.set_group(self.mouse_component, COM__group_x, mx - self.group_offset_x)
            self.o_page.set_group(self.mouse_component, COM__group_y, my - self.group_offset_y)

            self.mouse_mx = mx - self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_temp_x)
            self.mouse_my = my - self.o_page.get_component(self.mouse_component, self.mouse_pos, COM_temp_y)
            
            # コンポーネントのクリックオフセットを設定
            if self.o_page.get_group(self.mouse_component, COM__type)==TYP_SLIDER:
                pass
            else:
                self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_click_offset_x, self.mouse_mx)
                self.o_page.set_component(self.mouse_component, self.mouse_pos, COM_click_offset_y, self.mouse_my)

            # 見つかった
            self.b_found = True
            b_break = True

        return b_break

    def delete_component(self, g_no):
        ################################
        # 「項目の削除」ボタンクリック
        ################################

        # そのグループから項目を削除する
        component_entry_no = self.o_page.len_component(g_no)    

        if component_entry_no == 0:
            # ０個の要素なので、何もしない
            pass
        elif component_entry_no == 1:
            # グループを消す
            # 直前にpを保存する
            self.save_for_escape_undo()
            # グループを実際に消す
            self.o_page.delete_list(g_no)
            # グループを選択していることを止める
            self.o_page.select_group_no_on_design = -1
            # self.o_page.select_component_no_on_design = -1
            
        else:
            # １個以上の要素があるので、ｎ番目を削除
            # 右クリック時に、どのコンポーネントが選ばれたか
        
            # 直前にpを保存する
            self.save_for_escape_undo()
            
            if self.o_page.get_group(g_no, COM__dir) == DIR_COLUMN:
                # 上に縮める    
                for i in range(component_entry_no - 1, self.select_component_when_right, -1):
                    self.o_page.set_component(g_no, i, COM_y, self.o_page.get_component(g_no, i-1, COM_y))
                    self.o_page.set_component(g_no, i, COM_temp_y, self.o_page.get_component(g_no, i-1, COM_temp_y))
            elif self.o_page.get_group(g_no, COM__dir) == DIR_ROW:
                # 左に縮める
                for i in range(component_entry_no - 1, self.select_component_when_right, -1):
                    self.o_page.set_component(g_no, i, COM_x, self.o_page.get_component(g_no, i-1, COM_x))
                    self.o_page.set_component(g_no, i, COM_temp_x, self.o_page.get_component(g_no, i-1, COM_temp_x))

            # 本当にリストから削除
            
            # print(self.o_page.o_design.p[self.o_page.page_no + 2][g_no + 1])
            
            self.o_page.o_design.p[self.o_page.page_no + 2][g_no + 1].pop(self.select_component_when_right+1)
            # リストにあるコンポーネント番号を修正
            for i in range(self.select_component_when_right, component_entry_no - 1):
                self.o_page.o_design.p[self.o_page.page_no + 2][g_no+1][i + 1][2] -= 1

            if self.o_page.get_group(g_no, COM__dir) == DIR_COLUMN:
                # 上に縮める    
                # グループの縦幅を減らす
                unit_height = self.o_page.get_component(g_no, 0, COM_height)
                self.o_page.set_group(g_no, COM__group_height, self.o_page.get_group(g_no, COM__group_height) - unit_height - self.margin)
            elif self.o_page.get_group(g_no, COM__dir) == DIR_ROW:
                # 左に縮める    
                # グループの横幅を減らす
                unit_width = self.o_page.get_component(g_no, 0, COM_width)
                self.o_page.set_group(g_no, COM__group_width, self.o_page.get_group(g_no, COM__group_width) - unit_width - self.margin)

    def draw_tree(self):
        ################################
        # ツリーをプリントする
        ################################
        print("ルート：", self.o_page.o_design.p[0])
        page_total = len(self.o_page.o_design.p)

        save_page_no = self.o_page.page_no

        # print("ページ数：", page_total-2)
        for i_page in range(page_total-2):
            # 各ページを表示

            # ページ番号を保存する
            self.o_page.page_no = i_page

            print("ページ=", i_page, " G_Next=", self.o_page.get_page_information(COM___group_next_top), " G_Prev=", self.o_page.get_page_information(COM___group_previous_top))
            group_total = len(self.o_page.o_design.p[i_page+2])
            # print("グループ数：", group_total)
            for i_group in range(group_total-1):
                # 各グループを表示
                print("　グループ(" + str(i_group) +", " + str(self.o_page.get_group(i_group, COM__group_next))+", " + str(self.o_page.get_group(i_group, COM__group_previous))+") ", end="")
                component_total = len(self.o_page.o_design.p[i_page+2][i_group+1])
                # print("コンポーネント数：", component_total)
                s = "　コンポーネント＝"
                for i_component in range(1, component_total):
                    s += "「" + self.o_page.o_design.p[i_page+2][i_group+1][i_component][4][COM_text]+ "」"
                    # 各コンポーネントを表示
                print(s)

            print(self.o_page.o_design.p[i_page+2])

            # ページ番号を戻す
            self.o_page.page_no = save_page_no

    def dump_log(self):
        ################################
        # 番号のログのテキスト表示
        ################################

        # 保存されたログ       
        for i in range(self.log_top+1):
            print("<<< " + "temp" + str(i).zfill(3) + ">>>", self.log_top, self.log_new, self.log_bottom)
            temp_p = self.o_page.load_design("temp"+str(i).zfill(3))
            for j in range(1, len(temp_p[2][3])):
                print(str(j-1)+ "「" + temp_p[2][3][j][4][0]+"」", end="   ")
            print()    
            
        # 現在の未保存のログ
        print("<<< " + "cur_p" + ">>>", self.log_top, self.log_new, self.log_bottom)
        temp_p = self.o_page.o_design.p
        for j in range(1, len(temp_p[2][3])):
            print(str(j-1)+ "「" + temp_p[2][3][j][4][0]+"」", end="   ")
        print()    

    def escape_redo(self):
        ################################
        # 更新をREDOする
        ################################
        # Ctrl+Shift+zで戻る場所
        if self.log_new  + 1 >= self.log_top:
            # Redoできない
            return
        
        # pを復旧
        self.log_new += 2
        self.o_page.o_design.p = self.o_page.load_design("temp"+str(self.log_new).zfill(3))

        # ページを移動する
        self.o_page.page_no = self.o_page.get_root_information(COM____cur_page_no)
        self.o_page.set_page_no(self.o_page.page_no)

        self.log_new -= 1

        # ページ番号を復旧
        self.o_page.page_no = self.o_page.get_root_information(COM____page_no_save)

        # 右メニューを無効にする
        # クリック処理を止める
        self.o_page.set_group_right(COM__group_x, -300)
        self.o_page.set_group_right(COM__group_y, -200)
        self.o_page.set_group_right(COM__group_width, 4)
        self.o_page.set_group_right(COM__group_height, 4)

        self.mouse_click = MOU_CLICK_FALSE
        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
        self.o_page.set_group_right(COM__right_page_no, -1)

    def escape_undo(self):
        ################################
        # 更新をUNDOする
        ################################
        # Ctrl+zで戻る場所
        if self.log_new < self.log_bottom:
            # Undoできない
            return
        
        # pを復旧
        self.o_page.o_design.p = self.o_page.load_design("temp"+str(self.log_new).zfill(3))
        self.log_new -= 1

        # ページ番号を復旧
        self.o_page.page_no = self.o_page.get_root_information(COM____page_no_save)

        # 右メニューを無効にする
        # クリック処理を止める
        self.o_page.set_group_right(COM__group_x, -300)
        self.o_page.set_group_right(COM__group_y, -200)
        self.o_page.set_group_right(COM__group_width, 4)
        self.o_page.set_group_right(COM__group_height, 4)

        self.mouse_click = MOU_CLICK_FALSE
        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)

    def finish_right_menu(self):
        ################################
        # 右メニューを終わらせる
        ################################
                
        # print("右メニュー終わり")    
        self.o_page.set_group_right(COM__group_x, -300)
        self.o_page.set_group_right(COM__group_y, -200)
        self.o_page.set_group_right(COM__group_width, 4)
        self.o_page.set_group_right(COM__group_height, 4)

        self.mouse_click = MOU_CLICK_FALSE
        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)

        # 右メニューをリセット
        self.init_right_menu()

    def get_select_toggle_file_name(self):
        ################################
        # トグルで選ばれたテキストを返す
        ################################
        # 現在、仮でグループ１，コンポーネント０が設定してある
        
        # Page_6の１つ目のトグル
        g_no = 1
        
        c_no = self.o_page.get_group(g_no, COM__toggle_value)

        print("select_toggle_text g_no=", g_no, "c_no=", c_no)

        # トグル保存場所をリセット
        self.o_page.set_group(1, COM__toggle_value, -1)
        
        s = self.o_page.get_component(g_no, c_no, COM_text)
        print("*** トグル選択テキスト", s)

        if c_no == None:
            c_no = -1

        return s, c_no

    def get_select_toggle_file_scenario(self):
        ################################
        # トグルで選ばれたファイルを返す
        ################################
        # 現在、仮でグループ１，コンポーネント０が設定してある
        
        # Page_6の１つ目のトグル
        g_no = 1
        
        c_no = self.o_page.get_group(g_no, COM__toggle_value)

        # print("select_toggle_text g_no=", g_no, "c_no=", c_no)

        if c_no == None:
            c_no = -1

        if c_no == -1:
            # 指定がなかった
            s = "page_start_program"
        else:
            s = self.o_page.get_component(g_no, c_no, COM_text)
            # print("*** トグル選択シナリオ", s)

        return s, c_no

    def make_right_menu(self, menu_type, mx, my):
        ################################
        # 右メニューを作成する
        ################################
        # 右メニューを作る

        y_debug("　＋・＋　右メニューの作成", self.o_page.get_root_information(COM____right_mouse))

        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_COMPONENT_RIGHT)                            

        if menu_type == MNU_MAIN:
            # 右ボタンクリック時のメイン画面    

            # メニューを変更し、削除メニューを表示
            # もし、１エントリしかなかったら、２エントリ目を追加
            self.o_page.set_component_right(0, COM_text, "項目の追加")

            # ここで、右メニューの幅を設定
            self.o_page.set_group_right(COM__group_width, 280)

            height = 0
            self.o_page.set_component_direct_right(0, COM_y, height)
            self.o_page.set_component_direct_right(0, COM_temp_y, height)

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["項目の文字変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["項目のフォント変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["項目の文字色変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["項目の背景色変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["項目の削除", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["画像の濃度変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["グループのタイプ変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["グループのフォント変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["グループの文字色変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["グループの背景色変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["グループの削除", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["最前面へ移動", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["最背面へ移動", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.set_group_right(COM__group_height, height)

        elif menu_type == MNU_GROUP_TYPE:
            # 右メインで「グループのタイプ変更」
            entry_no = len(self.o_page.o_design.p[1][2])
            
            for i in range(entry_no-2):
                self.o_page.o_design.p[1][2].pop(1)

            self.o_page.set_component_right(0, COM_text, "フレーム")

            # ここで、右メニューの幅を設定
            height = 0
            self.o_page.set_component_direct_right(0, COM_y, height)
            self.o_page.set_component_direct_right(0, COM_temp_y, height)

            self.o_page.set_group_right(COM__group_width, 190)

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["ボタン", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["画像", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["スライダー", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["トグルボタン", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["チェックボックス", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["音楽", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["テキスト", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.set_group_right(COM__group_height, height)

        elif menu_type == MNU_NEW_GROUP:
            # 右メインで「グループの新規作成」
            entry_no = len(self.o_page.o_design.p[1][2])
            
            for i in range(entry_no-2):
                self.o_page.o_design.p[1][2].pop(1)

            self.o_page.set_component_right(0, COM_text, "グループの追加（縦）")

            # ここで、右メニューの幅を設定
            height = 0
            self.o_page.set_component_direct_right(0, COM_y, height)
            self.o_page.set_component_direct_right(0, COM_temp_y, height)
            
            self.o_page.set_group_right(COM__group_width, 300)

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["グループの追加（横）", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["このページのフォント変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["このページの文字色変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["このページの背景の色変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["このページの背景の画像変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["全ページの文字色変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["全ページの背景の色変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["全ページの背景の画像変更", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.set_group_right(COM__group_height, height)

        elif menu_type == MNU_NUMBER:
            # 右メインで「数字の表示」
            entry_no = len(self.o_page.o_design.p[1][2])
            
            for i in range(entry_no-2):
                self.o_page.o_design.p[1][2].pop(1)

            self.o_page.set_component_right(0, COM_text, "01")

            # ここで、右メニューの幅を設定
            height = 0
            self.o_page.set_component_direct_right(0, COM_y, height)
            self.o_page.set_component_direct_right(0, COM_temp_y, height)
            
            self.o_page.set_group_right(COM__group_width, 100)

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["02", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["03", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["04", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["05", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["06", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["07", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["08", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["09", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.o_design.p[1][2].append([0, 0, 0, "Toggle", ["10", 0, height, 110, 30, 0, height, 0, 0, -1]])

            height += 30
            self.o_page.set_group_right(COM__group_height, height)

        if self.o_page.get_group_right(COM__group_height) + my > self.o_page.screen_height:
            self.o_page.set_group_right(COM__group_y,\
                self.o_page.screen_height - self.o_page.get_group_right(COM__group_height))

        y_debug("　＋・＋　右メニューの作成(make_right_menu)", self.o_page.get_root_information(COM____right_mouse))

    def save_for_escape_undo(self):
        ################################
        # 更新をUNDOするために保存する
        ################################

        # Ctrl+zで戻る場所
        self.log_new += 1

        # トップより下かを確認
        if self.log_new > self.log_top:
            # トップの更新
            self.log_top += 1

        # ページ番号をルートに保管
        self.o_page.set_root_information(COM____page_no_save, self.o_page.page_no)
        # 直前にpを保存する
        self.o_page.save_design("temp"+str(self.log_new).zfill(3))

    def make_new_group(self, mx, my):                    
        ################################
        # 新グループを作成
        ################################

        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
        pos = self.o_page.get_page_information(COM___group_entry_no)

        # 再利用エントリがあるか確認
        empty_group = self.o_page.check_reuse()
        if empty_group == -1:
            # 再利用するエントリはない    
            # 右クリックで、新しいグループを直接作成
            if self.o_page.get_group_right(COM__group_width) < 32:
                self.o_page.set_group_right(COM__group_width, 32)
            if self.o_page.get_group_right(COM__group_height) < 32:
                self.o_page.set_group_right(COM__group_height, 32)
            
            # 新たなコンポーネントを作る
            g_no = self.o_page.create_new_component(empty_group, self.margin, True)
            print("create_new_component　Empty group no＊=", g_no)
            empty_group = g_no

        else:
            # 再利用
            self.o_page.set_group(empty_group, COM__group_x, self.o_page.get_group_right(COM__group_x))                        
            self.o_page.set_group(empty_group, COM__group_y, self.o_page.get_group_right(COM__group_y))                        
            if self.o_page.get_group_right(COM__group_width) < 32:
                self.o_page.set_group_right(COM__group_width, 32)
            if self.o_page.get_group_right(COM__group_height) < 32:
                self.o_page.set_group_right(COM__group_height, 32)
            self.o_page.set_group(empty_group, COM__group_width, self.o_page.get_group_right(COM__group_width)) 
            self.o_page.set_group(empty_group, COM__group_height, self.o_page.get_group_right(COM__group_height)) 
            self.o_page.set_component(empty_group, 0, COM_x, self.margin) 
            self.o_page.set_component(empty_group, 0, COM_y, self.margin) 
            self.o_page.set_component(empty_group, 0, COM_width, self.o_page.get_group_right(COM__group_width) - self.margin * 2) 
            self.o_page.set_component(empty_group, 0, COM_height, self.o_page.get_group_right(COM__group_height) - self.margin * 2) 
            self.o_page.set_component(empty_group, 0, COM_temp_x, self.margin) 
            self.o_page.set_component(empty_group, 0, COM_temp_y, self.margin) 
            self.o_page.insert_list(empty_group)

        # 方向をセット
        # 展開方向（縦がデフォルト）
        print("設定時の展開方向", self.new_dir)
        self.o_page.set_group(empty_group, COM__dir, self.new_dir)                        
        # フォントの色を設定
        self.o_page.set_component(empty_group, 0, COM_font_color , COL_BLACK)                        

        return empty_group

    def search_control_button(self, i_groups, mx, my):
        ################################
        # 更新をUNDOするために保存する
        ################################

        # 拡張グループ内にいた
        # グループ内であるが、コンポーネント上かをチェック
        self.mouse_pos = -1
        
        b_break = False
        
        for i in range(self.o_page.len_component(i_groups)):
            # コンポーネントにいるかチェック
            b_found_component = self.check_click_on_component(i_groups, i, mx, my)

            if b_found_component == True:
                # コンポーネント内にいた
                self.mouse_pos = i

                if self.o_page.get_group(i_groups, COM__move_control) == move_control_True:
                    # 制御ボタン
                    self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_CONTROL)
                    
                    self.mouse_click = MOU_CLICK_CONTROL

                    b_break = True
                    break 
                else:                                    
                    pass

        return b_break

    def init_right_menu(self):
        ################################
        # 右メニューを初期化
        ################################
        entry_no = len(self.o_page.o_design.p[1][2])
        for i in range(entry_no-2):
            self.o_page.o_design.p[1][2].pop(2)
    
    def move_mouse(self, mouse_component, mouse_pos):
        ################################
        # マウスの位置を移動
        ################################
        # マウスクリックの場所
        if mouse_component == -1:
            return
        mx, my = pygame.mouse.get_pos()
        mx = mx * rate_x
        my = my * rate_y    

        if self.mouse_click == MOU_CLICK_COMPONENT_LEFT:
            # 動かせるコンポーネント
            if self.o_page.get_group(mouse_component, COM__move_inhibit)==False:
                self.o_page.set_component(mouse_component, mouse_pos, COM_temp_x, \
                    mx - self.o_page.get_component(mouse_component, mouse_pos, COM_click_offset_x))
                self.o_page.set_component(mouse_component, mouse_pos, COM_temp_y, \
                    my - self.o_page.get_component(mouse_component, mouse_pos, COM_click_offset_y))

    def music_change_value(self, i_groups, mouse_pos):
        ################################
        # 音楽のフラグの値を変更        
        ################################
        # print("Music change Value", self.o_page.get_group(i_groups, COM__music_value), mouse_pos)
        if self.o_page.get_group(i_groups, COM__music_value) == mouse_pos:
            # 音楽を停止
            self.o_page.set_group(i_groups, COM__music_value, -1)
            pygame.mixer.music.stop()
        else:
            # 音楽を開始        
            self.o_page.set_group(i_groups, COM__music_value, mouse_pos)

            name = self.o_page.get_component(i_groups, mouse_pos, COM_text)
            file_name = self.o_page.get_root_information(COM____data_path) + name
            # print(file_name)

            if self.o_page.file_exist(file_name) == True:
                pass    
            else:
                # 音楽が存在しない
                name = "default.mp3"

            pygame.mixer.music.load(self.o_page.get_root_information(COM____data_path) + name)
            pygame.mixer.music.play()

    def right_click(self, mx, my, right_page_no):
        ################################
        # 右クリックの初期処理        
        ################################
        # 右クリック時のページ番号を覚えておく

        print("@@@ right_click")

        right_mouse = self.o_page.get_root_information(COM____right_mouse)

        menu_offset_y = self.o_page.get_right_menu_offset_y()

        self.o_page.set_group_right(COM__group_x, mx)
        self.o_page.set_group_right(COM__group_y, my)           

        if self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_RECTANGLE:
            # 矩形をキープ
            pass
        else:       
            if self.mouse_component >= 0:
                # GROUPかCOMPONENT
                if self.mouse_pos == -1:
                    self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_GROUP_RIGHT)                            

                else:
                    if self.mouse_component == -1:
                        # 完全にOUT
                        self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)                            

                    else:
                        # コンポーネント    
                        # 右メインメニューを出す
                        self.make_right_menu(MNU_MAIN, mx, my)    

            else:
                # 何も指していない    
                self.o_page.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)                            

                #右メインメニューを出す
                self.make_right_menu(MNU_NEW_GROUP, mx, my)    

            if self.o_page.get_root_information(COM____right_mouse) == MOU_CLICK_FALSE:
                # 新規
                self.b_found = False

                for i in range(self.o_page.len_component_right()):
                    if (self.o_page.get_component_right(i, COM_temp_x) <= mx 
                        <= self.o_page.get_component_right(i, COM_temp_x) + self.o_page.get_component_right(i, COM_width)\
                        and\
                        self.o_page.get_component_right(i, COM_temp_y) <= my\
                        <= self.o_page.get_component_right(i, COM_temp_y) + self.o_page.get_component_right(i, COM_height)):
                        # 右クリックコンポーネント内にマウスがある
                        self.mouse_component = 0
                        self.mouse_pos = i

                        self.mouse_click == MOU_CLICK_COMPONENT_RIGHT

                        self.group_offset_x = mx - self.o_page.get_group_right(COM__group_x)
                        self.group_offset_y = my - self.o_page.get_group_right(COM__group_y)

                        self.o_page.set_group_right(COM__group_x, mx - self.group_offset_x)
                        self.o_page.set_group_right(COM__group_y, my - self.group_offset_y)

                        self.mouse_mx = mx - self.o_page.get_component_right(self.mouse_pos, COM_temp_x)
                        self.mouse_my = my - self.o_page.get_component_right(self.mouse_pos, COM_temp_y)
                        
                        # コンポーネントのクリックオフセットを設定
                        self.o_page.set_component_right(self.mouse_pos, COM_click_offset_x, self.mouse_mx)
                        self.o_page.set_component_right(self.mouse_pos, COM_click_offset_y, self.mouse_my)

                        # 見つかった
                        self.b_found = True
                        break

                if self.b_found == True:
                    text = self.o_page.get_component_right(i, COM_text)                            

    def slider_change_value(self, i_groups, mouse_pos, mx):    
        ################################
        # スライダーの値を変更
        ################################
        # mxが最小５％なら０、最大５％ならmax、それ以外なら、１００で割って５を足す
        range_data = self.o_page.get_component(i_groups, mouse_pos, COM_slider_max) - \
                    self.o_page.get_component(i_groups, mouse_pos, COM_slider_min)
        width_len = self.o_page.get_component(i_groups, mouse_pos, COM_width) 
        width_5P_len = width_len * 0.05 
        offset_len = mx - self.o_page.get_component(i_groups, mouse_pos, COM_temp_x)           
        if (offset_len < width_5P_len):
            # 最小値
            self.o_page.set_component(i_groups, mouse_pos, COM_slider_value, 0)
        elif (offset_len > width_len * 0.95):    
            # 最大値
            self.o_page.set_component(i_groups, mouse_pos, COM_slider_value, 1)
        else:    
            # ９０％
            self.o_page.set_component(i_groups, mouse_pos, COM_slider_value, \
                (offset_len - width_5P_len) / (width_len * 0.9))

        print("＜＞",range_data, width_len, width_5P_len, offset_len, self.o_page.get_component(i_groups, mouse_pos, COM_slider_value))

    def toggle_change_value(self, i_groups, mouse_pos):
        ################################
        # トグルボタンの値を変更
        ################################
        self.o_page.set_group(i_groups, COM__toggle_value, mouse_pos)
        if self.o_page.get_component(i_groups, 0, COM_text) == "設計":
            # 設計と実行モードを切り替える
            if self.o_page.get_group(i_groups, COM__toggle_value) == 0:
                self.o_page.set_root_information(COM____mode, MOD_DESIGN)
            elif self.o_page.get_group(i_groups, COM__toggle_value) == 1:
                self.o_page.set_root_information(COM____mode, MOD_EXECUTE)
            # ウィンドウのタイトルを変える
            self.o_page.draw_window_title()
          
class Page():
    ###########################
    # ページクラス
    ###########################
    def __init__(self, o_design):
        ###########################
        # ページの初期化
        ###########################

        # スクリーンのサイズ
        self.screen_width = 1480
        self.screen_height = 700       

        # デザインオブジェクト
        self.o_design = o_design

        # グループの初期化
        self.o_group = [] 
        # 設計・実行モード
        # self.mode = MOD_EXECUTE #MOD_DESIGN
        self.mode = MOD_DESIGN

        # マウスで要素を移動可能なフレーム
        self.active_frame = -1
        # 最初のページの作成

        # 背景の色
        # self.page_back_color = COL_LIGHT_YELLOW
        self.page_back_color = "game_back_mountain.jpg"

        # self.group_back_color = COL_GREEN
        self.group_back_color = COL_WHITE

        # フレーム表示
        self.draw_frame = True
        # フレーム背景の色
        # self.page_frame_color = COL_LIGHT_ORANGE
        self.page_frame_color = COL_LIGHT_BLUE
        # self.back_color = COL_WHITE
        self.font_color =COL_BLACK
        self.font_light_color = COL_GRAY
        # self.slider_color =COL_BLUE
        # self.slider_light_color = COL_LIGHT_BLUE
        self.frame_color = COL_LIGHT_BLUE

        # フォントの種類
        self.font_type = FNT_MINCHO
        # self.font_type = FNT_GOTHIC

        # ページ生成
        self.page_no = 0

        # リスト情報書き出しファイル
        self.f_page_list = None

        # 最大ページ番号を設定
        self.max_page_no = 0

        # 作成モード
        self.draw_mode = False
        
        # 右モード
        self.right_mouse = MOU_CLICK_FALSE
        
        # 新しいページモード
        self.new_page = True

        # 日本語入力モード
        self.input_mode = False
        self.input_group_no = -1
        self.input_component_no = -1

        # 設計時に選択されているグループ番号
        self.select_group_no_on_design = 0
        
        # 設計時に選択されているコンポーネント番号
        # self.select_component_no_on_design = 0
        
        # 背景画像の変更のためページ番号を変更
        self.page_no_save = -1

        # グループ画像の変更のためグループ番号を変更
        self.group_no_save = -1

        # RGBデータを獲得するときのタイプ
        self.RGB_type = RGB_NONE

        # 制御フラグ
        self.CSV_control = [-1, -1, -1, -1, -1, -1, -1, -1]
        # self.flag_0 = -1
        # self.flag_1 = -1
        # self.flag_2 = -1
        # self.flag_3 = -1
        self.common_data_0 = -1
        self.file_list_page_no = -1
        self.RGB_page_no = -1

        # CSVリストの内訳
        self.CSV_list_selection = 0
        self.CSV_list_result_by_CSV = 0
        self.CSV_list_result = 0

        # 選択のとき、ステップを問題ごとにイクツにするかのリスト
        self.selection_step_size = []

    def get_group_all(self, i_groups):    
        ###########################
        # グループ全体を得る
        ###########################
        return self.o_design.p[self.page_no+2][i_groups+1][0]
    
    def get_component(self, i_groups, i, parm):    
        ###########################
        # コンポーネント値を得る
        ###########################
        if parm in (COM_x, COM_temp_x):
            return self.o_design.p[self.page_no+2][i_groups+1][0][COM__group_x] + self.o_design.p[self.page_no+2][i_groups+1][i+1][4][parm]
        elif parm in (COM_y, COM_temp_y):
            return self.o_design.p[self.page_no+2][i_groups+1][0][COM__group_y] + self.o_design.p[self.page_no+2][i_groups+1][i+1][4][parm]
        else:
            return self.o_design.p[self.page_no+2][i_groups+1][i+1][4][parm]

    def get_component_right(self, i, parm):    
        ###########################
        # 右クリックコンポーネント値を得る
        ###########################
        if parm in (COM_x, COM_temp_x):
            # print("get_component_right_X:", self.o_design.p[1][2][0][2], self.o_design.p[1][2][i+1][4][parm])
            return self.o_design.p[1][2][0][COM__group_x] + self.o_design.p[1][2][i+1][4][parm]
        elif parm in (COM_y, COM_temp_y):
            # print("get_component_right_Y:", self.o_design.p[1][2][0][3], self.o_design.p[1][2][i+1][4][parm])
            return self.o_design.p[1][2][0][COM__group_y] + self.o_design.p[1][2][i+1][4][parm]
        else:
            return self.o_design.p[1][2][i+1][4][parm]

    def get_group(self, i_groups, parm):    
        ###########################
        # グループ値を得る
        ###########################
        # print("グループ値を得る Page:", self.page_no, " Group:", i_groups, " Parm=", parm)
        return self.o_design.p[self.page_no+2][i_groups+1][0][parm]
    
    def get_group_right(self, parm):    
        ###########################
        # グループ値を得る
        ###########################
        # print(self.page_no, i_groups)
        return self.o_design.p[1][2][0][parm]
    
    def get_page_information(self, parm):    
        ###########################
        # ページ部の情報を得る
        ###########################
        return self.o_design.p[self.page_no+2][0][parm]
    
    def get_root_information(self, parm):    
        ###########################
        # プロジェクト部の情報を得る
        ###########################
        return self.o_design.p[0][parm]
    
    def get_project_right_click(self, parm):    
        ###########################
        # プロジェクト部の情報を得る
        ###########################
        return self.o_design.p[1][parm]
    
    def get_right_menu_offset_y(self):    
        ###########################
        # 右メニューｙオフセットを得る
        ###########################
        return self.o_design.p[1][3]
    
    def set_right_menu_offset_y(self, parm):    
        ###########################
        # 右メニューｙオフセットを代入
        ###########################
        #99999999
        self.o_design.p[1][3] = parm
    
    def len_component(self, i_groups):
        ###########################
        # コンポーネント長を得る
        ###########################
        return len(self.o_design.p[self.page_no+2][i_groups+1])-1

    def len_component_right(self):
        ###########################
        # コンポーネント長を得る
        ###########################
        return len(self.o_design.p[1][2])-1

    def len_group(self):
        ###########################
        # グループ長を得る
        ###########################
        return len(self.o_design.p[self.page_no+2])

    def len_page(self):
        ###########################
        # ページ長を得る
        ###########################
        return len(self.o_design.p)-2

    def set_component(self, i_groups, i, parm, value):    
        ###########################
        # コンポーネント値を設定する
        ###########################
        if parm in (COM_x, COM_temp_x):
            self.o_design.p[self.page_no+2][i_groups+1][i+1][4][parm] = value - self.o_design.p[self.page_no+2][i_groups+1][0][COM__group_x]
        elif parm in (COM_y, COM_temp_y):
            self.o_design.p[self.page_no+2][i_groups+1][i+1][4][parm] = value - self.o_design.p[self.page_no+2][i_groups+1][0][COM__group_y]
        else:
            self.o_design.p[self.page_no+2][i_groups+1][i+1][4][parm] = value

    def set_component_direct(self, i_groups, i, parm, value):    
        ###########################
        # コンポーネント値を直接設定
        ###########################
        self.o_design.p[self.page_no+2][i_groups+1][i+1][4][parm] = value

    def set_component_direct_right(self, i, parm, value):    
        ###########################
        # コンポーネント値を直接設定
        ###########################
        self.o_design.p[1][2][i+1][4][parm] = value

    def set_component_right(self, i, parm, value):    
        ###########################
        # コンポーネント値を設定する
        ###########################
        if parm in (COM_x, COM_temp_x):
            self.o_design.p[1][2][i+1][4][parm] = value - self.o_design.p[1][2][0][COM__group_x]
        elif parm in (COM_y, COM_temp_y):
            self.o_design.p[1][2][i+1][4][parm] = value - self.o_design.p[1][2][0][COM__group_y]
        else:
            self.o_design.p[1][2][i+1][4][parm] = value

    def set_component_root(self, g_no, i, no, data):
        ################################
        # コンポーネント根底部への代入        
        ################################
        self.o_design.p[self.page_no+2][g_no+1][i+1][no] = data

    def set_root_information(self, parm, value):    
        ###########################
        # ルート部の情報を設定
        ###########################
        self.o_design.p[0][parm] = value
    
    def set_page_information(self, parm, value):    
        ###########################
        # ページ部の情報を設定する
        ###########################
        self.o_design.p[self.page_no+2][0][parm] = value
    
    def set_group(self, i_groups, parm, value):    
        ###########################
        # グループ値を設定する
        ###########################
        self.o_design.p[self.page_no+2][i_groups+1][0][parm] = value

    def set_group_right(self, parm, value):    
        ###########################
        # グループ値を設定する
        ###########################
        self.o_design.p[1][2][0][parm] = value

    def switch_root_information(self, parm):    
        ###########################
        # ルート部の情報を切り替え
        ###########################
        if self.o_design.p[0][parm] == MOD_DESIGN:
            self.o_design.p[0][parm] = MOD_EXECUTE
        else:    
            self.o_design.p[0][parm] = MOD_DESIGN
    
    # def create_page(self):
    #     ###########################
    #     # ページの作成
    #     ###########################
    #     # print("全ページ作成")
    #     # ページ生成フラグがオンか調べる

    #     self.page_no = 0
    #     self.create_page_selection(self.page_no, PRM_Q_0, PRM_A_0_0, PRM_A_0_1)
    #     self.page_no = 1
    #     self.create_page_selection(self.page_no, PRM_Q_1, PRM_A_1_0, PRM_A_1_1)
    #     self.page_no = 2
    #     self.create_page_result_URL(self.page_no, URL_0_0, URL_0_1, URL_0_2)
    #     # self.page_no = 3
    #     # self.create_page_result(self.page_no, "おすすめは「Back Number」", "注目型.png")
    #     # self.page_no = 4
    #     # self.create_page_result(self.page_no, "おすすめは「One Direction」", "法則型.png")
    #     # self.page_no = 5
    #     # self.create_page_result(self.page_no, "あなたは「Ed Sheeran」", "理想型.png")
    #     self.page_no = 3
    #     self.create_page_result_URL(self.page_no, URL_1_0, URL_1_1, URL_1_2)
    #     self.page_no = 4
    #     self.create_page_result_URL(self.page_no, URL_2_0, URL_2_1, URL_2_2)
    #     self.page_no = 5
    #     self.create_page_result_URL(self.page_no, URL_3_0, URL_3_1, URL_3_2)

    #     self.page_no = 6
    #     # ファイルリストページ
    #     self.file_list_page_no = self.page_no
    #     self.create_page_file_list(self.page_no)

    #     self.page_no = 7
    #     # RGB値ページ
    #     self.RGB_page_no = self.page_no
    #     self.create_page_RGB(self.page_no)

    #     # ページ番号最大を設定
    #     self.max_page_no = self.page_no 
    #     # ページ番号を戻す
    #     self.page_no = 0 
    #     # print("Create Page page_no=", self.page_no)

    def calc_step_size(self):
        ################################
        # step_sizeを返す（１つ目は２･･･）
        ################################
                                
        # CSVリストの内訳
        add_page_no = 0
        b_selection = False

        # ステップサイズを計算
        branch_len = []
        for i_page in range(0, self.CSV_list_selection):
            list_len = len(self.CSV_list[i_page])-2
            branch_len.append(list_len)
        # step 1,2,6
        branch_len.reverse()
        step_size = []
        for i_page in range(self.CSV_list_selection):
            if i_page == 0:
                # ０のとき特別
                step_size.append(1)
            else:
                # ０以外のとき
                x = branch_len[0]
                for j in range(1, i_page):
                    x *= branch_len[j]
                # print(i_page, x)    
                step_size.append(x)    
        # これで、各ページのステップ
        step_size.reverse()        
        print("   @@@　step_size", step_size)

        # 選択のとき、ステップを問題ごとに いくつにするかのリスト
        self.selection_step_size = step_size

        # for i_page in range(0, self.CSV_list_selection):
        #     # list_len = (len(self.CSV_list[i_page])-2) // 2
        #     list_len = len(self.CSV_list[i_page])-2
        #     for i_component in range(list_len):
        #         # if name == self.CSV_list[i_page][i_component * 2 + 2]:
        #         if name == self.CSV_list[i_page][i_component + 2]:
        #             # 選択肢（i_component番目）
        #             self.CSV_control[i_page] = i_component * step_size[i_page]
        #             print("＊＊＊　selectionが見つかった　i_component=", i_component, " CSV_control=", self.CSV_control, " i_page=",i_page, " step_size=",step_size)
        #             # ページ番号を増やす    
        #             add_page_no = 1
        #             # self.set_page_no(self.page_no+1)
        #             b_selection = True
        #             # print("<<0>> i_page=",i_page)            
        #             break
        #         else:
        #             pass

        #     if b_selection == True:
        #         # 外側のforも処理を止める
        #         break

        # if b_selection == True:
        #     # selectionで該当の文字があった
        #     # print("<<2>> i_page=",i_page)            
        #     # CSV_controlにしたがって移動するページを設定            
        #     # 最終質問でページ番号を増やす    
        #     # print("self.CSV_list_selection=", self.CSV_list_selection)
        #     # print("add_page_no=", add_page_no, "i_page=", i_page)
        #     if i_page == self.CSV_list_selection - 1:
        #         data = 0        
        #         # フラグをすべて足す
        #         for i in range(self.CSV_list_selection):
        #             data += self.CSV_control[i]    
        #         print("selectionの最後：次は", self.page_no + data + 1, "ページ", i_page, self.CSV_control)
        #         self.set_page_no(self.page_no+data+1)
        #     else:
        #         # 単純に１ページ先に行く
        #         print("selectionの通常：次は", self.page_no+1, "ページ", i_page, self.CSV_control)
        #         self.set_page_no(self.page_no+1)

        # if b_selection == False:
        #     # selectionの処理
        #     # Result_CSVの処理    
        #     # b_result_by_CSV = False
        #     # Result_by_CSVを処理
        #     for i_page in range(self.CSV_list_selection, self.CSV_list_selection+self.CSV_list_result_by_CSV):
        #         if name == self.CSV_list[i_page][3]:
        #             # URLに飛ぶ
        #             webbrowser.open(self.CSV_list[i_page][4])

        #             break

    def construct_CSV_data(self, file_name):
        ###########################
        # CSVデータを作成
        ###########################
        print("construct_CSV_data file_name=", file_name)

        # ルートに新しいシナリオを設定
        self.set_root_information(COM____CSV_file_name, file_name)

        # ページ生成フラグがオンか調べる
        if type(file_name) is str:
            # 文字のときだけ処理
            self.CSV_list = self.load_CSV(file_name)
            if self.CSV_list == []:
                print("空CSV")
                exit(0)
                
            # CSVファイル名を読んでみる    
            print(self.get_root_information(COM____CSV_file_name))
            # CSVを読み込む

            # CSVが空でないので、self.CSV_listに読み込む
            for i in range(len(self.CSV_list)):
                for j in range(len(self.CSV_list[i])):
                    print(self.CSV_list[i][j])

            # CSVリストの内訳
            self.CSV_list_selection = 0
            self.CSV_list_result_by_CSV = 0
            self.CSV_list_result = 0

            # print("self.CSV_list 要素数：", len(self.CSV_list))
            self.page_no = 0
            #999
            # self.page_no = -1
            # print("<<1>> construct_CSV_data page_no=", self.page_no)
            for line_no in range(len(self.CSV_list)):
                if self.CSV_list[line_no][0] == "Start":
                    # 開始ページを作成
                    # branch_list = []
                    # branch_len = (len(self.CSV_list[line_no])-2) // 2
                    # for i in range(branch_len):
                    #     branch_list.append([self.CSV_list[line_no][2 * (i + 1)], self.CSV_list[line_no][2 * (i + 1) + 1]])

                    self.create_page_start_by_CSV(self.CSV_list[line_no][1])
                    # print("<<2>> construct_CSV_data page_no=", self.page_no, " line_no=", line_no)
                    self.page_no += 1
                    self.CSV_list_selection += 1

                elif self.CSV_list[line_no][0] == "New":
                    # 開始ページを作成
                    # branch_list = []
                    # branch_len = (len(self.CSV_list[line_no])-2) // 2
                    # for i in range(branch_len):
                    #     branch_list.append([self.CSV_list[line_no][2 * (i + 1)], self.CSV_list[line_no][2 * (i + 1) + 1]])

                    self.create_page_new_by_CSV(self.CSV_list[line_no][1])
                    # print("<<2.5>> construct_CSV_data page_no=", self.page_no, " line_no=", line_no)
                    self.page_no += 1
                    self.CSV_list_selection += 1

                elif self.CSV_list[line_no][0] == "Selection":
                    # 選択ページを作成（ページ番号,テキスト,{[答え, flag値]}）
                    branch_list = []
                    # branch_len = (len(self.CSV_list[line_no])-2) // 2
                    branch_len = len(self.CSV_list[line_no])-2
                    for i in range(branch_len):
                        # branch_list.append([self.CSV_list[line_no][2 * (i + 1)], self.CSV_list[line_no][2 * (i + 1) + 1]])
                        branch_list.append([self.CSV_list[line_no][i + 2]])
                    # print("branch_len=", branch_len, branch_list)
                    # exit(0)


                    self.create_page_selection_by_CSV(self.CSV_list[line_no][1], branch_list)
                    # print("<<3>> construct_CSV_data page_no=", self.page_no, " line_no=", line_no)
                    self.page_no += 1
                    self.CSV_list_selection += 1

                elif self.CSV_list[line_no][0] == "Result_URL":
                    # URL付の結果ページを作成（ページ番号,flag値,テキスト,URLボタン,URL）
                    # print(self.CSV_list[line_no])
                    self.create_page_result_URL_by_CSV(self.CSV_list[line_no][1], self.CSV_list[line_no][2], self.CSV_list[line_no][3], self.CSV_list[line_no][4])
                    # print("<<4>> construct_CSV_data page_no=", self.page_no, " line_no=", line_no)
                    self.page_no += 1
                    self.CSV_list_result_by_CSV += 1

                elif self.CSV_list[line_no][0] == "Result":
                    # 結果ページを作成（ページ番号,flag値,テキスト,画像ファイル名）
                    self.create_page_result_by_CSV(self.CSV_list[line_no][1], self.CSV_list[line_no][2], self.CSV_list[line_no][3])
                    # print("<<5>> construct_CSV_data page_no=", self.page_no, " line_no=", line_no)
                    self.page_no += 1
                    self.CSV_list_result += 1

                elif self.CSV_list[line_no][0] == "Result_3_image":
                    # 結果テキストページを作成（ページ番号,flag値,テキスト,画像ファイル名,追加画像１,追加画像２）
                    self.create_page_result_3_image_by_CSV(self.CSV_list[line_no][1], self.CSV_list[line_no][2],\
                        self.CSV_list[line_no][3], self.CSV_list[line_no][4],\
                        self.CSV_list[line_no][5], self.CSV_list[line_no][6])
                    # print("<<5>> construct_CSV_data page_no=", self.page_no, " line_no=", line_no)
                    self.page_no += 1
                    self.CSV_list_result_by_CSV += 1

                elif self.CSV_list[line_no][0] == "End":
                    # 終了
                    break
                else:
                    # 不明のコマンド     
                    print("ERROR05:CSVファイルに、存在しないコマンドが入っている", self.CSV_list[line_no][0])
                    exit(0)

            # コピーライトリストページ
            self.copyright_page_no = self.page_no
            self.create_page_copyright(self.page_no)
            # print("<<6>> construct_CSV_data page_no=", self.page_no, " self.copyright_page_no", self.copyright_page_no)
            self.page_no += 1

            # ファイルリストページ
            self.file_list_page_no = self.page_no
            self.create_page_file_list(self.page_no)
            # print("<<7>> construct_CSV_data page_no=", self.page_no, "self.file_list_page_no", self.file_list_page_no)
            self.page_no += 1

            # RGB値ページ
            self.RGB_page_no = self.page_no
            self.create_page_RGB(self.page_no)
            # print("<<8>> construct_CSV_data page_no=", self.page_no, "self.RGB_page_no", self.RGB_page_no)
            # self.page_no += 1

            # ページ番号最大を設定
            self.max_page_no = self.page_no - 3

            # ページ番号の双方向リストを作成    
            self.decide_page_dual_list()

            # print("決定　max_page_no=", self.max_page_no, " page_no=", self.page_no)
            
            # キャプション
            self.draw_window_title()


            #999
            # CSVファイル名を書き込む
            self.set_root_information(COM____CSV_file_name, file_name)


            # ページ番号を戻す
            self.page_no = 0 

    def create_page_by_CSV(self, name):
        ###########################
        # CSVによるページの作成
        ###########################
        # page_startのときは、最初のメニュー
        # それ以外は、選んだシナリオ

        # CSVデータを構成する
        self.construct_CSV_data(name)

        # # ページ生成フラグがオンか調べる
        # if name != -7777:
        #     self.CSV_list = self.load_CSV(name)
        #     if self.CSV_list == []:
        #         print("空CSV")
        #         exit(0)
                
        #     # CSVファイル名を読んでみる    
        #     file_name = self.get_root_information(COM____CSV_file_name)
        #     # CSVを読み込む

        #     # CSVが空でないので、self.CSV_listに読み込んだ    
        #     for i in range(len(self.CSV_list)):
        #         for j in range(len(self.CSV_list[i])):
        #             print(self.CSV_list[i][j])

        #     # CSVリストの内訳
        #     self.CSV_list_selection = 0
        #     self.CSV_list_result_by_CSV = 0
        #     self.CSV_list_result = 0

        #     # CSVデータを作成
        #     self.construct_CSV_data(file_name)

        #     print("create_page_by_CSV: CSV_list_selection=", self.CSV_list_selection, " list_result_by_CSV", self.CSV_list_result_by_CSV ," list_result=", self.CSV_list_result)

        #     # print("self.CSV_list 要素数：", len(self.CSV_list))
        #     self.page_no = 0
        #     for line_no in range(len(self.CSV_list)):
        #         if self.CSV_list[line_no][0] == "Start":
        #             # 開始ページを作成
        #             # branch_list = []
        #             # branch_len = (len(self.CSV_list[line_no])-2) // 2
        #             # for i in range(branch_len):
        #             #     branch_list.append([self.CSV_list[line_no][2 * (i + 1)], self.CSV_list[line_no][2 * (i + 1) + 1]])

        #             self.create_page_start_by_CSV(self.CSV_list[line_no][1])#, branch_list)
        #             self.page_no += 1
        #             self.CSV_list_selection += 1

        #         elif self.CSV_list[line_no][0] == "Selection":
        #             # 選択ページを作成（ページ番号,テキスト,{[答え, flag値]}）
        #             branch_list = []
        #             branch_len = (len(self.CSV_list[line_no])-2) // 2
        #             for i in range(branch_len):
        #                 branch_list.append([self.CSV_list[line_no][2 * (i + 1)], self.CSV_list[line_no][2 * (i + 1) + 1]])
        #             # print(branch_list)

        #             self.create_page_selection_by_CSV(self.CSV_list[line_no][1], branch_list)
        #             self.page_no += 1
        #             self.CSV_list_selection += 1

        #         elif self.CSV_list[line_no][0] == "Result_URL":
        #             # URL付の結果ページを作成（ページ番号,flag値,テキスト,URLボタン,URL）
        #             # print(self.CSV_list[line_no])
        #             self.create_page_result_URL_by_CSV(self.CSV_list[line_no][1], self.CSV_list[line_no][2], self.CSV_list[line_no][3], self.CSV_list[line_no][4])
        #             self.page_no += 1
        #             self.CSV_list_result_by_CSV += 1

        #         elif self.CSV_list[line_no][0] == "Result":
        #             # 結果ページを作成（ページ番号,flag値,テキスト,画像ファイル名）
        #             self.create_page_result_by_CSV(self.CSV_list[line_no][1], self.CSV_list[line_no][2], self.CSV_list[line_no][3])
        #             self.page_no += 1
        #             self.CSV_list_result += 1

        #         elif self.CSV_list[line_no][0] == "End":
        #             # 終了
        #             break
        #         else:
        #             # 不明のコマンド     
        #             print("ERROR05:CSVファイルに、存在しないコマンドが入っている", self.CSV_list[line_no][0])
        #             exit(0)
        #         # ページ番号を増やす
        #         # self.page_no = 0

            # # コピーライトリストページ
            # self.copyright_page_no = self.page_no
            # self.create_page_copyright(self.page_no)
            # self.page_no += 1

            # # ファイルリストページ
            # self.file_list_page_no = self.page_no
            # self.create_page_file_list(self.page_no)
            # self.page_no += 1

            # # RGB値ページ
            # self.RGB_page_no = self.page_no
            # self.create_page_RGB(self.page_no)
            # # self.page_no += 1

            # ページ番号最大を設定
            # self.max_page_no = self.page_no 

            # print("決定　max_page_no=", self.max_page_no, " page_no=", self.page_no)
            
            # # キャプション
            # self.draw_window_title()

            # # ページ番号を戻す
            # self.page_no = 0 

    def create_page_selection_by_CSV(self, question, list_of_branch):
        # 選択ページを作成（ページ番号,テキスト,{[答え, flag値]}）
        # print(self.page_no, "create_page_selection_by_CSV ", "Text=", question, " list_of_branch=", list_of_branch)
        # ３つ以上の引数を可能にする特別な選択ページ
        self.create_page_selection_2(self.page_no, question, list_of_branch)

    def create_page_start_by_CSV(self, question):#, list_of_branch):
        # 開始ページを作成（ページ番号,テキスト)#,{[答え, flag値]}）
        # print(self.page_no, "create_page_selection_by_CSV ", "Text=", question, " list_of_branch=", list_of_branch)
        # ３つ以上の引数を可能にする特別な選択ページ
        self.create_page_start_2(self.page_no, question)#, list_of_branch)

    def create_page_new_by_CSV(self, question):#, list_of_branch):
        # 開始ページを作成（ページ番号,テキスト)#,{[答え, flag値]}）
        # print(self.page_no, "create_page_selection_by_CSV ", "Text=", question, " list_of_branch=", list_of_branch)
        # ３つ以上の引数を可能にする特別な選択ページ
        self.create_page_new(self.page_no, question)#, list_of_branch)

    def create_page_result_URL_by_CSV(self, flag, title_message, URL_message, URL_data):
        # URL付の結果ページを作成（ページ番号,flag値,タイトル,URLボタン,URL）
        # self.create_page_result_URL_by_CSV(self.page_no, self.CSV_list[line_no][1], self.CSV_list[line_no][2], self.CSV_list[line_no][3], self.CSV_list[line_no][4])
        # print(self.page_no, "create_page_result_URL_by_CSV ", "flag=", flag, "Title=「", title_message, "」 URL_message=「", URL_message,"」URL=「", URL_data,"」")
        self.create_page_result_URL(self.page_no, title_message, URL_message, URL_data)

    def create_page_result_by_CSV(self, flag, title_message, image_file_name):
        # 結果ページを作成（ページ番号,flag値,タイトル,画像ファイル名）
        # self.create_page_result_by_CSV(self.page_no, self.CSV_list[line_no][1], self.CSV_list[line_no][2], self.CSV_list[line_no][3], self.CSV_list[line_no][4])
        # print(self.page_no, "create_page_result_by_CSV ", "flag=", flag, "Text=", title_message, " image_file_name=", image_file_name)
        self.create_page_result(self.page_no, title_message, image_file_name)

    def create_page_result_3_image_by_CSV(self, flag, title_message, image_file_name, add_image1, add_image2, add_image3):
        # 結果ページを作成（ページ番号,flag値,タイトル,画像ファイル名）
        # self.create_page_result_by_CSV(self.page_no, self.CSV_list[line_no][1], self.CSV_list[line_no][2], self.CSV_list[line_no][3], self.CSV_list[line_no][4])
        # print(self.page_no, "create_page_result_by_CSV ", "flag=", flag, "Text=", title_message, " image_file_name=", image_file_name)
        self.create_page_result_3_image(self.page_no, title_message, image_file_name, add_image1, add_image2, add_image3)

    # self.create_page_result_by_CSV(self.page_no, self.CSV_list[line_no][1], self.CSV_list[line_no][2], self.CSV_list[line_no][3], self.CSV_list[line_no][4])

    def create_root_information(self):
        ###########################
        # ルート共通情報を作成
        ###########################
        self.o_design.p = []
        # １ページ目（ルート情報）の作成

        # ルートの引数
        work = []

        # COM____name = 0
        work.append("NOCK")

        # COM____version = 1
        work.append("2025/10/12版")

        # COM____mode = 2
        work.append(self.mode)

        # COM____right_mouse = 3
        work.append(self.right_mouse)

        # COM____data_path = 4
        work.append("./data/")

        # COM____margin = 5
        # デフォルト間隔
        work.append(10)

        # COM____grid = 6
        # グリッド
        work.append(1)

        # COM____page_no_save = 7
        # Saveのためのページ番号
        work.append(0)

        # COM____cur_page_no = 8
        # 現在のページ番号
        work.append(0)

        # COM____page_next_top = 9
        work.append(0)

        # COM____page_previous_top = 10
        work.append(3)

        # ルートの予約域

        # 予約域０を、ロードのとき開くCSVファイル名にする
        # COM____CSV_file_name = 11
        # # COM____reserve_0 = 11
        work.append(RES_ROOT_FALSE)

        # COM____reserve_1 = 12
        work.append(RES_ROOT_FALSE)

        # COM____reserve_2 = 13
        work.append(RES_ROOT_FALSE)
        
        # ルート情報を作成
        self.o_design.p.append(work)

        work = []
        # ２ページ目（右クリック）の作成
        work.append("Right Click")
        work.append(False)
        w = []
        # 矩形の初期の大きさを(10,10)にする
        
        # 背景色を黄にしている
        w.append([-1, -1, -1, 0, 1, -100, -100, 110, 120, 20, (0, 0, 255), True, False, True, False,\
            RES_GROUP_FALSE, RES_GROUP_FALSE, RES_GROUP_FALSE, -1, -1]) 
        
        w.append([0, 0, 0, "Toggle", ["メ１", 0, 0, 110, 30, 0, 0, 0, 0, COL_BLACK, COL_GRAY, COL_BLACK, FNT_GOTHIC,\
            RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, -1]])
        work.append(w)
        work.append(0)
        self.o_design.p.append(work)

    def create_page_top(self, page_no, page_type):
        ###########################
        # ページ先頭情報を作成
        ###########################
        # ページの引数
        work = []
        
        # COM___page_no = 0
        work.append(page_no)

        # COM___page_next = 1
        work.append(0)

        # COM___page_previous = 2
        work.append(3)

        # COM___page_type = 3
        work.append(page_type)

        # COM___active_frame = 4
        work.append(self.active_frame)

        # COM___back_color = 5
        work.append(self.page_back_color)

        # COM___group_next_top = 6
        # グループの開始番号
        work.append(-1)

        # COM___group_previous_top = 7
        # グループの終了番号
        work.append(-1)

        # COM___group_entry_no = 8
        # グループのエントリ数
        work.append(0)

        # ページの予約域
        # COM___reserve_0 = 9
        work.append(RES_PAGE_FALSE)

        # COM___reserve_1 = 10
        work.append(RES_PAGE_FALSE)

        # COM___reserve_2 = 11
        work.append(RES_PAGE_FALSE)

        # ページ情報を追加
        self.o_design.p[page_no+2].append(work)

    def create_group_direct(self, page_no, group_no, type_no, list, direction, group_x, group_y, group_width, group_height, width, height,\
        font_size, font_color, font_light_color, font_type, frame_color, draw_frame, group_back_color,\
        move_exclusive, move_inhibit, move_control, group_value, component_value):
        ###########################
        # 直接グループ作成
        ###########################
        if type_no == TYP_BUTTON:
            type = "Button"
        elif type_no == TYP_CHECKBOX:
            type = "CheckBox"
        elif type_no == TYP_FRAME:
            type = "Frame"
        elif type_no == TYP_IMAGE:
            type = "Image"
        elif type_no == TYP_MUSIC:
            type = "Music"
        elif type_no == TYP_SLIDER:
            type = "Slider"
        elif type_no == TYP_TEXT:
            type = "Text"
        elif type_no == TYP_TOGGLE:
            type = "Toggle"
        entry_no = len(list)
        offset_x = 0
        offset_y = 0

        work = []
        # グループ情報        
        if type_no == TYP_MUSIC: 
            # 音楽の値
            work.append([group_no, -1, -1, type_no, direction, group_x, group_y, group_width, group_height, font_size, font_type, frame_color,\
                draw_frame, move_exclusive, move_inhibit, move_control, RES_GROUP_FALSE, RES_GROUP_FALSE, RES_GROUP_FALSE,\
                group_value[0], group_value[1]])
        else:
            # 音楽以外
            work.append([group_no, -1, -1, type_no, direction, group_x, group_y, group_width, group_height, font_size, font_type, frame_color,\
                draw_frame, move_exclusive, move_inhibit, move_control, RES_GROUP_FALSE, RES_GROUP_FALSE, RES_GROUP_FALSE,\
                group_value])

        if entry_no == 1:
            # １つだけのコンポーネント
            start_x = (group_width - width) // 2
            start_y = (group_height - height) // 2

            if type_no == TYP_SLIDER: 
                # スライダーの値
                work.append([page_no, group_no, 0, type, [list[0], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                    font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                    component_value[0], component_value[1], component_value[2]]])
            elif type_no == TYP_CHECKBOX: 
                # チェックボックスの値
                work.append([page_no, group_no, 0, type, [list[0], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                    font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                    component_value]])
            elif type_no == TYP_IMAGE:
                # 画像の値
                work.append([page_no, group_no, 0, type, [list[0], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                    font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                    component_value]])
            elif type_no == TYP_BUTTON: 
                # ボタンの値
                work.append([page_no, group_no, 0, type, [list[0], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                    font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                    component_value]])
            else:   
                # スライダー・チェックボックス以外
                work.append([page_no, group_no, 0, type, [list[0], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                    font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                    None]])
        else:
            # ２つ以上のコンポーネント
            if direction == DIR_COLUMN:
                # 縦に並ぶ
                virtual_x_offset = int((group_width - width)/2)
                # print("virtual_x_offset", virtual_x_offset)
                for j in range(entry_no):
                    if j == entry_no - 1:
                        start_y = group_height - virtual_x_offset - height
                    else:    
                        start_y = j * ((group_height - virtual_x_offset * 2 - height)\
                            // (entry_no - 1)) + virtual_x_offset

                    start_x = virtual_x_offset

                    if type_no == TYP_SLIDER: 
                        # スライダーの値
                        work.append([page_no, group_no, j, type, [list[j], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                            font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                            component_value[0], component_value[1], component_value[2]]])
                    elif type_no == TYP_CHECKBOX: 
                        # チェックボックスの値
                        work.append([page_no, group_no, j, type, [list[j], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                            font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                            component_value]])
                    elif type_no == TYP_IMAGE: 
                        # 画像の値
                        work.append([page_no, group_no, j, type, [list[j], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                            font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                            component_value]])
                    elif type_no == TYP_BUTTON: 
                        # ボタンの値
                        work.append([page_no, group_no, j, type, [list[j], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                            font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                            component_value]])
                    else:
                        # スライダー・チェックボックス以外
                        work.append([page_no, group_no, j, type, [list[j], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                            font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                            None]])

            else:
                # 横に並ぶ
                virtual_y_offset = int((group_height - height)/2)
                for i in range(entry_no):
                    if i == entry_no - 1:
                        start_x = group_width - virtual_y_offset - width
                    else:    
                        start_x = i * ((group_width - virtual_y_offset * 2 - width)\
                            // (entry_no - 1)) + virtual_y_offset

                    start_y = virtual_y_offset

                    if type_no == TYP_SLIDER: 
                        # スライダーの値
                        work.append([page_no, group_no, i, type, [list[i], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                            font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                            component_value[0], component_value[1], component_value[2]]])
                    elif type_no == TYP_CHECKBOX: 
                        # チェックボックスの値
                        work.append([page_no, group_no, i, type, [list[i], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                            font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                            component_value]])
                    elif type_no == TYP_IMAGE: 
                        # 画像の値
                        work.append([page_no, group_no, i, type, [list[i], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                            font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                            component_value]])
                    elif type_no == TYP_BUTTON: 
                        # ボタンの値
                        work.append([page_no, group_no, i, type, [list[i], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                            font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                            component_value]])
                    else:
                        # スライダー・チェックボックス以外
                        work.append([page_no, group_no, i, type, [list[i], start_x, start_y, width, height, start_x, start_y, offset_x, offset_y,\
                            font_color, font_light_color, group_back_color, font_type, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE, RES_COMPONENT_FALSE,\
                            None]])

        # グループ全体を書き出す            
        self.o_design.p[page_no+2].append(work)

        # リストで追加
        self.insert_list()

    def add(self, data):
        #################################
        # データの変換
        #################################
        # print("add=",data+4)
        return data + 1#self.offset
    
    def bottom_list(self, n):
        #################################
        # ボトムに移動
        #################################

        if self.get_page_information(COM___group_previous_top) == n:
            return
        #(1)bottomエントリ0を保存...Bottom_cur=1
        Bottom_cur = n
        #(2)Pを最後として3保存...Last_P=3
        Last_P = self.get_page_information(COM___group_previous_top)
        #(3)bottomエントリBottom_curのNext1を保存...Bottom_next=1
        Bottom_next = self.get_group(Bottom_cur, COM__group_next)
        #(4)bottomエントリBottom_curのPrev-1を保存...Bottom_prev=-1
        Bottom_prev = self.get_group(Bottom_cur, COM__group_previous)
        #(5)BottomエントリBottom_curのNextエントリのPrevにBottom_prevを設定
        data = self.get_group(Bottom_cur, COM__group_next)
        if data != -1:
            self.set_group(data, COM__group_previous, Bottom_prev)
        else:
            self.set_page_information(COM___group_previous_top, Bottom_prev)
        #(5.5)PのエントリのNextにBottom_curを設定
        self.set_group(self.get_page_information(COM___group_previous_top), COM__group_next, Bottom_cur)
        #(6)BottomエントリBottom_curのPrevエントリのNextにBottom_nextを設定、もし-1ならNにBottom_nextを設定
        data = self.get_group(Bottom_cur, COM__group_previous)
        if data != -1:
            self.set_group(data, COM__group_next, Bottom_next)
        else:
            self.set_page_information(COM___group_next_top, Bottom_next)
        #(7)BottomエントリBottom_curのNextに-1を設定
        self.set_group(Bottom_cur, COM__group_next, -1)
        #(8)bottomエントリBottom_curのPrevにLAST_Pを設定
        self.set_group(Bottom_cur, COM__group_previous, Last_P)
        #(9)PにBottom_curを設定
        self.set_page_information(COM___group_previous_top, Bottom_cur)
        # リストの表示
        self.display_list()

    def top_list(self, n):
        #################################
        # トップに移動
        #################################

        if self.get_page_information(COM___group_next_top) == n:
            return
        #(1)topエントリ0を保存...Bottom_cur=1
        Top_cur = n
        #(2)Pを最後として3保存...Last_P=3
        Last_P = self.get_page_information(COM___group_next_top)
        #(3)TopエントリTop_curのNext1を保存...Bottom_next=1
        Top_prev = self.get_group(Top_cur, COM__group_previous)
        #(4)TopエントリTop_curのPrev-1を保存...Top_prev=-1
        Top_next = self.get_group(Top_cur, COM__group_next)
        #(5)TopエントリTop_curのNextエントリのPrevにTop_prevを設定
        data = self.get_group(Top_cur, COM__group_previous)
        if data != -1:
            self.set_group(data, COM__group_next, Top_next)
        else:
            self.set_page_information(COM___group_next_top, Top_next)
        #(5.5)PのエントリのNextにTop_curを設定
        self.set_group(self.get_page_information(COM___group_next_top), COM__group_previous, Top_cur)
        #(6)TopエントリTop_curのPrevエントリのNextにTop_nextを設定、もし-1ならNにTop_nextを設定
        data = self.get_group(Top_cur, COM__group_next)
        if data != -1:
            self.set_group(data, COM__group_previous, Top_prev)
        else:
            self.set_page_information(COM___group_previous_top, Top_prev)
        #(7)TopエントリTop_curのNextに-1を設定
        self.set_group(Top_cur, COM__group_previous, -1)
        #(8)TopエントリTop_curのPrevにLAST_Pを設定
        self.set_group(Top_cur, COM__group_next, Last_P)
        #(9)PにTop_curを設定
        self.set_page_information(COM___group_next_top, Top_cur)
        # リストの表示
        self.display_list()

    def check_reuse(self):
        #################################
        # ページに再利用エントリがあるか確認
        #################################
        for i in range(self.len_group()-1):
            if self.get_group(i, COM__current_group) == -1:
                # 空き場所発見
                return i
        return -1

    def draw_tree_page(self, page_no):
        ################################
        # ツリーをプリントする
        ################################
        print("ルート：", self.o_design.p[0])
        page_total = len(self.o_design.p)

        save_page_no = self.page_no

        # print("ページ数：", page_total-2)
        i_page = page_no
        # for i_page in range(page_total-2):
            # 各ページを表示

        # ページ番号を保存する
        self.page_no = i_page

        print("ページ=", i_page, " G_Next=", self.get_page_information(COM___group_next_top), " G_Prev=", self.get_page_information(COM___group_previous_top))
        group_total = len(self.o_design.p[i_page+2])
        # print("グループ数：", group_total)
        for i_group in range(group_total-1):
            # 各グループを表示
            print("　グループ(" + str(i_group) +", " + str(self.get_group(i_group, COM__group_next))+", " + str(self.get_group(i_group, COM__group_previous))+") ", end="")
            component_total = len(self.o_design.p[i_page+2][i_group+1])
            # print("コンポーネント数：", component_total)
            s = "　コンポーネント＝"
            for i_component in range(1, component_total):
                s += "「" + self.o_design.p[i_page+2][i_group+1][i_component][4][COM_text]+ "」"
                # 各コンポーネントを表示
            print(s)

        print(self.o_design.p[i_page+2])

        # ページ番号を戻す
        self.page_no = save_page_no

    def add_component_element(self, g_no, i, data):
        ################################
        # コンポーネント要素の追加        
        ################################
        self.o_design.p[self.page_no+2][g_no+1][i+1][4].append(data)

    def add_group_element(self, g_no, data):
        ################################
        # グループ要素の追加        
        ################################
        self.o_design.p[self.page_no+2][g_no+1][0].append(data)

    def decide_page_dual_list(self):
        ################################
        # ページ番号の双方向リストを作成    
        ################################
        #999
        
        print("max_page_no:", self.max_page_no)
        # ルートのNext_topを決める
        self.set_root_information(COM____page_next_top, 0)

        # ルートのPrevious_topを決める
        self.set_root_information(COM____page_previous_top, self.max_page_no)

        if self.max_page_no == 0:
            # ページが１個のみ
            for i_page in range(self.max_page_no+4):
                self.page_no = i_page
                self.set_page_information(COM___page_next, -1)
                self.set_page_information(COM___page_previous, -1)
            
        else:
            # ページが２以上    
            
            # 各ページに書き込んでいく
            for i_page in range(self.max_page_no+1):
                # ページ番号を設定    
                self.page_no = i_page
                # Nextは１つ多くする
                if i_page == self.max_page_no:
                    # 最後なので-1    
                    self.set_page_information(COM___page_next, -1)
                else:
                    # 最後でないので１多くする
                    self.set_page_information(COM___page_next, i_page+1)
        
                # Previousは１つ少なくする    
                if i_page == 0:
                    # 最初なので-1
                    self.set_page_information(COM___page_previous, -1)
                else:
                    # 最初でないので１少なくする        
                    self.set_page_information(COM___page_previous, i_page-1)
       
        self.page_no = 0

        print("＠＠＠　decide_page_dual_list:", self.o_design.p[0])
        
    def delete_component_element(self, g_no, i):
        ################################
        # コンポーネント要素の削除        
        ################################
        self.o_design.p[self.page_no+2][g_no+1][i+1][4].pop()

    def delete_group_element(self, g_no):
        ################################
        # グループ要素の削除        
        ################################
        self.o_design.p[self.page_no+2][g_no+1][0].pop()

    def delete_list(self, n):
        #################################
        # 削除
        #################################
        if 0 <= n < self.len_group()-1:
            
            # print(n, "番目のリスト「", n, "」を削除")
            # (1)削除エントリのNext=3 Prev=1を保存
            Delete_next = self.get_group(n, COM__group_next)
            Delete_prev = self.get_group(n, COM__group_previous)

            # (2)削除エントリを-1, -1, -1, "削"に
            self.set_group(n, COM__current_group, -1)
            self.set_group(n, COM__group_next, -1)
            self.set_group(n, COM__group_previous, -1)

            # (3)削除エントリのNext=3のエントリのPrev=1に変更
            # (3)削除エントリのNext=-1のエントリがないときは、Pを削除エントリのPrevに変更
            if Delete_next == -1:
                # 次のエントリがない
                self.set_page_information(COM___group_previous_top, Delete_prev)
            else:
                self.set_group(Delete_next, COM__group_previous, Delete_prev)
            # (4)削除エントリのPrev=1のエントリのNext=3に変更
            # (4)削除エントリのPrev=-1のエントリがないときは、Nを削除エントリのNextに変更
            if Delete_prev == -1:
                # 前のエントリがない
                self.set_page_information(COM___group_next_top, Delete_next)
            else:
                # 前のエントリがある
                self.set_group(Delete_prev, COM__group_next, Delete_next)
            # (5)エントリ数の低減
            self.set_page_information(COM___group_entry_no, self.get_page_information(COM___group_entry_no)-1)

            # コンポーネント数の削減
            component_remain = self.len_component(n)
            for i in range(component_remain-1):
                self.o_design.p[self.page_no + 2][n+1].pop(2)

        else:
            print(n, "番目のリスト「", n, "」は存在しないので削除できない")
                 
    def clean_component(self, group_no):
        #################################
        # コンポーネントを新規作成
        #################################
        self.margin = self.get_root_information(COM____margin)

        # 新たなコンポーネントを作る
        self.create_new_component(group_no, self.margin, False)
              
    def clean_group(self, group_no):
        #################################
        # グループを新規作成
        #################################
        self.set_group(group_no, COM__dir, DIR_COLUMN)
        self.set_group(group_no, COM__group_x, self.get_group_right(COM__group_x))
        self.set_group(group_no, COM__group_y, self.get_group_right(COM__group_y))
        self.set_group(group_no, COM__group_width, self.get_group_right(COM__group_width))
        height = self.get_group_right(COM__group_height)
        if height <= 40:
            font_size = 10
        else:
            font_size = height - 30   
        self.set_group(group_no, COM__group_height, height)
        self.set_group(group_no, COM__font_size, font_size)
        # self.set_group(group_no, COM__font_color, self.font_color)
        # self.set_group(group_no, COM__font_light_color, self.font_light_color)
        self.set_group(group_no, COM__font_type, self.font_type)
        self.set_group(group_no, COM__frame_color, self.page_frame_color)
        self.set_group(group_no, COM__draw_frame, draw_frame_True)
        # self.set_group(group_no, COM__back_color, COL_WHITE)
        self.set_group(group_no, COM__move_exclusive, move_exclusive_True)
        self.set_group(group_no, COM__move_inhibit, move_inhibit_True)
        self.set_group(group_no, COM__move_control, move_control_False)
        self.set_group(group_no, COM__reserve_0, RES_GROUP_FALSE)
        self.set_group(group_no, COM__reserve_1, RES_GROUP_FALSE)
        self.set_group(group_no, COM__reserve_2, RES_GROUP_FALSE)

    def create_new_component(self, group_no, margin, b_new):
        #################################
        # 新たなコンポーネントを作る
        #################################
        if b_new == True:
            # 今のコンポーネントがない
            pos = self.get_page_information(COM___group_entry_no)
            # 実際に作る    
            self.create_group_direct(\
            self.page_no,\
            pos,\
            TYP_BUTTON,\
            ["新項目"], DIR_COLUMN,\
            self.get_group_right(COM__group_x),\
            self.get_group_right(COM__group_y),\
            self.get_group_right(COM__group_width),\
            self.get_group_right(COM__group_height),\
            self.get_group_right(COM__group_width)-margin,\
            self.get_group_right(COM__group_height)-margin, 24,\
            # COL_LIGHT_BLUE, self.font_light_color, self.frame_color,\
            COL_BLUE, COL_LIGHT_BLUE, self.font_type, COL_LIGHT_BLUE,\
            draw_frame_True, COL_LIGHT_BLUE, move_exclusive_False, move_inhibit_True, move_control_False,\
            group_value_None, "URL")
            group_no = pos

        self.set_component(group_no, 0, COM_text, "新項目")
        self.set_component(group_no, 0, COM_x, self.get_group(group_no, COM__group_x)+margin)
        self.set_component(group_no, 0, COM_y, self.get_group(group_no, COM__group_y)+margin)
        self.set_component(group_no, 0, COM_width, self.get_group(group_no, COM__group_width)-margin*2)
        self.set_component(group_no, 0, COM_height, self.get_group(group_no, COM__group_height)-margin*2)
        self.set_component(group_no, 0, COM_temp_x, self.get_group(group_no, COM__group_x)+margin)
        self.set_component(group_no, 0, COM_temp_y, self.get_group(group_no, COM__group_y)+margin)
        self.set_component(group_no, 0, COM_click_offset_x, 0)
        self.set_component(group_no, 0, COM_click_offset_y, 0)
        self.set_component(group_no, 0, COM_font_color, COL_BLACK)
        self.set_component(group_no, 0, COM_font_light_color, self.font_light_color)
        self.set_component(group_no, 0, COM_back_color, COL_LIGHT_BLUE)
        self.set_component(group_no, 0, COM_font_type, FNT_GOTHIC)
        self.set_component(group_no, 0, COM_reserve_0, RES_COMPONENT_FALSE)
        self.set_component(group_no, 0, COM_reserve_1, RES_COMPONENT_FALSE)
        self.set_component(group_no, 0, COM_reserve_2, RES_COMPONENT_FALSE)
        self.set_component(group_no, 0, COM_button_url, "URL")

        # 文字数と幅と高さからフォントの大きさを計算    
        char_number = get_east_asian_width_count(self.get_component(group_no, 0, COM_text))
        font_size = self.decide_font_size(group_no, char_number)
        self.set_group(group_no, COM__font_size, font_size)
        # 方向を設定
        self.set_group(group_no, COM__dir , DIR_COLUMN)
        # タイプ
        self.set_group(group_no, COM__type , TYP_BUTTON)
        
        # 新しいグループ番号を返す
        return group_no
        
    def decide_font_size(self, group_no, char_number):    
        #################################
        # フォントサイズを幅と高さから決定
        #################################
        font_size_by_right = int((self.get_component(group_no, 0, COM_width) - 22) / char_number * 2)
        font_size_by_bottom = self.get_component(group_no, 0, COM_height) - 14
        font_size = min(font_size_by_right, font_size_by_bottom)
        if font_size < 8:
            font_size = 8
        return font_size         
                 
    def display_list(self):
        #################################
        # 開始から表示
        #################################
        
        f_start = True 
        # print("Next=", self.get_page_information(COM___group_next_top),\
        #     " Previous=", self.get_page_information(COM___group_previous_top),\
        #     " Entry_no=", self.get_page_information(COM___group_entry_no))
        # nextが-1になるまで表示 
        while True:
            if f_start == True:
                f_start = False
                # 先頭ページを表示
                pos = self.get_page_information(COM___group_next_top)
            else:
                pos = self.get_group(pos, COM__group_next)
            # 本処理
            # print(self.get_group(pos, COM__current_group), self.get_group(pos, COM__group_next), self.get_group(pos, COM__group_previous))
            if  self.get_group(pos, COM__group_next) == -1:
                break
    
    def insert_list(self, group_no=-1):
        #################################
        # リストの最後に挿入
        #################################

        if group_no == -1:
            # 新規グループ場所
            # (1)空き場所を探し、それをnにする
            b_found = False
            for i in range(self.len_group()-1):
                if self.get_group(i, COM__current_group) == -1:
                    # 空き場所発見
                    n = i
                    b_found = True
                    break
        else:
            n = group_no                
            b_found = True

        # (2)新グループを追加  
        if b_found == False:
            n = self.get_page_information(COM___group_entry_no)
            self.set_group(n, COM__current_group, -1)
            self.set_group(n, COM__group_next, -1)
            self.set_group(n, COM__group_previous, -1)
                
            # これは、すでにエントリができている

        # (3)グループを設定
        self.set_group(n, COM__current_group, n)
        self.set_group(n, COM__group_next, -1)
        self.set_group(n, COM__group_previous, self.get_page_information(COM___group_previous_top))
            # これは、データの設定が終わっておる前提

        # (4)前後設定
        if self.get_page_information(COM___group_previous_top) != -1:
            # 前エントリがあった
            self.set_group(self.get_page_information(COM___group_previous_top), COM__group_next, n)
        self.set_page_information(COM___group_previous_top, n)
        if self.get_page_information(COM___group_next_top) == -1:
            self.set_page_information(COM___group_next_top, 0)

        # (5)エントリ数を１増やす
        self.set_page_information(COM___group_entry_no, self.get_page_information(COM___group_entry_no)+1)

        if b_found == True:
            # 再利用
            self.set_group(n, COM__type, TYP_BUTTON)
            self.clean_group(n)
            self.clean_component(n)
            self.set_group_right(COM__group_x, -100)
            self.set_group_right(COM__group_y, -100)
            self.set_group_right(COM__group_width, 4)
            self.set_group_right(COM__group_height, 4)

            # print("再利用　n=",n, " ダンプ：" ,self.o_design.p)
    
    def insert_list_oldest(self, page_no, group_no):
        #################################
        # リストの最後に挿入
        #################################
        # (1)空き場所を探し、それをnにする
        b_found = False
        for i in range(self.len_group()-1):
            if self.get_group(i, COM__current_group) == -1:
                # 空き場所発見
                n = i
                b_found = True
                break

        # (2)新グループを追加  
        if b_found == False:
            n = self.get_page_information(COM___group_entry_no)
            self.set_group(n, COM__current_group, -1)
            self.set_group(n, COM__group_next, -1)
            self.set_group(n, COM__group_previous, -1)
                
            # これは、すでにエントリができている

        # (3)グループを設定
        self.set_group(n, COM__current_group, n)
        self.set_group(n, COM__group_next, -1)
        self.set_group(n, COM__group_previous, self.get_page_information(COM___group_previous_top))

        # (4)前後設定
        if self.get_page_information(COM___group_previous_top) != -1:
            # 前エントリがあった
            self.set_group(self.get_page_information(COM___group_previous_top), COM__group_next, n)
        self.set_page_information(COM___group_previous_top, n)
        if self.get_page_information(COM___group_next_top) == -1:
            self.set_page_information(COM___group_next_top, 0)

        # (5)エントリ数を１増やす
        self.set_page_information(COM___group_entry_no, self.get_page_information(COM___group_entry_no)+1)

    def end_group(self, group_no):
        ###########################
        # グループ終了情報を設定
        ###########################

        # print("end_group", group_no)
        if group_no == -1:
            return
        
        # グループの最後のエントリを設定
        self.set_group(group_no, COM__group_next, -1)
        # グループ終了情報を設定
        self.set_page_information(COM___group_previous_top, group_no)

        # グループのエントリ数を設定
        self.set_page_information(COM___group_entry_no, group_no + 1)

    def create_page_0(self, page_no):
        ###########################
        # ページ０の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成
            self.create_page_top(self.page_no, "")
                     
            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, -1)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["赤と青とどちらが好きですか？"],\
                DIR_COLUMN,\
                220, 5, 600, 50, 550, 40, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["　"],\
                DIR_COLUMN,\
                220, 550, 600, 50, 550, 40, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # ２つの縦トグルを作成
            # pos += 1
            # self.create_group_direct(page_no, pos, TYP_TOGGLE, ["設計", "実行"], DIR_COLUMN,\
            #     1340, 20, 110, 80, 110, 40, 20,\
            #     COL_RED, COL_ORANGE, self.font_type, self.frame_color,\
            #     self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
            #     MOD_EXECUTE, component_value_None)
            # # 初期値で実行モードにする
            # self.set_group(pos, COM__toggle_value, MOD_EXECUTE)
            # self.set_root_information(COM____mode, MOD_EXECUTE)
            
            # ２つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["赤", "青"], DIR_ROW,\
                500, 200, 600, 300, 280, 300, 44,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_True,\
                # self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_False,\
                -1, "URL")

            # ４つの横ボタンを作成
            # move_controlがTrueなので、次にいける
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "データの読込", "データを保存", "表示"], DIR_ROW,\
                490, 630, 830, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_True,\
                # self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_False,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False

            # グループの削除
            # self.delete_group_element(0)

            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False

            # 再利用
            self.use_page(page_no)

            # print(self.o_design.p)

    def create_page_copyright(self, page_no):
        ###########################
        # コピーライトページの作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "Copyright")

            #88888888    
            # print(self.o_design.p)

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["NOCK(NO Coding Kit)"],\
                DIR_COLUMN,\
                550, 80, 600, 50, 550, 40, 36,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["designed by 25182102, 25182124, 25182227", "coded by Yamashita Laboratory"],\
                DIR_COLUMN,\
                450, 150, 600, 230, 550, 100, 24,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # １つの縦スライダーを作成
            # pos += 1
            # self.create_group_direct(page_no, pos, TYP_SLIDER, ["Red  ", "Green", "Blue "], DIR_COLUMN,\
            #     300, 150, 420, 330, 400, 60, 28,\
            #     self.font_color, self.font_light_color, self.font_type, self.frame_color,\
            #     self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_True, move_control_False,\
            #     group_value_None, [0.6, 0, 255])

            # １つの縦画像を作成
            # pos += 1
            
            # # フレームの色を変える
            # self.create_group_direct(page_no, pos, TYP_FRAME, ["色データ"], DIR_COLUMN,\
            #     800, 116, 400, 400, 300, 300, 32,\
            #     self.font_color, self.font_light_color, self.font_type, self.frame_color,\
            #     self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
            #     group_value_None, 255)

            # １つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["OK"], DIR_ROW,\
                1120, 570, 250, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            # グループの削除
            # self.delete_group_element(3)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_file_list(self, page_no):
        ###########################
        # ファイルリストページの作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "File_list")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # ファイルリストを獲得
            file_list = self.file_list_up("game_back_*.jpg")
            length = len(file_list)
            cut_len = len(self.get_root_information(COM____data_path))
            new_file_list = []
            for i in range(length):
                # 前を切る
                # './data\\game_back_stars.jpg'
                
                s = file_list[i][cut_len:]
                new_file_list.append(s)

            # print(new_file_list)
            # print(self.o_design.p[6])
            # exit(0)    
            
            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["使用する画像を選んでください。"],\
                DIR_COLUMN,\
                450, 50, 600, 50, 550, 40, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # １つの縦画像を作成(1024x576)
            pos += 1
            # file_list = ['Fighter_00.png']
            self.create_group_direct(page_no, pos, TYP_TOGGLE, new_file_list, DIR_COLUMN,\
                500, 150, 480, 400, 460, 70, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
                group_value_None, 255)

            # １つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["ファイルの決定", "キャンセル"], DIR_ROW,\
                920, 570, 520, 70, 250, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            # グループの削除
            # self.delete_group_element(3)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)





        # # グループ全体を書き出す            
        # if len(self.o_design.p)-2 <= page_no:
        #     self.new_page = True
        #     self.o_group = [] 

        #     self.o_design.p.append([])

        #     pos = -1
        #     # 新しいページを作成    
        #     self.create_page_top(self.page_no)

        #     # グループ開始情報を設定
        #     self.set_page_information(COM___group_next_top, -1)

        #     # ファイルリストを獲得
        #     file_list = self.file_list_up("game_back_*.jpg")
        #     length = len(file_list)

        #     print(self.o_design.p[6])

        #     # １つの縦トグルを作成
        #     pos += 1
        #     # self.create_group_direct(page_no, pos, TYP_TOGGLE, file_list,\
        #     self.create_group_direct(page_no, pos, TYP_TOGGLE, ["game_back_mountain.jpg"],\
        #         DIR_COLUMN,\
        #         450, 50, 600, 50 * length + self.get_root_information(COM____margin) * (length + 1), 550, 50, 40,\
        #         self.font_color, self.font_light_color, self.font_type, self.frame_color,\
        #         self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
        #         group_value_None, component_value_None)

        #     # １つの縦画像を作成(1024x576)
        #     # pos += 1
        #     # self.create_group_direct(page_no, pos, TYP_IMAGE, [image], DIR_COLUMN,\
        #     #     590, 220, 300, 240, 300, 220, 32,\
        #     #     self.font_color, self.font_light_color, self.font_type, self.frame_color,\
        #     #     self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
        #     #     group_value_None, 255)

        #     # １つの横ボタンを作成
        #     pos += 1
        #     self.create_group_direct(page_no, pos, TYP_BUTTON, ["決定", "キャンセル"], DIR_ROW,\
        #         920, 570, 450, 70, 200, 60, 32,\
        #         self.font_color, self.font_light_color, self.font_type, self.frame_color,\
        #         #222        
        #         # self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
        #         self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
        #         -1, "URL")

        #     # ６つの制御ボタンを作成
        #     pos += 1
        #     self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                # 360, 630, 1110, 70, 150, 60, 22,\
        #         self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
        #         self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
        #         -1, "URL")

        #     # グループ終了情報を設定
        #     self.end_group(pos)

        #     # グループの削除
        #     # self.delete_group_element(3)

        #     self.new_page = False
        #     # 再利用
        #     self.use_page(page_no)

        # else:
        #     self.new_page = False
        #     # 再利用
        #     self.use_page(page_no)

    def create_page_RGB(self, page_no):
        ###########################
        # RGBページの作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "RGB")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # # ファイルリストを獲得
            # file_list = self.file_list_up("game_back_*.jpg")
            # length = len(file_list)
            # cut_len = len(self.get_root_information(COM____data_path))
            # new_file_list = []
            # for i in range(length):
            #     # 前を切る
            #     # './data\\game_back_stars.jpg'
            #     s = file_list[i][cut_len:]
            #     new_file_list.append(s)

            # # print(new_file_list)
            # # print(self.o_design.p[6])
            # # exit(0)    
            
            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["色のRGB値を選んでください。"],\
                DIR_COLUMN,\
                450, 50, 600, 50, 550, 40, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # １つの縦スライダーを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_SLIDER, ["Red  ", "Green", "Blue "], DIR_COLUMN,\
                300, 150, 420, 330, 400, 60, 28,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_True, move_control_False,\
                group_value_None, [0.6, 0, 255])

            # １つの縦画像を作成
            pos += 1
            
            # フレームの色を変える
            self.create_group_direct(page_no, pos, TYP_FRAME, ["色データ"], DIR_COLUMN,\
                800, 116, 400, 400, 300, 300, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
                group_value_None, 255)

            # １つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["RGB値の決定", "キャンセル"], DIR_ROW,\
                920, 570, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            # グループの削除
            # self.delete_group_element(3)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_result(self, page_no, answer, image):
        ###########################
        # 結果ページの作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "Result")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, [answer],\
                DIR_COLUMN,\
                450, 50, 600, 50, 550, 40, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # １つの縦画像を作成(1024x576)
            pos += 1
            self.create_group_direct(page_no, pos, TYP_IMAGE, [image], DIR_COLUMN,\
                540, 170, 420, 400, 400, 380, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_True, move_control_False,\
                group_value_None, 255)

            # １つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["最初に戻る", "終了"], DIR_ROW,\
                920, 570, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            # グループの削除
            # self.delete_group_element(3)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_result_3_image(self, page_no, answer, image, add_image1, add_image2, add_image3):
        ###########################
        # 結果ページテキスト追加の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "Result")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, [answer],\
                DIR_COLUMN,\
                450, 50, 600, 50, 550, 40, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # １つの縦画像を作成(1024x576)
            pos += 1
            self.create_group_direct(page_no, pos, TYP_IMAGE, [image], DIR_COLUMN,\
                390, 150, 420, 420, 400, 380, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_True, move_control_False,\
                group_value_None, 255)

            # ２つの縦画像を作成(1024x576)
            pos += 1
            # 乱数で３つのうち２つを決める
            no_use_image = random.randint(0,2)
            if no_use_image == 0:
                use_image = [add_image2, add_image3]
            elif no_use_image == 1:
                use_image = [add_image1, add_image3]
            else:    
                use_image = [add_image1, add_image2]
                
            self.create_group_direct(page_no, pos, TYP_IMAGE, [use_image[0], use_image[1]], DIR_COLUMN,\
                840, 150, 220, 420, 200, 180, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_True, move_control_False,\
                group_value_None, 255)

            # １つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["最初に戻る", "終了"], DIR_ROW,\
                920, 570, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            # グループの削除
            # self.delete_group_element(3)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_selection(self, page_no, question, parm_0, parm_1):
        ###########################
        # 選択ページの作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成
            self.create_page_top(self.page_no, "Selection")
                     
            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, -1)

            # １つの縦テキストを作成
            pos += 1
            # print(pos)
            # self.create_group_direct(page_no, pos, TYP_TEXT, ["問"+str(self.page_no+1) + " " + parm_0 + "と" + parm_1 + "とどちらが好きですか？"],\
        
            self.create_group_direct(page_no, pos, TYP_TEXT, [question],\
                DIR_COLUMN,\
                350, 50, 800, 60, 700, 40, 42,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            pos += 1
            # print(pos)
            self.create_group_direct(page_no, pos, TYP_TEXT, ["　"],\
                DIR_COLUMN,\
                220, 550, 600, 50, 550, 40, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # ２つの縦トグルを作成
            # pos += 1
            # self.create_group_direct(page_no, pos, TYP_TOGGLE, ["設計", "実行"], DIR_COLUMN,\
            #     1340, 20, 110, 80, 110, 40, 20,\
            #     COL_RED, COL_ORANGE, self.font_type, self.frame_color,\
            #     self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
            #     MOD_EXECUTE, component_value_None)
            # # 初期値で実行モードにする
            # self.set_group(pos, COM__toggle_value, MOD_EXECUTE)
            # self.set_root_information(COM____mode, MOD_EXECUTE)
            
            # ２つの横ボタンを作成
            pos += 1
            # print(pos)
            self.create_group_direct(page_no, pos, TYP_BUTTON, [parm_0, parm_1], DIR_ROW,\
                140, 200, 1200, 320, 490, 300, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False

            # グループの削除
            # self.delete_group_element(0)

            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False

            # 再利用
            self.use_page(page_no)

            # print(self.o_design.p)

    def create_page_selection_2(self, page_no, question, branch_list):
        ###########################
        # 選択ページの作成（３つ以上）
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成
            self.create_page_top(self.page_no, "Selection")
                     
            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, -1)

            # １つの縦テキストを作成
            pos += 1
            # print(pos)
            # self.create_group_direct(page_no, pos, TYP_TEXT, ["問"+str(self.page_no+1) + " " + parm_0 + "と" + parm_1 + "とどちらが好きですか？"],\
        
            self.create_group_direct(page_no, pos, TYP_TEXT, [question],\
                DIR_COLUMN,\
                350, 50, 800, 60, 700, 40, 42,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            pos += 1
            # print(pos)
            self.create_group_direct(page_no, pos, TYP_TEXT, ["　"],\
                DIR_COLUMN,\
                220, 550, 600, 50, 550, 40, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # ２つの横ボタンを作成
            pos += 1
            # print(pos)
            name_list = []
            len_branch_list = len(branch_list)  
            for i in range(len_branch_list):
                name_list.append(branch_list[i][0])

            # 横幅を調整しておく
            margin = self.get_root_information(COM____margin)

            component_width = (1200 - margin * (len_branch_list + 1)) // len_branch_list 
            self.create_group_direct(page_no, pos, TYP_BUTTON, name_list, DIR_ROW,\
                140, 200, 1200, 320, component_width, 300, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False

            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False

            # 再利用
            self.use_page(page_no)

    def create_page_start(self, page_no, question):#, branch_list):
        ###########################
        # 開始ページの作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成
            self.create_page_top(self.page_no, "Start")
                     
            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, -1)

            # １つの縦テキストを作成
            pos += 1
            # print(pos)
            # self.create_group_direct(page_no, pos, TYP_TEXT, ["問"+str(self.page_no+1) + " " + parm_0 + "と" + parm_1 + "とどちらが好きですか？"],\
        
            self.create_group_direct(page_no, pos, TYP_TEXT, [question],\
                DIR_COLUMN,\
                350, 50, 800, 60, 700, 40, 42,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # pos += 1
            # # print(pos)
            # self.create_group_direct(page_no, pos, TYP_TEXT, ["　"],\
            #     DIR_COLUMN,\
            #     220, 550, 600, 50, 550, 40, 40,\
            #     self.font_color, self.font_light_color, self.font_type, self.frame_color,\
            #     self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
            #     group_value_None, component_value_None)

            # ２つの横ボタンを作成
            # pos += 1
            # # print(pos)
            # name_list = []
            # len_branch_list = len(branch_list)  
            # for i in range(len_branch_list):
            #     name_list.append(branch_list[i][0])

            # 横幅を調整しておく
            # margin = self.get_root_information(COM____margin)

            # component_width = (1200 - margin * (len_branch_list + 1)) // len_branch_list 
            # self.create_group_direct(page_no, pos, TYP_BUTTON, name_list, DIR_ROW,\
            #     140, 200, 1200, 320, component_width, 300, 40,\
            #     self.font_color, self.font_light_color, self.font_type, self.frame_color,\
            #     self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_False,\
            #     -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False

            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False

            # 再利用
            self.use_page(page_no)

    def create_page_start_2(self, page_no, question):
        ###########################
        # 開始ページの作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "Start")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # ファイルリストを獲得（CSVファイル）
            file_list = self.file_list_up("page_data_*.csv")
            length = len(file_list)
            cut_len = len(self.get_root_information(COM____data_path))
            new_file_list = []
            for i in range(length):
                # 前を切る
                s = file_list[i][cut_len:]
                new_file_list.append(s)

            # コンポーネント数から文字サイズを指定
            if length >= 7:
                font_size = 20
                component_height = 40
            else:    
                font_size = 32
                component_height = 70

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, [question],\
                DIR_COLUMN,\
                300, 50, 900, 50, 850, 40, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # １つの縦トグルを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TOGGLE, new_file_list, DIR_COLUMN,\
                400, 150, 680, 400, 660, component_height, font_size,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_True, move_control_False,\
                group_value_None, 255)

            # １つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["シナリオの決定", "キャンセル"], DIR_ROW,\
                920, 570, 520, 70, 250, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            # グループの削除
            # self.delete_group_element(3)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_new(self, page_no, question):
        ###########################
        # 新ページの作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "New")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # ファイルリストを獲得（CSVファイル）
            # file_list = self.file_list_up("page_data_*.csv")
            # length = len(file_list)
            # cut_len = len(self.get_root_information(COM____data_path))
            # new_file_list = []
            # for i in range(length):
            #     # 前を切る
            #     s = file_list[i][cut_len:]
            #     new_file_list.append(s)

            # # コンポーネント数から文字サイズを指定
            # if length >= 7:
            #     font_size = 20
            #     component_height = 40
            # else:    
            #     font_size = 32
            #     component_height = 70

            # １つの縦テキストを作成
            # pos += 1
            # self.create_group_direct(page_no, pos, TYP_TEXT, [question],\
            #     DIR_COLUMN,\
            #     300, 50, 900, 50, 850, 40, 40,\
            #     self.font_color, self.font_light_color, self.font_type, self.frame_color,\
            #     self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
            #     group_value_None, component_value_None)

            # １つの縦トグルを作成
            # pos += 1
            # self.create_group_direct(page_no, pos, TYP_TOGGLE, new_file_list, DIR_COLUMN,\
            #     400, 150, 680, 400, 660, component_height, font_size,\
            #     self.font_color, self.font_light_color, self.font_type, self.frame_color,\
            #     self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
            #     group_value_None, 255)

            # １つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "終了"], DIR_ROW,\
                670, 570, 770, 70, 250, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            # グループの削除
            # self.delete_group_element(3)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_result_URL(self, page_no, answer, URL_name, URL_address):
        ###########################
        # 結果ページURL付きの作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "Result_URL")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, [answer],\
                DIR_COLUMN,\
                450, 50, 600, 50, 550, 40, 40,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # １つの縦ボタンを作成(URLボタン)
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, [URL_name], DIR_COLUMN,\
                290, 280, 900, 120, 880, 110, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_True, move_control_False,\
                group_value_None, URL_address)

            # １つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["最初に戻る", "終了"], DIR_ROW,\
                920, 570, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ６つの制御ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データの読込", "データを保存", "htmlを作成", "終了"], DIR_ROW,\
                360, 630, 1110, 70, 150, 60, 22,\
                self.font_color, self.font_light_color, FNT_GOTHIC, self.frame_color,\
                self.draw_frame, COL_PINK, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_0_old(self, page_no):
        ###########################
        # ページ０の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成
            self.create_page_top(self.page_no, "")
                     
            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, -1)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["[0]ゲームのプログラムを開始するか、そのままゲームを開始するか、終了を選んでください。"],\
                DIR_COLUMN,\
                20, 5, 1200, 50, 1160, 40, 20,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # # １つの縦テキストを作成
            pos += 1
            # self.create_group_direct(page_no, pos, TYP_TEXT, ["ノープログラミングでゲーム作成 Ver1.0"], DIR_COLUMN,\
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["ゲーム作成 Ver1.00", "ゲーム作成 Ver2.012345"], DIR_COLUMN,\
            # self.create_group_direct(page_no, pos, TYP_BUTTON, ["ゲーム作成 Ver2.012345"], DIR_COLUMN,\
                # 290, 290, 890, 90, 880, 80, 44,\
                # 290, 290, 890, 290, 770, 70, 44,\
                # 290, 290, 520, 290, 500, 70, 44,\
                290, 290, 520, 310, 500, 140, 44,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_False,\
                group_value_None, component_value_None)

            # ２つの縦トグルを作成
            # pos += 1
            # self.create_group_direct(page_no, pos, TYP_TOGGLE, ["設計", "実行"], DIR_COLUMN,\
            #     1340, 20, 110, 80, 110, 40, 20,\
            #     COL_RED, COL_ORANGE, self.font_type, self.frame_color,\
            #     self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
            #     MOD_EXECUTE, component_value_None)
            # # 初期値で実行モードにする
            # self.set_group(pos, COM__toggle_value, MOD_EXECUTE)
            # self.set_root_information(COM____mode, MOD_EXECUTE)
            
            # ４つの横ボタンを作成
            pos += 1
            # self.create_group_d65ect(page_no, pos, TYP_BUTTON, ["次に進む", "データの読込", "ゲームを開始", "表示", "項目削除"], DIR_ROW,\
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "データを保存"], DIR_ROW,\
                420, 630, 480, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False

            # グループの削除
            # self.delete_group_element(0)

            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False

            # 再利用
            self.use_page(page_no)

    def create_page_1(self, page_no):
        ###########################
        # ページ１の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つの縦画像を作成(1024x576)
            pos += 1
            self.create_group_direct(page_no, pos, TYP_IMAGE, ["赤.jpg"], DIR_COLUMN,\
                420, 100, 600, 480, 580, 460, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
                group_value_None, 255)

            # ２つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "ゲームを開始"], DIR_ROW,\
                920, 630, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            # グループの削除
            # self.delete_group_element(3)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_1_old(self, page_no):
        ###########################
        # ページ１の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つのフレームを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_FRAME, ["フレーム１"], DIR_COLUMN,\
                370, 46, 1024, 576, 1000, 570, 24,\
                COL_LIGHT_BLUE, self.font_light_color, self.font_type, self.frame_color,\
                draw_frame_False, self.page_frame_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, 0)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT,\
                ["[1]背景にする画像を左からマウスで選び、右の水色四角の中に落としてください。「ゲームを開始」なら、今のゲームが始まります。"], DIR_COLUMN,\
                20, 5, 1300, 50, 1300, 40, 20,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # ４つの縦画像を作成(1024x576)
            pos += 1
            self.create_group_direct(page_no, pos, TYP_IMAGE, ["game_back_stars.jpg", "game_back_forest.jpg", "game_back_mountain.jpg", "game_back_space.jpg"], DIR_COLUMN,\
                80, 100, 224, 500, 204, 114, 16,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
                group_value_None, 255)

            # ２つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "ゲームを開始"], DIR_ROW,\
                920, 630, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            # グループの削除
            # self.delete_group_element(3)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_2(self, page_no):
        ###########################
        # ページ２の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つの縦画像を作成(1024x576)
            pos += 1
            self.create_group_direct(page_no, pos, TYP_IMAGE, ["青.jpg"], DIR_COLUMN,\
                420, 100, 600, 480, 580, 460, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
                group_value_None, 255)

            # ２つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "ゲームを開始"], DIR_ROW,\
                920, 630, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            # グループの削除
            # self.delete_group_element(3)

            self.new_page = False
            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_2_old(self, page_no):
        ###########################
        # ページ２の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つのフレームを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_FRAME, ["フレーム２"], DIR_COLUMN,\
                470, 192, 678, 384, 672, 378, 24,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                draw_frame_False, self.page_frame_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, 0)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT,\
                ["[2]プレイヤーにする画像を左からマウスで選び、右の水色四角の中に落としてください。プレイヤーの数も指定できます。"], DIR_COLUMN,\
                20, 5, 1200, 50, 1180, 40, 20,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # ４つの縦画像を作成(1024x576)
            pos += 1
            self.create_group_direct(page_no, pos, TYP_IMAGE, ["fighter_00.png", "fighter_01.png", "fighter_02.png", "fighter_03.png"], DIR_COLUMN,\
                80, 100, 148, 500, 128, 64, 16,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
                group_value_None, 255)

            # ２つの縦スライダーを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_SLIDER, ["残機", "残ライフ"], DIR_COLUMN,\
                450, 60, 520, 120, 500, 40, 24,\
                COL_BLUE, COL_LIGHT_BLUE, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                group_value_None, [0.5, 7, 20])

            # ２つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る"], DIR_ROW,\
                920, 630, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False
            # 再利用

            # グループの削除
            # self.delete_group_element(4)

            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_3(self, page_no):
        ###########################
        # ページ３の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, -1)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["[3]ステージの数を、マウスでスライダーをクリックし指示してください。"], DIR_COLUMN,\
                20, 5, 1040, 50, 1000, 40, 20,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # １つの縦スライダーを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_SLIDER, ["残機数"], DIR_COLUMN,\
                420, 80, 520, 50, 500, 40, 24,\
                COL_BLUE, COL_LIGHT_BLUE, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                group_value_None, [0.2, 2, 9])

            # ２つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る"], DIR_ROW,\
                920, 630, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False

            # グループの削除
            # self.delete_group_element(0)

            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)
        
    def create_page_4(self, page_no):
        ###########################
        # ページ４の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.o_group = [] 
            self.new_page = True

            pos = -1
            self.o_design.p.append([])

            # 新しいページを作成    
            self.create_page_top(self.page_no, "")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つのフレームを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_FRAME, ["フレーム４"], DIR_COLUMN,\
                370, 46, 1024, 576, 1000, 572, 24,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                draw_frame_False, self.page_frame_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, 0)

            # print("Page_4 active_frame=", self.get_page_information(COM___active_frame))

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["[4]敵キャラにする画像を左からマウスで選び、右の水色四角の中に落としてください。"],\
                DIR_COLUMN,\
                20, 5, 1000, 40, 1000, 40, 20,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # ４つの縦画像を作成(1024x576)
            pos += 1
            self.create_group_direct(page_no, pos, TYP_IMAGE, ["enemy_00.png", "enemy_01.png", "enemy_02.png", "enemy_03.png"], DIR_COLUMN,\
                80, 50, 168, 620, 128, 128, 16,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_False,\
                group_value_None, 255)

            # ２つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る"], DIR_ROW,\
                920, 630, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False

            # グループの削除
            # self.delete_group_element(3)

            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_5(self, page_no):
        ###########################
        # ページ５の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つのフレームを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_FRAME, ["フレーム５"], DIR_COLUMN,\
                370, 46, 1024, 576, 1000, 560, 24,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                draw_frame_False, self.page_frame_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, 0)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["[5]スコア・ハイスコア・残機などの位置を、右の水色四角の中で指定してください。"],\
                DIR_COLUMN,\
                20, 5, 1000, 40, 1000, 40, 20,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # ４つの縦ボタンを作成
            pos += 1
            
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["スコア", "ハイスコア", "残機", "クロック"], DIR_COLUMN,\
                80, 100, 220, 400, 200, 40, 30,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_False,\
                # self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, "URL")

            # ２つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る"], DIR_ROW,\
                920, 630, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False
            # 他のグループのコンポーネントが目標とするフレームを指定

            # グループの削除
            # self.delete_group_element(3)

            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 他のグループのコンポーネントが目標とするフレームを指定

            # 再利用
            self.use_page(page_no)

    def create_page_6(self, page_no):
        ###########################
        # ページ６の作成
        ###########################
        # グループ全体を書き出す            
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つのフレームを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_FRAME, ["フレーム６"], DIR_COLUMN,\
                370, 46, 1024, 576, 1000, 560, 24,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                draw_frame_False, self.page_frame_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, 0)

            # １つの縦テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT,\
                ["[6]流す音楽を左からマウスで選び、右の水色四角の中に落としてください。「データを保存」で新たなゲームが始まります。"], DIR_COLUMN,\
                20, 5, 1300, 50, 1280, 40, 20,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # ３つの縦音楽を作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_MUSIC, ["唱.mp3", "BringBangBangBorn.mp3", "アイドル２.mp3"], DIR_COLUMN,\
                30, 100, 340, 450, 320, 40, 30,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
                [-1, -1], component_value_None)

            # ３つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る", "データを保存"], DIR_ROW,\
                700, 630, 670, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False

            # グループの削除
            # self.delete_group_element(3)

            # 再利用
            self.use_page(page_no)

        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def create_page_7(self, page_no):
        ###########################
        # ページの作成
        ###########################
        if len(self.o_design.p)-2 <= page_no:
            self.new_page = True
            self.o_group = [] 

            self.o_design.p.append([])

            pos = -1
            # 新しいページを作成    
            self.create_page_top(self.page_no, "")

            # グループ開始情報を設定
            self.set_page_information(COM___group_next_top, -1)

            # １つのフレームを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_FRAME, ["フレーム_デフォルト"], DIR_COLUMN,\
                590, 100, 420, 400, 400, 380, 24,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                draw_frame_False, self.page_frame_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, component_value_None)

            # 他のグループのコンポーネントが目標とするフレームを指定
            self.set_page_information(COM___active_frame, 0)

            # ４つの縦画像を作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_IMAGE, ["dragon_00.png", "dragon_01.png", "dragon_02.png", "dragon_03.png"], DIR_COLUMN,\
                20, 100, 140, 480, 120, 114, 16,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_True, move_control_False,\
                group_value_None, 255)

            # ６つの縦ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["タイトル", "次へ", "前へ", "書出", "読込", "新規"], DIR_COLUMN,\
                370, 100, 220, 400, 200, 40, 30,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_False,\
                -1, "URL")

            # ３つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["Max", "Average", "Min"], DIR_ROW,\
                20, 50, 700, 50, 200, 40, 24,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_False, move_control_False,\
                -1, "URL")

            # ４つの横画像を作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_IMAGE, ["dragon_00.png", "dragon_01.png", "dragon_02.png", "dragon_03.png"], DIR_ROW,\
                160, 520, 820, 50, 120, 114, 24,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_False,\
                group_value_None, 255)

            # ２つの横スライダーを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_SLIDER, ["第１スライダー", "第２スライダー"], DIR_ROW,\
                650, 520, 820, 50, 400, 40, 24,\
                COL_BLUE, COL_LIGHT_BLUE, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, [0.5, 1, 10])

            # ２つの縦スライダーを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_SLIDER, ["第Ａスライダー", "第Ｂスライダー"], DIR_COLUMN,\
                750, 570, 420, 110, 400, 40, 24,\
                COL_BLUE, COL_LIGHT_BLUE, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, [0.2, 3, 6])

            # ４つの縦トグルを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TOGGLE, ["北風", "東風", "南風", "西風"], DIR_COLUMN,\
                170, 100, 200, 200, 180, 40, 30,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, component_value_None)

            # ３つの横トグルを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TOGGLE, ["序", "破", "急"], DIR_ROW,\
                860, 30, 570, 50, 180, 40, 30,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                -1, component_value_None)

            # ４つの縦チェックボックスを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_CHECKBOX, ["北海道", "本州", "四国", "九州"], DIR_COLUMN,\
                170, 310, 200, 200, 180, 40, 30,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, -1)

            # ３つの横チェックボックスを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_CHECKBOX, ["一年", "十年", "百年"], DIR_ROW,\
                1020, 100, 360, 50, 110, 40, 30,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_False,\
                group_value_None, -1)

            # ３つの縦音楽を作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_MUSIC, ["唱.mp3", "BringBangBangBorn.mp3", "アイドル.mp3"], DIR_COLUMN,\
                1024, 160, 350, 150, 340, 40, 30,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_True,\
                [-1, -1], component_value_None)

            # ３つの横音楽を作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_MUSIC, ["レーザー.mp3", "爆発.mp3"], DIR_ROW,\
                1010, 400, 460, 50, 210, 40, 30,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_True, move_inhibit_True, move_control_True,\
                [-1, -1], component_value_None)

            # ２つの横テキストを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_TEXT, ["サンプル", "本番"], DIR_ROW,\
                20, 5, 440, 50, 180, 40, 30,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_False, move_control_False,\
                group_value_None, component_value_None)

            # ２つの横ボタンを作成
            pos += 1
            self.create_group_direct(page_no, pos, TYP_BUTTON, ["次に進む", "前に戻る"], DIR_ROW,\
                940, 610, 450, 70, 200, 60, 32,\
                self.font_color, self.font_light_color, self.font_type, self.frame_color,\
                self.draw_frame, self.group_back_color, move_exclusive_False, move_inhibit_True, move_control_True,\
                -1, "URL")

            # グループ終了情報を設定
            self.end_group(pos)

            self.new_page = False

            # グループの削除
            # self.delete_group_element(3)

            # 再利用
            self.use_page(page_no)
        else:
            self.new_page = False
            # 再利用
            self.use_page(page_no)

    def use_page(self, page_no):
        ###########################
        # ページの再利用
        ###########################
        self.page_no = page_no
        # self.set_page_information(COM___active_frame, self.active_frame)
        self.draw_mode = True
        
        # 最初にリセット    
        self.set_root_information(COM____right_mouse, MOU_CLICK_FALSE)
        
    def decrease_page_no(self):
        ###########################
        # ページ番号を減らす
        ###########################
        if self.page_no == 0:
            self.page_no = self.max_page_no
            # 設計時に選択されているグループ番号
            self.select_group_no_on_design = 0
            self.select_component_no_on_design = 0
            self.set_root_information(COM____cur_page_no, self.max_page_no)
        else:    
            self.page_no -= 1
            # 設計時に選択されているグループ番号
            self.select_group_no_on_design = 0
            self.select_component_no_on_design = 0
            self.set_root_information(COM____cur_page_no, self.get_root_information(COM____cur_page_no)-1)

        # キャプションに書き出す
        self.draw_window_title()


    def draw(self, mode):
        ###########################
        # ページの描画
        ###########################

        # 背景を画像か色で描画
        if type(self.get_page_information(COM___back_color)) is str:
            # ファイルの文字列
            # print("back_color=「"+ self.get_page_information(COM___back_color)+ "」")
            if self.get_page_information(COM___back_color) == " ":
                # ファイルでない
                # RGB色
                #11111111
                self.page_no = 0
                # print("===", self.page_no, self.o_design.p[self.page_no+2])
                
                # self.set_page_information(COM___back_color, (255, 255, 0))
                # screen.fill(self.get_page_information(COM___back_color))
                screen.fill(COL_WHITE)
            else:                
                # ページ背景ファイル名を指定
                file_name = self.get_root_information(COM____data_path) + self.get_page_information(COM___back_color)

                # print("file_name=", file_name, "COM_DATA_PATH=", self.get_root_information(COM____data_path))    
                #11111111
                if file_name == self.get_root_information(COM____data_path):
                    print("ファイルがない")
                    exit(0)
                
                # イメージを作成
                image = pygame.transform.scale(pygame.image.load((file_name)).convert_alpha(), (1480, 700)) 

                # 半透明のサーフェスを作成
                # image.set_alpha(128)
                image.set_alpha(255)

                screen.blit(image, (0, 0))

        else:    
            # RGB色
            screen.fill(self.get_page_information(COM___back_color))

        if mode == False:
            # 初期画面作成
            # コンポーネントを描画
            pass
        else:
            # 作成済み画面表示
            if len(self.o_design.p)-2 >= self.page_no: 
                pass
            else:
                self.page_no = 0

            # 左下でコピーライト
            #7777777
            pygame.draw.rect(screen, COL_PINK, (10, self.screen_height - 30, 20, 20))
            pygame.draw.rect(screen, COL_RED, (10, self.screen_height - 30, 20, 20), 2)
                
            f_start = True
            while True:
                if f_start == True:
                    # グループ開始を設定
                    i_group = self.get_page_information(COM___group_next_top)

                    if i_group == -1:
                        # グループが１つもない
                        break

                    f_start = False
                
                else:
                    # 次のグループを表示
                    i_group = self.get_group(i_group, COM__group_next)                       

                ###############################
                # 各グループを描画する処理
                ###############################
                # グループを描画
                if self.get_root_information(COM____mode) == MOD_EXECUTE and\
                    self.get_group(i_group, COM__move_control) == move_control_True:
                    # 実行で制御ボタンは描かない
                    pass
                else:    
                    # 常に描く
                    for i_component in range(self.len_component(i_group)):
                            # 固定データ
                            self.draw_component_from_data(screen, False, self.page_no, i_group, i_component)
                            # 一時データ
                            self.draw_component_from_data(screen, True, self.page_no, i_group, i_component)

                # グループ終了を判断
                if self.get_group(i_group, COM__group_next) == -1:
                    break

            if self.get_root_information(COM____mode) == MOD_DESIGN:
                # デザインのときは、枠を表示    
                if self.select_group_no_on_design >= 0:
                    # フレームだけ表示


                    #666
                    # RGB画面から去るときエラーになる
                    
                    self.draw_outline(screen, self.page_no, self.select_group_no_on_design, self.get_group(i_group, COM__frame_color))

            if self.get_root_information(COM____right_mouse) in (MOU_CLICK_FALSE, MOU_CLICK_RECTANGLE):
                # 新規の矩形を描く
                # 左上からマウスまで、矩形を描く 
                pygame.draw.rect(screen, COL_PINK, (self.get_group_right(COM__group_x),\
                    self.get_group_right(COM__group_y),\
                    self.get_group_right(COM__group_width),\
                    self.get_group_right(COM__group_height)),\
                    2)
                # 四角描画モード    
                # self.set_root_information(COM____right_mouse, MOU_CLICK_RECTANGLE)

            elif self.get_root_information(COM____right_mouse) != MOU_CLICK_FALSE:        
                # 右ボタントグルを見に行く

                # 右メニューを描く
                
                # 右メニューのためのｙオフセット
                menu_offset_y = self.get_right_menu_offset_y()

                s = self.get_component_right(0, COM_text)
                y = self.get_group_right(COM__group_y)
                # y_up = 0
                if s == "項目の追加":
                    self.set_right_menu_offset_y(0)
                    # if y < 700 - 190:    
                    #     self.set_right_menu_offset_y(0)
                    # else:
                    #     self.set_right_menu_offset_y(190)
                    menu_offset_y = self.get_right_menu_offset_y()
                    height = self.get_group_right(COM__group_height)

                    # メニューの幅を設定
                    width = self.get_group_right(COM__group_width)
                    # y_up = 0 #190
                elif s == "フレーム":
                    self.set_right_menu_offset_y(0)
                    # if y < 700 - 410:    
                    #     self.set_right_menu_offset_y(0)
                    # else:
                    #     self.set_right_menu_offset_y(410)
                    menu_offset_y = self.get_right_menu_offset_y()
                    height = self.get_group_right(COM__group_height)

                    # メニューの幅を設定
                    width = self.get_group_right(COM__group_width)
                    # y_up = 190 + 120
                elif s == "グループの追加":
                    self.set_right_menu_offset_y(0)
                    # if y < 700 - 110:    
                    #     self.set_right_menu_offset_y(0)
                    # else:
                    #     self.set_right_menu_offset_y(110)
                    menu_offset_y = self.get_right_menu_offset_y()
                    height = self.get_group_right(COM__group_height)

                    # メニューの幅を設定
                    width = self.get_group_right(COM__group_width)
                    # y_up = 0 #190
                else:
                    self.set_right_menu_offset_y(0)
                    height = 100
                    height = self.get_group_right(COM__group_height)
                    menu_offset_y = self.get_right_menu_offset_y()

                    # メニューの幅を設定
                    width = self.get_group_right(COM__group_width)
                    # width = 130
                    # y_up = 0
                        
                # 背景の描画
                # pygame.draw.rect(screen, COL_WHITE, (self.get_group_right(COM__group_x),\
                #     self.get_group_right(COM__group_y) - menu_offset_y,\
                #     width,
                #     height))
                # pygame.draw.rect(screen, COL_BLACK, (self.get_group_right(COM__group_x),\
                #     self.get_group_right(COM__group_y) - menu_offset_y,\
                #     width,
                #     height), 1)
                pygame.draw.rect(screen, COL_WHITE, (self.get_group_right(COM__group_x),\
                    self.get_group_right(COM__group_y),\
                    width,
                    height))
                pygame.draw.rect(screen, COL_BLACK, (self.get_group_right(COM__group_x),\
                    self.get_group_right(COM__group_y),\
                    width,
                    height), 1)

                #11111111
                # print("＠右メニューの座標：",self.get_group_right(COM__group_x),\
                #     self.get_group_right(COM__group_y),\
                #     self.get_group_right(COM__group_width),\
                #     self.get_group_right(COM__group_height))
                # exit(0)        

                
                # 右メニューの表示
                for i_component in range(self.len_component_right()):
                    # 固定データ
                    self.draw_component_from_data_right(screen, False, i_component)
                    # 一時データ
                    self.draw_component_from_data_right(screen, True, i_component)

    def draw_box(self, screen, group_no, i_component, colors, x, y, width_minus, height_minus, thickness=-1):
        ###########################
        # ボックスを塗りつぶす
        ###########################
        if thickness == -1:
            # 塗りつぶし
            pygame.draw.rect(screen, colors, (x + width_minus, y + height_minus,\
                self.get_component(group_no, i_component, COM_width) - width_minus * 2,\
                self.get_component(group_no, i_component, COM_height) - height_minus * 2))
        else:
            # 枠塗り
            pygame.draw.rect(screen, colors, (x + width_minus, y + height_minus,\
                self.get_component(group_no, i_component, COM_width) - width_minus * 2,\
                self.get_component(group_no, i_component, COM_height) - height_minus * 2), thickness)

    def draw_component_from_data(self, screen, temp, page_no, group_no, i_component):
        ###########################
        # コンポーネントをdataで描く
        ###########################
        # フォントクラス
        # print("draw_component_from_data group_no=", group_no, "i_component=", i_component, " Font_size=", self.get_group(group_no, COM__font_size))

        #99999
        # 特定ページのツリー表示
        # self.draw_tree_page(0)

        self.o_font = Fonts(self.get_group(group_no, COM__font_size), self.get_component(group_no, i_component, COM_font_type))

        group_type = self.get_group(group_no, COM__type)

        if group_type == TYP_FRAME:
            ###########################
            # フレームの描画
            ###########################

            # tempありなしでのｘｙ座標獲得
            x, y = self.get_xy(group_no, i_component, temp)
                
            # 塗りつぶす
            if temp == True:
                # フレーム色で塗る
                colors = COM__frame_color
                self.draw_box(screen, group_no, i_component, self.get_group(group_no, colors), x, y, 0, 0)
            else:
                # 影のフォント色で塗る
                colors = COM_font_light_color
                self.draw_box(screen, group_no, i_component, self.get_component(group_no, i_component, colors), x, y, 0, 0)
            
            # 外枠を黒で塗る
            self.draw_box(screen, group_no, i_component, COL_BLACK, x, y, 0, 0, 2)

        elif group_type == TYP_TEXT:
            ###########################
            # テキストの描画
            ###########################

            # tempありなしでのｘｙ座標獲得
            x, y = self.get_xy(group_no, i_component, temp)

            # テキストの中央位置を計算
            name = self.get_component(group_no, i_component, COM_text)

            # テキストを左寄せにした位置を獲得
            width_start, height_start = self.get_text_pos(name, group_no, i_component, POS_LEFT)
            
            # tempによりフォントをレンダー
            text = self.get_text_render(temp, name, group_no, i_component)

            # テキストを描画
            screen.blit(text, (x + width_start, y + height_start))

        elif group_type == TYP_BUTTON:
            ###########################
            # ボタンの描画
            ###########################

            # tempありなしでのｘｙ座標獲得
            x, y = self.get_xy(group_no, i_component, temp)

            # 白で塗る
            # if type(self.get_group(group_no, COM__back_color)) is str:
            if type(self.get_component(group_no, i_component, COM_back_color)) is str:
                # 画像が背景

                # ファイルの文字列

                # ページ背景ファイル名を指定
                # file_name = self.get_root_information(COM____data_path) + self.get_group(group_no, COM__back_color)
                file_name = self.get_root_information(COM____data_path) + self.get_component(group_no, i_component, COM_back_color)
                
                # イメージを作成
                image = pygame.transform.scale(pygame.image.load((file_name)).convert_alpha(), (1480, 700)) 

                # 半透明のサーフェスを作成
                image.set_alpha(255)

                # 仮に赤にしておく
                pygame.draw.rect(screen, COL_RED,\
                    (self.get_component(group_no, i_component, COM_x),\
                    self.get_component(group_no, i_component, COM_y),\
                    self.get_component(group_no, i_component, COM_width),\
                    self.get_component(group_no, i_component, COM_height)))

            else:
                # 色が背景    
                # self.draw_box(screen, group_no, i_component, self.get_group(group_no, COM__back_color), x, y, 0, 0)
                self.draw_box(screen, group_no, i_component, self.get_component(group_no, i_component, COM_back_color), x, y, 0, 0)
            
            # 外枠を青で塗る
            self.draw_box(screen, group_no, i_component, COL_BLUE, x, y, 0, 0, 2)
            
            if self.get_group(group_no, COM__push) == -1:
                # 選択されていないボタン
                self.draw_box(screen, group_no, i_component, COL_BLUE, x, y, 4, 4, 1)

            elif self.get_group(group_no, COM__push) == i_component:
                # 選択されているボタン
                self.draw_box(screen, group_no, i_component, COL_BLUE, x, y, 4, 4, 3)
            else:
                # 選択されていないボタン
                self.draw_box(screen, group_no, i_component, COL_BLUE, x, y, 4, 4, 1)

            name = self.get_component(group_no, i_component, COM_text)

            # textの開始位置を計算
            width_start, height_start = self.get_text_pos(name, group_no, i_component, POS_CENTER)            

            # tempによりフォントをレンダー
            text = self.get_text_render(temp, name, group_no, i_component)

            # テキストを描画
            screen.blit(text, (x + width_start, y + height_start))

        elif group_type == TYP_IMAGE:
            ###########################
            # 画像の描画
            ###########################

            name = self.get_component(group_no, i_component, COM_text)

            # 背景の画像を持ってくる
            file_name = self.get_root_information(COM____data_path) + name

            if self.file_exist(file_name) != True:
                file_name = self.get_root_information(COM____data_path) + "default.jpg"
            
            else:
                pass
                        
            image = pygame.transform.scale(pygame.image.load((file_name)).convert_alpha(),\
                (self.get_component(group_no, i_component, COM_width),\
                self.get_component(group_no, i_component, COM_height))) 

            # tempありなしでのｘｙ座標獲得
            x, y = self.get_xy(group_no, i_component, temp)

            # 半透明のサーフェスを作成
            # アルファ値を設定 (例: 128は半透明)
            # print("@@@ draw_component_from_data alpha=", group_no, i_component, COM_image_brightness)

            #99999999999999
            if self.get_component(group_no, i_component, COM_image_brightness) == None:
                self.set_component(group_no, i_component, COM_image_brightness, 255)
            if temp == True:
                image.set_alpha(self.get_component(group_no, i_component, COM_image_brightness))
            else:
                image.set_alpha(self.get_component(group_no, i_component, COM_image_brightness)//2)
            screen.blit(image, (x, y))

        elif group_type == TYP_MUSIC:
            ###########################
            # 音楽の描画
            ###########################

            # tempありなしでのｘｙ座標獲得
            x, y = self.get_xy(group_no, i_component, temp)

            # 白で塗りつぶす
            self.draw_box(screen, group_no, i_component, COL_WHITE, x, y, 0, 0)

            # 外枠を青で塗る
            self.draw_box(screen, group_no, i_component, COL_BLUE, x, y, 0, 0, 2)
            
            if self.get_group(group_no, COM__music_push) == -1:
                # 選択されていないボタン
                self.draw_box(screen, group_no, i_component, COL_BLUE, x, y, 4, 4, 1)

            elif self.get_group(group_no, COM__music_push) == i_component:
                # 選択されているボタン
                self.draw_box(screen, group_no, i_component, COL_BLUE, x, y, 4, 4, 3)

            else:
                # 選択されていないボタン
                self.draw_box(screen, group_no, i_component, COL_BLUE, x, y, 4, 4, 1)
            
            name = self.get_component(group_no, i_component, COM_text)

            file_name = self.get_root_information(COM____data_path) + name

            if self.file_exist(file_name) == True:
                pass    
                # name = name[0:len(name)-4]
            else:
                # 音楽が存在しない
                name = "default.mp3"

            name = name[0:len(name)-4]

            # textの開始位置を計算
            width_start, height_start = self.get_text_pos(name, group_no, i_component, POS_CENTER)            

            # tempによりフォントをレンダー
            text = self.get_text_render(temp, name, group_no, i_component)
            
            # テキストを描画
            screen.blit(text, (x + width_start, y + height_start))

        elif group_type == TYP_CHECKBOX:
            ###########################
            # チェックボックスの描画
            ###########################

            # tempありなしでのｘｙ座標獲得
            x, y = self.get_xy(group_no, i_component, temp)

            # テキストの中央位置を計算
            name = " "+self.get_component(group_no, i_component, COM_text)

            # textの開始位置を計算
            width_start, height_start = self.get_text_pos(name, group_no, i_component, POS_CHECKBOX)            

            # tempによりフォントをレンダー
            text = self.get_text_render(temp, name, group_no, i_component)

            # テキストを描画
            screen.blit(text, (x + width_start, y + height_start))

            # 四角の大きさを変える
            rect_size = int(self.get_group(group_no, COM__font_size) / 1.5)

            # チェックボタンの四角を描画
            if self.get_component(group_no, i_component, COM_checkbox_value) == 1:
                if temp == False:
                    pygame.draw.rect(screen, self.font_light_color, (self.get_component(group_no, i_component, COM_x) + width_start / 2,\
                        self.get_component(group_no, i_component, COM_y) +\
                        # self.get_component(group_no, i_component, COM_height) * 5 / 16, rect_size, rect_size))
                        self.get_component(group_no, i_component, COM_height) / 2 - rect_size / 2, rect_size, rect_size))
                else:
                    pygame.draw.rect(screen, self.font_color, (self.get_component(group_no, i_component, COM_temp_x) + width_start / 2,\
                        self.get_component(group_no, i_component, COM_temp_y) +\
                        # self.get_component(group_no, i_component, COM_height) * 5 / 16, rect_size, rect_size))
                        self.get_component(group_no, i_component, COM_height) / 2 - rect_size / 2, rect_size, rect_size))
            else:
                if temp == False:
                    pygame.draw.rect(screen, self.font_light_color, (self.get_component(group_no, i_component, COM_x) + width_start / 2,\
                        self.get_component(group_no, i_component, COM_y) +\
                        # self.get_component(group_no, i_component, COM_height) * 5 / 16, rect_size, rect_size), 2)
                        self.get_component(group_no, i_component, COM_height) / 2 - rect_size / 2, rect_size, rect_size), 2)
                else:
                    pygame.draw.rect(screen, self.font_color, (self.get_component(group_no, i_component, COM_temp_x) + width_start / 2,\
                        self.get_component(group_no, i_component, COM_temp_y) +\
                        # self.get_component(group_no, i_component, COM_height) * 5 / 16, rect_size, rect_size), 2)
                        self.get_component(group_no, i_component, COM_height) / 2 - rect_size / 2, rect_size, rect_size), 2)

        elif group_type == TYP_SLIDER:
            ###########################
            # スライダーの描画
            ###########################
            pygame.draw.rect(screen, COL_WHITE,\
                (self.get_component(group_no, i_component, COM_x),\
                self.get_component(group_no, i_component, COM_y),\
                self.get_component(group_no, i_component, COM_width),\
                self.get_component(group_no, i_component, COM_height)))

            # 計算してテキストを作成
            # min_data = self.get_component(group_no, i_component, COM_slider_min) - 0.5 
            # max_data = self.get_component(group_no, i_component, COM_slider_max) + 0.5 
            min_data = self.get_component(group_no, i_component, COM_slider_min)
            max_data = self.get_component(group_no, i_component, COM_slider_max) 
            # print("****** min_data-max_data:", min_data , max_data)
            band_data = max_data - min_data
            # value_data = str(int(self.get_component(group_no, i_component, COM_slider_value) * band_data + min_data + 0.5))
            value_data = str(int(self.get_component(group_no, i_component, COM_slider_value) * band_data + min_data))

            # print("****** min_data=", min_data, " max_data=", max_data, " RGB_data=", value_data, " band_data=", band_data)
            # テキストの位置を計算
            name = self.get_component(group_no, i_component, COM_text)

            # textの開始位置を計算
            width_start, height_start = self.get_text_pos(name, group_no, i_component, POS_SLIDER)            

            # tempによりフォントをレンダー
            text = self.get_text_render_green(temp, name, group_no)
            text_value = self.get_text_render_green(temp, value_data, group_no)

            x, y = self.get_xy(group_no, i_component, temp)

            if temp == True:
                # 一時位置を使用して描画
                # colors = self.get_group(group_no, COM__font_color)
                colors = self.get_component(group_no, i_component, COM_font_color)
            else:
                # 通常位置を使用して描画
                # colors = self.get_group(group_no, COM__font_light_color)
                colors = self.get_component(group_no, i_component, COM_font_light_color)

            #1111111
            # slider_length = int(self.get_component(group_no, i_component, COM_slider_value) *\
            #     self.get_component(group_no, i_component, COM_width))
            width_data = self.get_component(group_no, i_component, COM_width)
            value_data = self.get_component(group_no, i_component, COM_slider_value)
            slider_length = int(0.05 * width_data + self.get_component(group_no, i_component, COM_slider_value) *\
                (self.get_component(group_no, i_component, COM_width) * 0.9))

            #1111111
            # 最小、最大のときは、左端、右端に寄せる
            if value_data == 0:
                slider_length = 0
            elif value_data == 1:
                slider_length = width_data

            pygame.draw.rect(screen, COL_SLIDER_LIGHT_BLUE, (x, y, slider_length, self.get_component(group_no, i_component, COM_height)))

            #11111111
            # 小矩形を描画
            if value_data == 0:
                # 左端
                pygame.draw.rect(screen, COL_SLIDER_BLUE, (x, y, int(width_data * 0.1),\
                    self.get_component(group_no, i_component, COM_height)))
            elif value_data == 1:
                # 右端
                pygame.draw.rect(screen, COL_SLIDER_BLUE, (x + int(width_data * 0.9), y, int(width_data * 0.1),\
                    self.get_component(group_no, i_component, COM_height)))
            else:    
                # マウスのｘ位置の左右    
                pygame.draw.rect(screen, COL_SLIDER_BLUE, (x + slider_length - int(width_data * 0.05), y, int(width_data * 0.1),\
                             self.get_component(group_no, i_component, COM_height)))
            
            # 枠を描画
            pygame.draw.rect(screen, COL_RED, (x, y, self.get_component(group_no, i_component, COM_width),\
                self.get_component(group_no, i_component, COM_height)), 1)

            # テキスト値を描画
            screen.blit(text_value, (x + width_start, y + height_start))
            # テキストを描画
            screen.blit(text, (x + width_start * 0.02, y + height_start))

        elif group_type == TYP_TOGGLE:
            ###########################
            # トグルボタンの描画
            ###########################
            # tempありなしでのｘｙ座標獲得
            x, y = self.get_xy(group_no, i_component, temp)
                
            # 塗りつぶす
            if temp == True:
                # フレーム色で塗る
                colors = COM__frame_color
                self.draw_box(screen, group_no, i_component, self.get_group(group_no, colors), x, y, 0, 0)
            else:
                # 影のフォント色で塗る
                colors = COM_font_light_color
                self.draw_box(screen, group_no, i_component, self.get_component(group_no, i_component, colors), x, y, 0, 0)

            # テキストの中央位置を計算
            name = " "+self.get_component(group_no, i_component, COM_text)

            # textの開始位置を計算
            width_start, height_start = self.get_text_pos(name, group_no, i_component, POS_CHECKBOX)            

            # tempによりフォントをレンダー
            text = self.get_text_render(temp, name, group_no, i_component)

            # テキストを描画
            screen.blit(text, (x + width_start, y + height_start))
            circle_size = int(self.get_group(group_no, COM__font_size) / 2.5)
            # circle_color = self.get_group(group_no, COM__font_color)
            circle_color = self.get_component(group_no, i_component, COM_font_color)
            # circle_light_color = self.get_group(group_no, COM__font_light_color)
            circle_light_color = self.get_component(group_no, i_component, COM_font_light_color)
            if temp == False:
                # 固定位置を使用して描画
                # コンポーネントの円を描画
                if self.get_group(group_no, COM__toggle_value) == i_component:
                    pygame.draw.circle(screen, circle_light_color, (self.get_component(group_no, i_component, COM_x) + width_start,\
                        self.get_component(group_no, i_component, COM_y) +\
                        self.get_component(group_no, i_component, COM_height) / 2), circle_size, circle_size)
                else:
                    pygame.draw.circle(screen, circle_light_color, (self.get_component(group_no, i_component, COM_x) + width_start,\
                        self.get_component(group_no, i_component, COM_y) +\
                        self.get_component(group_no, i_component, COM_height) / 2), circle_size, 2)
            else:
                # 一時位置を使用して描画
                # コンポーネントの円を描画
                if self.get_group(group_no, COM__toggle_value) == i_component:
                    pygame.draw.circle(screen, circle_color, (self.get_component(group_no, i_component, COM_temp_x) + width_start,\
                        self.get_component(group_no, i_component, COM_temp_y) +\
                        self.get_component(group_no, i_component, COM_height) / 2), circle_size, circle_size)
                else:
                    pygame.draw.circle(screen, circle_color, (self.get_component(group_no, i_component, COM_temp_x) + width_start,\
                        self.get_component(group_no, i_component, COM_temp_y) +\
                        self.get_component(group_no, i_component, COM_height) / 2), circle_size, 2)

        else:
            print("Other type", type)

    def draw_component_from_data_right(self, screen, temp, i_component):
        ###########################
        # 右クリックを描く
        ###########################
        # フォントクラス
        self.o_font = Fonts(self.get_group_right(COM__font_size), self.get_group_right(COM__font_type))

        ###########################
        # トグルボタンの描画
        ###########################
        group_no = -1
        # tempありなしでのｘｙ座標獲得
        x, y = self.get_xy_right(group_no, i_component, temp)
                                            
        # テキストの中央位置を計算
        name = " "+self.get_component_right(i_component, COM_text)

        # textの開始位置を計算
        width_start, height_start = self.get_text_pos_right(name, i_component, POS_CHECKBOX)            

        # tempによりフォントをレンダー
        text = self.get_text_render_right(i_component, temp, name)

        # テキストを描画
        # 下で見えないときの対処
        menu_offset_y = self.get_right_menu_offset_y()


        # print(" +++ menu_offset_y=", menu_offset_y)


        screen.blit(text, (x + width_start, y + height_start-menu_offset_y))
        circle_size = int(self.get_group_right(COM__font_size) / 2.5)
        # circle_color = self.get_group_right(COM__font_color)
        circle_color = COL_RED
        # circle_light_color = self.get_group_right(COM__font_light_color)
        circle_light_color = COL_PINK
        if temp == False:
            # 固定位置を使用して描画
            # コンポーネントの円を描画
            if self.get_group_right(COM__toggle_value) == i_component:
                pygame.draw.circle(screen, circle_light_color, (self.get_component_right(i_component, COM_x) + width_start,\
                    self.get_component_right(i_component, COM_y) - menu_offset_y +\
                    self.get_component_right(i_component, COM_height) / 2), circle_size, circle_size)
            else:
                pygame.draw.circle(screen, circle_light_color, (self.get_component_right(i_component, COM_x) + width_start,\
                    self.get_component_right(i_component, COM_y) - menu_offset_y +\
                    self.get_component_right(i_component, COM_height) / 2), circle_size, 2)
        else:
            # 一時位置を使用して描画
            # コンポーネントの円を描画
            if self.get_group_right(COM__toggle_value) == i_component:
                pygame.draw.circle(screen, circle_color, (self.get_component_right(i_component, COM_temp_x) + width_start,\
                    self.get_component_right(i_component, COM_temp_y) - menu_offset_y +\
                    self.get_component_right(i_component, COM_height) / 2), circle_size, circle_size)
            else:
                pygame.draw.circle(screen, circle_color, (self.get_component_right(i_component, COM_temp_x) + width_start,\
                    self.get_component_right(i_component, COM_temp_y) - menu_offset_y +\
                    self.get_component_right(i_component, COM_height) / 2), circle_size, 2)

    def draw_outline(self, screen, page_no, group_no, colors):
        ###########################
        # 枠を描く
        ###########################
        # 設計時に選択されているグループ番号と等しい
        # ベース
        pygame.draw.rect(screen, colors, (self.get_group(group_no, COM__group_x),\
            self.get_group(group_no, COM__group_y),\
            self.get_group(group_no, COM__group_width),\
            self.get_group(group_no, COM__group_height)), 1)

        #222
        # 左上にグループ番号を表示
        text = self.o_font.font.render(str(group_no), True, colors)

        # テキストを描画
        screen.blit(text, (self.get_group(group_no, COM__group_x) - 12, self.get_group(group_no, COM__group_y) - 16))


        # 左棒
        #222
        # pygame.draw.rect(screen, colors, (self.get_group(group_no, COM__group_x) - 4,\
        #     self.get_group(group_no, COM__group_y) + 4,\
        #     8,\
        #     self.get_group(group_no, COM__group_height) - 8))
        # 右棒
        pygame.draw.rect(screen, colors, (self.get_group(group_no, COM__group_x) +\
                                        self.get_group(group_no, COM__group_width) - 4,\
            self.get_group(group_no, COM__group_y) + 4,\
            8,\
            self.get_group(group_no, COM__group_height) - 8))
        # 上棒
        #222
        # pygame.draw.rect(screen, colors, (self.get_group(group_no, COM__group_x) + 4,\
        #     self.get_group(group_no, COM__group_y) - 4,\
        #     self.get_group(group_no, COM__group_width) - 8,\
        #     8))
        # 下棒
        pygame.draw.rect(screen, colors, (self.get_group(group_no, COM__group_x) + 4,\
            self.get_group(group_no, COM__group_y) + self.get_group(group_no, COM__group_height) - 4,\
            self.get_group(group_no, COM__group_width) - 8,\
            8))

    def draw_window_title(self):
        ###############################    
        # ウィンドウのタイトル
        ###############################
        if self.get_root_information(COM____mode) == 0:
            s = "設計モード"
        else:
            s = "実行モード"        
        pygame.display.set_caption(self.get_root_information(COM____name) +\
            " Ver " + self.get_root_information(COM____version) +\
            " [" + s + "] " + str(self.page_no) + "ページ 最大" + str(self.max_page_no) + "ページ"+ " save" + str(self.page_no_save) + "ページ")

    def file_exist(self, name):
        ###########################
        # ファイル存在確認
        ###########################
        is_file = os.path.isfile(name)

        return is_file
    
    def file_list_up(self, wild_card):
        ################################
        # 画像ファイルリストアップ
        ################################
        files = glob.glob("./data/" + wild_card)
        return files

    def get_text_render(self, temp, name, group_no, i_component):
        ###########################
        # tempによりフォントをレンダー
        ###########################
        if temp == False:
            # text = self.o_font.font.render(name, True, self.get_group(group_no, COM__font_light_color))
            text = self.o_font.font.render(name, True, self.get_component(group_no, i_component, COM_font_light_color))
        else:
            text = self.o_font.font.render(name, True, self.get_component(group_no, i_component, COM_font_color))
            # text = self.o_font.font.render(name, True, self.get_component(group_no, i_component, COM_font_type))
        return text

    def get_text_render_right(self, i_command, temp, name):
        ###########################
        # tempによりフォントをレンダー
        ###########################
        if temp == False:
            # text = self.o_font.font.render(name, True, self.get_group_right(COM__font_light_color))
            text = self.o_font.font.render(name, True, COL_PINK)
        else:
            # text = self.o_font.font.render(name, True, self.get_group_right(COM__font_color))
            text = self.o_font.font.render(name, True, COL_RED)
        return text

    def get_text_render_green(self, temp, name, group_no):
        ###########################
        # tempにより緑フォントをレンダー
        ###########################
        text = self.o_font.font.render(name, True, COL_GREEN)
        return text

    def get_text_render_red(self, temp, name, group_no):
        ###########################
        # tempにより赤フォントをレンダー
        ###########################
        text = self.o_font.font.render(name, True, COL_RED)
        return text

    def get_text_pos(self, name, group_no, i_component, pos_type):            
        ###########################
        # textの開始位置を計算
        ###########################
        if pos_type == POS_LEFT:
            # 左寄せ    
            text_width, text_height = self.o_font.font.size(name)

            # テキストの幅を計算
            text_width = get_east_asian_width_count(name) * self.get_group(group_no, COM__font_size) // 2
            height_start = (self.get_component(group_no, i_component, COM_height) - text_height) // 2
            width_start = int(self.get_component(group_no, i_component, COM_width) // 100)

        elif pos_type == POS_CENTER:
            # 中央寄せ    
            text_width, text_height = self.o_font.font.size(name)

            # テキストの幅を計算
            text_width = get_east_asian_width_count(name) * self.get_group(group_no, COM__font_size) // 2
            height_start = (self.get_component(group_no, i_component, COM_height) - text_height) // 2
            width_start = (self.get_component(group_no, i_component, COM_width) - text_width) // 2

        elif pos_type == POS_CHECKBOX:
            # チェックボックス型の位置
            text_width, text_height = self.o_font.font.size(name)

            # テキストの幅を計算
            text_width = get_east_asian_width_count(name) * self.get_group(group_no, COM__font_size) // 2
            text_height = self.o_font.font_size()

            # 文字を描画
            height_start = (self.get_component(group_no, i_component, COM_height) - text_height) // 2
            width_start = int(self.o_font.font_size() * 0.7)

        elif pos_type == POS_SLIDER:
            # スライダー型の位置
            text_width, text_height = self.o_font.font.size(name)

            # テキストの幅を計算
            text_width = get_east_asian_width_count(name) * self.get_group(group_no, COM__font_size) // 2
            text_height = self.o_font.font_size()

            # 文字を描画
            height_start = (self.get_component(group_no, i_component, COM_height) - text_height) // 2
            width_start = int(self.get_component(group_no, i_component, COM_width) * 0.9)

        return width_start, height_start

    def get_text_pos_right(self, name, i_component, pos_type):            
        ###########################
        # textの開始位置を計算
        ###########################
        # チェックボックス型の位置
        text_width, text_height = self.o_font.font.size(name)

        # テキストの幅を計算
        text_width = get_east_asian_width_count(name) * self.get_group_right(COM__font_size) // 2
        text_height = self.o_font.font_size()

        # 文字を描画
        height_start = (self.get_component_right(i_component, COM_height) - text_height) // 2
        width_start = int(self.o_font.font_size() * 0.7)

        return width_start, height_start

    def get_xy(self, group_no, i_component, temp):
        ###############################    
        # ｘ／ｙを求める
        ###############################    
        if temp == True:
            # 一時位置を使用して描画
            x = self.get_component(group_no, i_component, COM_temp_x)
            y = self.get_component(group_no, i_component, COM_temp_y)

        else:
            # 通常位置を使用して描画
            x = self.get_component(group_no, i_component, COM_x)
            y = self.get_component(group_no, i_component, COM_y)

        return x, y

    def get_xy_right(self, group_no, i_component, temp):
        ###############################    
        # ｘ／ｙを求める（右クリック）
        ###############################    
        if temp == True:
            # 一時位置を使用して描画
            x = self.get_component_right(i_component, COM_temp_x)
            y = self.get_component_right(i_component, COM_temp_y)

        else:
            # 通常位置を使用して描画
            x = self.get_component_right(i_component, COM_x)
            y = self.get_component_right(i_component, COM_y)

        return x, y

    def set_page_no(self, new_page):
        ###########################
        # 新たなページ番号を設定
        ###########################
        # if new_page > self.max_page_no:
        #     # ページを作りながら先へ
        #     self.page_no = 0
        #     self.set_root_information(COM____cur_page_no, 0)
        # else:        
        self.page_no = new_page
        self.set_root_information(COM____cur_page_no, new_page)

        # キャプションに書き出す
        self.draw_window_title()

    def increase_page_no(self):
        ###########################
        # ページ番号を増やす
        ###########################
        if self.page_no == self.max_page_no:
            self.page_no = 0
            # 設計時に選択されているグループ番号
            self.select_group_no_on_design = 0
            self.select_component_no_on_design = 0
            self.set_root_information(COM____cur_page_no, 0)
        else:    
            self.page_no += 1
            # 設計時に選択されているグループ番号
            self.select_group_no_on_design = 0
            self.select_component_no_on_design = 0
            self.set_root_information(COM____cur_page_no, self.get_root_information(COM____cur_page_no)+1)

        # キャプションに書き出す
        self.draw_window_title()

    def next_page_no(self):
        ###########################
        # ページ番号を次に行かせる
        ###########################

        self.select_group_no_on_design = 0
        self.select_component_no_on_design = 0

        # 現在のページ番号を得る
        cur_page_no = self.page_no
        print("cur_page_no：", cur_page_no)

        # 先頭ページを設定
        i_page = self.get_root_information(COM____page_next_top)

        print("先頭ページ：", i_page)

        b_catch_cur_page_no = False
        while i_page != -1:
            # ページがある中、進む
            self.page_no = i_page
            i_page = self.get_page_information(COM___page_no)
            print("ルートから見た最初のページ：", i_page)
            print("b_catch_cur_page_no：", b_catch_cur_page_no)

            # 現在のページを見つけたか
            if b_catch_cur_page_no == True:
                # ここが発見したページ
                self.page_no = i_page

                # 次が本命
                i_page = self.get_page_information(COM___page_next)
                print("本命ページ：", i_page)

                if i_page == cur_page_no:
                    # i_page目が現在のページ番号
                    # 次が本命
                    self.page_no = i_page
                    # ルートの現在ページ番号に設定
                    self.set_root_information(COM____cur_page_no, i_page)
                    break

                else:
                    # i_page目が現在のページ番号でない
                    # 次が本命
                    self.page_no = i_page
                    # ルートの現在ページ番号に設定
                    self.set_root_information(COM____cur_page_no, i_page)
                    break

            else:
                # まだ現在のページに行きついていない
                # 次が本命ではない
                # i_page = self.get_page_information(COM___page_next)
                
                print("次のページ１", i_page)
                   
                if i_page == cur_page_no:
                    # i_page目が現在のページ番号
                    b_catch_cur_page_no = True
                    # 次が本命
                    print("次が本命ページ１：", i_page)
                    i_page = self.get_page_information(COM___page_next)
                    print("次が本命ページ２：", i_page)
                    # 本命

                    if i_page == -1:
                        # その先がなかった
                        self.page_no = 0
                        # ルートの現在ページ番号に設定
                        self.set_root_information(COM____cur_page_no, i_page)
                        print("本命ページ番号", i_page)
                        
                    else:
                        # その先があった    
                        # i_page = self.get_root_information(COM____page_next_top)
                        self.page_no = i_page
                        # ルートの現在ページ番号に設定
                        self.set_root_information(COM____cur_page_no, i_page)
                        print("本命ページ番号", i_page)
                    break

                elif i_page == -1:
                    # 発見できず
                    print("発見できず", i_page)
                    # 先頭ページにしておく
                    i_page = self.get_root_information(COM____page_next_top)
                    self.page_no = i_page
                    # ルートの現在ページ番号に設定
                    self.set_root_information(COM____cur_page_no, i_page)
                    print("ルートの現在ページ番号に設定しておく", i_page)
                    break
            
                else:
                    # 開始ぺージでもなく、発見するために回るところ    
                    print("開始ぺージでもなく、発見するために回るところ", i_page)
            
                    print("次を見る１：", i_page)
                    i_page = self.get_page_information(COM___page_next)
                    print("次を見る２：", i_page)

            # else:
            #     # 現在のページでなく、未発見でもない
            #     if b_catch_cur_page_no == True:
            #         # ここが発見したページ
            #         self.page_no = i_page
            #         # ルートの現在ページ番号に設定
            #         self.set_root_information(COM____cur_page_no, i_page)
            #         break
                    
            #     else:
            #         # まだ現在のページをみつけていない
            #         pass
                                    
        print("決定ページ：", self.page_no)

        # キャプションに書き出す
        self.draw_window_title()

    def previous_page_no(self):
        ###########################
        # ページ番号を前に行かせる
        ###########################

        self.select_group_no_on_design = 0
        self.select_component_no_on_design = 0

        # 現在のページ番号を得る
        cur_page_no = self.page_no
        print("cur_page_no：", cur_page_no)

        # 先頭ページを設定
        i_page = self.get_root_information(COM____page_previous_top)

        print("先頭ページ：", i_page)

        b_catch_cur_page_no = False
        while i_page != -1:
            # ページがある中、進む
            self.page_no = i_page
            i_page = self.get_page_information(COM___page_no)
            print("ルートから見た最初のページ：", i_page)
            print("b_catch_cur_page_no：", b_catch_cur_page_no)

            # 現在のページを見つけたか
            if b_catch_cur_page_no == True:
                # ここが発見したページ
                self.page_no = i_page

                # 前が本命
                i_page = self.get_page_information(COM___page_previous)
                print("本命ページ：", i_page)

                if i_page == cur_page_no:
                    # i_page目が現在のページ番号
                    # 次が本命
                    self.page_no = i_page
                    # ルートの現在ページ番号に設定
                    self.set_root_information(COM____cur_page_no, i_page)
                    break

                else:
                    # i_page目が現在のページ番号でない
                    # 次が本命
                    self.page_no = i_page
                    # ルートの現在ページ番号に設定
                    self.set_root_information(COM____cur_page_no, i_page)
                    break

            else:
                # まだ現在のページに行きついていない
                # 次が本命ではない
                # i_page = self.get_page_information(COM___page_next)
                
                print("次のページ１", i_page)
                   
                if i_page == cur_page_no:
                    # i_page目が現在のページ番号
                    b_catch_cur_page_no = True
                    # 次が本命
                    print("次が本命ページ１：", i_page)
                    i_page = self.get_page_information(COM___page_previous)
                    print("次が本命ページ２：", i_page)
                    # 本命

                    if i_page == -1:
                        # その先がなかった
                        self.page_no = self.get_root_information(COM____page_previous_top)

                        # ルートの現在ページ番号に設定
                        self.set_root_information(COM____cur_page_no, i_page)
                        print("本命ページ番号", i_page)
                        
                    else:
                        # その先があった    
                        # i_page = self.get_root_information(COM____page_next_top)
                        self.page_no = i_page
                        # ルートの現在ページ番号に設定
                        self.set_root_information(COM____cur_page_no, i_page)
                        print("本命ページ番号", i_page)
                    break

                elif i_page == -1:
                    # 発見できず
                    print("発見できず", i_page)
                    # 先頭ページにしておく
                    i_page = self.get_root_information(COM____page_previous_top)
                    self.page_no = i_page
                    # ルートの現在ページ番号に設定
                    self.set_root_information(COM____cur_page_no, i_page)
                    print("ルートの現在ページ番号に設定しておく", i_page)
                    break
            
                else:
                    # 開始ぺージでもなく、発見するために回るところ    
                    print("開始ぺージでもなく、発見するために回るところ", i_page)
            
                    print("次を見る１：", i_page)
                    i_page = self.get_page_information(COM___page_previous)
                    print("次を見る２：", i_page)

        print("決定ページ：", self.page_no)

        # キャプションに書き出す
        self.draw_window_title()

    def show(self, p_no, g_no):
        # ページ番号を表示
        if p_no == -1:
            print("<<< Program name =", self.o_design.p[0][COM____name], " Project Information >>>",\
                  " Version=", self.o_design.p[0][COM____version],\
                  " Mode=", self.o_design.p[0][COM____mode],\
                  " right mouse =", self.o_design.p[0][COM____right_mouse],\
                  " page entry no =", len(self.o_design.p)-2,\
                  " data path =", self.o_design.p[0][COM____data_path],\
                  " margin =", self.o_design.p[0][COM____margin],\
                  " grid =", self.o_design.p[0][COM____grid],\
                  " page no (save) =", self.o_design.p[0][COM____page_no_save], file = self.f_page_list)

        else:        
            # ページ番号を表示
            page_no = p_no + 2
            # self.page_no = page_no
            if g_no == 0:
                # print("<< Page_no =", page_no-1, ", Group Information >>", file = self.f_page_list)
                print("<< Page_no =", page_no-2, ", Group Information >>", file = self.f_page_list)
                print("  Page_no=", self.o_design.p[page_no][g_no][COM___page_no],\
                    " active_frame=", self.o_design.p[page_no][g_no][COM___active_frame],\
                    " back_color=", self.o_design.p[page_no][g_no][COM___back_color],\
                    " group entry max =", len(self.o_design.p[page_no])-1,\
                    " group < next =", self.o_design.p[page_no][g_no][COM___group_next_top],\
                    " , prev =", self.o_design.p[page_no][g_no][COM___group_previous_top],\
                    " , group entry_no =", self.o_design.p[page_no][g_no][COM___group_entry_no], " >", file = self.f_page_list)

            else:    
                group_no = g_no - 1
                print("<< Page_no = ", page_no-2, ", Group No=", group_no, ">>", file = self.f_page_list)

                type = self.o_design.p[page_no][g_no][0][COM__type]

                print("  List Current=", self.o_design.p[page_no][g_no][0][COM__current_group],\
                    " Next=", self.o_design.p[page_no][g_no][0][COM__group_next], \
                    " Previous=", self.o_design.p[page_no][g_no][0][COM__group_previous], file = self.f_page_list)

                # タイプの表示
                if self.o_design.p[page_no][g_no][0][COM__type]==TYP_FRAME:
                    s_type = "FRAME"
                elif self.o_design.p[page_no][g_no][0][COM__type]==TYP_BUTTON:
                    s_type = "BUTTON"
                elif self.o_design.p[page_no][g_no][0][COM__type]==TYP_IMAGE:
                    s_type = "IMAGE"
                elif self.o_design.p[page_no][g_no][0][COM__type]==TYP_SLIDER:
                    s_type = "SLIDER"
                elif self.o_design.p[page_no][g_no][0][COM__type]==TYP_TOGGLE:
                    s_type = "TOGGLE"
                elif self.o_design.p[page_no][g_no][0][COM__type]==TYP_CHECKBOX:
                    s_type = "CHECKBOX"
                elif self.o_design.p[page_no][g_no][0][COM__type]==TYP_MUSIC:
                    s_type = "MUSIC"
                elif self.o_design.p[page_no][g_no][0][COM__type]==TYP_TEXT:
                    s_type = "TEXT"
                else:
                    s_type = "type_unknown"
                # 方向の表示
                if self.o_design.p[page_no][g_no][0][COM__dir] == DIR_COLUMN:
                    s_dir = "COLUMN"
                elif self.o_design.p[page_no][g_no][0][COM__dir] == DIR_ROW:
                    s_dir = "ROW"
                else:
                    s_dir = "dir_unknown"
                s_print = "  type=" + s_type + " dir=" + s_dir + \
                    " group_x="+ str(self.o_design.p[page_no][g_no][0][COM__group_x])+\
                    " group_y="+ str(self.o_design.p[page_no][g_no][0][COM__group_y])+\
                    " group_width="+ str(self.o_design.p[page_no][g_no][0][COM__group_width])+\
                    " group_height="+ str(self.o_design.p[page_no][g_no][0][COM__group_height])+\
                    " font_size="+ str(self.o_design.p[page_no][g_no][0][COM__font_size])+\
                    " draw_frame="+ str(self.o_design.p[page_no][g_no][0][COM__draw_frame])+\
                    " move_exclusive="+ str(self.o_design.p[page_no][g_no][0][COM__move_exclusive])+\
                    " move_inhibit="+ str(self.o_design.p[page_no][g_no][0][COM__move_inhibit])+\
                    " move_control="+ str(self.o_design.p[page_no][g_no][0][COM__move_control])+\
                    " push="+ str(self.o_design.p[page_no][g_no][0][COM__push])
                if type == TYP_MUSIC:
                    s_print_2 =\
                        " music_push="+ str(self.o_design.p[page_no][g_no][0][COM__music_push])+\
                        " music_value="+ str(self.o_design.p[page_no][g_no][0][COM__music_value])
                elif type == TYP_TOGGLE:
                    s_print_2 = " toggle_value="+ str(self.o_design.p[page_no][g_no][0][COM__toggle_value])
                else:
                    s_print_2 = " "

                print(s_print+s_print_2)

                for i in range(len(self.o_design.p[page_no][g_no])-1):
                    s_print = "   P.G.C=("+str(self.o_design.p[page_no][g_no][i+1][0])+"."
                    s_print += str(self.o_design.p[page_no][g_no][i+1][1])+"."
                    s_print += str(self.o_design.p[page_no][g_no][i+1][2])+")"
                    s_print += " type_text= "+str(self.o_design.p[page_no][g_no][i+1][3])
                    s_print += " text=["+self.o_design.p[page_no][g_no][i+1][4][COM_text]+"]"
                    s_print += " x="+str(self.o_design.p[page_no][g_no][i+1][4][COM_x])
                    s_print += " y="+str(self.o_design.p[page_no][g_no][i+1][4][COM_y])
                    s_print += " width="+str(self.o_design.p[page_no][g_no][i+1][4][COM_width])
                    s_print += " height="+str(self.o_design.p[page_no][g_no][i+1][4][COM_height])
                    s_print_3 = " temp_x="+str(self.o_design.p[page_no][g_no][i+1][4][COM_temp_x])
                    s_print_3 += " temp_y="+str(self.o_design.p[page_no][g_no][i+1][4][COM_temp_y])
                    s_print_3 += " click_offset_x="+str(self.o_design.p[page_no][g_no][i+1][4][COM_click_offset_x])
                    s_print_3 += " click_offset_y="+str(self.o_design.p[page_no][g_no][i+1][4][COM_click_offset_y])
                    s_print_3 += " font_color="+str(self.o_design.p[page_no][g_no][i+1][4][COM_font_color])
                    s_print_3 += " font_light_color="+str(self.o_design.p[page_no][g_no][i+1][4][COM_font_light_color])
                    s_print_3 += " back_color="+str(self.o_design.p[page_no][g_no][i+1][4][COM_back_color])
                    s_print_3 += " font_type="+str(self.o_design.p[page_no][g_no][i+1][4][COM_font_type])

                    if self.o_design.p[page_no][g_no][0][COM__type]==TYP_SLIDER:
                        s_print_2 = " slider_value="+str(str(self.o_design.p[page_no][g_no][i+1][4][COM_slider_value]))+\
                            " slider_min="+str(self.o_design.p[page_no][g_no][i+1][4][COM_slider_min])+\
                            " slider_max="+str(self.o_design.p[page_no][g_no][i+1][4][COM_slider_max])
                    elif self.o_design.p[page_no][g_no][0][COM__type]==TYP_CHECKBOX:
                        s_print_2 = " checkbox_value="+str(self.o_design.p[page_no][g_no][i+1][4][COM_checkbox_value])
                    elif self.o_design.p[page_no][g_no][0][COM__type]==TYP_IMAGE:
                        s_print_2 = " image_brightness="+str(self.o_design.p[page_no][g_no][i+1][4][COM_image_brightness])
                    elif self.o_design.p[page_no][g_no][0][COM__type]==TYP_BUTTON:
                        s_print_2 = " URL=["+str(self.o_design.p[page_no][g_no][i+1][4][COM_value])+"]"
                    else:
                        s_print_2 = " value="+str(self.o_design.p[page_no][g_no][i+1][4][COM_value])

                    print(s_print+s_print_3+s_print_2)

    def show_all(self):
        s_print += ページ番号を総表示
        with open("a_page_list.txt", "w") as self.f_page_list:
            # プロジェクト情報表示
            self.show(-1, 0)
            # 各ページ表示
            for page_no in range(self.len_page()):
                for g_no in range(self.len_group()):
                    self.show(page_no, g_no)

    def shows(self, page_no):
        # ページ番号を総表示
        for g_no in range(len(self.o_group)):
            self.show(page_no, g_no)

    def load_CSV(self, name):
        #################################
        # CSVファイルのリストの読込
        #################################
        file_name = self.o_design.data_path + name + ".csv"

        is_file = os.path.isfile(file_name)

        if is_file:
            # CSVファイルが存在する
            with open(file_name, encoding="shift-jis") as f:
                reader = csv.reader(f)
                l = [row for row in reader]
                return l
        
        else:
            # CSVファイルが存在しない
            print("CSVファイルが存在しない。")
            return []

    def load_design(self, name):
        #################################
        # デザイン辞書の読込
        #################################
        file_name = self.o_design.data_path + name + ".pkl"

        is_file = os.path.isfile(file_name)
        if is_file:
            # デザイン辞書が存在する
            # リストをそのまま保存
            with open(file_name, "rb") as f:
                # デザイン辞書を読み込む
                target = pickle.load(f)

                return target

        else:
            # デザイン辞書が存在しない
            print("デザイン辞書が存在しない。")
            return []

    def save_design(self, name):
        ###############################    
        # デザイン辞書の書き出し
        ###############################    
        file_name = self.o_design.data_path + name + ".pkl"

        self.set_root_information(COM____cur_page_no, self.page_no)

        # リストをそのまま保存
        with open(file_name, "wb") as f:
            # デザイン辞書を保存する
            pickle.dump(self.o_design.p, f)

    def super_group(self, p_no, g_no):
        ###############################    
        # グループ情報
        ###############################    
        # print(self.o_design.p[0+2][2+1])
        # self.show(0, 3)
        print(self.o_design.p[p_no+2][g_no+1])
        self.show(p_no, g_no+1)

    def write_html_by_CSV(self, CSV_list):
        #################################
        # htmlファイルのCSV_listでの書出し
        #################################
        
        # まずStep_sizeを計算
        self.calc_step_size()
        # CSVリストの内訳
        # self.CSV_list_selection = 0
        # self.CSV_list_result_by_CSV = 0
        # self.CSV_list_result = 0
        print(self.selection_step_size)
        print(self.CSV_list_selection, self.CSV_list_result_by_CSV, self.CSV_list_result)

        selection_no = -1
        for line in range(len(CSV_list)):
            print(CSV_list[line][0])
            # Selection
            if CSV_list[line][0] == "Selection":
                # 選択
                selection_no += 1
                if selection_no == 0:
                    # トップページ
                    self.write_html("index")
                else:
                # elif selection_no == 1:
                    # ｎ番目のページ
                    self.write_html("p0"+str(selection_no))
            elif CSV_list[line][0] == "Result_URL":
                # Result_URLのページ
                self.write_html("last")
            elif CSV_list[line][0] in ("Result", "Result_3_image"):
                # Resultのページ
                self.write_html("last_3")
                           
    def write_html(self, name):
        #################################
        # htmlファイルの書き出し
        #################################
        if name in ("last_2", "last_3"):
            file_name = self.o_design.data_path + "last" + ".html"
        else:
            file_name = self.o_design.data_path + name + ".html"

        # is_file = os.path.isfile(file_name)

        print("Write_html ファイル名：", file_name)

        with open(file_name, "w", encoding="utf-8") as f:
            # html:開始
            # グループ情報
            self.html_start(f)
            if name == "index":
                self.page_no = 0
                # html:値１の保存
                self.html_save_value(f, 1)
                # html:選択肢：問１
                self.html_select_branch(f, 1)
            elif name == "last":
                self.page_no = self.CSV_list_selection + 1
                f.write('  <script>\n')
                # html:値の計算
                self.html_calc_value(f)
                # html:値による分岐
                self.html_jump_to_result(f)
                f.write('  </script>\n')
                # html:最初に戻る
                self.html_back_to_start(f)
            elif name == "last_2":
                self.page_no = self.CSV_list_selection + 1
                f.write('  <script>\n')
                # html:値の計算
                self.html_calc_value_2(f)
                # html:値による分岐(写真の印刷)
                self.html_display_photo(f)
                f.write('  </script>\n')
                # html:最初に戻る
                self.html_back_to_start_photo(f)
            elif name == "last_3":
                self.page_no = self.CSV_list_selection + 1
                f.write('  <script>\n')
                # html:値の計算
                self.html_calc_value_3(f)
                f.write('  </script>\n')
                # html:最初に戻る
                self.html_back_to_start_photo_3(f)
            else:
                # p0xの処理    
                p0x_no = int(name[2])
                self.page_no = p0x_no
                # html:値ｎの保存
                self.html_save_value(f, p0x_no + 1)
                # html:選択肢：問ｎ
                self.html_select_branch(f, p0x_no + 1)
    
    def html_start(self, f_file):
        ###############################    
        # html:開始
        ###############################    

        # プログラム名＋バージョン
        s_title = self.get_root_information(COM____name)+" "+self.get_root_information(COM____version)
        # 背景
        s_back_image = self.get_page_information(COM___back_color)
        length = len(s_back_image)
        if s_back_image[length-1:length] != 'g':
            s_back_image = 'game_back_forest.jpg'
            
        f_file.write('<!DOCTYPE html>\n')
        f_file.write('<html lang="ja">\n')
        f_file.write('<head>\n')
        f_file.write('  <meta charset="UTF-8">\n')
        f_file.write('  <title>' + s_title + '</title>\n')
        f_file.write('  <style>\n')
        f_file.write('    /* ページ全体を画面いっぱいにする設定 */\n')
        f_file.write('    html, body {\n')
        f_file.write('      height: 100%;\n')
        f_file.write('      margin: 0;\n')
        f_file.write('      padding: 0;\n')
        f_file.write('    }\n')
        f_file.write('    /* 背景画像設定（画面いっぱいに表示） */\n')
        f_file.write('    body {\n')
        f_file.write('      background-image: url("' + s_back_image + '");\n')
        f_file.write('      background-size: cover;          /* 画面いっぱいに拡大 */\n')
        f_file.write('      background-repeat: no-repeat;    /* 繰り返さない */\n')
        f_file.write('      background-position: center;     /* 中央に配置 */\n')
        f_file.write('      display: flex;                   /* 中央配置のためのflex設定 */\n')
        f_file.write('      justify-content: center;         /* 横方向中央 */\n')
        f_file.write('      align-items: center;             /* 縦方向中央 */\n')
        f_file.write('      flex-direction: column;          /* 縦に並べる（タイトル→ボタン） */\n')
        f_file.write('      color: white;                    /* 文字を白にする */\n')
        f_file.write('    }\n')
        f_file.write('    /* タイトルのスタイル */\n')
        f_file.write('    h1 {\n')
        f_file.write('      color: white;\n')
        f_file.write('      text-shadow: 2px 2px 4px rgba(0,0,0,0.7);\n')
        f_file.write('      margin-bottom: 40px;\n')
        f_file.write('      font-size: 32px;\n')
        f_file.write('    }\n')
        f_file.write('    /* ボタン配置用コンテナ */\n')
        f_file.write('    .button-container {\n')
        f_file.write('      display: flex;\n')
        f_file.write('      gap: 40px; /* ボタン間の間隔 */\n')
        f_file.write('    }\n')
        f_file.write('    #result\n')
        f_file.write('      {\n')
        f_file.write('      font-size: 32px;\n')
        f_file.write('      margin-bottom: 20px;\n')
        f_file.write('      }\n')
        f_file.write('    /* ボタンの基本スタイル */\n')
        f_file.write('    button {\n')
        f_file.write('      padding: 15px 40px;\n')
        f_file.write('      font-size: 32px;\n')
        f_file.write('      background-color: #007bff;\n')
        f_file.write('      color: white;\n')
        f_file.write('      border: none;\n')
        f_file.write('      border-radius: 12px;\n')
        f_file.write('      cursor: pointer;\n')
        f_file.write('      transition: background-color 0.3s, transform 0.2s;\n')
        f_file.write('      box-shadow: 0 4px 8px rgba(0,0,0,0.3);\n')
        f_file.write('    }\n')
        f_file.write('    button:hover {\n')
        f_file.write('      background-color: #005600;\n')
        f_file.write('      transform: scale(1.05);\n')
        f_file.write('    }\n')
        f_file.write('    .bottom-right {\n')
        f_file.write('      position: fixed;\n')
        f_file.write('      right: 20px;\n')
        f_file.write('      bottom: 20px;\n')
        f_file.write('    }\n')
        f_file.write('    #artistImage {\n')
        f_file.write('      margin-top: 40px;\n')
        f_file.write('      display: none;\n')
        f_file.write('      max-width: 80%;\n')
        f_file.write('      border-radius: 16px;\n')
        f_file.write('      box-shadow: 0 4px 12px rgba(0,0,0,0.5);\n')
        f_file.write('    }\n')
        f_file.write('    .container {\n')
        f_file.write('      display: flex;\n')
        f_file.write('      align-items: center;\n')
        f_file.write('      gap: 20px;\n')
        f_file.write('    }\n')
        f_file.write('    .left-img img{\n')
        f_file.write('      width 300px;\n')
        f_file.write('    }\n')
        f_file.write('    .right-imgs {\n')
        f_file.write('      display: flex;\n')
        f_file.write('      flex-direction: column;\n')
        f_file.write('      gap: 10px;\n')
        f_file.write('    }\n')
        f_file.write('    .right-imgs img{\n')
        f_file.write('      width: 150px;\n')
        f_file.write('    }\n')
        f_file.write('  </style>\n')
        
    def html_save_value(self, f_file, value_no):
        ###############################    
        # html:値ｎの保存
        ###############################    
        f_file.write('  <script>\n')
        f_file.write('    function saveValue(value) {\n')
        f_file.write('      // 値をlocalStorage_' + str(value_no) + 'に保存\n')
        f_file.write('      localStorage.setItem("selectedValue_' + str(value_no) + '", value);\n')
        f_file.write('      // 次のページへ移動するURL\n')
        if value_no == self.CSV_list_selection:
            f_file.write('      location.href = "last.html";\n')
        else:
            f_file.write('      location.href = "p0' + str(value_no) + '.html";\n')

        f_file.write('    }\n')
        f_file.write('  </script>\n')

    def html_calc_value(self, f_file):
        ###############################    
        # html:値の計算
        ###############################    
        f_file.write('    window.onload = function() {\n')
        for i in range(self.CSV_list_selection):
            f_file.write('      const value_' + str(i+1) + ' = localStorage.getItem("selectedValue_' + str(i+1) + '");\n')

        s = '      const value = parseInt(value_1) + parseInt(value_2)'             
        # for i in range(self.CSV_list_selection):
        if self.CSV_list_selection == 2:
            f_file.write(s + ';\n')
        else:
            for i in range(self.CSV_list_selection - 2):
                s += ' + parseInt(value_' + str(i + 3) + ')'
            f_file.write(s + ';\n')

        # CSVリストの内訳
        print("self.CSV_list_selection", self.CSV_list_selection) #2
        print("self.CSV_list_result_by_CSV", self.CSV_list_result_by_CSV) #4
        print("self.CSV_list_result", self.CSV_list_result) #0

        #99999999
        f_file.write('      const result = document.getElementById("result");\n')
        f_file.write('      const button = document.getElementById("myButton");\n')
        f_file.write('      const image = document.getElementById("artistImage");\n')

        # ここで、URL付でもなしでも要素を追記
        for result_page in range(self.CSV_list_result_by_CSV):
            if result_page == 0:
                f_file.write('      if (value == 0) {\n')
            else:
                f_file.write('      } else if (value == ' + str(result_page) + ') {\n')
            s_player = self.CSV_list[self.CSV_list_selection + result_page][2]
            f_file.write('        document.getElementById("result").textContent = "' + s_player + '";\n')

        for result_page in range(self.CSV_list_result):
            if result_page == 0:
                f_file.write('      if (value == 0) {\n')
            else:
                f_file.write('      } else if (value == ' + str(result_page) + ') {\n')
            s_player = self.CSV_list[self.CSV_list_selection + result_page][2]
            f_file.write('        document.getElementById("result").textContent = "' + s_player + '";\n')

        f_file.write('      }\n')

    def html_calc_value_2(self, f_file):
        ###############################    
        # html:値の計算(result時)
        ###############################    
        f_file.write('    window.onload = function() {\n')
        for i in range(self.CSV_list_selection):
            f_file.write('      const value_' + str(i+1) + ' = localStorage.getItem("selectedValue_' + str(i+1) + '");\n')

        s = '      const value = parseInt(value_1) + parseInt(value_2)'             
        # for i in range(self.CSV_list_selection):
        if self.CSV_list_selection == 2:
            f_file.write(s + ';\n')
        else:
            for i in range(self.CSV_list_selection - 2):
                s += ' + parseInt(value_' + str(i + 3) + ')'
            f_file.write(s + ';\n')

        # CSVリストの内訳
        print("self.CSV_list_selection", self.CSV_list_selection) #2
        print("self.CSV_list_result_by_CSV", self.CSV_list_result_by_CSV) #4
        print("self.CSV_list_result", self.CSV_list_result) #0

        #99999999
        f_file.write('      const result = document.getElementById("result");\n')
        f_file.write('      const button = document.getElementById("myButton");\n')
        f_file.write('      const image = document.getElementById("artistImage");\n')

        # ここで、URL付でもなしでも要素を追記
        for result_page in range(self.CSV_list_result_by_CSV):
            if result_page == 0:
                f_file.write('      if (value == 0) {\n')
            else:
                f_file.write('      } else if (value == ' + str(result_page) + ') {\n')
            s_player = self.CSV_list[self.CSV_list_selection + result_page][2]
            f_file.write('        document.getElementById("result").textContent = "' + s_player + '";\n')

        for result_page in range(self.CSV_list_result):
            if result_page == 0:
                f_file.write('      if (value == 0) {\n')
            else:
                f_file.write('      } else if (value == ' + str(result_page) + ') {\n')
            s_player = self.CSV_list[self.CSV_list_selection + result_page][2]
            f_file.write('        result.textContent = "' + s_player + '";\n')
            s_image_file = self.CSV_list[self.CSV_list_selection + result_page][3]
            f_file.write('        image.src = "' + s_image_file + '";\n')
            f_file.write('        image.style.display = "block";\n')

    def html_calc_value_3(self, f_file):
        ###############################    
        # html:値の計算(result_3_image時)
        ###############################
        f_file.write('    window.onload = function() {\n')
        for i in range(self.CSV_list_selection):
            f_file.write('      const value_' + str(i+1) + ' = localStorage.getItem("selectedValue_' + str(i+1) + '");\n')

        s = '      const value = parseInt(value_1) + parseInt(value_2)'             
        # for i in range(self.CSV_list_selection):
        if self.CSV_list_selection == 2:
            f_file.write(s + ';\n')
        else:
            for i in range(self.CSV_list_selection - 2):
                s += ' + parseInt(value_' + str(i + 3) + ')'
            f_file.write(s + ';\n')

        # CSVリストの内訳
        print("self.CSV_list_selection", self.CSV_list_selection) #2
        print("self.CSV_list_result_by_CSV", self.CSV_list_result_by_CSV) #4
        print("self.CSV_list_result", self.CSV_list_result) #0

        #99999999
        f_file.write('      const result = document.getElementById("result");\n')
        f_file.write('      const button = document.getElementById("myButton");\n')
        f_file.write('      const image = document.getElementById("artistImage");\n')
        f_file.write('      const image_1 = document.getElementById("rightImage1");\n')
        f_file.write('      const image_2 = document.getElementById("rightImage2");\n')

        # ここで、URL付でもなしでも要素を追記
        for result_page in range(self.CSV_list_result_by_CSV):
            if result_page == 0:
                f_file.write('      if (value == 0) {\n')
            else:
                f_file.write('      } else if (value == ' + str(result_page) + ') {\n')
            f_file.write('        result.textContent = "' + self.CSV_list[self.CSV_list_selection + result_page][2] + '";\n')
            f_file.write('        image.src = "' + self.CSV_list[self.CSV_list_selection + result_page][3] + '";\n')
            # 乱数で決める
            no_use_image = random.randint(4,6)
            image_use = []
            for i_image in range(4, 7):
                if i_image == no_use_image:
                    pass
                else:
                    # 未使用でない
                    image_use.append(i_image)
                    
            f_file.write('        image_1.src = "' + self.CSV_list[self.CSV_list_selection + result_page][image_use[0]] + '";\n')
            f_file.write('        image_2.src = "' + self.CSV_list[self.CSV_list_selection + result_page][image_use[1]] + '";\n')
            f_file.write('        image.style.display = "block";\n')
        f_file.write('      }\n')
        f_file.write('     };\n')

    def html_jump_to_result(self, f_file):
        ###############################    
        # html:値による分岐
        ###############################    
        for result_page in range(self.CSV_list_result_by_CSV):
            if result_page == 0:
                f_file.write('      if (value == 0) {\n')
            else:
                f_file.write('      } else if (value == ' + str(result_page) + ') {\n')
            s_player = self.CSV_list[self.CSV_list_selection + result_page][2]
            # print("s_player=", s_player)
            s_HP = self.CSV_list[self.CSV_list_selection + result_page][3]
            s_URL = self.CSV_list[self.CSV_list_selection + result_page][4]
            f_file.write('        button.textContent = "' + s_HP + '";\n')
            f_file.write('        button.onclick = function() {\n')
            f_file.write('          window.location.href = "' + s_URL + '";\n')
            f_file.write('        };\n')
        f_file.write('      }\n')
        f_file.write('    };\n')

    def html_display_photo(self, f_file):
        ###############################    
        # html:値による分岐(写真)
        ###############################    
        for result_page in range(self.CSV_list_result_by_CSV):
            if result_page == 0:
                f_file.write('      if (value == 0) {\n')
            else:
                f_file.write('      } else if (value == ' + str(result_page) + ') {\n')
            s_player = self.CSV_list[self.CSV_list_selection + result_page][2]
            s_photo = self.CSV_list[self.CSV_list_selection + result_page][3]
            f_file.write('        button.textContent = "' + s_photo + '";\n')
            f_file.write('        };\n')
        f_file.write('      }\n')
        f_file.write('    };\n')

    def html_select_branch(self, f_file, value_no):
        ###############################    
        # html:選択肢：問ｎ
        ###############################    
        s_question = self.CSV_list[value_no-1][1]

        step_no = self.selection_step_size[value_no-1]

        s_pos = []
        s_pos_name = []

        # 選択肢の数
        branch_no = len(self.CSV_list[value_no-1]) - 2
        
        for i in range(branch_no):
            s_pos.append("'" + str(i * step_no) + "'")    
            s_pos_name.append(self.CSV_list[value_no-1][i + 2])

        f_file.write('</head>\n')
        f_file.write('<body style="text-align:center; margin-top:50px;">\n')
        f_file.write('  <!-- 質問 -->\n')
        f_file.write('  <h1>' + s_question + '</h1>\n')
        f_file.write('  <!-- 選択肢（ボタン） -->\n')
        f_file.write('  <div class="button-container">\n')
        for i in range(branch_no):
            f_file.write('    <button onclick="saveValue(' + s_pos[i] + ')">' + s_pos_name[i] + '</button>\n')
        f_file.write('  </div>\n')
        f_file.write('</body>\n')
        f_file.write('</html>\n')

    def html_back_to_start(self, f_file):
        ###############################    
        # html:最初に戻る
        ###############################    
        f_file.write('</head>\n')
        f_file.write('<body style="text-align:center; margin-top:50px;">\n')
        f_file.write(' <p id="result"></p>\n')
        f_file.write(' <button id="myButton"></button>\n')
        f_file.write(' <button class="bottom-right" onclick="location.href=' + "'index.html'" + '">最初に戻る</button>\n')
        f_file.write('</body>\n')
        f_file.write('</html>\n')

    def html_back_to_start_photo(self, f_file):
        ###############################    
        # html:最初に戻る(result時)
        ###############################    
        f_file.write('</head>\n')
        f_file.write('<body style="text-align:center; margin-top:50px;">\n')
        f_file.write(' <p id="result"></p>\n')
        f_file.write('   <img id="artistImage" alt="アーティスト画像">\n')
        # f_file.write(' <button id="myButton"></button>\n')
        f_file.write(' <button class="bottom-right" onclick="location.href=' + "'index.html'" + '">最初に戻る</button>\n')
        f_file.write('</body>\n')
        f_file.write('</html>\n')

    def html_back_to_start_photo_3(self, f_file):
        ###############################    
        # html:最初に戻る(result_3_image時)
        ###############################    
        f_file.write('</head>\n')
        f_file.write('<body style="text-align:center; margin-top:50px;">\n')
        f_file.write('  <p id="result"></p>\n')
        f_file.write('  <div class="container">\n')
        f_file.write('    <div class="left-img">\n')
        f_file.write('      <img id="artistImage" alt="アーティスト画像">\n')
        f_file.write('    </div>\n')
        f_file.write('    <div class="right-imgs">\n')
        f_file.write('      <img id="rightImage1" alt="おすすめ画像1">\n')
        f_file.write('      <img id="rightImage2" alt="おすすめ画像2">\n')
        f_file.write('    </div>\n')
        f_file.write('  <button class="bottom-right" onclick="location.href=' + "'index.html'" + '">最初に戻る</button>\n')
        f_file.write('</body>\n')
        f_file.write('</html>\n')

class design:
    ###############################    
    ###############################    
    ###############################    
    # デザインクラス
    ###############################    
    ###############################    
    ###############################    
    def __init__(self, screen):
        # 画面
        self.screen = screen
        # ここでdesignを読み込む
        self.design = {}
        self.design["DESIGN"] = []
        self.data_path = ""
        # デザインのパラメタを初期化
        self.p = []

    def data_path(self, data):
        self.data_path = data

class Group_1up:
    #################################
    # １つ浮くグループでリストを修正
    ################################# 
    def __init__(self):
        #################################
        # 初期化
        #################################
        exit(0)
        self.next = -1
        self.previous = -1
        self.entry_no = 0
        self.list = []
        self.list.append(["ヘッダ0"])
        self.offset = 1
        self.insert("[1]1")
        self.insert("NoCode1")
        self.insert("設計・実行1")
        self.insert("次・前1")
        self.insert("左戦闘機1")
        self.insert("中戦闘機1")
        self.insert("右戦闘機1")
        self.display()

        self.bottom(0)
        self.display()

        # self.display()
        self.delete(5)
        self.display()
        self.delete(4)
        self.display()
        self.delete(3)
        self.display()
        self.delete(0)
        self.display()
        self.delete(2)
        self.display()
        self.delete(1)
        self.display()
        # self.delete(6)
        # self.display()
        print("++++++++++++++++++++++")
        self.insert("[1]")
        self.display()
        self.insert("NoCode")
        self.display()
        self.insert("設計・実行")
        self.display()
        self.insert("次・前")
        self.display()
        self.insert("左戦闘機")
        self.display()
        self.insert("中戦闘機")
        self.display()
        self.insert("サービス")
        self.display()
        exit(0)

    def bottom(self, n):
        #################################
        # ボトムに移動
        #################################
        print(n, "番目のリスト「", n, "」をボトムに移動")
        if self.previous == n:
            return
        #(1)bottomエントリ0を保存...Bottom_cur=1
        Bottom_cur = n   #0
        #(2)Pを最後として3保存...Last_P=3
        Last_P = self.previous
        #(3)bottomエントリBottom_curのNext1を保存...Bottom_next=1
        Bottom_next = self.list[self.add(Bottom_cur)][1]
        #(4)bottomエントリBottom_curのPrev-1を保存...Bottom_prev=-1
        Bottom_prev = self.list[self.add(Bottom_cur)][2]
        #(5)BottomエントリBottom_curのNextエントリのPrevにBottom_prevを設定
        data = self.list[self.add(Bottom_cur)][1]
        if data != -1:
            self.list[self.add(data)][2] = Bottom_prev
        else:
            self.preview = Bottom_prev
        #(5.5)PのエントリのNextにBottom_curを設定
        self.list[self.add(self.previous)][1] = Bottom_cur
        #(6)BottomエントリBottom_curのPrevエントリのNextにBottom_nextを設定、もし-1ならNにBottom_nextを設定
        data = self.list[self.add(Bottom_cur)][2]
        if data != -1:
            self.list[self.add(data)][1] = Bottom_next
        else:
            self.next = Bottom_next
        #(7)BottomエントリBottom_curのNextに-1を設定
        self.list[self.add(Bottom_cur)][1] = -1
        #(8)bottomエントリBottom_curのPrevにLAST_Pを設定
        self.list[self.add(Bottom_cur)][2] = Last_P
        #(9)PにBottom_curを設定
        self.previous = Bottom_cur

    def delete(self, n):
        #################################
        # 削除
        #################################
        print(n, "番目のリスト「", n, "」を削除")
        # (1)削除エントリのNext=3 Prev=1を保存
        Delete_next = self.list[self.add(n)][1]   #3
        Delete_prev = self.list[self.add(n)][2]   #1
        # (2)削除エントリを-1, -1, -1, "削"に
        self.list[self.add(n)][0] = -1
        self.list[self.add(n)][1] = -1
        self.list[self.add(n)][2] = -1
        self.list[self.add(n)][3] = "削"
        # (3)削除エントリのNext=3のエントリのPrev=1に変更
        # (3)削除エントリのNext=-1のエントリがないときは、Pを削除エントリのPrevに変更
        if Delete_next == -1:
            # 次のエントリがない
            self.previous = Delete_prev
        else:
            self.list[self.add(Delete_next)][2] = Delete_prev
        # (4)削除エントリのPrev=1のエントリのNext=3に変更
        # (4)削除エントリのPrev=-1のエントリがないときは、Nを削除エントリのNextに変更
        if Delete_prev == -1:
            # 前のエントリがない
            self.next = Delete_next
        else:
            # 前のエントリがある
            self.list[self.add(Delete_prev)][1] = Delete_next
        # (5)エントリ数の低減
        self.entry_no -= 1
                 
    def add(self, data):
        #################################
        # データの変換
        #################################
        return data + self.offset

    def display(self):
        #################################
        # 開始から表示
        #################################
        print(self.list)
        f_start = True 
        print("Next=", self.next, " Previous=", self.previous, " Entry_no=", self.entry_no)
        # nextが-1になるまで表示 
        
        if self.next == -1:
            return
        
        while True:
            if f_start == True:
                f_start = False
                # 先頭ページを表示
                pos = self.next
            else:
                pos = self.list[self.add(pos)][1]                       
            # 本処理
            print(self.list[self.add(pos)])
            if  self.list[self.add(pos)][1] == -1:
                break

    def insert(self, data):
        #################################
        # リストに挿入
        #################################
        # i_group = self.get_page_information(COM___group_next_top)
        # length = self.get_page_information(COM___group_entry_no)
        # for i in range(length):
        # i_group = self.get_group(i_group, COM__group_next)                       
        print(self.entry_no, "個ある中にリスト「", data, "」を挿入")


        # (1)空き場所を探し、それをnにする
        b_found = False
        for i in range(len(self.list)-1):
            if self.list[self.add(i)][0] == -1:
                # 空き場所発見
                n = i
                b_found = True
                break
        # (2)新グループを追加  
        if b_found == False:
            n = self.entry_no
            self.list.append([-1, -1, -1, ""])

        # (3)グループを設定
        self.list[self.add(n)][0] = n
        self.list[self.add(n)][1] = -1
        self.list[self.add(n)][2] = self.previous
        self.list[self.add(n)][3] = data

        # (4)前後設定
        if self.previous != -1:
            # 前エントリがあった
            self.list[self.add(self.previous)][1] = n
        self.previous = n                           
        if self.next == -1:
            self.next = 0

        # (5)エントリ数を１増やす
        self.entry_no += 1
        
def get_east_asian_width_count(text):
    #################################
    # 文字数カウント
    #################################
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in "FWA":
            count += 2
        else:
            count += 1
    if count == 0:
        count = 2
    return count        
            
def y_debug(data1, data2):
    #################################
    # 制御デバッグprint
    #################################
    pass
    print(data1, data2)


# 幅1480px、高さ700pxのサーフェス（書き出しはしない）
screen = pygame.Surface((1480, 700))  
# 最終書き出し
final_screen = pygame.display.set_mode((1480, 700), pygame.RESIZABLE)  

rate_x = 1
rate_y = 1

# l = Group_1up()

###################################################
# 最初にtempで始まりpklで終わるファイルを削除しておく 
###################################################
file_list = glob.glob("./data/temp*pkl")
for file in file_list:
    os.remove(file)

# PyGameの初期化
pygame.init()

# デザインを作成
o_design = design(screen)

# ページの作成
o_page = Page(o_design)

# ページ番号
o_page.page_no = 0

# 共通部を作成する
o_page.create_root_information()


# データパスを設定する
o_design.data_path = o_page.get_root_information(COM____data_path)

# 全ページを作成する
#555
# o_page.create_page()

# ページ開始を作る
o_page.create_page_by_CSV("page_start_program")

# ウィンドウタイトル
o_page.draw_window_title()

# マウス作業クラスを作成
o_Mouse_Control = Mouse_Control(o_page)

# テキスト処理のロジックTextクラスをインスタンス化
text = Text()  

# input, editingイベントをキャッチするようにするPyGameの命令
pygame.key.start_text_input()  

# 入力文字を描画するための関数　# 起動時にカーソルを表示するようにする
o_font = Fonts(32, FNT_MINCHO)
o_J = c_Input_Japanese(text, screen, o_Mouse_Control)
o_J.draw_text(format(text), o_font)  

# テキスト入力時のキーとそれに対応するイベント
event_trigger = {
    K_BACKSPACE: text.delete_left_of_cursor,
    K_DELETE: text.delete_right_of_cursor,
    K_LEFT: text.move_cursor_left,
    K_RIGHT: text.move_cursor_right,
    K_RETURN: text.enter,
}

# 入力モードをオフにする
o_page.input_mode = False
o_page.input_group_no = -1
o_page.input_component_no = -1
get_input_data = "" 

# メインループ
b_loop = True
while b_loop:
    # イベントキースキャン
    
    if o_page.input_mode == False:
        ####################
        # 非入力モード
        ####################
        if get_input_data != "":
            print("新しい文字が得られた「", get_input_data, "」")
            get_input_data = ""
        b_loop = o_Mouse_Control.event_key_scan()

        if b_loop == False:
            # ループを抜ける
            break

        # コンポーネントを描画
        o_page.draw(o_page.draw_mode)    

        g_no = o_Mouse_Control.select_group_when_right
        c_no = o_Mouse_Control.select_component_when_right

        # True画面をFinal画面に転送
        width = 1480
        window_x = 1480
        height = 700       
        window_y = 700
        # リサイズ後のサイズを取得
        image_width, image_height = final_screen.get_size()
        rate_x = 1480 / image_width
        rate_y = 700 / image_height
        if rate_x < 1:
            # 上限以上には拡大できない
            final_screen = pygame.display.set_mode((1480, 700), pygame.RESIZABLE)  
        final_screen.blit(pygame.transform.scale(screen,\
                (width/rate_x, height/rate_y)), (0, 0), (0, 0, window_x, window_y))

    else:
        ####################
        # 入力モードオン
        ####################

        # 背景の色
        get_input_data = ""
        o_J.input_text = ""  

        # 塗りつぶし    
        o_J.draw_out_frame(True)

        # 文字の描画
        o_J.draw_in_text()

        # 枠の描画
        o_J.draw_out_frame(False)
        
        # #33333333
        # exit(0)

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit(0)

            # キーダウンかつ、全角のテキスト編集中でない
            elif event.type == KEYDOWN and not text.is_editing:
                if event.key in event_trigger.keys():
                    o_J.input_text = event_trigger[event.key]()
                
                # 入力の確定
                if event.unicode in ("\r", "") and event.key == K_RETURN:
                    # 入力を完了

                    s = o_J.decide()                    

                    if s=="":
                        print("ERROR002:決定で入力がない")
                        
                    o_page.set_component(o_page.input_group_no, o_page.input_component_no, COM_text, s)
                    o_J.save_input_text = ""
                    o_J.input_text = ""
                    get_input_data = ""
                    o_page.input_mode = False
                    o_page.input_group_no = -1
                    o_page.input_component_no = -1
                    break

            elif event.type == TEXTEDITING:  
                # 全角入力
                o_J.input_2()
                # print("input_2")

            elif event.type == TEXTINPUT:  
                # 半角入力、もしくは全角入力時にenterを押したとき
                o_J.input_1()
                # print("input_1")

            else:
                pass    
                
            # 描画しなおす必要があるとき
            o_J.redraw()

        # True画面をFinal画面に転送
        # o_page.screen_width = 1480
        window_x = o_page.screen_width
        # o_page.screen_height = 700       
        window_y = o_page.screen_height
        # リサイズ後のサイズを取得
        image_width, image_height = final_screen.get_size()
        rate_x = 1480 / image_width
        rate_y = 700 / image_height
        if rate_x < 1:
            # 上限以上には拡大できない
            final_screen = pygame.display.set_mode((1480, 700), pygame.RESIZABLE)  
        final_screen.blit(pygame.transform.scale(screen,\
                (o_page.screen_width/rate_x, o_page.screen_height/rate_y)), (0, 0), (0, 0, window_x, window_y))

    # 画面を更新
    pygame.display.flip()  

# PyGameの終了処理
pygame.quit()    
        
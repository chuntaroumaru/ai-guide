import os
import datetime

template_css = """
  :root {
    --bg: #f8f9fa;
    --bg-card: #ffffff;
    --text: #212529;
    --text-muted: #6c757d;
    --border: #dee2e6;
    --accent: #0d6efd;
    --accent-hover: #0b5ed7;
    --badge-beginner: #198754;
    --badge-intermediate: #fd7e14;
    --badge-advanced: #dc3545;
    --shadow: 0 2px 8px rgba(0,0,0,0.08);
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #1a1d23;
      --bg-card: #252830;
      --text: #e9ecef;
      --text-muted: #adb5bd;
      --border: #3d4147;
      --accent: #4d94ff;
      --accent-hover: #6ba3ff;
      --shadow: 0 2px 8px rgba(0,0,0,0.4);
    }
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, "Yu Gothic", sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.8;
    font-size: 16px;
  }
  header {
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
    padding: 20px 32px;
    box-shadow: var(--shadow);
  }
  header .breadcrumb {
    font-size: 0.82rem;
    color: var(--text-muted);
    margin-bottom: 6px;
  }
  header .breadcrumb a { color: var(--accent); text-decoration: none; }
  header .breadcrumb a:hover { text-decoration: underline; }
  header h1 { font-size: 1.5rem; font-weight: 700; }
  header .subtitle { font-size: 0.88rem; color: var(--text-muted); margin-top: 4px; }
  .badge {
    display: inline-block;
    font-size: 0.72rem;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 4px;
    color: #fff;
    margin-left: 10px;
    vertical-align: middle;
    letter-spacing: 0.03em;
  }
  .badge-beginner { background: #198754; }
  .badge-intermediate { background: #fd7e14; }
  .badge-advanced { background: #dc3545; }
  .badge-overview { background: #0d6efd; }
  main {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 24px;
  }
  #toc {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px 24px;
    margin-bottom: 40px;
  }
  #toc h2 {
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 10px;
  }
  #toc ul { list-style: none; }
  #toc ul li { margin: 4px 0; }
  #toc ul li a { color: var(--accent); text-decoration: none; font-size: 0.92rem; }
  #toc ul li a:hover { text-decoration: underline; }
  h2.section-heading {
    font-size: 1.25rem;
    font-weight: 700;
    margin: 40px 0 16px;
    padding-bottom: 8px;
    border-bottom: 2px solid var(--border);
    scroll-margin-top: 16px;
  }
  h3.sub-heading {
    font-size: 1.05rem;
    font-weight: 700;
    margin: 24px 0 10px;
    scroll-margin-top: 16px;
  }
  p { margin-bottom: 14px; }
  ul, ol { margin: 0 0 14px 24px; }
  li { margin-bottom: 6px; }
  code {
    font-family: "Consolas", "Courier New", monospace;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 3px;
    padding: 1px 5px;
    font-size: 0.88em;
  }
  pre {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 16px 18px;
    overflow-x: auto;
    margin-bottom: 16px;
    font-size: 0.87em;
    line-height: 1.6;
  }
  pre code { background: none; border: none; padding: 0; font-size: inherit; }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 16px;
    font-size: 0.9em;
  }
  th, td {
    border: 1px solid var(--border);
    padding: 8px 12px;
    text-align: left;
  }
  th { background: var(--bg-card); font-weight: 700; }
  .back-to-toc {
    display: inline-block;
    margin-top: 16px;
    font-size: 0.82rem;
    color: var(--accent);
    text-decoration: none;
  }
  .back-to-toc:hover { text-decoration: underline; }
  .level-nav {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 32px;
  }
  .level-nav a {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 600;
    text-decoration: none;
    color: #fff;
    transition: opacity 0.15s;
  }
  .level-nav a:hover { opacity: 0.85; }
  .btn-overview { background: #0d6efd; }
  .btn-beginner { background: #198754; }
  .btn-intermediate { background: #fd7e14; }
  .btn-advanced { background: #dc3545; }
  .callout {
    background: var(--bg-card);
    border-left: 4px solid var(--accent);
    border-radius: 0 6px 6px 0;
    padding: 14px 18px;
    margin-bottom: 16px;
    font-size: 0.92rem;
  }
  .callout.tip { border-color: #198754; }
  .callout.warning { border-color: #fd7e14; }
  .callout.danger { border-color: #dc3545; }
  footer {
    text-align: center;
    padding: 24px;
    color: var(--text-muted);
    font-size: 0.82rem;
    border-top: 1px solid var(--border);
    margin-top: 48px;
  }
  footer a { color: var(--accent); text-decoration: none; }
  footer a:hover { text-decoration: underline; }
  @media (max-width: 600px) {
    header { padding: 14px 16px; }
    main { padding: 24px 16px; }
  }
"""

content = {
    "index": {
        "title": "概要",
        "class": "overview",
        "toc": ["Geminiの基本アーキテクチャと特徴", "Googleエコシステムとの統合", "業務システム開発における位置づけ", "各レベルの学習ロードマップ"],
        "body": """
<h2 class="section-heading" id="sec1">Geminiの基本アーキテクチャと特徴</h2>
<p>Gemini（ジェミニ）はGoogleが開発したマルチモーダルネイティブなAIモデルです。最初からテキスト、画像、音声、動画、コードを同時に理解できるように設計されている点が最大の特徴です。</p>
<p>特に <strong>Gemini 1.5 Pro</strong> は、最大200万トークンという桁違いのコンテキストウィンドウを持ち、1時間の動画、数万行のコードベース、あるいは数十冊のPDFマニュアルを一度に飲み込んで解析することが可能です。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">Googleエコシステムとの統合</h2>
<p>Geminiのもう一つの強みは、Google Workspace（Docs, Sheets, Drive, Gmail）やGoogle Cloud（GCP）とのシームレスな統合です。ブラウザ版のGemini Advancedでは、ユーザーのGoogle Drive内にあるファイルを直接参照して回答を生成できます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">業務システム開発における位置づけ</h2>
<p>フリーランスエンジニアにとって、Geminiは「超大規模データのバッチ処理・解析」および「GCP環境での開発支援」に最も適しています。</p>
<p>例えば、「過去10年分の業務要件変更履歴（Wordファイル群）をすべて読み込ませ、特定の機能がなぜ現在の仕様になったのかの経緯を時系列で抽出する」といった、人間の記憶力と検索能力の限界を超えるタスクで真価を発揮します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">各レベルの学習ロードマップ</h2>
<ul>
  <li><strong>初級編</strong>：Google Drive連携、画像・PDFのマルチモーダル解析。</li>
  <li><strong>中級編</strong>：超長文コンテキストの活用、GCP連携（Gemini Code Assist）、動画からの情報抽出。</li>
  <li><strong>上級編</strong>：Gemini API (Vertex AI) の組み込み、Function Calling、System Instructionsの最適化。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "beginner": {
        "title": "初級編",
        "class": "beginner",
        "toc": ["Google Workspace拡張機能の活用", "画像とPDFのマルチモーダル解析", "データ集計と表の作成", "よくある落とし穴"],
        "body": """
<h2 class="section-heading" id="sec1">Google Workspace拡張機能の活用</h2>
<p>ブラウザ版Gemini（またはGemini Advanced）では、設定から拡張機能をオンにすることで、Google Drive、Gmail、Google Docsのデータを直接検索・参照できます。</p>
<p><strong>プロンプト例：</strong></p>
<pre><code>@Google Drive
「2025年度_病院物流システム移行計画」という名前のドキュメントを探して、その中の「フェーズ2のスケジュール」を要約してください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">画像とPDFのマルチモーダル解析</h2>
<p>Geminiは視覚情報の処理に優れています。手書きのアーキテクチャ図（ホワイトボードの写真）や、レガシーシステムの画面キャプチャをアップロードし、そこからテキストや構造を抽出させます。</p>
<p><strong>プロンプト例：</strong></p>
<pre><code>（VB6.0の画面キャプチャ画像を添付）
この画面のUI要素（テキストボックス、ボタン、グリッド）をリストアップし、それぞれの要素がどのような業務アクションに対応しているか推測してください。その後、このUIをC#のWPFで再現するためのXAMLコードの骨組みを生成してください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">データ集計と表の作成</h2>
<p>非構造化データ（テキストの羅列やメールのやり取り）を構造化データ（表）に変換し、それをGoogle Sheetsに直接エクスポートする機能が強力です。</p>
<pre><code>以下の会議の議事録テキストから、「決定事項」「担当者」「期限」を抽出し、Markdownの表形式で出力してください。
出力後、Googleスプレッドシートにエクスポートするボタンを表示してください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">よくある落とし穴</h2>
<div class="callout warning">
  <strong>⚠️ Warning:</strong> GeminiはGoogle検索（グラウンディング）を自動的に行い、最新情報を取り入れますが、検索結果に引きずられて独自の推論が弱くなる（一般的なWeb記事の要約になってしまう）ことがあります。純粋なコードの推論や論理的思考を求める場合は、「Web検索は行わず、あなたの知識と論理的推論のみで回答してください」と明示的に指示する方が良い結果を得られる場合があります。
</div>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "intermediate": {
        "title": "中級編",
        "class": "intermediate",
        "toc": ["超長文コンテキスト（2Mトークン）の活用", "動画・音声からの情報抽出", "Gemini Code AssistによるGCP開発", "Pythonコード実行環境の活用"],
        "body": """
<h2 class="section-heading" id="sec1">超長文コンテキスト（2Mトークン）の活用</h2>
<p>Gemini 1.5 Proの最大の特徴である200万トークンのコンテキストウィンドウを活用します。これは「英語の小説なら約20冊分」「ソースコードなら数万行」に相当します。</p>
<p>GitHubからクローンした巨大なOSSプロジェクトのディレクトリ全体、あるいは自社のレガシーシステムのソースコード群を丸ごとZIPで固めて（またはGoogle AI Studio経由で）アップロードし、「このシステムにおいて、ユーザー認証からDBのセッション管理までのデータフローを追跡して解説して」といった指示が可能です。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">動画・音声からの情報抽出</h2>
<p>Geminiは動画ファイル（mp4等）や音声ファイルをそのままアップロードし、タイムスタンプ付きで内容を解析できます。システムの操作マニュアル動画や、要件定義の録画データ（Zoomの録画など）の解析に最適です。</p>
<p><strong>プロンプト例：</strong></p>
<pre><code>（1時間のシステム操作説明の動画を添付）
この動画から、ユーザーが「月次締め処理」を行っている箇所（タイムスタンプ）を特定し、その操作手順を箇条書きのテキストマニュアルとして書き起こしてください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">Gemini Code AssistによるGCP開発</h2>
<p>Google Cloud環境で開発を行う場合、VS CodeやIntelliJに「Gemini Code Assist」プラグインを導入することで、GitHub Copilotと同様のインライン補完やチャット機能を利用できます。特にGCPのAPI（Cloud Storage, Cloud Run, BigQueryなど）を利用するコードの生成や、IAM権限のトラブルシューティングにおいて、Google公式AIならではの正確さを発揮します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">Pythonコード実行環境の活用</h2>
<p>ブラウザ版のGemini Advancedには、ChatGPTのAdvanced Data Analysisに相当する「Pythonコードの実行環境」が備わっています。複雑な計算やデータプロットを要求すると、GeminiはバックグラウンドでPythonコードを書き、実行し、その結果（グラフやCSV）を返します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "advanced": {
        "title": "上級編",
        "class": "advanced",
        "toc": ["Gemini API (Vertex AI) の業務統合", "Structured Outputs (JSON) の強制", "System Instructionsによるペルソナ制御", "RAGアーキテクチャの構築"],
        "body": """
<h2 class="section-heading" id="sec1">Gemini API (Vertex AI) の業務統合</h2>
<p>エンタープライズ向けのシステム開発では、Google Cloudの「Vertex AI」経由でGemini APIを呼び出します。これにより、SLAの保証、エンタープライズレベルのデータプライバシー（学習への不使用）、VPC Service Controlsによるネットワーク制限など、業務システムに必須の要件を満たすことができます。</p>
<pre><code>// C#からVertex AIのGemini 1.5 Proを呼び出す概念コード
var client = new VertexAIClient("your-project-id", "asia-northeast1");
var model = client.GenerativeModel("gemini-1.5-pro");
var response = await model.GenerateContentAsync("物流システムの在庫予測アルゴリズムを提案して");
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">Structured Outputs (JSON) の強制</h2>
<p>業務システムでAIの出力をプログラム（C#など）で処理する場合、出力フォーマットが厳密なJSONであることが求められます。Gemini APIでは <code>response_mime_type</code> を <code>application/json</code> に指定し、さらに <code>response_schema</code> でJSON Schemaを定義することで、確実にパース可能なJSONを出力させることができます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">System Instructionsによるペルソナ制御</h2>
<p>API呼び出し時に <code>System Instructions</code> を設定することで、モデルの振る舞いや制約を根底から制御します。</p>
<pre><code>あなたは35年の経験を持つ、病院物流システムに精通したシニアデータベースエンジニアです。
- 回答は常に論理的で、客観的な事実に基づき、曖昧な推測は避けてください。
- SQL Server (T-SQL) のパフォーマンスチューニングの観点を必ず含めてください。
- 感情的な表現や過度な挨拶は不要です。
</code></pre>
<p>このように設定することで、ユーザー（フリーランスSE）の好みに完全に合致した、的確で無駄のないアシスタントをAPI経由で構築できます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">RAGアーキテクチャの構築</h2>
<p>Geminiの巨大なコンテキストウィンドウ（2Mトークン）は、従来のRAG（Retrieval-Augmented Generation：ベクトル検索で関連箇所だけを抽出してLLMに渡す手法）の概念を変えつつあります。</p>
<p>数万ページのドキュメントであれば、ベクトル検索（チャンク分割）を行わず、ドキュメント全体をそのままGeminiのコンテキストに放り込む「Long-Context RAG」というアプローチが可能です。これにより、文脈の分断（チャンク境界での情報の欠落）を防ぎ、より高精度な回答を得ることができます。Vertex AIでは、このアプローチを容易にするためのキャッシュ機能（Context Caching）も提供されています。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    }
}

for level_id, data in content.items():
    toc_html = ""
    for i, item in enumerate(data["toc"]):
        toc_html += f'<li><a href="#sec{i+1}">{item}</a></li>\n'
        
    level_nav_html = ""
    for l_id, l_data in content.items():
        if l_id == level_id:
            level_nav_html += f'<a href="{l_id}.html" class="btn-{l_data["class"]}" style="box-shadow: 0 0 0 2px var(--text);">{l_data["title"]}</a>\n'
        else:
            level_nav_html += f'<a href="{l_id}.html" class="btn-{l_data["class"]}">{l_data["title"]}</a>\n'
            
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gemini {data["title"]} — AIツール使いこなし指南</title>
  <style>{template_css}</style>
</head>
<body>
  <header>
    <div class="breadcrumb">
      <a href="../index.html">← ツール一覧へ戻る</a>
    </div>
    <h1>Gemini <span class="badge badge-{data["class"]}">{data["title"]}</span></h1>
    <p class="subtitle">フリーランスSE向け実践リファレンス</p>
  </header>

  <main>
    <div class="level-nav">
      {level_nav_html}
    </div>

    <nav id="toc">
      <h2>目次</h2>
      <ul>
        {toc_html}
      </ul>
    </nav>

    {data["body"]}
  </main>

  <footer>
    <p><a href="../index.html">← ツール一覧へ戻る</a></p>
    <p style="margin-top:8px;">最終更新：2026年06月08日</p>
  </footer>
</body>
</html>"""
    
    file_path = f"/home/ubuntu/ai-guide/gemini/{level_id}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {file_path}")


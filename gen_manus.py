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
        "toc": ["Manusの基本概念", "自律型エージェントとしての特長", "業務システム開発・運用における位置づけ", "各レベルの学習ロードマップ"],
        "body": """
<h2 class="section-heading" id="sec1">Manusの基本概念</h2>
<p>Manusは、単なるチャットAIではなく「自律型汎用AIエージェント」です。インターネットに接続されたサンドボックス環境（仮想マシン）を持ち、シェルコマンドの実行、ファイルの読み書き、ブラウザの操作、APIの呼び出しなどを自律的に組み合わせて、ユーザーから与えられたオープンエンドな目標を達成します。</p>
<p>「コードを書いて」と指示するのではなく、「この仕様書に基づいてWebサイトを構築し、サーバーにデプロイして」と指示することで、必要なツールを自ら選び、エラーが出れば自己修正しながらタスクを完了させます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">自律型エージェントとしての特長</h2>
<ul>
  <li><strong>Turing-completeな環境</strong>：Ubuntuベースのサンドボックス内で、Python、Node.js、シェルスクリプトなどを自由に実行可能。</li>
  <li><strong>エージェントループ</strong>：計画立案 → ツール選択 → 実行 → 結果の観察 → 計画の修正、というループを自律的に回します。</li>
  <li><strong>ブラウザ操作</strong>：Chromiumブラウザを制御し、ログインが必要なサイトの操作や、動的ページのスクレイピングが可能です。</li>
  <li><strong>マルチモーダル</strong>：画像や動画、音声の生成・編集ツールを内包しています。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">業務システム開発・運用における位置づけ</h2>
<p>フリーランスエンジニアにとって、Manusは「非常に優秀だが、時折監視が必要なアシスタントエンジニア」として機能します。</p>
<p>例えば、「AWSのS3バケットから先月分のログをダウンロードし、PythonのPandasで集計して、結果をグラフ化し、PDFのレポートにまとめて」といった、複数のツールとステップを跨ぐ「作業」を丸投げできます。これにより、開発者はアーキテクチャ設計や顧客折衝などの高付加価値な業務に専念できます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">各レベルの学習ロードマップ</h2>
<ul>
  <li><strong>初級編</strong>：Manusへの適切な指示（プロンプト）の出し方、得意なタスクと不得意なタスクの理解。</li>
  <li><strong>中級編</strong>：サンドボックス環境の活用、スクレイピングやデータ分析の自動化、エラー発生時の介入方法。</li>
  <li><strong>上級編</strong>：GitHub連携、Webアプリの自動構築（Scaffolding）、スケジュール実行（cron）の活用。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "beginner": {
        "title": "初級編",
        "class": "beginner",
        "toc": ["オープンエンドな指示の出し方", "得意なタスクとユースケース", "成果物の受け取り方", "やってはいけない指示"],
        "body": """
<h2 class="section-heading" id="sec1">オープンエンドな指示の出し方</h2>
<p>Manusには、手順を一つ一つ教える必要はありません。「最終的に何が欲しいか（Goal）」を明確に伝えます。</p>
<p><strong>悪い例：</strong>「PythonでRequestsライブラリをインストールして。次にURLにアクセスして...」</p>
<p><strong>良い例：</strong>「厚生労働省のサイトから最新の『医療施設動態調査』のExcelデータをダウンロードし、都道府県別の病床数を集計して、見やすい棒グラフ（PNG形式）を作成してください。」</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">得意なタスクとユースケース</h2>
<ul>
  <li><strong>情報収集とレポート作成</strong>：複数サイトを検索・閲覧し、事実確認を行った上で、MarkdownやPDFのレポートを作成する。</li>
  <li><strong>データクレンジング</strong>：表記揺れのあるCSVデータをPythonで整形し、クリーンなデータセットを出力する。</li>
  <li><strong>ドキュメント変換</strong>：Markdownで書かれた仕様書を、見栄えの良いHTMLやPDF、スライド（PPTX）に変換する。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">成果物の受け取り方</h2>
<p>Manusはサンドボックス内で作業を行うため、生成されたファイル（PDF、画像、CSVなど）は、最終的にManusからのメッセージの「添付ファイル」として受け取ります。プロンプト内で「結果はファイルに保存して添付してください」と明示すると確実です。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">やってはいけない指示</h2>
<div class="callout danger">
  <strong>🚫 Danger:</strong> Manusのサンドボックスはタスク終了時（または一定時間の非アクティブ状態）に初期化・破棄される可能性があります。「データベースサーバーを立ち上げて、ずっと稼働させておいて」といった、永続的なバックグラウンドプロセスの実行を要求するタスクには適していません。（※別途「Persistent Computing」環境が提供されている場合を除く）
</div>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "intermediate": {
        "title": "中級編",
        "class": "intermediate",
        "toc": ["ブラウザ操作とスクレイピング", "サンドボックス環境のハック", "並列処理（Map）の活用", "エラー時の介入とリカバリ"],
        "body": """
<h2 class="section-heading" id="sec1">ブラウザ操作とスクレイピング</h2>
<p>単純なHTTPリクエストでは取得できない、JavaScriptで動的にレンダリングされるページや、ログインが必要なページからの情報抽出を行います。</p>
<p><strong>プロンプト例：</strong></p>
<pre><code>以下のURL（社内のSaaSツール）にアクセスしてください。
ログイン画面が表示されたら、私にブラウザの操作権限（Takeover）を要求してください。
私がログインを完了した後、ダッシュボードから「今月の売上データ」のテーブルを読み取り、CSVファイルとして出力してください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">サンドボックス環境のハック</h2>
<p>ManusはUbuntu環境で動作しているため、標準でインストールされていないパッケージ（例えば特定のデータベースクライアントや、画像処理用のCライブラリなど）が必要な場合、<code>apt-get</code> や <code>pip install</code> を使って自ら環境を構築させることができます。</p>
<pre><code>処理の前に、`sudo apt-get update` と `sudo apt-get install -y sqlite3` を実行し、SQLite環境を構築してから以下のタスクを進めてください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">並列処理（Map）の活用</h2>
<p>大量のデータを処理する場合、Manusの並列処理ツール（Map）を活用させます。これはPythonの `Pool.map()` のように、数百のサブタスクを並列で実行する機能です。</p>
<p>「この100社の企業名リストについて、それぞれの企業のCIOの名前とメールアドレスを検索し、結果をCSVにまとめて」といった、広範なリサーチ作業を劇的に高速化できます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">エラー時の介入とリカバリ</h2>
<p>Manusがタスクの途中でスタックした場合（例：予期せぬポップアップでブラウザ操作が失敗した、APIのRate Limitに引っかかった等）、チャットを通じて直接助け舟を出します。</p>
<p>「現在の画面スクリーンショットを見せて」と指示して状況を確認し、「ポップアップの右上の[X]ボタン（index: 15）をクリックしてから再試行して」と具体的に介入することで、タスクを完了に導きます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "advanced": {
        "title": "上級編",
        "class": "advanced",
        "toc": ["GitHub連携と自動デプロイ", "WebDev Scaffoldによるアプリ構築", "スケジュール実行と定期タスク", "外部API・MCPとの連携"],
        "body": """
<h2 class="section-heading" id="sec1">GitHub連携と自動デプロイ</h2>
<p>ManusはGitHub CLI (`gh`) を標準で利用できます。これを利用して、コードの修正からPRの作成、マージまでを自動化します。</p>
<pre><code>以下のリポジトリをクローンしてください: `gh repo clone user/repo`
src/utils/calc.py に存在するバグ（ゼロ除算の可能性）を修正し、テストコードを追加してください。
修正完了後、新しいブランチを作成し、コミットしてPull Requestを作成してください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">WebDev Scaffoldによるアプリ構築</h2>
<p>ManusにはWebアプリケーションの雛形（Scaffold）を瞬時に構築する機能（`webdev_init_project`）が備わっています。</p>
<ul>
  <li><strong>web-static</strong>: Vite + React + TypeScript + TailwindCSS （LPなどに最適）</li>
  <li><strong>web-db-user</strong>: 上記に加え、Drizzle ORM + DB + 認証 + S3ストレージ （SaaSのプロトタイプに最適）</li>
</ul>
<p>「在庫管理システムのプロトタイプを作りたい。ユーザー認証と、備品一覧のCRUD機能を持つ `web-db-user` 構成でプロジェクトを初期化し、要件に合わせてUIを実装して」と指示するだけで、動くWebアプリが数分で立ち上がります。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">スケジュール実行と定期タスク</h2>
<p>Manusの設定ツール（`manus-config`）を利用すると、特定のタスクをcron形式で定期実行させることができます。</p>
<pre><code># 毎週月曜の朝8時に実行するスケジュールの設定例
manus-config schedule create \
  --title "週次競合調査" \
  --detail "競合他社3社のWebサイトの更新状況をチェックし、差分があればレポートを作成して私に通知してください。" \
  --cron "0 8 * * 1" \
  --repeated
</code></pre>
<p>これにより、Manusを単なるアシスタントから、24時間365日稼働する「自動化ワーカー」へと昇華させることができます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">外部API・MCPとの連携</h2>
<p>Model Context Protocol (MCP) を利用して、Manusに社内の非公開システムや独自のAPIを操作させることができます。例えば、社内のActive Directoryと連携するMCPサーバーを立てておけば、Manusに「来月入社する新入社員3名のアカウントを作成しておいて」と指示するだけで、セキュアな環境内でプロビジョニングが完了します。</p>
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
  <title>Manus {data["title"]} — AIツール使いこなし指南</title>
  <style>{template_css}</style>
</head>
<body>
  <header>
    <div class="breadcrumb">
      <a href="../index.html">← ツール一覧へ戻る</a>
    </div>
    <h1>Manus <span class="badge badge-{data["class"]}">{data["title"]}</span></h1>
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
    
    file_path = f"/home/ubuntu/ai-guide/manus/{level_id}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {file_path}")


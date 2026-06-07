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
        "toc": ["OpenClawとは", "他のAIエージェントとの違い", "業務システムにおける活用シナリオ", "各レベルの学習ロードマップ"],
        "body": """
<h2 class="section-heading" id="sec1">OpenClawとは</h2>
<p>OpenClaw（旧称：ClawDBot / MoltBot）は、オープンソースで開発されている自律型AIエージェントフレームワークです。最大の特長は、<strong>WhatsAppやTelegramなどのメッセージングアプリをインターフェースとして、自然言語で指示を出し、バックグラウンドで複雑なタスクを実行できる点</strong>にあります。</p>
<p>内部的にはLangChainやLlamaIndexのアーキテクチャを拡張しており、Webスクレイピング、ファイル操作、データベースクエリ、スケジュール実行などの「ツール」を自律的に組み合わせて目標を達成します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">他のAIエージェントとの違い</h2>
<p>ManusやChatGPT（Advanced Data Analysis）がクラウド上のサンドボックスで動作するのに対し、OpenClawは<strong>自社のローカルサーバーやVPSにデプロイして稼働させる</strong>ことができます。</p>
<ul>
  <li><strong>データの秘匿性</strong>：社内の閉域網にあるデータベース（OracleやSQL Server）に直接接続し、社外にデータを出さずに集計や分析を行わせることが可能です。</li>
  <li><strong>常駐型プロセス</strong>：デーモンとして常時稼働するため、cronライクなスケジュール実行や、特定のイベント（メール受信、DB更新）をトリガーとした自律処理が得意です。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">業務システムにおける活用シナリオ</h2>
<p>フリーランスエンジニアが、クライアント（病院など）の業務効率化のためにOpenClawを導入するシナリオが考えられます。</p>
<p>例えば、「毎朝7時に、物流システムのSQL Serverから前日の欠品リストを抽出し、Excelにまとめて、担当者のTelegramに送信する」という一連の処理を、プログラムを組むことなく、自然言語の設定ファイルだけで実現できます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">各レベルの学習ロードマップ</h2>
<ul>
  <li><strong>初級編</strong>：ローカル環境へのデプロイ、Telegramボットとしての初期設定。</li>
  <li><strong>中級編</strong>：カスタムツールの追加（DB接続、ファイル操作）、スクレイピングの自動化。</li>
  <li><strong>上級編</strong>：ベクトルデータベース（Milvus等）との連携によるRAG構築、業務フローへの完全統合。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "beginner": {
        "title": "初級編",
        "class": "beginner",
        "toc": ["環境構築とデプロイ", "メッセージングアプリとの連携", "基本的なコマンドと対話", "ログの確認とトラブルシューティング"],
        "body": """
<h2 class="section-heading" id="sec1">環境構築とデプロイ</h2>
<p>OpenClawはPythonベースのフレームワークです。Dockerを使用するのが最も簡単です。</p>
<pre><code># docker-compose.yml の例
version: '3.8'
services:
  openclaw:
    image: openclaw/core:latest
    environment:
      - OPENAI_API_KEY=sk-...
      - TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234...
    volumes:
      - ./data:/app/data
</code></pre>
<p><code>docker-compose up -d</code> で起動すると、設定したTelegramのボットトークン経由でアクセス可能になります。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">メッセージングアプリとの連携</h2>
<p>TelegramでBotFatherからボットを作成し、取得したトークンを環境変数にセットするだけで、スマホからエージェントに指示を出せるようになります。移動中や出先から「現在のDBサーバーのCPU使用率を確認して」といった指示が可能になります。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">基本的なコマンドと対話</h2>
<p>チャット画面から直接自然言語で指示を出します。</p>
<ul>
  <li>「今日のIT系ニュースをスクレイピングして要約して」</li>
  <li>「/data ディレクトリにある <code>sales.csv</code> を読み込んで、売上の合計を計算して」</li>
</ul>
<p>OpenClawは利用可能なツール（Web Search, File Reader, Python REPL等）を自律的に選択し、結果をチャットに返します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">ログの確認とトラブルシューティング</h2>
<p>エージェントが「何を考えてどのツールを選択したか」の思考プロセス（Chain of Thought）は、Dockerのログに出力されます。意図しない動作をした場合は、<code>docker logs openclaw</code> を確認し、プロンプトの曖昧さを修正します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "intermediate": {
        "title": "中級編",
        "class": "intermediate",
        "toc": ["カスタムツールの開発", "社内データベースとの接続", "定期実行タスクの設定", "状態（State）の保持"],
        "body": """
<h2 class="section-heading" id="sec1">カスタムツールの開発</h2>
<p>OpenClawの真価は、自社の業務に合わせた「カスタムツール」をPythonで記述して追加できる点にあります。</p>
<pre><code># カスタムツールの例：在庫確認ツール
from openclaw.tools import BaseTool

class CheckInventoryTool(BaseTool):
    name = "check_inventory"
    description = "指定されたアイテムの現在の在庫数を社内システムから取得します。"
    
    def _run(self, item_name: str) -> str:
        # ここにDBアクセスや社内API呼び出しのロジックを書く
        return f"{item_name}の在庫は現在150個です。"
</code></pre>
<p>これを登録することで、チャットから「シリンジの在庫いくつ？」と聞くだけで、エージェントがこのツールを呼び出して回答します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">社内データベースとの接続</h2>
<p>SQL ServerやOracleへの接続ツールを実装します。セキュリティの観点から、エージェントに直接SQLを書かせる（Text-to-SQL）のではなく、あらかじめ定義したストアドプロシージャやViewを呼び出すツールを用意するアプローチが安全です。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">定期実行タスクの設定</h2>
<p>OpenClawにはスケジューラが組み込まれており、自然言語で定期タスクを設定できます。</p>
<p>「毎朝8時に、<code>check_inventory</code> ツールを使って在庫が10個以下のアイテムをリストアップし、このチャットに通知して」</p>
<p>エージェントはこの指示をパースし、内部のcronジョブとして登録します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">状態（State）の保持</h2>
<p>長期的なタスクをこなすために、エージェントは過去の対話や取得したデータをローカルのSQLiteなどに記憶（Memory）として保持します。「昨日頼んだあの件の続きをやって」といったコンテキストを跨いだ指示が可能になります。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "advanced": {
        "title": "上級編",
        "class": "advanced",
        "toc": ["Milvusを用いたエンタープライズRAG", "マルチエージェント協調システム", "セキュリティとアクセス制御", "本番環境での運用設計"],
        "body": """
<h2 class="section-heading" id="sec1">Milvusを用いたエンタープライズRAG</h2>
<p>社内の膨大なマニュアルや過去の障害対応履歴を、ベクトルデータベース（Milvusなど）に格納し、OpenClawと連携させます。これにより、エージェントは「知識」を持った状態で回答できるようになります。</p>
<p>「エラーコード ORA-01555 が出たんだけど、過去にどう対応した？」という質問に対し、エージェントはMilvusを検索（Retrieval）し、過去の対応履歴を踏まえた具体的な解決策を生成（Generation）してチャットに返します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">マルチエージェント協調システム</h2>
<p>単一のエージェントにすべてをやらせるのではなく、役割を分担した複数のエージェントを協調させます。</p>
<ul>
  <li><strong>リサーチャー・エージェント</strong>：Webから情報を集める。</li>
  <li><strong>コーダー・エージェント</strong>：集めた情報からPythonスクリプトを書く。</li>
  <li><strong>レビュアー・エージェント</strong>：書かれたコードをテストし、安全性を確認する。</li>
</ul>
<p>OpenClawのフレームワーク上でこれらのエージェントが互いに通信し、最終的な成果物だけをユーザー（Telegram）に届ける高度な自律システムを構築できます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">セキュリティとアクセス制御</h2>
<p>チャット経由でDBの更新（DELETEやUPDATE）を許可するのは非常に危険です。業務システムに組み込む場合は、「Read Only」のツールと「Write」のツールを厳格に分け、Write系のツールを実行する前には必ずユーザー（Telegram上の特定のChat ID）に「実行してもよろしいですか？ (Yes/No)」の承認（Human-in-the-loop）を求めるフローを実装します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">本番環境での運用設計</h2>
<p>エージェントが暴走して無限ループに陥る（API費用が枯渇する）のを防ぐため、<code>max_iterations</code>（最大思考回数）の設定や、1日あたりのAPIトークン消費量のアラート設定が必須です。また、エージェントの行動ログはすべて監査証跡として保存し、後から追跡できるように設計します。</p>
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
  <title>OpenClaw {data["title"]} — AIツール使いこなし指南</title>
  <style>{template_css}</style>
</head>
<body>
  <header>
    <div class="breadcrumb">
      <a href="../index.html">← ツール一覧へ戻る</a>
    </div>
    <h1>OpenClaw <span class="badge badge-{data["class"]}">{data["title"]}</span></h1>
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
    
    file_path = f"/home/ubuntu/ai-guide/openclaw/{level_id}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {file_path}")


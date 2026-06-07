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
        "toc": ["Claudeの基本アーキテクチャと特徴", "ChatGPTとの違い・使い分け", "業務システム開発における位置づけ", "各レベルの学習ロードマップ"],
        "body": """
<h2 class="section-heading" id="sec1">Claudeの基本アーキテクチャと特徴</h2>
<p>Anthropic社が開発したClaude（クロード）シリーズ（Claude 3.5 Sonnet / Opus など）は、特に<strong>長文コンテキストの処理能力</strong>と<strong>論理的で洗練された日本語の出力</strong>において高い評価を得ている大規模言語モデルです。</p>
<p>一度に処理できるトークン数（コンテキストウィンドウ）が非常に大きく、数百ページに及ぶ要件定義書や、数十個のソースコードファイルを丸ごと読み込ませて、その全体像を踏まえた上で回答させることが可能です。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">ChatGPTとの違い・使い分け</h2>
<p>エンジニア視点での使い分けは以下のようになります。</p>
<table>
  <tr>
    <th>比較軸</th>
    <th>Claude 3.5 Sonnet / Opus</th>
    <th>ChatGPT (GPT-4o / o3)</th>
  </tr>
  <tr>
    <td><strong>長文処理</strong></td>
    <td>◎ 巨大なログやソースコード群を丸投げしての全体解析が得意。情報の取りこぼしが少ない。</td>
    <td>〇 コンテキストが長すぎると、途中の中間情報を無視する傾向がある（Lost in the middle現象）。</td>
  </tr>
  <tr>
    <td><strong>コーディング</strong></td>
    <td>◎ 堅牢でバグの少ない、洗練されたコードを出力する。特にフロントエンド（React/Vue）のUI生成に強い（Artifacts機能）。</td>
    <td>◎ 複雑なアルゴリズムやSQLの推論（o3モデル）においては依然としてトップクラス。</td>
  </tr>
  <tr>
    <td><strong>文章のトーン</strong></td>
    <td>◎ 人間らしく、自然で論理的な日本語。ドキュメント作成に最適。</td>
    <td>〇 翻訳調やAI特有の「AI構文」になりがち。</td>
  </tr>
</table>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">業務システム開発における位置づけ</h2>
<p>35年の経験を持つエンジニアにとって、Claudeは「巨大なレガシーシステムの全容把握」と「設計ドキュメントの自動生成」における最強のパートナーです。</p>
<p>VB6.0のプロジェクト全体（数十個の .frm や .bas ファイル）をZipで固めてアップロードし、「このシステムの業務フローを解析し、PlantUMLでシーケンス図を出力して」といった離れ業が可能です。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">各レベルの学習ロードマップ</h2>
<ul>
  <li><strong>初級編</strong>：Claudeの基本的な使い方、長文プロンプトの記述方法（XMLタグの活用）。</li>
  <li><strong>中級編</strong>：Projects機能を用いた社内ナレッジの共有、Artifactsを用いたUIプロトタイピング。</li>
  <li><strong>上級編</strong>：Claude API (Anthropic API) のシステム統合、Prompt Cachingによるコストとレイテンシの最適化。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "beginner": {
        "title": "初級編",
        "class": "beginner",
        "toc": ["XMLタグを用いたプロンプト設計", "長文ドキュメントの要約と抽出", "コードのレビューとリファクタリング", "ArtifactsによるUIの即時プレビュー"],
        "body": """
<h2 class="section-heading" id="sec1">XMLタグを用いたプロンプト設計</h2>
<p>Claudeはプロンプト内の構造を理解する能力に長けており、公式でも<strong>XMLタグ</strong>を用いたプロンプトの構造化が推奨されています。これにより、指示とデータ（ソースコードなど）を明確に分離できます。</p>
<pre><code>以下のVB.NETのコードをC#に変換してください。

&lt;instructions&gt;
- Entity Framework Coreを使用すること
- 変数名はcamelCaseとすること
&lt;/instructions&gt;

&lt;source_code&gt;
Public Function GetPatient(ByVal id As Integer) As Patient
    ' ... VB.NETのコード ...
End Function
&lt;/source_code&gt;
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">長文ドキュメントの要約と抽出</h2>
<p>病院物流システムの数百ページに及ぶPDF仕様書をアップロードし、特定の情報だけを抽出させます。</p>
<p><strong>プロンプト例：</strong></p>
<pre><code>添付の要件定義書（PDF）を読み込み、以下のタスクを実行してください。

1. 「滅菌材料の有効期限管理」に関する業務ルールを箇条書きで抽出してください。
2. そのルールを実装する上で、データベース設計において考慮すべき点を3つ挙げてください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">コードのレビューとリファクタリング</h2>
<p>Claudeは「なぜそのように修正したか」の論理的な説明が非常に丁寧です。複雑なビジネスロジックを含むメソッドのレビューに適しています。</p>
<pre><code>&lt;code&gt;タグ内のC#コードをレビューしてください。
私はこのコードが「Solid原則」の「単一責任の原則 (SRP)」に違反していると考えていますが、
具体的なリファクタリング案（クラスの分割案）を提示してください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">ArtifactsによるUIの即時プレビュー</h2>
<p>Claudeの強力な機能の一つが「Artifacts」です。HTML/CSS/JSやReactコンポーネントを生成させると、チャット画面の右側にプレビューが即座に表示されます。</p>
<p>「病院の在庫管理ダッシュボードのUIモックアップをTailwind CSSで作って」と指示するだけで、動的なプロトタイプが完成し、設計の壁打ちが視覚的に行えます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "intermediate": {
        "title": "中級編",
        "class": "intermediate",
        "toc": ["Projects機能によるコンテキスト共有", "巨大ログファイルの異常検知", "複雑なSQLの解析とチューニング", "システム移行計画の立案"],
        "body": """
<h2 class="section-heading" id="sec1">Projects機能によるコンテキスト共有</h2>
<p>Claudeの「Projects」機能を使用すると、特定のプロジェクト専用のチャット環境を作成し、そこに「社内コーディング規約」「既存のデータベース定義書（DDL）」「アーキテクチャ設計書」などのファイルを「Knowledge」として永続的に登録しておけます。</p>
<p>これにより、毎回プロンプトで前提条件を説明する手間が省け、「いつものDBのT_Patientテーブルに対するクエリを書いて」といった抽象的な指示で正確なコードが返ってくるようになります。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">巨大ログファイルの異常検知</h2>
<p>数万行のIISアクセスログや、SQL ServerのError Logをテキストファイルとしてそのままアップロードし、解析させます。</p>
<pre><code>添付のログファイルから、以下の条件に合致する異常を検知し、レポートを作成してください。

&lt;conditions&gt;
- HTTPステータス 500 が連続して発生している時間帯
- 実行に3秒以上かかっている遅延リクエストのURLエンドポイントTop 5
&lt;/conditions&gt;

&lt;format&gt;
結果はMarkdownのテーブル形式で出力してください。
&lt;/format&gt;
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">複雑なSQLの解析とチューニング</h2>
<p>数百行に及ぶ、サブクエリとJOINが入り乱れたレガシーなストアドプロシージャの解読にClaudeは最適です。</p>
<pre><code>以下のOracle PL/SQLのストアドプロシージャを解析してください。
1. このプロシージャが最終的に何を取得・更新しようとしているか、業務的な意図を推測して要約してください。
2. これをSQL ServerのT-SQLに移行する場合の書き換えコードを提示してください。
3. その際、カーソル（CURSOR）処理をセットベース（Window関数など）の処理にリファクタリングしてください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">システム移行計画の立案</h2>
<p>現行システムの仕様と、移行先システムのアーキテクチャ方針を与え、WBS（Work Breakdown Structure）を伴う移行計画を立案させます。経験豊富なエンジニアの視点として、「どこにリスクが潜んでいるか」を重点的に指摘させます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "advanced": {
        "title": "上級編",
        "class": "advanced",
        "toc": ["Anthropic APIの業務統合", "Prompt Cachingによるコスト最適化", "Tool Use (Function Calling) の実装", "Computer Useの概念と応用"],
        "body": """
<h2 class="section-heading" id="sec1">Anthropic APIの業務統合</h2>
<p>C#からAnthropic API（Claude）を呼び出して、社内システムに高度な自然言語処理機能を組み込みます。公式のSDK、またはHTTPクライアントを使用してJSONベースのREST APIを叩きます。</p>
<pre><code>// HttpClientを使用したAnthropic API呼び出しの基本構造 (C#)
var requestBody = new {
    model = "claude-3-5-sonnet-20241022",
    max_tokens = 1024,
    messages = new[] {
        new { role = "user", content = "病院物流におけるABC分析の手法を解説してください。" }
    }
};
// x-api-key ヘッダーと anthropic-version ヘッダーが必須です。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">Prompt Cachingによるコスト最適化</h2>
<p>Claude APIの強力な機能に「Prompt Caching」があります。これは、巨大なシステムプロンプトや長文のドキュメント（例えば社内規約のPDFテキスト）をAPI側でキャッシュし、2回目以降の呼び出しで入力トークン費用とレイテンシ（応答時間）を劇的に削減する技術です。</p>
<p>業務システムで毎回同じDBスキーマ情報をLLMに渡してSQLを生成させるようなRAGシステムにおいて、キャッシュの有無はランニングコストに直結します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">Tool Use (Function Calling) の実装</h2>
<p>ChatGPTと同様に、ClaudeにもTool Use（関数呼び出し）機能があります。ClaudeのTool UseはJSON Schemaの定義に厳密に従い、複雑な引数を持つ関数の推論に優れています。</p>
<p>自社システムのAPI（例：在庫引き当てAPI、発注API）をToolとしてClaudeに渡し、「A病棟のシリンジが足りないから補充しておいて」という自然言語の指示から、自動的に在庫確認→発注処理のAPIをシーケンシャルに叩く自律エージェントを構築できます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">Computer Useの概念と応用</h2>
<p>2024年後半に発表されたClaude 3.5 Sonnetの「Computer Use」機能は、API経由でAIに<strong>「マウスの操作」や「キーボード入力」</strong>を行わせる画期的な機能です。</p>
<p>APIがないレガシーな業務システム（VB6.0で作られたGUIアプリなど）の画面スクリーンショットをClaudeに渡し、Claudeが「どこをクリックし、何を入力すべきか」の座標を返すことで、RPA（Robotic Process Automation）をAIベースで動的に実行することが可能になります。</p>
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
  <title>Claude {data["title"]} — AIツール使いこなし指南</title>
  <style>{template_css}</style>
</head>
<body>
  <header>
    <div class="breadcrumb">
      <a href="../index.html">← ツール一覧へ戻る</a>
    </div>
    <h1>Claude <span class="badge badge-{data["class"]}">{data["title"]}</span></h1>
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
    
    file_path = f"/home/ubuntu/ai-guide/claude/{level_id}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {file_path}")


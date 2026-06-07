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
        "toc": ["GitHub Copilotの基本概念", "IDE統合のメリット", "業務システム開発での位置づけ", "各レベルの学習ロードマップ"],
        "body": """
<h2 class="section-heading" id="sec1">GitHub Copilotの基本概念</h2>
<p>GitHub Copilotは、OpenAIのモデル（GPT-4等）をベースにした、IDE（統合開発環境）向けAIペアプログラマーです。エディタ上でコードをタイピングしている最中に、文脈をリアルタイムに解析し、次に書くべきコードの行やブロック全体を提案（ゴーストテキストとして表示）します。</p>
<p>単なるスニペットツールとは異なり、現在開いているファイルだけでなく、プロジェクト内の他のファイル（タブで開いているファイルなど）もコンテキストとして読み込むため、プロジェクト固有の変数名やメソッド名を正確に推論します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">IDE統合のメリット</h2>
<p>ブラウザベースのChatGPTと比較した最大の利点は「コンテキストスイッチの排除」です。コードをコピーしてブラウザに貼り付け、結果をまたIDEに戻す手間が不要になります。さらに、Visual StudioやVS CodeのCopilot Chat機能を使えば、エディタ内で直接「このメソッドのリファクタリング案を出して」「選択した範囲の単体テストを書いて」といった対話型指示が可能です。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">業務システム開発での位置づけ</h2>
<p>病院物流システムのような大規模で複雑な業務アプリケーション開発において、Copilotは「タイピング速度を劇的に向上させる強力なインテリセンス」として機能します。</p>
<ul>
  <li><strong>ボイラープレートの削減</strong>：DTOとEntity間のマッピングコードや、プロパティの羅列を自動補完します。</li>
  <li><strong>命名規約の自動適用</strong>：既存のコード（<code>_camelCase</code> や <code>PascalCase</code>）のパターンを学習し、それに従った変数名を提案します。</li>
  <li><strong>SQL Serverとの連携</strong>：C#のコード内に記述するインラインSQLやLINQクエリを、周囲のコンテキストから正確に推論します。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">各レベルの学習ロードマップ</h2>
<ul>
  <li><strong>初級編</strong>：基本的なインライン補完の使い方、コメントからのコード生成、Copilot Chatの基本操作。</li>
  <li><strong>中級編</strong>：Copilotに正しいコンテキストを読ませるためのタブ管理術、スラッシュコマンド（<code>/explain</code>, <code>/tests</code>）の活用。</li>
  <li><strong>上級編</strong>：Copilot Workspaceの活用、大規模リファクタリング（VB.NETからC#への移行など）におけるプロジェクト全体の文脈共有。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "beginner": {
        "title": "初級編",
        "class": "beginner",
        "toc": ["インライン補完の基本操作", "コメント駆動でのコード生成", "Copilot Chatの基本", "よくある落とし穴と対策"],
        "body": """
<h2 class="section-heading" id="sec1">インライン補完の基本操作</h2>
<p>コードを入力していると、グレーの文字（ゴーストテキスト）で提案が表示されます。これがCopilotの基本機能です。</p>
<ul>
  <li><strong>提案を受け入れる</strong>：<code>Tab</code> キー</li>
  <li><strong>単語単位で受け入れる</strong>：<code>Ctrl + RightArrow</code>（Windows）</li>
  <li><strong>別の提案を見る</strong>：<code>Alt + ]</code> / <code>Alt + [</code></li>
  <li><strong>提案を拒否する</strong>：そのままタイピングを続けるか、<code>Esc</code> キー</li>
</ul>
<p>関数名を入力した直後や、<code>if</code> 文の条件式を書こうとした瞬間に、最も効果的な提案が行われます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">コメント駆動でのコード生成</h2>
<p>実装したい処理をコメントとして記述し、改行すると、そのコメントの意図を汲み取ったコードブロックが提案されます。</p>
<pre><code>// 指定されたPatientIdに紐づく、過去1年間の有効な処方箋履歴を取得し、日付の降順で返す
public async Task&lt;List&lt;Prescription&gt;&gt; GetRecentPrescriptionsAsync(int patientId)
{
    // ← ここで改行して少し待つと、Entity Framework Coreを使ったLINQクエリが提案される
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">Copilot Chatの基本</h2>
<p>エディタのサイドバー、またはインライン（<code>Ctrl + I</code>）で開くチャットウィンドウです。コードを選択した状態で質問すると、そのコードをコンテキストとして回答してくれます。</p>
<p><strong>活用例：</strong></p>
<ul>
  <li>複雑な正規表現を選択して「この正規表現が何をしているか解説して」</li>
  <li>エラーが出ている行を選択して「このエラーの原因と修正案を教えて」</li>
  <li>メソッドを選択して「この処理を非同期（async/await）に書き換えて」</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">よくある落とし穴と対策</h2>
<div class="callout warning">
  <strong>⚠️ Warning:</strong> Copilotは「もっともらしいコード」を提案しますが、それが「正しいコード」とは限りません。特に、存在しないライブラリのメソッドをでっち上げる（ハルシネーション）ことがあります。提案を受け入れた後は、必ずコンパイルエラーが出ないか、意図したロジックになっているかを目視で確認する癖をつけてください。
</div>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "intermediate": {
        "title": "中級編",
        "class": "intermediate",
        "toc": ["コンテキストの制御（タブ管理術）", "スラッシュコマンドと変数", "単体テストの効率的な生成", "ドキュメントの自動生成"],
        "body": """
<h2 class="section-heading" id="sec1">コンテキストの制御（タブ管理術）</h2>
<p>Copilotが適切な提案をするためには、必要な情報（コンテキスト）を与え、不要な情報を排除することが極めて重要です。Copilotは<strong>現在開いているタブ</strong>を優先的に読み込みます。</p>
<p><strong>ベストプラクティス：</strong></p>
<ul>
  <li>新しいクラスを実装する際、依存するインターフェースや、似たような処理を行っている別のクラスを<strong>隣のタブで開いておく</strong>。</li>
  <li>関係のないファイル（過去のプロジェクトの残骸など）は閉じておく。</li>
  <li>Copilot Chatでは、<code>#file:FileName.cs</code> のように明示的にファイルを参照させる。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">スラッシュコマンドと変数</h2>
<p>Copilot Chatでは、特定のタスクを素早く実行するためのスラッシュコマンドが用意されています。</p>
<ul>
  <li><code>/explain</code>：選択したコードの解説（レガシーコードの解読に最適）</li>
  <li><code>/fix</code>：選択したコードの問題点を修正</li>
  <li><code>/tests</code>：選択したコードの単体テストを生成</li>
  <li><code>/doc</code>：選択したコードのXMLドキュメントコメントを生成</li>
</ul>
<p>また、<code>@workspace</code> を指定すると、開いているプロジェクト全体から関連する情報を検索して回答してくれます（例：「<code>@workspace</code> データベース接続文字列はどこで定義されていますか？」）。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">単体テストの効率的な生成</h2>
<p>テスト対象のメソッドを選択し、<code>/tests</code> コマンドを実行します。この時、チャットのプロンプトに社内規約を追加することで、手戻りを減らせます。</p>
<p><strong>プロンプト例：</strong></p>
<pre><code>/tests
以下の条件に従ってxUnitのテストを生成してください。
- AAA (Arrange, Act, Assert) パターンに従うこと。
- 依存関係のモック化には Moq を使用すること。
- 正常系だけでなく、引数が null の場合や、DBからデータが取得できなかった場合の異常系も含めること。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">ドキュメントの自動生成</h2>
<p>メソッドのシグネチャ（引数と戻り値）を定義した直後に <code>///</code> (C#の場合) と入力すると、Copilotがメソッドの目的、各引数の説明、戻り値の説明を含むXMLドキュメントコメントを自動生成します。複雑なロジックを実装した後は、<code>/doc</code> コマンドでコードの意図をドキュメント化させると、保守性が向上します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "advanced": {
        "title": "上級編",
        "class": "advanced",
        "toc": ["Copilot Workspaceによるタスク駆動開発", "大規模リファクタリング戦略", "独自ルール（Custom Instructions）の適用", "セキュリティとプライバシーの管理"],
        "body": """
<h2 class="section-heading" id="sec1">Copilot Workspaceによるタスク駆動開発</h2>
<p>Copilot Workspaceは、単一ファイルの補完を超え、GitHub Issueから直接コードの変更計画（Plan）を作成し、複数ファイルにまたがる実装を一気に生成する機能です。</p>
<ol>
  <li>GitHub Issueに「Oracleの在庫テーブル参照処理をSQL Server向けに移行し、Dapperで実装する」といった要件を記述する。</li>
  <li>WorkspaceでIssueを開くと、AIが現状のコードベースを解析し、変更すべきファイルと修正内容の計画（Plan）を提示する。</li>
  <li>エンジニアが計画をレビュー・修正し、実行（Implement）させると、複数ファイルの差分（Diff）が生成される。</li>
  <li>内容を確認し、直接Pull Requestを作成する。</li>
</ol>
<p>これにより、設計レベルの指示から実装までをシームレスに繋ぐことができます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">大規模リファクタリング戦略</h2>
<p>VB.NETからC#への全面移行や、モノリスからマイクロサービスへの分割など、大規模なリファクタリングにおいてCopilotを活用する戦略です。</p>
<ul>
  <li><strong>段階的移行</strong>：一気に全体を変換するのではなく、ドメインモデル（Entity）→ データアクセス層（Repository）→ ビジネスロジック（Service）の順に、コンテキストを絞りながら変換を指示します。</li>
  <li><strong>インターフェース主導</strong>：先にC#でモダンなインターフェースを定義し、そのインターフェースを実装する形でVB.NETの旧ロジックを移植するよう指示すると、アーキテクチャの改善とコード変換を同時に行えます。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">独自ルール（Custom Instructions）の適用</h2>
<p>プロジェクトのルートディレクトリに <code>.github/copilot-instructions.md</code> などの設定ファイルを配置し、Copilotにプロジェクト固有のコーディング規約やアーキテクチャのルールを強制します。</p>
<pre><code># プロジェクト規約
- データベースへのアクセスは直接 `DbContext` を触らず、必ず `IRepository&lt;T&gt;` を経由すること。
- 日付と時刻はすべて `DateTimeOffset` を使用し、ローカル時間は使用しないこと。
- 変数名はキャメルケース、メソッド名はパスカルケースを厳守すること。
</code></pre>
<p>これにより、生成されるコードが最初から社内標準に準拠する確率が大幅に高まります。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">セキュリティとプライバシーの管理</h2>
<p>業務システムのソースコードを扱う以上、セキュリティ設定の理解は必須です。GitHub Copilot Business / Enterprise エディションでは、組織の管理者が「ユーザーのコードスニペットをOpenAIのモデル学習に使用させない」設定を強制できます。</p>
<p>また、機密情報（APIキーやパスワード）を含むファイルを開いている場合、その内容がコンテキストとして送信される可能性があるため、<code>.copilotignore</code> （または類似の機能）を使用して、特定のファイルやディレクトリをCopilotの解析対象から除外する運用を徹底する必要があります。</p>
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
  <title>GitHub Copilot {data["title"]} — AIツール使いこなし指南</title>
  <style>{template_css}</style>
</head>
<body>
  <header>
    <div class="breadcrumb">
      <a href="../index.html">← ツール一覧へ戻る</a>
    </div>
    <h1>GitHub Copilot <span class="badge badge-{data["class"]}">{data["title"]}</span></h1>
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
    
    file_path = f"/home/ubuntu/ai-guide/copilot/{level_id}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {file_path}")


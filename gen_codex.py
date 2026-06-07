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
        "toc": ["Codexとは何か", "GitHub Copilotとの違い", "業務システム開発における位置づけ", "各レベルの学習ロードマップ"],
        "body": """
<h2 class="section-heading" id="sec1">Codexとは何か</h2>
<p>OpenAI Codexは、GPT-3/GPT-4アーキテクチャをベースに、数十億行の公開ソースコードを学習させたプログラミング特化型の言語モデルです。自然言語の指示をコードに変換したり、コードの続きを推論して自動補完したりする能力に長けています。</p>
<p>※2026年現在、純粋な「Codex」という単独の製品よりも、GPT-4oやo3などの最新モデルがCodexの能力を内包しているケースが多く、またその技術はGitHub Copilotの基盤として広く普及しています。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">GitHub Copilotとの違い</h2>
<p>Codexは「モデルそのもの（API経由でアクセスするエンジン）」であり、GitHub Copilotは「Codexモデルを利用したIDE向けのアシスタント製品」です。</p>
<ul>
  <li><strong>Codex (API)</strong>：自社システムに組み込んで、独自のコード生成ツールや自動レビューツールを作るための基盤。</li>
  <li><strong>GitHub Copilot</strong>：VS CodeやVisual Studioなどのエディタに統合され、タイピング中にリアルタイムで補完を行うエンドユーザー向けツール。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">業務システム開発における位置づけ</h2>
<p>フリーランスエンジニアにとって、Codex（およびそれを内包する最新API）は、「自作のコードジェネレータ」や「静的解析ツールの拡張」として利用価値があります。</p>
<p>例えば、DBのスキーマ定義（DDL）から、C#のEntity Framework Core用エンティティクラス群、リポジトリ層、さらには基本的なCRUD操作のAPIコントローラーまでを<strong>一括で自動生成するスクリプト</strong>を自作する際、裏側のエンジンとしてCodex系APIが活躍します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">各レベルの学習ロードマップ</h2>
<ul>
  <li><strong>初級編</strong>：Codexの得意・不得意の理解、基本的なコード生成プロンプトの書き方。</li>
  <li><strong>中級編</strong>：コンテキスト（周辺コード）の与え方、複数言語間の翻訳（VBAからC#への変換など）。</li>
  <li><strong>上級編</strong>：APIを利用したカスタムコードジェネレータの開発、社内コーディング規約を強制するファインチューニングやRAGの応用。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "beginner": {
        "title": "初級編",
        "class": "beginner",
        "toc": ["Codexへの指示の基本", "コメント駆動開発 (CDD)", "定型コードの生成", "SQLクエリの生成"],
        "body": """
<h2 class="section-heading" id="sec1">Codexへの指示の基本</h2>
<p>Codex（コード生成特化モデル）に対しては、自然言語での指示をソースコードの「コメント」として記述する手法が効果的です。モデルはコメントに続く最適なコードを予測して出力します。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">コメント駆動開発 (CDD)</h2>
<p>実現したい処理のステップを、詳細なコメントとして先に記述します。</p>
<pre><code>// C#
// 1. 指定されたディレクトリ内のすべてのCSVファイルを取得する
// 2. 各ファイルを読み込み、ヘッダー行をスキップする
// 3. 2列目の値（金額）を合計する
// 4. 合計値をコンソールに出力する
// 5. 例外発生時はエラーメッセージをログに出力する
public void CalculateTotalAmount(string directoryPath)
{
</code></pre>
<p>このように具体的な手順を列挙することで、Codexは意図通りの堅牢なコードを生成しやすくなります。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">定型コードの生成</h2>
<p>クラスのプロパティ定義や、単純なマッピング処理など、手作業では面倒な定型コードの生成はCodexの独壇場です。</p>
<pre><code>// 以下のSQLテーブル定義に対応するC#のEntity Framework Coreエンティティクラスを作成してください。
// CREATE TABLE [dbo].[T_Patient] (
//   [PatientId] INT IDENTITY(1,1) PRIMARY KEY,
//   [PatientCode] VARCHAR(20) NOT NULL,
//   [LastName] NVARCHAR(50) NOT NULL,
//   [FirstName] NVARCHAR(50) NOT NULL,
//   [BirthDate] DATE NOT NULL
// );
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">SQLクエリの生成</h2>
<p>テーブルスキーマを提示した上で、自然言語で抽出条件を指示すると、正確なSQL（T-SQLやPL/SQL）を生成します。</p>
<pre><code>-- テーブル: T_Orders (OrderId, PatientId, OrderDate, TotalAmount)
-- テーブル: T_Patient (PatientId, PatientCode, LastName, FirstName)
-- 指示: 2026年5月に注文があり、合計金額が50,000円を超える患者のPatientCodeと氏名を取得するクエリ。
-- 注文金額の降順でソートすること。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "intermediate": {
        "title": "中級編",
        "class": "intermediate",
        "toc": ["コンテキストの提供手法", "レガシーコードのモダン化", "テストコードの自動生成", "正規表現とパーサーの実装"],
        "body": """
<h2 class="section-heading" id="sec1">コンテキストの提供手法</h2>
<p>Codexから精度の高いコードを引き出すには、対象の関数だけでなく、それが依存するクラスやインターフェースの定義（コンテキスト）をプロンプトに含める必要があります。</p>
<p>例えば、特定のリポジトリインターフェースを実装するクラスを生成させる場合、インターフェースの定義を先頭に配置します。</p>
<pre><code>// 依存するインターフェース
public interface IPatientRepository {
    Task&lt;Patient?&gt; GetByIdAsync(int patientId);
    Task&lt;IEnumerable&lt;Patient&gt;&gt; GetActivePatientsAsync();
}

// 上記インターフェースを実装し、Dapperを使用してSQL Serverにアクセスする
// PatientRepositoryクラスを実装してください。
public class PatientRepository : IPatientRepository {
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">レガシーコードのモダン化</h2>
<p>VB6.0やVBAのコードをC#に変換する際、単なる直訳ではなく、最新の言語機能を活用したモダンなコードへのリファクタリングを指示します。</p>
<pre><code>以下のVB6.0のコードをC# (.NET 8) に変換してください。
変換時の要件：
- ADODBは使用せず、Entity Framework CoreまたはDapperを使用すること。
- On Error GoTo は使用せず、適切な try-catch ブロックに置き換えること。
- コレクションの操作にはLINQを使用すること。
- 変数名はcamelCaseに変更すること。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">テストコードの自動生成</h2>
<p>実装済みのメソッドを与え、それに対するユニットテスト（xUnit, NUnitなど）を生成させます。正常系だけでなく、エッジケースや異常系のテストも明示的に要求します。</p>
<pre><code>以下の CalculateDiscount メソッドに対する xUnit テストクラスを生成してください。
境界値（0円、マイナス金額）や、nullが渡された場合の異常系テストも含めてください。
Moqを使用して依存関係をモック化してください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">正規表現とパーサーの実装</h2>
<p>複雑な文字列処理やログファイルのパース処理の実装を依頼します。</p>
<pre><code>以下の形式のIISアクセスログから、IPアドレス、リクエスト日時、HTTPステータスコードを抽出するC#の正規表現と、それを用いてオブジェクトのリストに変換するメソッドを実装してください。
ログ形式: 2026-05-10 10:00:00 192.168.1.10 GET /api/patients - 200 ...
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "advanced": {
        "title": "上級編",
        "class": "advanced",
        "toc": ["カスタムコードジェネレータの開発", "AST（抽象構文木）との連携", "社内規約を強制するプロンプト設計", "自動コードレビューパイプラインの構築"],
        "body": """
<h2 class="section-heading" id="sec1">カスタムコードジェネレータの開発</h2>
<p>OpenAI API（Codex相当のモデル）を利用し、データベースのスキーマ情報からシステム全体のボイラープレートコードを自動生成するCLIツールを開発します。</p>
<ol>
  <li>SQL Serverのシステムカタログ（sys.tables, sys.columns等）からテーブル定義を抽出する。</li>
  <li>抽出した定義をプロンプトに埋め込み、「C#のEntityクラス」「リポジトリインターフェース」「リポジトリ実装」「APIコントローラー」の生成をAPIに要求する。</li>
  <li>返されたコードをパースし、適切なディレクトリ階層に `.cs` ファイルとして出力する。</li>
</ol>
<p>これにより、新規テーブル追加時の単純作業をゼロにすることができます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">AST（抽象構文木）との連携</h2>
<p>より高度なリファクタリングツールを作る場合、Roslyn（.NET Compiler Platform）を使用してC#コードをASTに変換し、特定のノード（例えば古い形式のメソッド呼び出し）だけを抽出し、その部分のモダン化をCodex APIに依頼します。文字列ベースの置換よりもはるかに安全で正確なコード変換が可能になります。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">社内規約を強制するプロンプト設計</h2>
<p>生成されるコードがプロジェクト固有のアーキテクチャや命名規約に確実に従うよう、システムプロンプト（System Prompt）に詳細なルールを定義します。</p>
<pre><code>あなたは[病院名]物流システムのシニアアーキテクトです。
コード生成ルール：
1. データベースアクセスは必ず提供された `IDbConnectionFactory` を通じて行うこと。
2. 日付の比較には必ず `DateTimeOffset.UtcNow` を使用すること。
3. トランザクションは `TransactionScope` を使用して管理すること。
4. 例外発生時は `AppLogger.LogError` で記録し、カスタム例外 `SystemAppException` でラップしてスローすること。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">自動コードレビューパイプラインの構築</h2>
<p>GitHub ActionsなどのCI/CDパイプラインにCodex APIを組み込みます。Pull Requestが作成された際、変更された差分（diff）をAPIに送信し、以下の観点で自動レビューを行わせます。</p>
<ul>
  <li>N+1問題が発生していないか（Entity Framework Coreの遅延読み込み等）</li>
  <li>SQLインジェクションの脆弱性がないか</li>
  <li>リソースの解放（Dispose処理）が適切に行われているか</li>
</ul>
<p>レビュー結果は自動的にPRのコメントとして投稿させ、人間のレビュアーの負担を大幅に軽減します。</p>
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
  <title>Codex {data["title"]} — AIツール使いこなし指南</title>
  <style>{template_css}</style>
</head>
<body>
  <header>
    <div class="breadcrumb">
      <a href="../index.html">← ツール一覧へ戻る</a>
    </div>
    <h1>Codex <span class="badge badge-{data["class"]}">{data["title"]}</span></h1>
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
    
    file_path = f"/home/ubuntu/ai-guide/codex/{level_id}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {file_path}")


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
        "toc": ["ChatGPTの基本アーキテクチャ", "業務システム開発における位置づけ", "モデルの選定基準 (2026年最新版)", "各レベルの学習ロードマップ"],
        "body": """
<h2 class="section-heading" id="sec1">ChatGPTの基本アーキテクチャ</h2>
<p>ChatGPTはOpenAIが提供する大規模言語モデル(LLM)のインターフェースです。2026年現在、GPT-4o、o3、o4-mini、GPT-5系列といった複数のモデルが提供されており、それぞれ得意分野が異なります。</p>
<p>内部的には、プロンプトとして入力されたテキストに対して、確率的に最も適切な次の単語（トークン）を予測し続ける仕組みです。そのため、「正解」を検索して返すのではなく、「文脈的に妥当な文字列」を生成しています。この特性を理解することが、幻覚（ハルシネーション）を防ぎ、業務で安全に活用するための第一歩となります。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">業務システム開発における位置づけ</h2>
<p>35年の業務システム開発経験を持つエンジニアにとって、ChatGPTは「コードスニペットの検索ツール」にとどまりません。その真価は<strong>「高度な壁打ち相手」</strong>および<strong>「レガシーコードの翻訳機」</strong>にあります。</p>
<p>VBAやVB6.0で書かれた数千行のレガシーコードをC#やVB.NETに移行する際、単なる構文変換ではなく、アーキテクチャの刷新（例：イベント駆動からMVVMへの移行、ADOからEntity Framework Coreへの移行）を伴う設計レベルの相談が可能です。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">モデルの選定基準 (2026年最新版)</h2>
<p>用途に応じて適切なモデルを選択することが、コストとパフォーマンスの最適化に直結します。</p>
<table>
  <tr>
    <th>モデル名</th>
    <th>特徴</th>
    <th>推奨ユースケース</th>
  </tr>
  <tr>
    <td><strong>o3 / o4-mini (推論モデル)</strong></td>
    <td>回答前に内部で深い推論（Chain of Thought）を行う。出力まで時間はかかるが論理的整合性が極めて高い。</td>
    <td>複雑なアルゴリズムの設計、難解なバグの解析、レガシーシステムの仕様リバースエンジニアリング</td>
  </tr>
  <tr>
    <td><strong>GPT-4o / GPT-5.5</strong></td>
    <td>高速かつマルチモーダル（画像・音声）に対応。推論能力も高いが、o3系列ほど深くは考えない。</td>
    <td>日常的なコーディング支援、APIドキュメントの要約、正規表現の生成、画像からのUI要件抽出</td>
  </tr>
</table>
<div class="callout tip">
  <strong>💡 Tip:</strong> 複雑なSQL（例えばOracleの階層問い合わせ `CONNECT BY` をSQL Serverの `CTE` に変換する等）を依頼する場合は、o3モデルを選択すると一発で正確なクエリが得られる確率が跳ね上がります。
</div>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">各レベルの学習ロードマップ</h2>
<ul>
  <li><strong>初級編</strong>：ChatGPTの基本的な特性を理解し、日常的なコーディングの疑問解決やエラー解析、簡単なコード変換（VBA → VB.NET）を正確に行わせるプロンプト技術を習得します。</li>
  <li><strong>中級編</strong>：要件定義やデータベース設計における「壁打ち」手法、長文の仕様書解析、セキュリティやパフォーマンスを考慮したコードレビューの自動化手法を学びます。</li>
  <li><strong>上級編</strong>：OpenAI APIを利用した業務システムへの組み込み、Function Callingを用いた自律的エージェントの構築、RAG（Retrieval-Augmented Generation）による社内ドキュメント検索システムの設計を解説します。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "beginner": {
        "title": "初級編",
        "class": "beginner",
        "toc": ["エンジニア向けプロンプトの基本構造", "レガシーコードの翻訳と解説", "エラー解析とトラブルシューティング", "正規表現と定型処理の生成"],
        "body": """
<h2 class="section-heading" id="sec1">エンジニア向けプロンプトの基本構造</h2>
<p>ChatGPTから正確で実用的な回答を引き出すには、前提条件を明確に定義することが不可欠です。特に、35年の経験を持つエンジニアであれば、初心者向けの冗長な解説は不要です。以下のようなフォーマットをテンプレート化しておくことを推奨します。</p>
<pre><code># 命令
あなたはシニアソフトウェアエンジニアです。以下の[要件]を満たすC#のコードを記述してください。

# 前提条件
- 対象フレームワーク: .NET 8
- データベース: SQL Server 2022
- ORM: Entity Framework Core
- 命名規約: 
  - ローカル変数: camelCase
  - プライベート変数: _camelCase
  - クラス、構造体、関数、メソッド: PascalCase
  - 定数: UPPER_SNAKE_CASE
  - DBフィールド: snake_case

# 制約事項
- 初心者向けの解説や前置きは一切不要です。コードのみを出力してください。
- エラーハンドリング（try-catch）を必ず含めること。
- SQLインジェクション対策としてパラメータ化クエリを使用すること。

# 要件
...
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">レガシーコードの翻訳と解説</h2>
<p>VB6.0やVBA、古いPL/SQLのコードを最新のC#やT-SQLに移行する際、ChatGPTは強力な翻訳機となります。ただし、単に「変換して」と指示するのではなく、<strong>「なぜそのような実装になっているか」の意図を汲み取らせる</strong>ことが重要です。</p>
<div class="callout warning">
  <strong>⚠️ Warning:</strong> レガシーコードには、当時のハードウェア制約や古いライブラリのバグを回避するための「ハック（Workaround）」が含まれていることが多々あります。ChatGPTに翻訳させる際は、「このVBAコードをC#に変換してください。その際、現代のC#のベストプラクティス（LINQの活用など）を用いてリファクタリングし、不要なハックがあれば除外して理由を説明してください」と指示します。
</div>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">エラー解析とトラブルシューティング</h2>
<p>例外のスタックトレースや、SQL Serverの実行計画エラーを解析させる際は、エラーメッセージだけでなく、関連するコードブロックやテーブルのスキーマ定義（CREATE TABLE文）を一緒に渡すことで、回答の精度が劇的に向上します。</p>
<p><strong>悪い例：</strong>「C#でNullReferenceExceptionが出ます。なぜですか？」</p>
<p><strong>良い例：</strong>「以下のC#メソッド実行時にNullReferenceExceptionが発生します。スタックトレースと関連するクラス定義は以下の通りです。原因箇所を特定し、null安全なコード（C# 8.0以降のnull許容参照型を考慮）に修正してください。」</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">正規表現と定型処理の生成</h2>
<p>複雑な正規表現の構築や、CSVファイルのパース、特定のフォーマットの日付変換など、頭を使うが定型的な処理はChatGPTに任せるべき代表例です。</p>
<p>プロンプト例：</p>
<pre><code>C#で使用する正規表現を生成してください。
要件：
1. 日本の固定電話番号（例: 03-1234-5678, 045-123-4567）にマッチすること。
2. ハイフンは必須。
3. マッチした結果から、市外局番、市内局番、加入者番号を名前付きキャプチャグループ（AreaCode, CityCode, SubscriberNumber）で抽出できること。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "intermediate": {
        "title": "中級編",
        "class": "intermediate",
        "toc": ["システム設計の壁打ちとレビュー", "プロンプトエンジニアリングの高度な技法", "データベース設計とSQL最適化", "セキュリティ脆弱性の発見"],
        "body": """
<h2 class="section-heading" id="sec1">システム設計の壁打ちとレビュー</h2>
<p>中規模以上の業務システム（病院物流システムなど）を設計する際、自身の設計案の妥当性をChatGPTに検証させます。人間相手では遠慮が生じるような根本的な設計の欠陥も、AIであれば客観的かつ冷酷に指摘してくれます。</p>
<p><strong>壁打ちプロンプトの例：</strong></p>
<pre><code>以下の病院物流システムの在庫管理モジュールのアーキテクチャ案をレビューしてください。
私は以下の理由からこの設計が最適だと考えていますが、私が「見落としている盲点」や「将来的に技術的負債となるリスク（機会費用を含む）」を、遠慮なく客観的かつ論理的に指摘してください。

【アーキテクチャ案】
...
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">プロンプトエンジニアリングの高度な技法</h2>
<p>より複雑な推論を要求する場合、以下の手法を組み合わせます。</p>
<ul>
  <li><strong>Few-shot Prompting</strong>：期待する入力と出力のペアをいくつか提示し、出力のフォーマットや思考プロセスを強制します。</li>
  <li><strong>Chain-of-Thought (CoT)</strong>：「ステップバイステップで考えてください（Let's think step by step）」と指示することで、結論に至るまでの論理展開を可視化させ、計算ミスや論理の飛躍を防ぎます。（※o3モデルなどの推論モデルでは内部的に自動で行われます）</li>
  <li><strong>Role-Playing & Perspective</strong>：「DBAの視点から」「セキュリティエンジニアの視点から」と複数のペルソナを指定し、多角的なレビューを行わせます。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">データベース設計とSQL最適化</h2>
<p>OracleからSQL Serverへの移行など、RDBMS間の非互換性を埋める作業においてChatGPTは極めて有用です。単なる構文変換だけでなく、実行計画（Execution Plan）を考慮した最適化を依頼します。</p>
<p><strong>SQL最適化の依頼例：</strong></p>
<pre><code>以下のSQL Server (T-SQL) クエリは実行に5秒かかっています。
対象テーブルの行数は約1000万件です。
インデックスは [CREATE INDEX文] の通り設定されています。

このクエリのパフォーマンスボトルネックを推測し、
1. クエリの書き換え案（Window関数の活用など）
2. 追加・修正すべきインデックスの提案
を論理的な根拠とともに提示してください。
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">セキュリティ脆弱性の発見</h2>
<p>実装したコードブロックを貼り付け、「このC#コードに存在する可能性のあるセキュリティ脆弱性（OWASP Top 10に基づく）を指摘し、修正案を提示してください」と指示することで、静的解析ツールに近いコードレビューを即座に実施できます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
    },
    "advanced": {
        "title": "上級編",
        "class": "advanced",
        "toc": ["OpenAI APIの業務システムへの統合", "Function Callingによるエージェント化", "RAGによる社内ナレッジベース構築", "構造化出力 (Structured Outputs) の活用"],
        "body": """
<h2 class="section-heading" id="sec1">OpenAI APIの業務システムへの統合</h2>
<p>ChatGPTの真の価値は、WebブラウザのUIを離れ、APIを通じて自作の業務システムに組み込んだ時に発揮されます。C# (.NET) からOpenAI APIを呼び出す場合、公式の `OpenAI` NuGetパッケージ、またはAzure OpenAI Serviceを利用する場合は `Azure.AI.OpenAI` を使用します。</p>
<pre><code>// C# 12 / .NET 8 での OpenAI API 呼び出し例
using OpenAI.Chat;

var client = new ChatClient("gpt-4o", Environment.GetEnvironmentVariable("OPENAI_API_KEY"));
var messages = new List&lt;ChatMessage&gt;
{
    new SystemChatMessage("あなたは病院物流システムの専門家です。"),
    new UserChatMessage("消費期限切れ間近の医療材料リストから、優先的に配置転換すべき品目を抽出してください。")
};

var response = await client.CompleteChatAsync(messages);
Console.WriteLine(response.Value.Content[0].Text);
</code></pre>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">Function Callingによるエージェント化</h2>
<p>Function Calling（関数呼び出し）機能を使用すると、LLMに「どの関数を、どのような引数で実行すべきか」を決定させることができます。これにより、LLMが自律的に社内データベースを検索したり、外部APIを叩いたりするエージェントを構築できます。</p>
<p>例えば、「A病院の先月の注射器の消費量は？」という自然言語の質問に対し、LLMが `GetMonthlyConsumption(hospitalId: "A", itemCategory: "Syringe", month: "2026-05")` という関数を実行すべきと判断し、システム側でそのSQLを実行、結果をLLMに戻して最終的な自然言語の回答を生成させます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">RAGによる社内ナレッジベース構築</h2>
<p>RAG (Retrieval-Augmented Generation) は、LLMが学習していない社内固有のデータ（過去の仕様書、障害報告書、マニュアルなど）を回答に組み込むためのアーキテクチャです。</p>
<ol>
  <li>社内ドキュメントをテキスト化し、Embedding APIを用いてベクトル（数値の配列）に変換する。</li>
  <li>ベクトルデータベース（Pinecone, Qdrant, または SQL Server 2022のベクトル検索機能など）に保存する。</li>
  <li>ユーザーの質問もベクトル化し、類似度の高いドキュメントをデータベースから検索（Retrieval）する。</li>
  <li>検索されたドキュメントをコンテキストとしてプロンプトに埋め込み、LLMに回答を生成（Generation）させる。</li>
</ol>
<p>これにより、幻覚（ハルシネーション）を抑えつつ、社内事情に精通したAIアシスタントを構築できます。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec4">構造化出力 (Structured Outputs) の活用</h2>
<p>業務システムでLLMの出力をプログラムで処理する場合、出力が厳密なJSONフォーマットであることが求められます。OpenAI APIの <code>response_format</code> で JSON Schema を定義することで、100%スキーマに合致したJSON出力を保証させることができます。</p>
<p>これにより、非構造化データ（長文のテキストやPDF）から、システムに取り込み可能な構造化データ（C#のクラスにデシリアライズ可能なJSON）への変換処理を、極めて高い信頼性で自動化できます。</p>
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
  <title>ChatGPT {data["title"]} — AIツール使いこなし指南</title>
  <style>{template_css}</style>
</head>
<body>
  <header>
    <div class="breadcrumb">
      <a href="../index.html">← ツール一覧へ戻る</a>
    </div>
    <h1>ChatGPT <span class="badge badge-{data["class"]}">{data["title"]}</span></h1>
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
    
    file_path = f"/home/ubuntu/ai-guide/chatgpt/{level_id}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {file_path}")


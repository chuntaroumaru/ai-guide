import os
import datetime

tools = {
    "chatgpt": "ChatGPT",
    "codex": "Codex",
    "copilot": "GitHub Copilot",
    "claude": "Claude",
    "manus": "Manus",
    "gemini": "Gemini",
    "openclaw": "OpenClaw"
}

levels = {
    "index": ("概要", "overview"),
    "beginner": ("初級編", "beginner"),
    "intermediate": ("中級編", "intermediate"),
    "advanced": ("上級編", "advanced")
}

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

today_str = "2026年06月08日"

content_dict = {
    "chatgpt": {
        "index": {
            "toc": ["ChatGPTの概要", "対象読者と活用方針", "各レベルの案内"],
            "body": """
<h2 class="section-heading" id="sec1">ChatGPTの概要</h2>
<p>OpenAIが提供する汎用対話型AI。GPT-4o、o3、GPT-5系列のモデルを利用可能。推論能力やコーディング支援に優れ、業務システム開発における要件定義の壁打ち、コードのレビュー、SQLの最適化など多岐にわたる用途で活用できる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">対象読者と活用方針</h2>
<p>VBA/VB.NET/C#/SQL Server/Oracleに精通したシステムエンジニアにとって、ChatGPTは単なる「検索の代替」ではなく、「ペアプログラマー」や「設計の壁打ち相手」として機能する。特に、習得中のC#やSQL ServerのT-SQLにおけるベストプラクティスの学習や、レガシーコード（VB6.0/VBA）からモダンな言語への移行支援において強力な武器となる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">各レベルの案内</h2>
<ul>
  <li><strong>初級編</strong>：基本的な使い方、プロンプトの書き方、典型的なユースケース（コード解説、エラー解析）</li>
  <li><strong>中級編</strong>：効果的なプロンプト設計、システム設計時の壁打ち、他ツールとの使い分け</li>
  <li><strong>上級編</strong>：API連携・自動化、エージェント活用、業務システム開発への応用（データ変換スクリプトの自動生成など）</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "beginner": {
            "toc": ["基本的な使い方", "プロンプトの書き方", "典型的なユースケース"],
            "body": """
<h2 class="section-heading" id="sec1">基本的な使い方</h2>
<p>Webインターフェースを通じて自然言語で質問や指示を入力する。モデルの選択（GPT-4oなど）によって応答の速度や推論能力が異なるため、用途に応じて適切なモデルを選択する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">プロンプトの書き方</h2>
<p>明確な役割を与え、前提条件や制約事項を具体的に記述することが重要。例えば、「あなたは35年の経験を持つシステムエンジニアです。以下のVBAコードをC#に変換してください。命名規約はローカル変数:camelCase、メソッド:PascalCaseに従うこと。」のように指示する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">典型的なユースケース</h2>
<ul>
  <li><strong>コード解説</strong>：難解なPL/SQLプロシージャやVB.NETのコードを貼り付け、処理内容の解説を求める。</li>
  <li><strong>エラー解析</strong>：エラーメッセージと関連するコードを提示し、原因と解決策を提案させる。</li>
  <li><strong>正規表現の生成</strong>：要件（例：「郵便番号の形式に一致する正規表現」）を伝え、正規表現を生成させる。</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "intermediate": {
            "toc": ["効果的なプロンプト設計", "システム設計時の壁打ち", "他ツールとの使い分け"],
            "body": """
<h2 class="section-heading" id="sec1">効果的なプロンプト設計</h2>
<p>Few-shot prompting（いくつかの例を提示する手法）やChain-of-Thought（推論の過程を段階的に記述させる手法）を活用し、より複雑な論理展開や高品質な出力を引き出す。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">システム設計時の壁打ち</h2>
<p>要件定義やデータベース設計の段階で、想定されるテーブル構造や業務フローを提示し、不足している観点や潜在的なリスク（例：パフォーマンスの懸念、正規化の不足）を指摘させる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">他ツールとの使い分け</h2>
<p>IDEに統合されたGitHub Copilotはコーディング中のリアルタイムな補完に優れる一方、ChatGPTはアーキテクチャの検討やアルゴリズムの全体的な設計など、より広範なコンテキストを必要とするタスクに適している。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "advanced": {
            "toc": ["API連携・自動化", "エージェント活用", "業務システム開発への応用"],
            "body": """
<h2 class="section-heading" id="sec1">API連携・自動化</h2>
<p>OpenAI APIを利用し、自作の業務システムやツールにChatGPTの機能を組み込む。例えば、ログファイルの自動解析ツールや、ユーザーからの問い合わせに対する一次回答システムなどを構築する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">エージェント活用</h2>
<p>Function Calling機能を利用し、ChatGPTが外部APIやデータベース（OracleやSQL Serverなど）と連携して自律的にタスクを実行するエージェントを構築する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">業務システム開発への応用</h2>
<p>大量のレガシーコード（VB6.0等）を解析し、仕様書を自動生成するスクリプトの作成や、テストデータ生成ツールの構築など、開発プロセス全体の効率化に活用する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        }
    },
    "codex": {
        "index": {
            "toc": ["Codexの概要", "対象読者と活用方針", "各レベルの案内"],
            "body": """
<h2 class="section-heading" id="sec1">Codexの概要</h2>
<p>OpenAIが提供するターミナル上で動作するコーディングエージェント。ローカルのコードベースを直接読み取り、変更し、実行する能力を持つ。自律的なコード操作が可能で、コマンドラインインターフェース（CLI）を通じて対話する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">対象読者と活用方針</h2>
<p>ターミナル操作に抵抗がなく、ローカル環境でのスクリプト実行やファイルの一括処理を自動化したいエンジニア向け。VBAやVB.NETのプロジェクトにおいて、定型的なリファクタリングやファイル名の変更などを一括で行う際に有用。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">各レベルの案内</h2>
<ul>
  <li><strong>初級編</strong>：インストールと基本的な使い方、ターミナルでの操作方法</li>
  <li><strong>中級編</strong>：ローカルコードベースの操作、一括リファクタリング</li>
  <li><strong>上級編</strong>：自律的なタスク実行、CI/CDパイプラインへの組み込み</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "beginner": {
            "toc": ["インストールと基本的な使い方", "ターミナルでの操作方法"],
            "body": """
<h2 class="section-heading" id="sec1">インストールと基本的な使い方</h2>
<p>npmや特定のパッケージマネージャーを通じてCodex CLIをインストールする。APIキーを設定し、ターミナルからコマンドを実行して起動する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">ターミナルでの操作方法</h2>
<p>自然言語で「現在のディレクトリ内の.vbファイルをすべて検索し、特定の関数名を含むものをリストアップして」といった指示を与える。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "intermediate": {
            "toc": ["ローカルコードベースの操作", "一括リファクタリング"],
            "body": """
<h2 class="section-heading" id="sec1">ローカルコードベースの操作</h2>
<p>プロジェクト全体のコンテキストを読み込ませ、特定の要件に基づいたコードの追加や修正を依頼する。ファイル間の依存関係を考慮した変更が可能。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">一括リファクタリング</h2>
<p>古い命名規約（例：ハンガリアン記法）から新しい命名規約（例：camelCaseやPascalCase）への一括変換スクリプトを作成・実行させる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "advanced": {
            "toc": ["自律的なタスク実行", "CI/CDパイプラインへの組み込み"],
            "body": """
<h2 class="section-heading" id="sec1">自律的なタスク実行</h2>
<p>テストの失敗を検知し、その原因を分析して修正コードを提案・適用するといった一連のプロセスを自律的に実行させる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">CI/CDパイプラインへの組み込み</h2>
<p>GitHub ActionsなどのCI/CD環境でCodexを動作させ、プルリクエスト作成時に自動でコードレビューや軽微な修正を行わせる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        }
    },
    "copilot": {
        "index": {
            "toc": ["GitHub Copilotの概要", "対象読者と活用方針", "各レベルの案内"],
            "body": """
<h2 class="section-heading" id="sec1">GitHub Copilotの概要</h2>
<p>GitHubとMicrosoftが提供するAIペアプログラマー。VS CodeやVisual StudioなどのIDEに統合され、コードを記述する際に文脈に応じた補完や提案を行う。チャット機能やエージェントモードも搭載。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">対象読者と活用方針</h2>
<p>日常的にIDE（特にVisual StudioやVS Code）を使用してC#やVB.NETのコーディングを行うエンジニアにとって必須のツール。定型コードの記述時間を大幅に削減し、ロジックの構築に集中できる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">各レベルの案内</h2>
<ul>
  <li><strong>初級編</strong>：基本的なコード補完、コメントからのコード生成</li>
  <li><strong>中級編</strong>：Copilot Chatの活用、テストコードの自動生成</li>
  <li><strong>上級編</strong>：エージェントモードの活用、ワークスペース全体の理解と操作</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "beginner": {
            "toc": ["基本的なコード補完", "コメントからのコード生成"],
            "body": """
<h2 class="section-heading" id="sec1">基本的なコード補完</h2>
<p>コードを入力し始めると、変数名やメソッド名、さらには関数全体のロジックを推測してグレーのテキストで提案が表示される。Tabキーで提案を受け入れる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">コメントからのコード生成</h2>
<p>実現したい処理をコメント（例：`// データベースから指定されたIDのユーザー情報を取得する`）として記述すると、それに続くコードが自動的に提案される。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "intermediate": {
            "toc": ["Copilot Chatの活用", "テストコードの自動生成"],
            "body": """
<h2 class="section-heading" id="sec1">Copilot Chatの活用</h2>
<p>IDE内のチャットウィンドウで、選択したコードブロックの解説を求めたり、リファクタリングの提案を受けたりする。`/explain`や`/fix`などのスラッシュコマンドを活用する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">テストコードの自動生成</h2>
<p>実装したメソッドに対して、正常系および異常系の単体テスト（ユニットテスト）のコードを自動生成させる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "advanced": {
            "toc": ["エージェントモードの活用", "ワークスペース全体の理解と操作"],
            "body": """
<h2 class="section-heading" id="sec1">エージェントモードの活用</h2>
<p>Copilot Agent Modeを使用し、複数ファイルにまたがる複雑なタスク（例：「データベース接続のライブラリをAからBに移行する」）を自律的に実行させる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">ワークスペース全体の理解と操作</h2>
<p>`@workspace`を利用して、プロジェクト全体の構造や依存関係に基づいた質問やコード生成を行う。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        }
    },
    "claude": {
        "index": {
            "toc": ["Claudeの概要", "対象読者と活用方針", "各レベルの案内"],
            "body": """
<h2 class="section-heading" id="sec1">Claudeの概要</h2>
<p>Anthropicが提供する対話型AI。長大なコンテキストウィンドウ（大量のテキストを一度に処理できる能力）を持ち、コードの理解や論理的な推論に優れている。安全性を重視した設計が特徴。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">対象読者と活用方針</h2>
<p>長大な仕様書やログファイル、レガシーシステムのソースコード群を一括で解析させたい場合に非常に有効。表面的な回答ではなく、深い論理的考察を求めるエンジニアに適している。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">各レベルの案内</h2>
<ul>
  <li><strong>初級編</strong>：基本的な使い方、長文ドキュメントの要約</li>
  <li><strong>中級編</strong>：コードベースの解析、複雑な論理的推論</li>
  <li><strong>上級編</strong>：API連携、システム移行の全体計画立案</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "beginner": {
            "toc": ["基本的な使い方", "長文ドキュメントの要約"],
            "body": """
<h2 class="section-heading" id="sec1">基本的な使い方</h2>
<p>Webインターフェースで自然言語による対話を行う。文章が自然で、ユーザーの意図を汲み取った丁寧な回答が得られる傾向がある。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">長文ドキュメントの要約</h2>
<p>数十ページに及ぶPDFの仕様書やマニュアルをアップロードし、要点の抽出や特定の条件に合致する情報の検索を行わせる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "intermediate": {
            "toc": ["コードベースの解析", "複雑な論理的推論"],
            "body": """
<h2 class="section-heading" id="sec1">コードベースの解析</h2>
<p>複数のソースコードファイル（例：VB.NETのクラスファイルと関連するSQLスクリプト）を同時に読み込ませ、システム間の依存関係やデータフローを可視化・解説させる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">複雑な論理的推論</h2>
<p>業務要件の矛盾点や、エッジケース（例外的な状況）におけるシステムの挙動について議論し、設計の穴を塞ぐ。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "advanced": {
            "toc": ["API連携", "システム移行の全体計画立案"],
            "body": """
<h2 class="section-heading" id="sec1">API連携</h2>
<p>Anthropic APIを使用して、社内ドキュメント検索システムや、高度な推論を必要とするデータ処理パイプラインを構築する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">システム移行の全体計画立案</h2>
<p>オンプレミスからクラウドへの移行や、VB6.0からC#へのマイグレーションなど、大規模プロジェクトにおけるフェーズ分け、リスク評価、必要なリソースの算出を行わせる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        }
    },
    "manus": {
        "index": {
            "toc": ["Manusの概要", "対象読者と活用方針", "各レベルの案内"],
            "body": """
<h2 class="section-heading" id="sec1">Manusの概要</h2>
<p>Manusチームが開発した汎用AIエージェント。サンドボックス環境内で、ブラウザ操作、シェルコマンドの実行、ファイル操作などを自律的に行い、ユーザーが与えた目標を達成する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">対象読者と活用方針</h2>
<p>単なるテキスト生成を超えて、「実際の作業」をAIに代行させたいエンジニア向け。Webからの情報収集や、特定の環境構築、データのスクレイピングと加工などを自動化する際に強力なツールとなる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">各レベルの案内</h2>
<ul>
  <li><strong>初級編</strong>：基本的なタスク依頼、ブラウザ操作の自動化</li>
  <li><strong>中級編</strong>：ファイル操作とデータ処理、スクリプトの作成と実行</li>
  <li><strong>上級編</strong>：スキル拡張機構の活用、複雑な多段階タスクの設計</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "beginner": {
            "toc": ["基本的なタスク依頼", "ブラウザ操作の自動化"],
            "body": """
<h2 class="section-heading" id="sec1">基本的なタスク依頼</h2>
<p>「特定のトピックについてWebで調査し、レポートをマークダウン形式でまとめて」といった、明確なゴールを持つタスクを依頼する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">ブラウザ操作の自動化</h2>
<p>指定したWebサイトにアクセスし、必要な情報を抽出したり、フォームへの入力を行わせたりする。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "intermediate": {
            "toc": ["ファイル操作とデータ処理", "スクリプトの作成と実行"],
            "body": """
<h2 class="section-heading" id="sec1">ファイル操作とデータ処理</h2>
<p>CSVやExcelファイルを読み込ませ、データのクレンジング、集計、グラフ化などの一連の処理を行わせる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">スクリプトの作成と実行</h2>
<p>Pythonやシェルスクリプトを記述させ、それをサンドボックス環境内で実行して結果を得る。エラーが発生した場合は自律的に修正を試みる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "advanced": {
            "toc": ["スキル拡張機構の活用", "複雑な多段階タスクの設計"],
            "body": """
<h2 class="section-heading" id="sec1">スキル拡張機構の活用</h2>
<p>特定の業務フローや外部ツールとの連携方法を定義した「スキル」を作成し、Manusの能力をカスタマイズ・拡張する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">複雑な多段階タスクの設計</h2>
<p>「Webから最新の技術動向をスクレイピングし、データベースに格納し、要約レポートを生成してメールで送信する」といった、複数のツールやステップを組み合わせたワークフローを設計・実行させる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        }
    },
    "gemini": {
        "index": {
            "toc": ["Geminiの概要", "対象読者と活用方針", "各レベルの案内"],
            "body": """
<h2 class="section-heading" id="sec1">Geminiの概要</h2>
<p>Google DeepMindが提供するマルチモーダルAI。テキスト、画像、音声、動画をシームレスに理解し処理できる。特に長大なコンテキストウィンドウ（100万トークン超）を持つモデルが強力。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">対象読者と活用方針</h2>
<p>Google Workspace（ドキュメント、スプレッドシート、ドライブ等）を頻繁に利用するユーザーや、画像や動画を含む資料（例：画面キャプチャ付きの操作マニュアル）を解析・作成したいエンジニアに最適。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">各レベルの案内</h2>
<ul>
  <li><strong>初級編</strong>：基本的な使い方、マルチモーダル機能の活用</li>
  <li><strong>中級編</strong>：Google Workspace連携、超長文コンテキストの処理</li>
  <li><strong>上級編</strong>：Gemini APIの活用、カスタムAIアプリケーションの開発</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "beginner": {
            "toc": ["基本的な使い方", "マルチモーダル機能の活用"],
            "body": """
<h2 class="section-heading" id="sec1">基本的な使い方</h2>
<p>テキストでの対話に加え、画像やドキュメントをアップロードして質問する。レスポンスが高速である点が特徴。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">マルチモーダル機能の活用</h2>
<p>エラー画面のスクリーンショットや、手書きのシステム構成図の画像をアップロードし、その内容の解説やテキスト化、コード化を依頼する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "intermediate": {
            "toc": ["Google Workspace連携", "超長文コンテキストの処理"],
            "body": """
<h2 class="section-heading" id="sec1">Google Workspace連携</h2>
<p>Googleドライブ内の特定のドキュメントやスプレッドシートの内容を参照して回答させたり、Gmailのメールを要約させたりする。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">超長文コンテキストの処理</h2>
<p>プロジェクト全体のソースコード群や、数千ページに及ぶログファイルを一度に読み込ませ、特定のエラーパターンやボトルネックを特定させる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "advanced": {
            "toc": ["Gemini APIの活用", "カスタムAIアプリケーションの開発"],
            "body": """
<h2 class="section-heading" id="sec1">Gemini APIの活用</h2>
<p>Gemini APIを使用して、自社システムに画像認識機能や高度な自然言語処理機能を組み込む。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">カスタムAIアプリケーションの開発</h2>
<p>Function Callingや構造化出力（JSON形式での出力）を活用し、業務システムと連携して動作する堅牢なAIアプリケーションを開発する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        }
    },
    "openclaw": {
        "index": {
            "toc": ["OpenClawの概要", "対象読者と活用方針", "各レベルの案内"],
            "body": """
<h2 class="section-heading" id="sec1">OpenClawの概要</h2>
<p>オープンソースのローカルAIエージェントフレームワーク。WhatsAppやTelegramなどのメッセージングアプリをインターフェースとして、AIモデル（ローカルまたはクラウド）と通信し、様々な自動化タスクを実行する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">対象読者と活用方針</h2>
<p>プライバシーを重視し、自前のサーバーやローカル環境でAIエージェントを稼働させたいエンジニア向け。日常的なコミュニケーションツールからサーバーの監視や定型業務の実行を指示したい場合に適している。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec3">各レベルの案内</h2>
<ul>
  <li><strong>初級編</strong>：環境構築と基本設定、メッセージングアプリとの連携</li>
  <li><strong>中級編</strong>：ローカルLLMの利用、スケジュール実行とWebスクレイピング</li>
  <li><strong>上級編</strong>：カスタムスキルの開発、業務システムとのセキュアな連携</li>
</ul>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "beginner": {
            "toc": ["環境構築と基本設定", "メッセージングアプリとの連携"],
            "body": """
<h2 class="section-heading" id="sec1">環境構築と基本設定</h2>
<p>Node.js環境でのインストール、ゲートウェイの設定、使用するAIモデル（OpenAI APIなど）の設定を行う。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">メッセージングアプリとの連携</h2>
<p>TelegramやWhatsAppなどのBotトークンを設定し、スマートフォンからOpenClawエージェントと対話できる環境を構築する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "intermediate": {
            "toc": ["ローカルLLMの利用", "スケジュール実行とWebスクレイピング"],
            "body": """
<h2 class="section-heading" id="sec1">ローカルLLMの利用</h2>
<p>Ollamaなどを利用してローカル環境で動作するLLMをOpenClawのバックエンドとして設定し、完全にオフライン（外部APIに依存しない）で動作するエージェントを構築する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">スケジュール実行とWebスクレイピング</h2>
<p>cronライクな設定を利用して定期的にタスク（例：毎朝特定のWebサイトをスクレイピングしてニュースを要約し、Telegramに送信する）を実行させる。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        },
        "advanced": {
            "toc": ["カスタムスキルの開発", "業務システムとのセキュアな連携"],
            "body": """
<h2 class="section-heading" id="sec1">カスタムスキルの開発</h2>
<p>JavaScript/TypeScriptを用いて独自のツール（スキル）を開発し、OpenClawの機能を拡張する。例えば、社内データベースにクエリを発行するツールなど。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>

<h2 class="section-heading" id="sec2">業務システムとのセキュアな連携</h2>
<p>VPNやプライベートネットワーク内でOpenClawを稼働させ、外部に公開できない業務システム（Oracle DBや社内ファイルサーバー）の操作を、認証されたメッセージングアカウントから安全に行う仕組みを構築する。</p>
<a href="#toc" class="back-to-toc">▲ 目次へ戻る</a>
"""
        }
    }
}

def generate_html(tool_id, tool_name, level_id, level_name, level_class):
    content = content_dict[tool_id][level_id]
    
    toc_html = ""
    for i, item in enumerate(content["toc"]):
        toc_html += f'<li><a href="#sec{i+1}">{item}</a></li>\n'
        
    level_nav_html = ""
    for l_id, (l_name, l_class) in levels.items():
        if l_id == level_id:
            level_nav_html += f'<a href="{l_id}.html" class="btn-{l_class}" style="box-shadow: 0 0 0 2px var(--text);">{l_name}</a>\n'
        else:
            level_nav_html += f'<a href="{l_id}.html" class="btn-{l_class}">{l_name}</a>\n'
            
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{tool_name} {level_name} — AIツール使いこなし指南</title>
  <style>{template_css}</style>
</head>
<body>
  <header>
    <div class="breadcrumb">
      <a href="../index.html">← ツール一覧へ戻る</a>
    </div>
    <h1>{tool_name} <span class="badge badge-{level_class}">{level_name}</span></h1>
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

    {content["body"]}
  </main>

  <footer>
    <p><a href="../index.html">← ツール一覧へ戻る</a></p>
    <p style="margin-top:8px;">最終更新：{today_str}</p>
  </footer>
</body>
</html>"""
    
    file_path = f"/home/ubuntu/ai-guide/{tool_id}/{level_id}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {file_path}")

for tool_id, tool_name in tools.items():
    for level_id, (level_name, level_class) in levels.items():
        generate_html(tool_id, tool_name, level_id, level_name, level_class)

print("All pages generated successfully.")

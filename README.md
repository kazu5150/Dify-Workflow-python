# Dify Workflow Runner

このプロジェクトは、ローカル環境にDockerでインストールしたDifyにリクエストを送信し、その応答を処理するPythonスクリプトです。
この例では、自分のPCにDifyをインストールし、ワークフローを作成しています。


![Difyスクリーンショット](Dify-workflow.png "Dify Workflow Runnerのスクリーンショット")


## 概要

このスクリプトは以下の機能を提供します：

1. Dify APIにワークフロー実行リクエストを送信
2. ストリーミングレスポンスを受信して処理
3. ワークフローの実行情報と生成されたコンテンツ（詩）を整形して表示

## 前提条件

- Python 3.6以上
- Docker
- ローカル環境にインストールされたDify

## セットアップ

1. このリポジトリをクローンします：

   ```
   git clone https://github.com/yourusername/dify-workflow-runner.git
   cd dify-workflow-runner
   ```

2. 必要なPythonパッケージをインストールします：

   ```
   pip install -r requirements.txt
   ```

   これにより、`requests`と`python-dotenv`を含む必要なすべての依存関係がインストールされます。

3. `.env`ファイルを作成し、必要な環境変数を設定します：

   ```
   API_URL=http://localhost/v1/workflows/run
   API_KEY=your_api_key_here
   ```

   注意: `API_KEY`は実際のDify APIキーに置き換えてください。

## 使用方法

スクリプトを実行するには、以下のコマンドを使用します：

```
python dify_workflow_runner.py
```

スクリプトは、Dify APIにリクエストを送信し、レスポンスを処理して結果を表示します。

## 出力

スクリプトは以下の情報を出力します：

1. ワークフローの実行情報
   - ワークフロー実行ID
   - タスクID
   - ステータス
   - 合計トークン数
   - 合計ステップ数
   - 作成者ID
   - ユーザー
   - 作成時刻
   - 終了時刻
   - 実行時間

2. 生成されたコンテンツ（詩）

## 注意事項

- このスクリプトは、ローカル環境で動作するDifyを対象としています。他の環境で使用する場合は、`API_URL`を適切に変更してください。
- APIキーは機密情報です。`.env`ファイルをGitリポジトリにコミットしないよう注意してください。
- 依存関係は`requirements.txt`ファイルで管理されています。新しい依存関係を追加する場合は、このファイルを更新してください。

## 依存関係の更新

プロジェクトの依存関係を更新する場合は、以下の手順に従ってください：

1. `requirements.txt`ファイルを編集し、必要な変更を加えます。
2. 以下のコマンドを実行して、依存関係を更新します：

   ```
   pip install -r requirements.txt --upgrade
   ```

## ライセンス

[MITライセンス](LICENSE)

## 貢献

プルリクエストは歓迎します。大きな変更を加える場合は、まずissueを開いて変更内容を議論してください。

## サポート

問題や質問がある場合は、GitHubのissueを開いてください。
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()


def unix_to_datetime(unix_time):
    return datetime.fromtimestamp(unix_time).strftime('%Y年%m月%d日 %H:%M:%S')


# 環境変数からURLとAPIキーを取得
url = os.getenv('API_URL')
api_key = os.getenv('API_KEY')

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}
data = {
    "inputs": {
        "query": "Hear I go again!!"},
    "response_mode": "streaming",
    "user": "abc-123"
}

response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)

if response.status_code == 200:
    for line in response.iter_lines():
        if line:
            line = line.decode('utf-8')
            if line.startswith('data: '):
                event_data = json.loads(line[6:])
                if event_data['event'] == 'workflow_finished':
                    workflow_data = event_data['data']

                    print("1. ワークフローの実行情報:")
                    print(f"   - ワークフロー実行ID: {workflow_data['id']}")
                    print(f"   - タスクID: {event_data['task_id']}")
                    print(f"   - ステータス: {workflow_data['status']}")
                    print(f"   - 合計トークン数: {workflow_data['total_tokens']}")
                    print(f"   - 合計ステップ数: {workflow_data['total_steps']}")
                    print(f"   - 作成者ID: {workflow_data['created_by']['id']}")
                    print(f"   - ユーザー: {workflow_data['created_by']['user']}")
                    print(f"   - 作成時刻: {unix_to_datetime(workflow_data['created_at'])}")
                    print(f"   - 終了時刻: {unix_to_datetime(workflow_data['finished_at'])}")
                    print(f"   - 実行時間: 約{workflow_data['elapsed_time']:.2f}秒")
                    print("\n2. 生成されたコンテンツ（詩）:")
                    print(workflow_data['outputs']['response'])
else:
    print(f"エラー: ステータスコード {response.status_code}")
    print(response.text)

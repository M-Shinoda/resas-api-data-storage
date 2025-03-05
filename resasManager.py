from dotenv import load_dotenv, set_key
import requests
import json
from datetime import datetime, timezone, timedelta
import time
import os

api_key = "b5lYwOpEwxY4eZSczl77AL0mn5PxFhQjWfKlSdKi"
jst = timezone(timedelta(hours=9))


def mkdir_if_not_exists(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)


def update_count_env():
    env_file = ".env"
    load_dotenv(env_file, override=True)
    current_date_str = datetime.now(jst).strftime("%Y-%m-%d")
    count = os.getenv(current_date_str, "0")
    set_key(env_file, current_date_str, str(int(count) + 1))
    return load_dotenv(env_file, override=True)


def api_request(endpoint: str, params: dict) -> requests.Response:
    try:
        res = requests.get(
            f"https://opendata.resas-portal.go.jp/api/v1/{endpoint}",
            headers={"Content-Type": "application/json", "X-API-KEY": api_key},
            params=params,
        )
    except Exception as e:
        print(e)
        raise Exception(e)

    update_count_env()
    return res


def request_param_sqlit(response: requests.Response):
    url_parts = response.request.url.split("?")
    params = url_parts[1] if len(url_parts) > 1 else ""  # クエリがない場合は空文字
    if not params == "":
        params = params + "-"
    return params


def request_save_json(endpoint: str, params: dict):
    sleep_time = 1
    print(f"{sleep_time}秒待機中")
    time.sleep(sleep_time)  # 1秒あたりリクエスト平均数が5のため、余裕を持って1秒待機

    print("取得中...")
    response = api_request(endpoint, params)
    if response.status_code != 200:
        raise Exception(
            f"APIリクエストエラー: {response.status_code}", response.content
        )
    data = json.loads(response.content.decode("UTF-8"))
    current_time = datetime.now(jst).isoformat()

    data["request_params"] = response.request.url  # リクエストパラメータを保存
    data["request_datetime"] = current_time  # リクエスト日時を保存
    param = request_param_sqlit(response)
    endpoint = response.request.url.split("api/")[-1].replace("/", "-").split("?")[0]

    response_file_dir = f"response/{endpoint}"
    mkdir_if_not_exists(response_file_dir)

    with open(f"{response_file_dir}/{param}{current_time}.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"取得完了: {response_file_dir}/{current_time}.json")
    print()

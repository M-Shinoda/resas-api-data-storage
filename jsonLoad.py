import os
import json


def load_recent_json_file_from_directory(directory_path: str) -> dict:
    file_list = os.listdir(directory_path)
    file_list.sort()
    recent_filename = file_list[-1]

    if recent_filename.endswith(".json"):
        file_path = os.path.join(directory_path, recent_filename)
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data


def load_all_file_from_directory(directory_path: str) -> list[dict]:
    file_list = os.listdir(directory_path)

    datas = []
    for file_name in file_list:
        if file_name.endswith(".json"):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, "r", encoding="utf-8") as file:
                datas.extend(json.load(file)["result"])
    return datas

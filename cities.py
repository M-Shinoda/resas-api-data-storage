from jsonLoad import load_recent_json_file_from_directory
from resasManager import request_save_json


prefectures_json_data = load_recent_json_file_from_directory(
    "./response/v1-prefectures"
)


for pref_result in prefectures_json_data["result"]:
    print(pref_result["prefCode"], pref_result["prefName"])
    request_save_json(
        "cities",
        {
            "prefCode": pref_result["prefCode"],
        },
    )

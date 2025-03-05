from jsonLoad import load_recent_json_file_from_directory
from resasManager import request_save_json


prefectures_json_data = load_recent_json_file_from_directory(
    "./response/v1-prefectures"
)


for pref_result in prefectures_json_data["result"]:
    print(pref_result["prefCode"], pref_result["prefName"])
    # 1980-2045年（5年毎）のデータを取得
    # yearLeftとyearRightを使って、5年毎のデータを取得
    # それぞれを比較するような用途で使うため前データを左右で取得し取得回数を削減
    # yearLeft + 5 = yearRightとする
    for yearLeft in [1980, 1990, 2000, 2010, 2020, 2030, 2040]:
        yearRight = yearLeft + 5
        request_save_json(
            "population/composition/pyramid",
            {
                "cityCode": "-",
                "prefCode": pref_result["prefCode"],
                "yearLeft": yearLeft,
                "yearRight": yearRight,
            },
        )

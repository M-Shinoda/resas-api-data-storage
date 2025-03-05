####################
###市区町村指定あり
from jsonLoad import load_all_file_from_directory
from resasManager import request_save_json


cities_json_datas = load_all_file_from_directory("response/v1-cities")


for citie_result in cities_json_datas:
    print(citie_result["prefCode"], citie_result["cityCode"], citie_result["cityName"])
    request_save_json(
        "population/composition/perYear",
        {
            "prefCode": citie_result["prefCode"],
            "cityCode": citie_result["cityCode"],
        },
    )


#####################
# ###市区町村指定なし
# from jsonLoad import load_recent_json_file_from_directory
# from resasManager import request_save_json


# prefectures_json_data = load_recent_json_file_from_directory(
#     "./response/v1-prefectures"
# )


# for pref_result in prefectures_json_data["result"]:
#     print(pref_result["prefCode"], pref_result["prefName"])
#     request_save_json(
#         "population/composition/perYear",
#         {
#             "cityCode": "-",
#             "prefCode": pref_result["prefCode"],
#         },
#     )

#####################
# ###市区町村指定ありの途中まで取得していた分のあまりを取得
# import os
# from jsonLoad import load_all_file_from_directory
# from resasManager import request_save_json


# cities_json_datas = load_all_file_from_directory("response/v1-cities")

# i = 0
# for citie_result in cities_json_datas:
#     already_file_list = os.listdir(
#         "./response/v1-population-composition-perYear/市区町村指定あり"
#     )

#     check_file_name_parts = (
#         f"prefCode={citie_result['prefCode']}&cityCode={citie_result['cityCode']}"
#     )
#     check_name_starts = [
#         s for s in already_file_list if s.startswith(check_file_name_parts)
#     ]

#     if len(check_name_starts) == 0:
#         print(
#             citie_result["prefCode"], citie_result["cityCode"], citie_result["cityName"]
#         )
#         request_save_json(
#             "population/composition/perYear",
#             {
#                 "prefCode": citie_result["prefCode"],
#                 "cityCode": citie_result["cityCode"],
#             },
#         )

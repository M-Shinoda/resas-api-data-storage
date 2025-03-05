from resasManager import request_save_json

# パラメータなしエンドポイント(カテゴリ：共通)
endpoints: list[str] = {
    "prefectures",
    "industries/broad",
    "jobs/broad",
    "patents/broad",
    "regions/broad",
    "regions/agricultureDepartments",
    "tradeInfoItemTypes/broad",
}

for endpoint in endpoints:
    print(endpoint)
    request_save_json(endpoint, {})

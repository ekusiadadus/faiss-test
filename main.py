from pymongo import MongoClient

# MongoDBが動いているDockerコンテナに接続
client = MongoClient('localhost', 27019)

# 既存のデータベース名をリストで取得
database_names = client.list_database_names()

# データベース名を出力
print("Existing databases:")
for db_name in database_names:
    print(db_name)

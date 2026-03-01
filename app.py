from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient  # 導入 MongoDB 套件

app = Flask(__name__)

# --- 1. MySQL 設定 ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:5201314@localhost/my_practice_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(100))
# --- 2. MongoDB 設定 (改為雲端網址) ---
# 提示：請確保密碼正確，且 Network Access 已設為 0.0.0.0/0
uri = "mongodb+srv://s411147136_db_user:RBKafVx8fzDWmCNm@cluster0.481tf8l.mongodb.net/?appName=Cluster0"

try:
    mongo_client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    mongo_db = mongo_client['my_mongo_db']
    collection = mongo_db['test_collection']
    mongo_client.server_info()
    print("✅ 雲端 MongoDB 連線成功")
except Exception as e:
    print(f"❌ 雲端 MongoDB 連線失敗: {e}")

# --- 3. API 路由設定 ---

# MySQL 查詢 (GET)
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        # 增加 id 欄位
        output.append({git add .
git commit -m "Update MongoDB to Cloud Atlas and add requirements"
git push origin main
            'id': user.id,
            'name': user.username,
            'email': user.email
        })
    return jsonify(output)

# MongoDB 新增 (POST)
@app.route('/api/mongo/add', methods=['POST'])
def add_mongo():
    # 這裡我們模擬存入一筆 JSON 資料
    data = {"item": "Laptop", "brand": "Apple", "tags": ["tech", "work"]}
    result = collection.insert_one(data)
    return jsonify({
        "message": "MongoDB 資料新增成功！",
        "inserted_id": str(result.inserted_id)
    })


from flask import request  # 務必在最上面 import 補上 request


# 新增用戶的 API (POST 請求)
@app.route('/api/users/add', methods=['POST'])
def add_user():
    # 接收 Postman 傳過來的 JSON 資料
    data = request.get_json()

    # 建立一個新的 User 物件
    new_user = User(username=data['username'], email=data['email'])

    # 存入 MySQL
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": f"用戶 {data['username']} 註冊成功！"}), 201
@app.route('/api/mongo/list', methods=['GET'])
def list_mongo():
    # 這裡從 MongoDB 抓出所有資料
    data = list(collection.find())
    output = []
    for d in data:
        # 因為 MongoDB 的 _id 是物件，要轉成字串才能傳給 Postman
        d['_id'] = str(d['_id'])
        output.append(d)
    return jsonify(output)


# 證明 MongoDB 存在：列出所有資料
@app.route('/api/mongo/all', methods=['GET'])
def get_mongo_all():
    # collection.find() 會抓出所有文件
    all_data = list(collection.find())

    # 這裡有個 High SQL 轉換概念：
    # MongoDB 的 _id 是 ObjectId 對象，JSON 不認識，我們要把它轉成字串
    for item in all_data:
        item['_id'] = str(item['_id'])

    return jsonify(all_data)


@app.route('/api/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # 改用 db.session.get(模型, ID) 這是最新版最穩定的寫法
        user = db.session.get(User, user_id)

        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": f"ID 為 {user_id} 的用戶已成功刪除！"}), 200
        else:
            return jsonify({"error": "找不到該用戶"}), 404

    except Exception as e:
        # 如果還是噴 500，這行會在 PyCharm 的終端機印出真正的死因
        print(f"❌ 刪除時發生錯誤: {e}")
        return jsonify({"error": "伺服器內部錯誤", "details": str(e)}), 500
# --- 4. 啟動伺服器 ---
if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
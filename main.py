from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/test', methods=['GET'])
def hello_world():
    # 這裡可以寫 SQL 查詢邏輯
    return jsonify({"message": "成功連線到 PyCharm 的 API!", "status": "Happy Coding"})

if __name__ == '__main__':
    app.run(port=5000)
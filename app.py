from flask import Flask
from flask import jsonify

app = Flask(__name__)

# from flask import jsonify
@app.route("/")
def hello():
    data = {
        "name": "Keisuke",
        "age": 32,
        "message": "Hello API"
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

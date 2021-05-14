from flask import Flask, jsonify
import os
from subprocess import call

cwd = os.getcwd()


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    call("cd "cwd+"&& python3 telegramShellBot.py &", shell=True)
    

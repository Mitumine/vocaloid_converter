# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request
import re
# from models import convert


# Flaskオブジェクトの生成
app = Flask(__name__)


# 「/」へアクセスがあった場合に、'Hello World'の文字列を返す
# 「/index」へアクセスがあった場合に、「index.html」を返す

@app.route('/')
def index():
    name = request.args.get('before')
    return render_template('index.html')


@app.route('/', methods=['post'])
def post():
    body = request.form['before']
    # body = convert.convert(body)
    return render_template('index.html', body=body)


if __name__ == "__main__":
    app.run(debug=True)

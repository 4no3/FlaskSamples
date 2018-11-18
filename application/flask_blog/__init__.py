# flask_blog/__init__.py
from flask import Flask

app = Flask(__name__)   # アプリケーション本体を作成
app.config.from_object('flask_blog.config') # config ファイルの設定を config として扱う

import flask_blog.views # view ファイルをインポートする
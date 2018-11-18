# server.py
# サーバーの起動ファイル

from flask_blog import app

if __name__ == '__main__':
    app.run()   # 起動するモードは、config.py で設定する
# flask_blog\views.py
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

# http://127.0.0.1:5000/ にリクエストがあったときの処理
@app.route('/')
def show_entires():
    return render_template('entries/index.html')
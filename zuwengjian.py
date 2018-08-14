# -*- coding: UTF-8 -*-
from flask import Flask,request,make_response,redirect,render_template
import MySQLdb

app = Flask(__name__)

@app.route('/')
def index():
    '''return redirect('https://www.csdn.net/')#（redirect）直接进入这个网站'''

    return render_template('index.html')

if __name__ == '__main__':
    app.run()

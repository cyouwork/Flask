#-*- coding=utf-8 -*-
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/index')
def index():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

@app.route('/user/<username>')
def profile(username):
    pass

@app.route('/urltest')
def urltest():
    s = ""
    s = url_for('static', filename='Readme')
#    with app.test_request_context():
#        s += url_for('index')
#        s += url_for('login')
#        s += url_for('login', next='/')
#        s += url_for('profile', username='yang jinyun')   
    return s


if __name__ == '__main__':
    app.debug = True
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occured (%d apples)', 42)
    app.logger.error('An error occured')
    app.run(host='0.0.0.0')

import os
import json
import hashlib
import sys


from flask import Flask, request, session, redirect, url_for, escape,\
    abort, render_template
from urllib.parse import urlparse
from .test1 import *
from .UserFunctions import *
from uuid import uuid4

initConnect()

testFlaskApp = Flask(__name__)

try:
    appStorePath = os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))) +\
        '\\PlaidSandbox\\static\\'

    oldPath = os.getenv('LOCALAPPDATA').rstrip('\\') +\
        '\\Python Sandbox Data\\PlaidSandbox\\test01\\'
except:
    pass

argIdxInArgv = 1

uN = 'username'
pW = 'password'

sKey = b'\x1d3\xb7]?\x033 \x96\x1c\x86\xebI\x12E7J\x87\x1d\xfe\xb3y\xe1\xf6'


def encPwd(pwd, salt=''):
    if(salt == ''):
        salt = uuid4().hex
    return hashlib.sha256(
        salt.encode() +
        pwd.encode()).hexdigest() + ':' + salt


def checkPass(usr, pwd):
    phash, salt = usr.password.split(':')
    return usr.password == encPwd(pwd, salt)


@testFlaskApp.route('/register', methods=['GET', 'POST'])
def reg():
    extraLine = 'Enter your credentials here'
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        initConnect(force_connect=True)
        extraLine = 'Username already exists'
        usr = User.objects.raw({uN: request.form[uN]})
        if(usr.count() == 0):
            extraLine = 'Passwords do not match'
            if(request.form[pW] == request.form['re' + pW]):
                u = User(
                    username=request.form[uN],
                    password=encPwd(request.form[pW]))
                try:
                    u.save()
                    session[uN] = request.form[uN]
                    return redirect(url_for('index'))
                except:
                    extraLine = 'Error Saving record'
    return '''
        <p>Hello unknown user! running on port %s
        <p><font color="red">%s</font>
        <p>
        <form method="post">
            <p>Username: <input type=text name=username>
            <p>Password: <input type=password name=password>
            <p>Re-enter Password: <input type=password name=repassword>
            <p><input type=submit value=Submit>
        </form>
        <a href="%s">Home</a>
        <p>
    ''' % (
        urlparse(request.url).port,
        extraLine,
        url_for('index'))


@testFlaskApp.route('/test')
def test():
    return render_template('t_index.html.j2')


@testFlaskApp.route("/")
def index():
    if 'username' in session:
        return '''
            <p>Hello %s! running on port %s
            <p><a href="%s">Logout</a>
            <p><a href="%s">Test</a>
        ''' % (
            escape(session['username']),
            urlparse(request.url).port,
            url_for('logout'),
            url_for('test'))
    return '''
        <p>Hello unknown user! running on port %s
        <p>
        <p><a href="%s">Login</a>
        <p>
        <p><a href="%s">Click Here</a> to register
    ''' % (
        urlparse(request.url).port,
        url_for('login'),
        url_for('reg'))


@testFlaskApp.route('/login', methods=['GET', 'POST'])
def login():
    extraLine = ''
    if request.method == 'POST':
        initConnect(force_connect=True)
        extraLine = 'Login Failed!! Username or password invalid'
        usr = User.objects.raw({uN: request.form[uN]})
        if(usr.count() != 0):
            if(checkPass(usr.first(), request.form[pW]) is True):
                session[uN] = request.form[uN]
                return redirect(url_for('index'))
    return '''
        <p>Hello unknown user! running on port %s
        <p><font color="red">%s</font>
        <p>
        <form method="post">
            <p>Username: <input type=text name=username>
            <p>Password: <input type=password name=password>
            <p><input type=submit value=Submit>
        </form>
        <p><a href="%s">Click Here</a> to register
    ''' % (
        urlparse(request.url).port,
        extraLine,
        url_for('reg'))


@testFlaskApp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


# @testFlaskApp.route('/getfile/<filename>')
# def getfile(filename):
#
#     filename = appStorePath +\
#         filename.lstrip('.,\\/')
#
#     filereturned = runGetChase(filename)
#
#     print(os.path.basename(
#         filereturned.replace('\\', '/').replace('C:', '')))
#
#     if filereturned is None:
#         abort(404)
#     return testFlaskApp.send_static_file(
#         os.path.basename(
#             filereturned.replace('\\', '/').replace('C:', '')))
#     # return send_file(
#     #     filereturned.replace('\\', '/').replace('C:', ''))
#
#
@testFlaskApp.route('/banklinks')
def banklinks():
    pass


@testFlaskApp.route('/banklinks/add')
def addbanklink():
    pass


@testFlaskApp.route('/banklinks/remove')
def removebanklink():
    pass


@testFlaskApp.route('/banklinks/<blid>')
def getbanklink(blid):
    pass


@testFlaskApp.route('/virtaccounts')
def virtaccounts():
    pass


@testFlaskApp.route('/virtaccounts/add')
def addvirtaccounts():
    pass


@testFlaskApp.route('/virtaccounts/remove')
def removevirtaccounts():
    pass


testFlaskApp.secret_key = sKey


def runthis():
    hostToRun = '127.0.0.1'
    portToRun = '37002'

    print(testFlaskApp.template_folder)

    if(len(sys.argv)) > argIdxInArgv:
        print(sys.argv[argIdxInArgv])
        jsonArgs = json.loads(sys.argv[argIdxInArgv])

        if 'dev' in jsonArgs:
            if jsonArgs['dev'] is False:
                hostToRun = '0.0.0.0'

        try:
            if isinstance(jsonArgs['port'], int):
                portToRun = jsonArgs[port]
        except:
            pass

    testFlaskApp.run(
        host=hostToRun,
        port=portToRun
    )


if __name__ == "__main__":
    runthis()

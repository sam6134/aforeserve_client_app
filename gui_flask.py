from flaskwebgui import FlaskUI #get the FlaskUI class
import requests
from flask import Flask, request, render_template, jsonify
#import printer
#import email_s
import socket
from getmac import get_mac_address
from platform import platform
from getpass import getuser

app = Flask(__name__)

ui = FlaskUI(app)

hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()
macid = get_mac_address()
OS_v = platform()
username = getuser()

#data = fetch_data_db("select * from login;",'creds')

@app.route('/', methods = ['GET','POST'])
def login():
    if request.method == 'POST': 
        user = request.form['user']
        passw = request.form['pass']
        if user == 'User' and passw == '12345':
            return render_template('index.html')
        else:
            return render_template('login.html')
    return render_template('login.html')

@app.route('/newt/<symptom>/<description>', methods = ['GET','POST'])
def newt(symptom,description):
    # urgency = request.args.get('urgency')
    # impact = request.args.get('impact')
    # priority = request.args.get('priority')
    # classification = request.args.get('classification')
    # wg = request.args.get('wg')
    # medium = request.args.get('medium')
    # symptom = request.args.get('symptom')
    # description = request.args.get('description')
    url = 'http://35.184.236.4:7005/newt/'+symptom+'/'+description
    res = requests.get(str(url))
    print(res)
    a = {
        'id':int(res.text)
    }
    print(a)
    return jsonify(a)

# @app.route('/submit', methods = ['GET','POST'])
# def sub():
#     text = request.args.get('text')
#     url = 'http://35.184.236.4:7005/submit/'+text
#     print('------------')
#     print(url)
#     print('------------')
#     res = requests.get(str(url))
#     print('------------')
#     print(res)
#     print('------------')
#     a = {
#         'id' : int(res.text)
#     }
#     print(a)
#     return jsonify(a)

@app.route('/ref', methods = ['GET', 'POST'])
def ref():
    text = request.args.get('id')
    url = 'http://35.184.236.4:7005/ref/'+str(text)
    res = requests.get(str(url))
    ab = res.text
    print(ab)
    return(ab)

@app.route('/pr', methods = ['GET','POST'])
def pr():
    flg,out = printer.printerConfig()
    return out

@app.route('/em', methods = ['GET','POST'])
def em():
    flg,out = email_s.mailConfig()
    return out

@app.route('/passw', methods = ['GET','POST'])
def passw():
    return 'Yet to implement'

@app.route('/dc', methods = ['GET','POST'])
def dc():
    return 'Yet to implement'

@app.route('/sft', methods = ['GET','POST'])
def sft():
    return 'Yet to implement'

@app.route('/newrequest', methods = ['GET','POST'])
def newreq():
    return '''
    <p class="speech-bubble btn-primary" style="height: 25%;">
        Please verify the below details to continue with Aforesight
       <br>
       <br>
        Your IP : '''+str(IP)+'''
       <br>
       Your Hostname : '''+str(hostname)+'''
    </p>
    '''
@app.route('/confirmnew', methods = ['GET', 'POST'])
def connew():
    arg = request.args.get('con1')
    if arg == 'confirm':
        return '''
    <p class="speech-bubble btn-primary" style="height: 75%;">
                            Please select desired option…
                            <br>
                            <br>
                                    <button class="btn btn-secondary" onclick="sft2install()">Software Installation</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="sysrelated()">System Related</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="apprelated()">Application Related</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="osrelated()">OS Related</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="printerrelated()">Printer Related</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="netrelated()">Network Related</button>
                                            
    </p>
    '''
    elif arg == 'sftcon':
        return '''
        <p class="speech-bubble btn-primary" style="height: 55%;">
                            Please select desired option…
                            <br>
                            <br>
                                    <button class="btn btn-secondary" onclick="msoffice()">MS Office</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="adobe()">Adobe Reader</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="anti()">Antivirus</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="otherssft()">Others</button>
                                            
    </p>
        '''
    elif arg == 'msoff':
        return '''
        <p class="speech-bubble btn-primary" style="padding-right:3%;">
                            Please describe the issue
        </p>
        <div class="md-form" >
            <textarea id="textms" class="form-control md-textarea" length="120" rows="3" style="width:70%" placeholder="Description"></textarea>
        </div>
        <button class="btn btn-secondary" onclick="conms()">Confirm</button>
        
        '''
    elif arg == 'conms':
        arg2 = request.args.get('text')
        return '''
        <p class="speech-bubble btn-light" style="padding-right:3%;">Description Added : <br>'''+arg2+'''</p>'''
    elif arg == 'other':
        return '''
        <p class="speech-bubble btn-primary" style="padding-right:3%;height: 10%;">
            Which software you want to install/configure
        </p>
        '''
    elif arg == 'othercon':
        arg2 = request.args.get('text')
        return '''
        <br><p class="speech-bubble btn-light" style="padding-right:3%;height: 10%;">Description Added : <br>'''+arg2+'''</p>
        '''

ui.run()
from flaskwebgui import FlaskUI #get the FlaskUI class
import requests
from flask import Flask, request, render_template, jsonify
import socket
from getmac import get_mac_address
from platform import platform, system, release
from getpass import getuser

rel = release()

#for windows 10
import printer
import email_s
import diskCleanup

#for windows 8
import Printer_Latest_Remove_Latency_for_8
import test_fetch_mail_for_8

#for windows 7
import Printer_Latest_Remove_Latency_for_7
import test_fetch_mail_for_7



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
sernum = '12345'
lap_desk = 'desk'
url = 'http://35.184.236.4:7005/inoutserver/'+macid
res = requests.get(url)
res = res.json()
inser,outser = res['inserver'],res['outserver']
dprint = '2'
#data = fetch_data_db("select * from login;",'creds')
url = 'http://35.184.236.4:7005/userdetails/'+hostname+'/'+IP+'/'+macid+'/'+sernum+'/'+OS_v+'/'+lap_desk+'/'+inser+'/'+outser+'/'+dprint+'/'+username
requests.get(url)

@app.route('/', methods = ['GET','POST'])
def login():
    if request.method == 'POST': 
        user = request.form['user']
        passw = request.form['pass']
        if user == 'User' and passw == '12345':
            return render_template('index.html',User = hostname.title())
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
    manufac_name = request.args.get('manuname')
    mdelname = request.args.get('model')
    if rel == '8.1':
        flg,out = Printer_Latest_Remove_Latency_for_8.printerConfig(manufac_name,mdelname)
        return out
    elif rel == '7':
        flg,out = Printer_Latest_Remove_Latency_for_7.printerConfig(manufac_name,mdelname)
        return out
    else:
        flg,out = printer.printerConfig(manufac_name,mdelname)
        return out

@app.route('/emailconfig', methods = ['GET','POST'])
def em():
    username = request.args.get('username')
    email_ss = request.args.get('email_s')
    password_s = request.args.get('password_s')
    if rel == '8.1':
        flg,out = test_fetch_mail_for_8.mailConfig(username,inser,outser,email_ss,password_s)
        return out
    elif rel == '7':
        flg,out = test_fetch_mail_for_7.mailConfig(username,inser,outser,email_ss,password_s)
        return out
    else:
        flg,out = email_s.mailConfig(username,inser,outser,email_ss,password_s)
        return out

@app.route('/passw', methods = ['GET','POST'])
def passw():
    return 'Yet to implement'

@app.route('/diskclean', methods = ['GET','POST'])
def dc():
    error,out = diskCleanup.startCleanup()
    print(error)
    return out

@app.route('/sft', methods = ['GET','POST'])
def sft():
    return 'Yet to implement'

#flow start for new request

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
                                    <button class="btn btn-secondary" onclick="networkrelated()">Network Related</button>
                                            
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
        <div class="md-form" style="">
            <textarea id="textms" class="form-control md-textarea" length="120" rows="3" style="width:70%;color:white;" placeholder="Description"></textarea>
        </div>
        <button class="btn btn-secondary" onclick="conms()">Confirm</button>
        
        '''
    elif arg == 'conms':
        arg2 = request.args.get('text')
        return '''
        <p class="speech-bubble btn-light" style="padding-right:3%;height: 11%;">Description Added : <br>'''+arg2+'''</p>'''
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
    elif arg == 'no':
        return'''
        <p class="speech-bubble btn-primary" style="padding-right:3%;height: 10%;">
            Please contact IT Helpdesk on +91 9999999 to raise ticket on behalf of others…
        </p>
        '''

@app.route('/sysrelated', methods = ['GET', 'POST'])
def sysrelated():
    arg = request.args.get('con1')
    if arg == 'sysrelated':
        return '''
        <p class="speech-bubble btn-primary" style="height: 77%;">
                            Please select desired option…
                            <br>
                            <br>
                                    <button class="btn btn-secondary" onclick="performance()">Performance Issue/System Slow</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="disk()">Disk full/No Space</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="autoshutres()">Auto shutdown/restart</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="forgetpsw()">Forget login password</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="unablelog()">Unable to login</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="sysother()">Other</button>                
    </p>
        '''
    elif arg == 'psw':
        return '''
        <p class="speech-bubble btn-primary" style="height: 54%;padding-right: 3%;">
                            All fields are mandatory
                            <br>
                            <br>
                                    <input type="password" id="password1" class="form-control" placeholder = "New Password">
                            <br>
                                    <input type="password" id="password2" class="form-control" placeholder = "Confirm Password">
                            <br>
                                    <button class="btn btn-secondary" onclick="new_pass()">Proceed</button>                        
    </p>
        '''
@app.route('/apprelated', methods = ['GET','POST'])
def apprelated():
    arg = request.args.get('con1')
    if arg == 'apprelated':
        return '''
        <p class="speech-bubble btn-primary" style="height: 84%;">
                            Please select desired option…
                            <br>
                            <br>
                                    <button class="btn btn-secondary" onclick="outlook()">Outlook related issue</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="exc_el()">Excel not responding</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="sap()">SAP not working</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="emailconf()">Email Configuration</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="ieconf()">IE Configuration</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="vpnconf()">VPN Configuration</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="appother()">Other</button>                        
    </p>
        '''
    elif arg == 'email':
        return '''
        <p class="speech-bubble btn-primary" style="height: 54%;padding-right: 3%;">
                            All fields are mandatory
                            <br>
                            <br>
                                    <input type="text" id="username" class="form-control" placeholder="UserName">
                            <br>
                                    <input type="text" id="useremail" class="form-control" placeholder = "Email">
                            <br>
                                    <input type="password" id="password" class="form-control" placeholder = "Password">
                            <br>
                                    <button class="btn btn-secondary" onclick="email_reg()">Proceed</button>                        
    </p>
        '''
@app.route('/osrelated', methods = ['GET','POST'])
def osrelated():
    arg = request.args.get('con1')
    if arg == 'osrelated':
        return '''
        <p class="speech-bubble btn-primary" style="height: 42%;">
                            Please select desired option…
                            <br>
                            <br>
                                    <button class="btn btn-secondary" onclick="addpcdomain()">Add PC with Domain</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="osnotbooting()">OS not booting</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="osother()">Other</button>                        
    </p>
        '''

@app.route('/printerrelated', methods = ['GET','POST'])
def printerrelated():
    arg = request.args.get('con1')
    if arg == 'printerrelated':
        return '''
        <p class="speech-bubble btn-primary" style="height: 53%;">
                            Please select desired option…
                            <br>
                            <br>
                                    <button class="btn btn-secondary" onclick="newprinter()">Printer - New configuration</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="printernotworking()">Printer not working</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="printernotproper()">Printout not proper</button>                        
                            <br>
                                    <button class="btn btn-secondary" onclick="printerother()">Other</button>        
    </p>
        '''
    elif arg == 'newprinter':
        return '''
        <p class="speech-bubble btn-primary" style="height: 54%;padding-right: 3%;">
                            All fields are mandatory
                            <br>
                            <br>
                                    <input type="text" id="manuname" class="form-control" placeholder="Manufaturer Name">
                            <br>
                                    <input type="text" id="model" class="form-control" placeholder = "Model Name">
                            <br>
                                    <button class="btn btn-secondary" onclick="new_print()">Proceed</button>                        
    </p>
        '''

@app.route('/networkrelated', methods = ['GET','POST'])
def networkrelated():
    arg = request.args.get('con1')
    if arg == 'networkrelated':
        return '''
        <p class="speech-bubble btn-primary" style="height: 63%;">
                            Please select desired option…
                            <br>
                            <br>
                                    <button class="btn btn-secondary" onclick="IEnotworking()">Internet not working</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="noacessserver()">Unable to access server</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="ipchange()">IP Address - Change</button>                        
                            <br>
                                    <button class="btn btn-secondary" onclick="wificonf)">Wi-Fi Configuration</button>                        
                            <br>
                                    <button class="btn btn-secondary" onclick="networkother()">Other</button>        
    </p>
        '''
# flow end for new request

#flow know your ticket
@app.route('/knowticket', methods = ['GET','POST'])
def knowticket():
    arg = request.args.get('con1')
    if arg == 'know':
        return '''
        <p class="speech-bubble btn-light" style="padding-right:3%;">Select one from your previous tickets : <br></p>
            <table class="table">
                <thead class="black white-text">
                    <tr>
                        <th scope="col">Ticket ID</th>
                        <th scope="col">Status</th>
                        <th scope="col">Issue</th>
                        <th scope="col">Description</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>111</td>
                        <td>New</td>
                        <td>Printer</td>
                        <td>Printer has to be resolved</td>
                    </tr>
                    <tr>
                        <td>423</td>
                        <td>Resolved</td>
                        <td>Password</td>
                        <td>Printer has to be resolved</td>
                    </tr>
                    <tr>
                        <td>567</td>
                        <td>In Progress</td>
                        <td>Email</td>
                        <td>Printer has to be resolved</td>
                    </tr>
                </tbody>
            </table>
        '''

#flow new query
@app.route('/newquery', methods = ['GET','POST'])
def newquery():
    arg = request.args.get('con1')
    if arg == 'newq':
        return '''
        <p class="speech-bubble btn-primary" style="height: 42%;">
                            Please select desired option…
                            <br>
                            <br>
                                    <button class="btn btn-secondary" onclick="itpolicies()">Know your IT Policies</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="helpdesk()">Contact of IT Helpdesk</button>
                            <br>
                                    <button class="btn btn-secondary" onclick="asset()">Know your IT Asset</button>                        
    </p>
        '''
    elif arg == 'asset':
        return '''
    <p class="speech-bubble btn-primary" style="height: 11%;">
        Please verify your Username : '''+str(hostname)+''' and EmailID : xyz@emai.com 
    </p>
    '''
ui.run()
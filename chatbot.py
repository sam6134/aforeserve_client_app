import socket
from getmac import get_mac_address
from platform import platform
from getpass import getuser
from flask import Flask, render_template, request

hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()
macid = get_mac_address()
OS_v = platform()
username = getuser()

app = Flask(__name__)

@app.route('/')
def l():
    return render_template('chatbot.html')

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
                                    <button class="btn btn-secondary" onclick="sftinstall()">Software Installation</button>
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
        <p class="speech-bubble btn-light" style="padding-right:3%;">Description Added : <br>'''+arg2+'''</p>
        '''
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
if __name__ == '__main__':
    app.run()
    
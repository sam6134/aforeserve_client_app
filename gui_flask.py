from flaskwebgui import FlaskUI  # get the FlaskUI class
from requests import get
from flask import Flask, request, render_template, jsonify
import socket
from getmac import get_mac_address
from platform import platform, system, release
from getpass import getuser
import uuid
import os.path

# for windows 10
import Printer_Latest_Remove_Latency_win10
import test_fetch_mail_win10
import diskCleanup

# for windows 8
import Printer_Latest_Remove_Latency_for_8
import test_fetch_mail_for_8

# for windows 7
import Printer_Latest_Remove_Latency_for_7
import test_fetch_mail_for_7

# http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7001/lab
# creating new id
print(os.path.isfile('static/ids.txt'))
if(os.path.isfile('static/ids.txt')):
    global ids
    ids = open('static/ids.txt')
    ids = ids.read()
    ids = ids.replace('\n', '')
    all_id = get('http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/getalluniqueid')
    all_id = all_id.json()
    all_id = all_id['MAC_ID']
    flag = 0
    for i in range(0, len(all_id)):
        if str(ids) == all_id[str(i)]:
            flag += 1
    if flag > 0:
        pass
    else:
        token = True
        while token:
            ids = uuid.uuid1()
            ids = str(ids)
            ids = ids.replace('-', '')
            all_id = get('http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/getalluniqueid')
            all_id = all_id.json()
            all_id = all_id['MAC_ID']
            flag = 0
            for i in range(0, len(all_id)):
                if ids == all_id[str(i)]:
                    flag += 1
                else:
                    pass
            if flag == 0:
                with open('static/ids.txt', 'w') as file:
                    file.write(str(ids))
                url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/userdetails/new/1/1/' + \
                    str(ids)+'/1/1/1/outlook.office365.com/smtp.office.com/1/1'
                res = get(url)
                token = False
else:
    token = True
    while token:
        ids = uuid.uuid1()
        ids = str(ids)
        ids = ids.replace('-', '')
        all_id = get('http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/getalluniqueid')
        all_id = all_id.json()
        all_id = all_id['MAC_ID']
        flag = 0
        for i in range(0, len(all_id)):
            if ids == all_id[str(i)]:
                flag += 1
            else:
                pass
        if flag == 0:
            with open('static/ids.txt', 'w') as file:
                file.write(str(ids))
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/userdetails/new/1/1/' + \
                str(ids)+'/1/1/1/outlook.office365.com/smtp.office.com/1/1'
            res = get(url)
            token = False

rel = release()

app = Flask(__name__)

ui = FlaskUI(app)

hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()
# macid = get_mac_address()
OS_v = platform()
username = getuser()
sernum = '12345'
lap_desk = 'desk'
url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/inoutserver/'+str(ids)
print('------------')
print(url)
res = get(url)
res = res.json()
inser, outser = res['inserver'], res['outserver']
dprint = '2'

# creating new user


url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/userdetails/old/'+hostname+'/'+IP+'/' + \
    str(ids)+'/'+sernum+'/'+OS_v+'/'+lap_desk + \
    '/'+inser+'/'+outser+'/'+dprint+'/'+username
get(url)


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('index.html', User=username.title())

@app.route('/pr', methods=['GET', 'POST'])
def pr():
    manufac_name = request.args.get('manuname')
    mdelname = request.args.get('model')
    url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/Printer_to_be_configured/Printer_to_be_configured/' + \
        str(ids)
    res = get(url)
    if rel == '8.1':
        out = Printer_Latest_Remove_Latency_for_8.printerConfig(
            manufac_name, mdelname)
        if out == 'success':
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/upt/'+res.text
            res = get(url)
            return res.text
        elif out == 'failed':
            #Assing to department
            return 'Issue not resolved assigning it to other department'
    elif rel == '7':
        out = Printer_Latest_Remove_Latency_for_7.printerConfig(
            manufac_name, mdelname)
        if out == 'success':
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/upt/'+res.text
            res = get(url)
            return res.text
        elif out == 'failed':
            #Assing to department
            return 'Issue not resolved assigning it to other department'
    else:
        out = Printer_Latest_Remove_Latency_win10.printerConfig(
            manufac_name, mdelname)
        if out == 'success':
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/upt/'+res.text
            res = get(url)
            return res.text
        elif out == 'failed':
            #Assing to department
            return 'Issue not resolved assigning it to other department'


@app.route('/emailconfig', methods=['GET', 'POST'])
def em():
    username = request.args.get('username')
    email_ss = request.args.get('email_s')
    password_s = request.args.get('password_s')
    url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/Email_to_be_configured/Email_to_be_configured/' + \
        str(ids)
    res = get(url)
    print(res.text)
    if rel == '8.1':
        out = test_fetch_mail_for_8.mailConfig(
            username, inser, outser, email_ss, password_s)
        if out == 'success':
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/upt/'+res.text
            res = get(url)
            return res.text
        elif out == 'failed':
            #Assing to department
            return 'Issue not resolved assigning it to other department'
    elif rel == '7':
        out = test_fetch_mail_for_7.mailConfig(
            username, inser, outser, email_ss, password_s)
        if out == 'success':
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/upt/'+res.text
            res = get(url)
            return res.text
        elif out == 'failed':
            #Assing to department
            return 'Issue not resolved assigning it to other department'
    else:
        out = test_fetch_mail_win10.mailConfig(
            username, inser, outser, email_ss, password_s)
        if out == 'success':
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/upt/'+res.text
            res = get(url)
            return res.text
        elif out == 'failed':
            #Assing to department
            return 'Issue not resolved assigning it to other department'


@app.route('/passw', methods=['GET', 'POST'])
def passw():
    url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/password_has_to_be_changed/password_has_to_be_changed/' + \
        str(ids)
    res = get(url)
    url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/upt/'+res.text
    res = get(url)
    return res.text


@app.route('/diskclean', methods=['GET', 'POST'])
def dc():
    url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/Disk_full_disk_clean_to_be_configured/disk_full_disk_clean_to_be_configured/' + \
        str(ids)
    get(url)
    out = diskCleanup.startCleanup()
    if out == 'success':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/upt/'+res.text
        res = get(url)
        return res.text
    elif out == 'failed':
        #Assing to department
        return 'Issue not resolved assigning it to other department'


@app.route('/sft', methods=['GET', 'POST'])
def sft():
    return 'Yet to implement'

# flow start for new request


@app.route('/newrequest', methods=['GET', 'POST'])
def newreq():
    return '''
    <p class="speech-bubble btn-primary" style="height: 25%;">
        Please verify the below details to continue with Aforesight
       <br>
       <br>
        Your IP : '''+str(IP)+'''
       <br>
       Your Hostname : '''+str(username.title())+'''
    </p>
    '''


@app.route('/confirmnew', methods=['GET', 'POST'])
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
    elif arg == 'msoffice':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/MS_office_installation/MS_office_installation/' + str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'adobe':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/adobe_installation/adobe_installation/' + str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'anti':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/Antivirus_installation/Antivirus_installation/' + str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'otherssft':
        return '''
            <p class="speech-bubble btn-primary" style="height: 43%;padding-right: 3%;">
                            All fields are mandatory
                            <br>
                            <br>
                                    <input type="text" id="sftsymptom" class="form-control" placeholder="Symptom">
                            <br>
                                    <input type="text" id="sftdes" class="form-control" placeholder = "Description">
                            <br>
                                    <button class="btn btn-secondary" onclick="sftothernew()">Proceed</button>                        
    </p>
            '''
    elif arg == 'newt':
        symp = request.args.get('symptom')
        des = request.args.get('des')
        if len(symp) >= 10 and len(des) >= 10:
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/'+symp+'/'+des+'/' + str(ids)
            res = get(url)
            return '''
                <p class="speech-bubble btn-primary" style="height: 7%;">
                Ticket ID : '''+res.text+'''
                </p>
                '''
        else:
            return '''
                <p class="speech-bubble btn-primary" style="height: 10%;">
                Symptom and Description should not be less than 10 characters
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


@app.route('/sysrelated', methods=['GET', 'POST'])
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
    elif arg == 'autoshut':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/auto_shutdown_restart/auto_shutdown_restart/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'unlog':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/unable_to_login/unable_to_login/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'sysother':
        return '''
            <p class="speech-bubble btn-primary" style="height: 43%;padding-right: 3%;">
                            All fields are mandatory
                            <br>
                            <br>
                                    <input type="text" id="syssymptom" class="form-control" placeholder="Symptom">
                            <br>
                                    <input type="text" id="sysdes" class="form-control" placeholder = "Description">
                            <br>
                                    <button class="btn btn-secondary" onclick="sysothernew()">Proceed</button>                        
    </p>
            '''
    elif arg == 'newt':
        symp = request.args.get('symptom')
        des = request.args.get('des')
        if len(symp) >= 10 and len(des) >= 10:
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/'+symp+'/'+des+'/' + str(ids)
            res = get(url)
            return '''
                <p class="speech-bubble btn-primary" style="height: 7%;">
                Ticket ID : '''+res.text+'''
                </p>
                '''
        else:
            return '''
                <p class="speech-bubble btn-primary" style="height: 10%;">
                Symptom and Description should not be less than 10 characters
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


@app.route('/apprelated', methods=['GET', 'POST'])
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
    elif arg == 'outlook':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/outlook_related_issue/outlook_related_issue/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'excel':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/excel_not_responding/excel_not_responding/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'sap':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/sap_not_responding/sap_not_responding/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'ie':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/ie_configuration/ie_configuration/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'vpn':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/vpn_configuration/vpn_configuration/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'appother':
        return '''
            <p class="speech-bubble btn-primary" style="height: 43%;padding-right: 3%;">
                            All fields are mandatory
                            <br>
                            <br>
                                    <input type="text" id="appsymptom" class="form-control" placeholder="Symptom">
                            <br>
                                    <input type="text" id="appdes" class="form-control" placeholder = "Description">
                            <br>
                                    <button class="btn btn-secondary" onclick="appothernew()">Proceed</button>                        
    </p>
            '''
    elif arg == 'newt':
        symp = request.args.get('symptom')
        des = request.args.get('des')
        symp = symp.replace(' ', '_')
        des = des.replace(' ', '_')
        if len(symp) >= 10 and len(des) >= 10:
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/'+symp+'/'+des+'/' + str(ids)
            res = get(url)
            return '''
                <p class="speech-bubble btn-primary" style="height: 7%;">
                Ticket ID : '''+res.text+'''
                </p>
                '''
        else:
            return '''
                <p class="speech-bubble btn-primary" style="height: 10%;">
                Symptom and Description should not be less than 10 characters
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


@app.route('/osrelated', methods=['GET', 'POST'])
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
    elif arg == 'addpc':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/add_pc_with_domain/add_pc_with_domain/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'osnot':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/os_not_booting/os_not_booting/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'osother':
        return '''
            <p class="speech-bubble btn-primary" style="height: 43%;padding-right: 3%;">
                            All fields are mandatory
                            <br>
                            <br>
                                    <input type="text" id="ossymptom" class="form-control" placeholder="Symptom">
                            <br>
                                    <input type="text" id="osdes" class="form-control" placeholder = "Description">
                            <br>
                                    <button class="btn btn-secondary" onclick="osothernew()">Proceed</button>                        
    </p>
            '''
    elif arg == 'newt':
        symp = request.args.get('symptom')
        des = request.args.get('des')
        symp = symp.replace(' ', '_')
        des = des.replace(' ', '_')
        if len(symp) >= 10 and len(des) >= 10:
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/'+symp+'/'+des+'/' + str(ids)
            res = get(url)
            return '''
                <p class="speech-bubble btn-primary" style="height: 7%;">
                Ticket ID : '''+res.text+'''
                </p>
                '''
        else:
            return '''
                <p class="speech-bubble btn-primary" style="height: 10%;">
                Symptom and Description should not be less than 10 characters
                </p>
                '''


@app.route('/printerrelated', methods=['GET', 'POST'])
def printerrelated():
    arg = request.args.get('con1')
    if arg == 'printerrelated':
        return '''
        <p class="speech-bubble btn-primary" style="height: 56%;width:75%">
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
    elif arg == 'notprinter':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/Printer_Not_working/Printer_Not_working/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'notproper':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/Printer_not_proper/Printer_Not_proper/' + \
            str(ids)
        res = get(url)
        return '''
        <p class="speech-bubble btn-primary" style="height: 7%;">
        Ticket ID : '''+res.text+'''
        </p>
        '''
    elif arg == 'otherprint':
        return '''
            <p class="speech-bubble btn-primary" style="height: 43%;padding-right: 3%;">
                            All fields are mandatory
                            <br>
                            <br>
                                    <input type="text" id="printsymptom" class="form-control" placeholder="Symptom">
                            <br>
                                    <input type="text" id="printdes" class="form-control" placeholder = "Description">
                            <br>
                                    <button class="btn btn-secondary" onclick="printother()">Proceed</button>                        
    </p>
            '''
    elif arg == 'newt':
        symp = request.args.get('symptom')
        des = request.args.get('des')
        symp = symp.replace(' ', '_')
        des = des.replace(' ', '_')
        if len(symp) >= 10 and len(des) >= 10:
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/'+symp+'/'+des+'/' + str(ids)
            res = get(url)
            return '''
                <p class="speech-bubble btn-primary" style="height: 7%;">
                Ticket ID : '''+res.text+'''
                </p>
                '''
        else:
            return '''
                <p class="speech-bubble btn-primary" style="height: 10%;">
                Symptom and Description should not be less than 10 characters
                </p>
                '''


@app.route('/networkrelated', methods=['GET', 'POST'])
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
                                    <button class="btn btn-secondary" onclick="wificonf()">Wi-Fi Configuration</button>                        
                            <br>
                                    <button class="btn btn-secondary" onclick="networkother()">Other</button>        
    </p>
        '''
    elif arg == 'ie':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/Internet_explorer_not_working/Internet_explorer_not_working/' + \
            str(ids)
        res = get(url)
        return '''
            <p class="speech-bubble btn-primary" style="height: 7%;">
            Ticket ID : '''+res.text+'''
            </p>
            '''
    elif arg == 'noaccess':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/Unable_to_access_server/Unable_to_access_server/' + \
            str(ids)
        res = get(url)
        return '''
            <p class="speech-bubble btn-primary" style="height: 7%;">
            Ticket ID : '''+res.text+'''
            </p>
            '''
    elif arg == 'ipchange':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/IP_address_change/IP_address_change/' + \
            str(ids)
        res = get(url)
        return '''
            <p class="speech-bubble btn-primary" style="height: 7%;">
            Ticket ID : '''+res.text+'''
            </p>
            '''
    elif arg == 'wifi':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/wi_fi_configuration/wi_fi_configuration/' + \
            str(ids)
        res = get(url)
        return '''
            <p class="speech-bubble btn-primary" style="height: 7%;">
            Ticket ID : '''+res.text+'''
            </p>
            '''
    elif arg == 'other':
        return '''
            <p class="speech-bubble btn-primary" style="height: 43%;padding-right: 3%;">
                            All fields are mandatory
                            <br>
                            <br>
                                    <input type="text" id="netsymptom" class="form-control" placeholder="Symptom">
                            <br>
                                    <input type="text" id="netdes" class="form-control" placeholder = "Description">
                            <br>
                                    <button class="btn btn-secondary" onclick="netother()">Proceed</button>                        
    </p>
            '''
    elif arg == 'newt':
        symp = request.args.get('symptom')
        des = request.args.get('des')
        symp = symp.replace(' ', '_')
        des = des.replace(' ', '_')
        if len(symp) >= 10 and len(des) >= 10:
            url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/newt/'+symp+'/'+des+'/' + str(ids)
            res = get(url)
            return '''
                    <p class="speech-bubble btn-primary" style="height: 7%;">
                    Ticket ID : '''+res.text+'''
                    </p>
                    '''
        else:
            return '''
                    <p class="speech-bubble btn-primary" style="height: 10%;">
                    Symptom and Description should not be less than 10 characters
                    </p>
                    '''
# flow end for new request

# flow know your ticket
@app.route('/knowticket', methods=['GET', 'POST'])
def knowticket():
    arg = request.args.get('con1')
    if arg == 'know':
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/know/'+str(ids)
        res = get(url)
        res = res.json()
        ticket_id = res['Incident ID']
        status = res['Status']
        issue = res['Issue_Class']
        description = res['Description']
        print(ticket_id, status, issue, description)
        ht = '''<p class="speech-bubble btn-light" style="padding-right:3%;">Select one from your previous tickets : <br></p><table class="table" style="background-color: #eec0c6;background-image: linear-gradient(315deg, #eec0c6 0%, #7ee8fa 74%);"><thead class="black white-text"><tr><th scope="col">Ticket ID</th><th scope="col">Status</th><th scope="col">Issue</th><th scope="col">Description</th></tr></thead><tbody>'''
        for i in range(0, len(ticket_id)):
            ht = ht + '''<tr><td>'''+str(ticket_id[str(i)])+'''</td><td>'''+str(status[str(i)])+'''</td><td>'''+str(
                issue[str(i)])+'''</td><td>'''+str(description[str(i)])+'''</td></tr>'''
        ht = ht + '''</tbody></table>'''
        return ht

    elif arg == 'newr':
        return '''
    <p class="speech-bubble btn-primary" style="height: 25%;">
        Please verify the below details to continue with Aforesight
       <br>
       <br>
        Your IP : '''+str(IP)+'''
       <br>
       Your Hostname : '''+str(username.title())+'''
    </p>
    '''
    elif arg == 'proceed':
        tid = request.args.get('id')
        url = 'http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005/oldt/'+str(tid)
        msg = get(url)
        return msg.text
# flow new query
@app.route('/newquery', methods=['GET', 'POST'])
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
        Please verify your Username : '''+str(username.title())+''' and EmailID : xyz@emai.com 
    </p>
    '''

ui.run()

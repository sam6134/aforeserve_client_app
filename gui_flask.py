from flaskwebgui import FlaskUI #get the FlaskUI class
import requests
#from get_data import fetch_data_db
from flask import Flask, request, render_template, jsonify
import printer
import email_s

app = Flask(__name__)

ui = FlaskUI(app)

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

@app.route('/newt/<urgency>/<impact>/<priority>/<classification>/<wg>/<medium>/<symptom>/<description>', methods = ['GET','POST'])
def newt(urgency,impact,priority,classification,wg,medium,symptom,description):
    # urgency = request.args.get('urgency')
    # impact = request.args.get('impact')
    # priority = request.args.get('priority')
    # classification = request.args.get('classification')
    # wg = request.args.get('wg')
    # medium = request.args.get('medium')
    # symptom = request.args.get('symptom')
    # description = request.args.get('description')
    print(urgency,impact,priority,classification,wg,medium,symptom,description)
    url = 'http://35.184.236.4:7005/newt/'+urgency+'/'+impact+'/'+priority+'/'+classification+'/'+wg+'/'+medium+'/'+symptom+'/'+description
    res = requests.get(str(url))
    a = {
        'id':res.text
    }
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
    return(ab)

@app.route('/pr', methods = ['GET','POST'])
def pr():
    flg,out = printer.printerConfig()
    return out

@app.route('/em', methods = ['GET','POST'])
def em():
    flg,out = email_s.mailConfig()

ui.run()
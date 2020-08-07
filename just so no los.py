from flask import Flask, request, render_template, jsonify
import random
from apscheduler.schedulers.background import BackgroundScheduler
import createticket
from predict import *
import pandas as pd
import create_db
import updateticketstatus
import generate_mail

app = Flask(__name__)
# schdular for predict function
# sched = BackgroundScheduler()
# job = sched.add_job(predict,'interval',minutes=10)
# job.remove()
# schdular for update ticket 

# predict()
@app.route('/newt/<symptom>/<description>/<macid>', methods = ['GET','POST'])
def newt(symptom,description,macid):
    print(symptom,description)
    t_id = createticket.loginAndCreateTickets(symptom,description)
#     t_id = "456"
    print(t_id)
    predict(macid)
    generate_mail.raiseticket('bramhesh.srivastav@algo8.ai','issue',t_id)
    return str(t_id)

@app.route('/inoutserver/<macid>')
def inoutserver(macid):
    df = create_db.getuser_Data()
    df = df.loc[df['MAC_ID']==macid]
    print(df)
    ins = df['IN_SERVER'].values[0]
    outs = df['OUT_SERVER'].values[0]
    print(ins,outs)
    data = {
        'inserver':str(ins),
        'outserver':str(outs)
    }
    return jsonify({'inserver':str(ins),'outserver':str(outs)})

@app.route('/userdetails/<Hostname>/<IP_Address>/<MAC_ID>/<Serial_Number>/<OS_Version>/<Laptop_Desktop>/<IN_SERVER>/<OUT_SERVER>/<Direct_Printers>/<User_Name>', methods=['GET', 'POST'])
def userdetail(Hostname, IP_Address, MAC_ID, Serial_Number, OS_Version, Laptop_Desktop, IN_SERVER, OUT_SERVER, Direct_Printers, User_Name):
    print(Hostname, IP_Address, MAC_ID, Serial_Number, OS_Version, Laptop_Desktop, IN_SERVER, OUT_SERVER, Direct_Printers, User_Name)
    df = create_db.getuser_Data()
    if len(df.loc[df["MAC_ID"] == MAC_ID])>0:
        create_db.adduser_update(Hostname, IP_Address, MAC_ID, Serial_Number, OS_Version, Laptop_Desktop, IN_SERVER, OUT_SERVER, Direct_Printers, User_Name)
    else:
        create_db.adduser_details(Hostname, IP_Address, MAC_ID, Serial_Number, OS_Version, Laptop_Desktop, IN_SERVER, OUT_SERVER, Direct_Printers, User_Name)
    return "done"


@app.route('/oldt/<tid>', methods = ['GET', 'POST'])
def oldt(tid):
    query = "select * from Tickets where `Incident ID` = '"+str(tid)+"';"
    df = create_db.fetchquery(query)
    text = 'You had '+str(df.loc[df["Incident ID"] == str(tid)].Description.values[0])+' issue and status is '+str(df.loc[df["Incident ID"] == str(tid)].Status.values[0])
    return text

@app.route('/upt/<tid>', methods = ['GET','POST'])
def upt(tid):
    outp = create_db.updatenew(tid)
#     df = create_db.get_data()
    query = "select * from Tickets where `Incident ID` ='"+str(tid)+"';"
    print(query)
    df = create_db.fetchquery(query)
    print(df["Issue_Class"][0])
    updateticketstatus.updateTicket_2(str(tid),'Resolved','Issue has been successfully resolved')
    generate_mail.updateticket("hardik.seth@prithvi.ai",df["Issue_Class"][0],str(tid))
    if outp == 'Updated':
        return 'Ticket resolved successfully'
    else:
        return 'Some Error While Resolving Issue'
    return 'Ticket resolved successfully'

@app.route('/know/<macid>',methods = ['GET','POST'])
def know(macid):
    query = "select * from Tickets where MAC_ID = '"+macid+"';"
    df = create_db.fetchquery(query)
    df = df.to_json()
    return df

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 7005)
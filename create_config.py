import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {"URL" : "http://35.184.236.4:7005",
                     "Incoming Server": "outlook.office365.com",
                     "Outgoing Server" : "smtp.office.com",
                     "IT helpdesk": "+91-9191919191",
                     "logo": "images/logo.png"}

with open('config_test.ini', 'w') as configfile:
  config.write(configfile)
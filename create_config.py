import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {"URL" : "http://ec2-3-129-90-244.us-east-2.compute.amazonaws.com:7005",
                     "Incoming Server": "outlook.office365.com",
                     "Outgoing Server" : "smtp.office.com",
                     "IT helpdesk": "+91-9191919191",
                     "logo": "images/logo.png"}

with open('config_test.ini', 'w') as configfile:
  config.write(configfile)
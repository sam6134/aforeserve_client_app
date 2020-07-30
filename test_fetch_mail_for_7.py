import pyautogui
import pywinauto
import time
import pandas as pd


from ctypes import *
from pywinauto.controls.win32_controls import ButtonWrapper
from pywinauto.keyboard import send_keys, KeySequenceError
import config
flag=0
def mailConfig(username,inser,outser,email_ss,password_s):
    try:
        #windll.user32.BlockInput(True)
        global flag
        config.logger.info('opening control panel for email configuration ')
        control_panel=pywinauto.Application(backend='uia').start(r'C:\Windows\System32\control.exe',timeout=50)
                
        #time.sleep(4)
        
        #pyautogui.hotkey('win','up')
        
        time.sleep(2)
        
        window=None
        
        def checkForWindowExistence(window_title):
            
            print(window_title)
            global window
            #print('WINDOW IS ',window)
            config.logger.info('Searching for '+str(window_title)+' via infinite loop')
            while True:
                print('In Loop part')
                try:
                    window=pywinauto.findwindows.find_windows(best_match=window_title)
                except:
                    window=None
                if window:
                    break
            print('Out of Loop part',window)
            
            return window
        
        try:  
            config.logger.info('Searching for All Control Panel Items window')
            control_panel_window=pywinauto.findwindows.find_windows(best_match=u'All Control Panel Items')
        except:
            control_panel_window=checkForWindowExistence(u'All Control Panel Items')
        
        
        if control_panel_window:
            
            mail=control_panel.window_(handle=control_panel_window[0])
            
            mail.set_focus()
            try:
                
                mail.child_window(title="Category").click()
                time.sleep(2)
                pyautogui.press('down',presses=2)
                pyautogui.press('enter')
                
            except Exception as e:
                
                pass
                #print(e)
                
            #click mail icon on control panel   
            #try:
            #config.logger.info('Searching for Mail (Microsoft Outlook 2016) (32-bit) icon')
            #mail.child_window(title="Mail (Microsoft Outlook 2016) (32-bit)").wait('visible', timeout=120, retry_interval=0.5).click_input()
            #print('Code in try block')
            #except Exception as e:
            config.logger.info('Searching for Mail icon')
            mail.child_window(title="Mail", auto_id="name").wait('visible', timeout=120, retry_interval=0.5).click_input()
            #print('Code in except block')
                
            #time.sleep(20)
            try:
                config.logger.info('Searching for Mail Setup - AFS window')
                mail_setup_outlook=pywinauto.findwindows.find_windows(best_match='Mail Setup - AFS')
            except:
                mail_setup_outlook=checkForWindowExistence('Mail Setup - AFS)
            
            if mail_setup_outlook:
                        mail_setup_outlook=control_panel.window_(handle=mail_setup_outlook[0])
                        mail_setup_outlook.set_focus()
                        #mail_setup_outlook.
                        #mail_setup_outlook.child_window(title_re="Email Accounts...",control_type="Button").click()
                        try:
                        config.logger.info('Searching for E-mail Accounts button')
                        mail_setup_outlook.child_window(title_re="E-mail Accounts...",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                        except:
                        mail_setup_outlook.child_window(title_re="E-mail Accounts...",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                        print("test-1")    
                    # time.sleep(5)
                        
                        try:
                            config.logger.info('Searching for Account Settings window')
                            print('Searching for Account Settings window')
                            account_settings=pywinauto.findwindows.find_windows(best_match='Account Settings')
                        except:
                            account_settings=checkForWindowExistence(u'Account Settings')
                        
                        if account_settings:
                            account_settings=control_panel.window_(handle=account_settings[0])
                            account_settings.set_focus()
                            try:
                                config.logger.info('Clicking on Email and New button in Account Settings window')
                                print('Clicking on Email and New button in Account Settings window')
                                #account_settings.child_window(title="Email").wait('visible', timeout=120, retry_interval=0.5).click_input()
                                mail_setup_outlook.child_window(title="New...", control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                print('In try')
                            except:
                                account_settings.child_window(title="New...", control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                print('In Except')
                            
                            
                            #time.sleep(4)
                            try:
                                config.logger.info('Searching for Add Account window for clicking on Manual Setup radio button')
                                print('Searching for Add Account window for clicking on Manual Setup radio button')
                                add_account=pywinauto.findwindows.find_windows(best_match='Add New E-mail Account')
                                print("Done-test1")
                            except:
                                add_account=checkForWindowExistence(u'Add New E-mail Account')
                            
                            if add_account:
                                add_account=control_panel.window_(handle=add_account[0])
                                add_account.set_focus()
                                add_account.child_window(title="Manually configure server settings or additional server types",control_type="CheckBox").wait('visible', timeout=120, retry_interval=0.5).click()
                                add_account.child_window(title="Next >",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                
                                time.sleep(4)
                                
                                try:
                                    #config.logger.info('Searching for Add Account window for clicking on POP or IMAP radio button')
                                    print('Searching for Add Account window for clicking on POP or IMAP radio button')
                                    add_account=pywinauto.findwindows.find_windows(best_match='Add New E-mail Account')
                                
                                except:
                                    add_account=checkForWindowExistence(u'Add New E-mail Account')
                                
                                if add_account:
                                    add_account=control_panel.window_(handle=add_account[0])
                                    add_account.set_focus()
                                    add_account.child_window(title="Internet E-mail",control_type="RadioButton").wait('visible', timeout=120, retry_interval=0.5).click()
                                    add_account.child_window(title="Next >",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                    
                                    
                                    #time.sleep(4)
                                    
                                    try:
                                        config.logger.info('Searching for Add Account window for entering user details recevied via chatbot')
                                        add_account=pywinauto.findwindows.find_windows(best_match='Add New E-mail Account')
                                    
                                    except:
                                        add_account=checkForWindowExistence(u'Add New E-mail Account')
                                        
                                    if add_account:
                                        add_account=control_panel.window_(handle=add_account[0])
                                        add_account.set_focus()
                                        
                                        
                                        #user_details=pd.read_csv('http://127.0.0.1:8000/input.csv').columns
                                        
                                        user_details=[username,email_ss,password_s
                                        
                                        add_account["Your Name:Edit"].type_keys(user_details[0])    
                                        
                                        add_account["Email Address:Edit"].type_keys(user_details[1])
                                        
                                        add_account["Incoming mail server:Edit"].type_keys(inser)
                                        
                                        add_account["Outgoing mail server (SMTP):Edit"].type_keys(outser)
                                        
                                        add_account["User Name:Edit"].type_keys('^a{BACKSPACE}')
                                        #add_account["User Name:Edit"].Edit.set_edit_text(u'')
                                        
                                        add_account["Password:Edit"].type_keys(user_details[2])
                                        
                                        add_account["User Name:Edit"].type_keys(user_details[1])
                                        
                                        add_account.child_window(title="More Settings ...").wait('visible', timeout=120, retry_interval=0.5).click()
                                        
                                        time.sleep(4)
                                        
                                        try:
                                            config.logger.info('Searching for Internet Email Settings for entering Incoming and Outgoing port details')
                                            internet_email_settings=pywinauto.findwindows.find_windows(best_match='Internet Email Settings')
                                        
                                        except:
                                            internet_email_settings=checkForWindowExistence(u'Internet Email Settings')
                                        
                                        if internet_email_settings:
                                            
                                            internet_email_settings=control_panel.window_(handle=internet_email_settings[0])
                                            
                                            internet_email_settings.set_focus()
                                        
                                            internet_email_settings.child_window(title="Outgoing Server").wait('visible', timeout=120, retry_interval=0.5).click_input()
                                            
                                            send_keys('some text{TAB 2}')
                                            send_keys('some text{SPACE}')
                                            #internet_email_settings.child_window(title="My outgoing server (SMTP) requires authentication",control_type="RadioButton").wait('visible', timeout=120, retry_interval=0.5).click()
                                            
                                            internet_email_settings.child_window(title="Advanced").wait('visible', timeout=120, retry_interval=0.5).click_input()
                                            
                                            internet_email_settings.child_window(title="Incoming server (POP3):",control_type="Edit").type_keys('^a{BACKSPACE}')
                                            
                                            internet_email_settings.child_window(title="Incoming server (POP3):",control_type="Edit").type_keys('995')
                                            pyautogui.press('tab')
                                            pyautogui.press('tab')
                                            pyautogui.press('space')
                                    
                                            internet_email_settings.child_window(title="Outgoing server (SMTP):",control_type="Edit").type_keys('^a{BACKSPACE}')
                                            
                                            internet_email_settings.child_window(title="Outgoing server (SMTP):",control_type="Edit").type_keys('587')
                                            
                                        
                                            
        
                                            try:
                                                internet_email_settings.child_window(title="Use the following type of encrypted connection:",control_type="ComboBox").select('Auto')
                                            
                                            except:
                                                pass
                                            
                                            
                                            #pyautogui.press('enter')
                                            internet_email_settings.child_window(title="OK",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                            
                                            add_account.child_window(title="Next >",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                            send_keys('"%{F4}"')
                                            time.sleep(2)
                                            test_account=pywinauto.findwindows.find_windows(best_match='Account Settings')
                                            test_account=control_panel.window_(handle=test_account[0])
                                            test_account.set_focus()
                                            time.sleep(2)
                                            pyautogui.press('tab',presses=4)
                                            #send_keys('{DOWN}')
                                            time.sleep(2)
                                            send_keys('"%{ENTER}')
                                            try:
                                                config.logger.info('Searching for change Account window for entering user details recevied via chatbot')
                                                change_account=pywinauto.findwindows.find_windows(best_match='Change E-mail Account')
                                    
                                            except:
                                                change_account=checkForWindowExistence(u'Change E-mail Account')
                                            change_account=control_panel.window_(handle=change_account[0])
                                            change_account.set_focus()
                                            change_account.child_window(title='Test Account Settings ...',control_type="Button").wait('visible',timeout=10, retry_interval=0.5).click()
                                            while(1):
                                                try:
                                                    config.logger.info('Searching for change Account window for entering user details recevied via chatbot')
                                                    change_account=pywinauto.findwindows.find_windows(best_match='Internet Security Warning')
                                                    if(change_account==None):
                                                        continue
                                                    break
                                                except:
                                                    continue
                                            change_account=control_panel.window_(handle=change_account[0])
                                            change_account.set_focus()
                                            change_account.child_window(title='Yes',control_type="Button").wait('visible',timeout=10, retry_interval=0.5).click()
                                            while(1):
                                                print("In our test while")
                                                
                                                print('Searching for change Account window for entering user details recevied via chatbot')
                                                try:
                                                    change_account=pywinauto.findwindows.find_windows(best_match='Internet Security Warning')
                                                    if(change_account):
                                                        break
                                                except:
                                                        
                                                        print("Into except TEST")
                                                        try:
                                                            invalid_password = pywinauto.findwindows.find_windows(best_match='Enter Network Password')
                                                            if(invalid_password != None):
                                                                send_keys('"%{F4}"')
                                                        
                                                                send_keys('"%{F4}"')
                                                        
                                                                send_keys('"%{F4}"')
                                                        
                                                                send_keys('"%{F4}"')
                                                        
                                                                send_keys('"%{F4}"')
                                                        
                                                                send_keys('"%{F4}"')
                                                                return "Invalid Password"
                                                                
                                                        except:
                                                            print("Both windows not found")
                                                            continue
                                                    
                                            change_account=control_panel.window_(handle=change_account[0])
                                            change_account.set_focus()
                                            change_account.child_window(title='Yes',control_type="Button").wait('visible',timeout=10, retry_interval=0.5).click()
                                            try:
                                                config.logger.info('Searching for change Account window for entering user details recevied via chatbot')
                                                change_account=pywinauto.findwindows.find_windows(best_match='Test Account Settings')
                                    
                                            except:
                                                change_account=checkForWindowExistence(u'Test Account Settings')
                                            change_account=control_panel.window_(handle=change_account[0])
                                            change_account.set_focus()
                                            time.sleep(5)
                                            change_account.child_window(title='Close',control_type="Button").wait('visible',timeout=60, retry_interval=0.5).click()
                                            
                                            #time.sleep(5)
                                            #test_account=pywinauto.findwindows.find_windows(best_match='Account Settings')
                                            #test_account=control_panel.window_(handle=test_account[0])
                                            #test_account.set_focus()
                                            #test_account.child_window(title='Close',control_type="Button").wait('visible',timeout=120, retry_interval=0.5).click()
                                        
                                            #time.sleep(5)
                                            #add_account.child_window(title="Finish", control_type="Button").click()
                                            #time.sleep(2)
                                            #add_account.child_window(title="Cancel", control_type="Button").click()
                                            time.sleep(2)
                                            
                                            #account_settings.child_window(title='Close',control_type="Button").wait('visible',timeout=120, retry_interval=0.5).click()
                                            #account_settings.child_window(title="Close", control_type="Button").click()
                                            send_keys('"%{F4}"')
                                            
                                            time.sleep(2)
                                            send_keys('"%{F4}"')
                                            #mail_setup_outlook.child_window(title="Close", control_type="Button").click()
                                            
                                            time.sleep(2)
                                            send_keys('"%{F4}"')
                                            send_keys('%{F4}')
                                            flag=1
        
        
        #windll.user32.BlockInput(False)
        return "Success"
    except:
        return "Failure"


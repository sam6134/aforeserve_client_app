import pyautogui
import pywinauto
import time
import config

flag=0

def printerConfig(manufac_name,mdelname):
    
    global flag
    
    config.logger.info('opening control panel for printer configuration ')
    
    control_panel=pywinauto.Application(backend='uia').start(r'C:\Windows\System32\control.exe',timeout=50)
        
    time.sleep(2)
    
    pyautogui.hotkey('win','up')
    
    #time.sleep(5)
    # click on device and printers button 
    window=None
    
    def checkForWindowExistence(window_title):
        
        print(window_title)
        global window
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
        
        config.logger.info(str(window_title)+' is obtained')    
        
        return window
    
    def checkForHeaderInWindows(window,header,control_type):
        
        header_flag=window.child_window(title=header,control_type=control_type).exists()
        if header_flag:
            return header_flag
        while header_flag!=True:
            header_flag=window.child_window(title=header,control_type=control_type).exists()
        return header_flag
        
    try:
        config.logger.info('Searching for All Control Panel Items window')
        control_panel_window=pywinauto.findwindows.find_windows(best_match=u'All Control Panel Items')
    except:
        control_panel_window=checkForWindowExistence(u'All Control Panel Items')
        
    time.sleep(5)
    
    if control_panel_window:
         device_printers=control_panel.window_(handle=control_panel_window[0])
         device_printers.set_focus()
         device_printers.child_window(best_match="Devices and Printers", auto_id="name", control_type="Hyperlink").click_input()
         #click on Add a printer
         #time.sleep(8)
         try:
             config.logger.info('Searching for Devices and Printers window')
             device_printer_window=pywinauto.findwindows.find_windows(best_match=u'Devices and Printers')
         except:
             device_printer_window=checkForWindowExistence(u'Devices and Printers')
             
         if device_printer_window:
            device_printer_window=control_panel.window_(handle=device_printer_window[0])
            time.sleep(3)
            device_printer_window.set_focus()
            device_printer_window.child_window(title="Add a printer",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
            #time.sleep(5)
            # click on printer not listed'
            try:
                config.logger.info('Searching for Add a Device window')
                add_a_device_window=pywinauto.findwindows.find_windows(best_match=u'Add a device')
            except:
                add_a_device_window=checkForWindowExistence(u'Add a device')
                
            time.sleep(5)
            if add_a_device_window:
                add_a_device_window=control_panel.window_(handle=add_a_device_window[0])
                add_a_device_window.set_focus()
                add_a_device_window.child_window(title="The printer that I want isn't listed").wait('visible', timeout=120, retry_interval=0.5).click_input()
                #time.sleep(5)
                
                #add a local printer
                try:
                    config.logger.info('Searching for Add Printer window for a adding a local printer')
                    add_a_local_printer=pywinauto.findwindows.find_windows(best_match=u'Add Printer')
                except:
                    add_a_local_printer=checkForWindowExistence(u'Add Printer')
                    
                if add_a_local_printer:
                    add_a_local_printer=control_panel.window_(handle=add_a_local_printer[0])
                    add_a_local_printer.set_focus()
                    add_a_local_printer.child_window(title="Add a local printer or network printer with manual settings",control_type="RadioButton").wait('visible', timeout=120, retry_interval=0.5).click()
                    add_a_local_printer.child_window(title="Next",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                    #time.sleep(5)
                    
                    # select printer port
                    try:
                        config.logger.info('Searching for Add Printer window for selecting printer port')
                        new_port=pywinauto.findwindows.find_windows(best_match=u'Add Printer')
                    except:
                        new_port=checkForWindowExistence(u'Add Printer')
                        
                    if new_port:
                        new_port=control_panel.window_(handle=new_port[0])
                        new_port.set_focus()
                        header_flag=checkForHeaderInWindows(new_port,'Choose a printer port','Text')
                        if header_flag:
                            new_port.child_window(title="Create a new port:", control_type="RadioButton").wait('visible', timeout=120, retry_interval=0.5).click()
                            new_port.child_window(title="Type of port:", control_type="ComboBox").select('Standard TCP/IP Port')
                            time.sleep(1)
                            new_port.child_window(title="Next",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                            #time.sleep(5)
                            
                            # add hostname and portname
                            try:
                                config.logger.info('Searching for Add Printer window for adding hostname and portname')
                                printer_host_port=pywinauto.findwindows.find_windows(best_match=u'Add Printer')
                            except:
                                printer_host_port=checkForWindowExistence(u'Add Printer')
                                
                            if printer_host_port:
                                printer_host_port=control_panel.window_(handle=printer_host_port[0])
                                printer_host_port.set_focus()
                                header_flag=checkForHeaderInWindows(printer_host_port,'Type a printer hostname or IP address','Text')
                                
                                if header_flag:
                                    printer_host_port.child_window(title="Hostname or IP address:", control_type="Edit").wait('visible', timeout=120, retry_interval=0.5).type_keys('10.0.1.14')
                                    #printer_host_port.child_window(title="Port name:",control_type="Edit").type_keys("{BACKSPACE}")
                                    #printer_host_port.child_window(title="Port name:", control_type="Edit").type_keys('adi129_10.0.1.14')
                                    printer_host_port.child_window(title="Next",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                    #time.sleep(65)
                                    
                                    #additional port info
                                    try:
                                        config.logger.info('Searching for Add Printer window for additonal printer info')
                                        additional_port_info=pywinauto.findwindows.find_windows(best_match=u'Add Printer')
                                        print('Code in try block')
                                        print(additional_port_info)
                                    except:
                                        print('Code in Except block')
                                        additional_port_info=checkForWindowExistence(u'Add Printer')
                                        
                                    if additional_port_info:
                                        try:
                                            additional_port_info=control_panel.window_(handle=additional_port_info[0])
                                            print('Entered')
                                            additional_port_info.set_focus()
                                            header_flag=checkForHeaderInWindows(additional_port_info,'Additional port information required','Text')
                                            if header_flag:
                                                additional_port_info.child_window(title="Next",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                        except:
                                            pyautogui.press('enter')
                                            print('Sleeping')
                                            #time.sleep(70)
                                            print('Done Sleeping')
                                            #install printer driver
                                        try:
                                            config.logger.info('Searching for Add Printer window for selecting manufacturer name and printer name')
                                            printer_driver=pywinauto.findwindows.find_windows(best_match=u'Add Printer')
                                        except:
                                            printer_driver=checkForWindowExistence(u'Add Printer')
                                        
                                        if printer_driver:
                                            printer_driver=control_panel.window_(handle=printer_driver[0])
                                            printer_driver.set_focus()
                                            header_flag=checkForHeaderInWindows(printer_driver,'Install the printer driver','Text')
                                            #printer_model=pd.read_csv('http://127.0.0.1:8000/input.csv').columns
                                            if header_flag:
                                                #printer_model=['Microsoft','Microsoft OpenXPS Class Driver']
                                                model_name,model_type=manufac_name,mdelname
                                                time.sleep(5)
                
                                                # ask from chatbot
                                                printer_driver.child_window(title=model_name, control_type="ListItem").select()
                                                #printer_driver.child_window(title="Printers", auto_id="HeaderItem 0", control_type="HeaderItem").ListView()
                                                #a.get_item('Remote Desktop Easy Print').click()
                                                # ask from chatbot
                                                time.sleep(2)
                                                printer_driver.child_window(best_match=model_type, control_type="ListItem").select()
                                                time.sleep(2)
                                                printer_driver.child_window(title="Next",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                                #time.sleep(5)
                                                
                                                # confirmation for version
                                                #try:
                                                 #   config.logger.info('Searching for Add Printer window for confirming printer version')
                                                  #  printer_version_confirm=pywinauto.findwindows.find_windows(best_match=u'Add Printer')
                                                #except:
                                                 #   printer_version_confirm=checkForWindowExistence(u'Add Printer')
                                                
                                                #if printer_version_confirm:
                                                 #   printer_version_confirm=control_panel.window_(handle=printer_version_confirm[0])
                                                 #   printer_version_confirm.set_focus()
                                                  #  header_flag=checkForHeaderInWindows(printer_version_confirm,'Which version of the driver do you want to use?','Text')
                                                   # if header_flag:
                                                    #    printer_version_confirm.child_window(title="Next",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                                    #time.sleep(5)                          
                                                    #click for printer name
                                                try:
                                                    config.logger.info('Searching for Add Printer window for selecting printer name')
                                                    printer_name=pywinauto.findwindows.find_windows(best_match=u'Add Printer')
                                                except:
                                                    printer_name=checkForWindowExistence(u'Add Printer')
                
                                                if printer_name:
                                                    printer_name=control_panel.window_(handle=printer_name[0])
                                                    printer_name.set_focus()
                                                    header_flag=checkForHeaderInWindows(printer_name,'Type a printer name','Text')
                                                    if header_flag:
                                                        printer_name.child_window(title="Next",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                
                                                        #time.sleep(10)
                                                        
                                                        #click for printer don't share
                                                    try:
                                                        config.logger.info('Searching for Add Printer window for selecting printer do not share')
                                                        printer_not_share=pywinauto.findwindows.find_windows(best_match=u'Add Printer')
                                                    except:
                                                        printer_not_share=checkForWindowExistence(u'Add Printer')
                                                        
                                                    try:
                                                        if printer_not_share:
                                                            printer_not_share=control_panel.window_(handle=printer_not_share[0])
                                                            printer_not_share.set_focus()
                                                            print('Share in try')
                                                            header_flag=checkForHeaderInWindows(printer_name,'Printer Sharing','Text')
                                                            if header_flag:
                                                                printer_not_share.child_window(title="Next",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                                    except:
                                                        pyautogui.press('tab')
                                                        pyautogui.press('enter')
                                                        print('Share in except')
                                                            #time.sleep(5)
                                                            #click finish for successful installation
                                                    try:
                                                        config.logger.info('Searching for Add Printer window for selecting finish button')
                                                        finish_page=pywinauto.findwindows.find_windows(best_match=u'Add Printer')
                                                    except:
                                                        finish_page=checkForWindowExistence(u'Add Printer')
                                                    try:
                                                        if finish_page:
                                                            finish_page=control_panel.window_(handle=finish_page[0])
                                                            finish_page.set_focus()
                                                            header_flag=checkForHeaderInWindows(finish_page,'Print a test page','Button')
                                                            if header_flag:
                                                                print('Finish in try')
                                                                finish_page.child_window(title="Finish",control_type="Button").wait('visible', timeout=120, retry_interval=0.5).click()
                                                    except:
                                                        print('Finish in except')
                                                        pyautogui.press('tab')
                                                        pyautogui.press('tab')
                                                        pyautogui.press('enter')

                                                    config.logger.info("Default printer not set window closing")
                                                        
                                                    try:
                                                        last_page = pywinauto.findwindows.find_windows(best_match=u'Add Printer')
                                                        if last_page:
                                                            last_page=control_panel.window_(handle=last_page[0])
                                                            last_page.set_focus()
                                                            header_flag=checkForHeaderInWindows(last_page,"Default printer cannot be set.","Text")
                                                            last_page.child_window(title='OK',control_type="Button").wait('visible',timeout=120, retry_interval=0.5).click()
                                                            print('Finish in try for last page')
                                                    except:
                                                        print('Finish in except for last page')
                                                        pyautogui.press('enter')
                                                            
                                                    device_printer_window.child_window(title="Close", control_type="Button").click()
                                                             
    flag=1
    return flag,'Successfully Configured'
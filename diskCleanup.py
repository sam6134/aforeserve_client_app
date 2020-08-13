import os
def startCleanup():

    try:
        clean=os.popen('cleanmgr.exe /sagerun:1').read() 
        return "Success"
    except:
        return "Failed"

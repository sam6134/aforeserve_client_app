import subprocess

def startCleanup():

    p = subprocess.Popen([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe","-ExecutionPolicy",
                          "Unrestricted","./Start-Cleanup.ps1"])
    #,stdout=sys.stdout
    #print(p.communicate())
    
    return p.errors,'Success'
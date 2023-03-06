import time
import network
import functions
import SysData
import machine
ssid = "Kliksafe"
password = "Klaasse750?"
time.sleep(0.1)
station = network.WLAN(network.STA_IF)
Autoinstall = True
SettingsRootPage = "https://Clock.matthiasklaasse.repl.co"
if station.isconnected() == False:
    functions.launchWifi(ssid, password)
def update():
    maxsoft = functions.checkupdate()
    print(maxsoft)
    if SysData.Softwareversion < int(maxsoft):
        if Autoinstall:
            print("Update to version "+str(SysData.Softwareversion+1))
            CommandPath = SettingsRootPage+"/updaters/updater"+str(SysData.Softwareversion+1)+".py"
            print(CommandPath)
            UpdateCommand = functions.getPage(CommandPath)
            try:
                exec(UpdateCommand)
            except:
                machine.reset()
            data = open("SysData.py", "w") 
            data.write("Softwareversion = "+str(SysData.Softwareversion+1)) 
            data.close()
            print("Update done")
            machine.reset()
try:
    update()
except:
    machine.reset()
import Boot
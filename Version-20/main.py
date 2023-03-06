import time
import network
import functions
import SysData
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
            CommandPath = SettingsRootPage+"/updaters/updater"+str(SysData.Softwareversion+1)+".py"
            print(CommandPath)
            UpdateCommand = functions.getPage(CommandPath)
            exec(UpdateCommand)
update()
import Boot
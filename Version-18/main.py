try:
    import bootscreen
    import functions
    import time
    import network
    import SysData
    import machine
    ssid = "Kliksafe"
    password = "Klaasse750?"
    time.sleep(0.1)
    station = network.WLAN(network.STA_IF)
    Autoinstall = True
    SettingsRootPage = "https://Clock.matthiasklaasse.repl.co"

    print(functions.launchWifi(ssid, password))

    pixels = functions.setupNeopixels()
    dots = functions.setupDots()


            
    def update():
        maxsoft = functions.checkupdate()
        print(maxsoft)
        if SysData.Softwareversion < int(maxsoft):
            for i in range(4):
                if i == 2:
                    dots[0] = [0,0,0]
                    dots[1] = [0,0,0]
                else:
                    dots[0] = [50,0,0]
                    dots[1] = [0,50,0]
                dots.write()
                for l in range(7):
                    if functions.bootanimation[i][l] == 1:
                        pixels[i*7+l] = [0,50,0]
                        time.sleep(0.1)
                        pixels.write()
            if Autoinstall:
                print("Updateing to version "+str(SysData.Softwareversion+1))
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
except:
    import Errorhandler
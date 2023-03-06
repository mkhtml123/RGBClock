import functions
import time
import random
try:
  import usocket as socket
except:
  import socket
from machine import Pin
import network
import esp
esp.osdebug(None)
import gc
import os
import SysData
gc.collect()

station = network.WLAN(network.STA_IF)



SettingsRootPage = "https://Clock.matthiasklaasse.repl.co"
Date = functions.setupTime()
Hours = Date[0]
Minutes = Date[1]
Pixels = functions.setupNeopixels()
Dots = functions.setupDots()
RootHTML = open("Webpage/html/index.html").read()
colorsHTML = open("Webpage/html/colors.html").read()
colorsjs = open("Webpage/java/colors.js").read()
Stlye = open("Webpage/css/style.css").read()
General = open("Webpage/html/general.html").read()
Script = open("Webpage/java/script.js").read()


animationspeed = functions.animationspeed
animated = functions.animated
Numbers = functions.Numbers
Bootdisplay = functions.bootanimation
Colors = functions.colors
Digits = [0,0,0,0]
rgb = [100,100,0]
rgbd = [0,0,0]
countfornc = 0
animationfrequency = 0
color = 0
brightness = 100
webmode = False
webmodec = 0
updatesettings = True
autobright = True
Autoinstall = True
CheckMinute = 23

ap = network.WLAN(network.AP_IF)
ap.active(False)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
s.settimeout(0.2)


while True:
    if updatesettings:
        updatesettings = False
        with open('Settings/General.txt', 'r') as setting:
            text = setting.readlines()
            animationfrequency = int(text[2])
            if text[0].startswith("true"):
                animationspeed = int(text[1])
                animated = True
            else:
                animated = False
                animationspeed = 255
            if text[3].startswith("true"):
                autobright = True
            else:
                autobright = False
            brightness = int(text[4])
    try:
        conn, addr = s.accept()
        wemode = True
        webmodec = 0
        request = conn.recv(1024)
        request = str(request)
        request = request.split(" ")[1]
        print(request)
        if request == "/":
           conn.sendall(RootHTML)
        elif request == "/index.html":
            conn.sendall(RootHTML)
        elif request == "/style.css":
            conn.sendall(Stlye)
        elif request == "/colors.html":
            conn.sendall(colorsHTML)
        elif request == "/colors.js":
            conn.sendall(colorsjs)
        elif request == "/updatepackages":
            conn.sendall("alr")
            RootHTML = functions.getPage(SettingsRootPage)
            Stlye = functions.getPage(SettingsRootPage+"/style.css")
            General = functions.getPage(SettingsRootPage+"/general.html")
            Script = functions.getPage(SettingsRootPage+"/script.js")
        elif request == "/general.html":
            conn.sendall(General)
        elif request == "/script.js":
            conn.sendall(Script)
        elif request == ("/Getgeneral"):
            ing = open('Settings/General.txt', 'r')
            resp = ""
            for data in ing.readlines():
                resp = resp+data
            conn.sendall(resp)
        elif request == ("/getcolors"):
            ing = open('Settings/colors.txt', 'r')
            resp = ""
            for data in ing.readlines():
                resp = resp+data
            print(resp)
            conn.sendall(resp)
        elif request.startswith("/Addcolor"):
            os.remove('Settings/colors.txt')
            newcolor = request
            print(newcolor)
            newcolor = request.split(",")
            print(newcolor)
            newcolor.pop(0)
            print(newcolor)
            with open('Settings/colors.txt', 'x') as colorfile:
                colorfile.write("\n".join(newcolor))
            conn.sendall("New settings applied")
            functions.reloadcolors()
        elif request.startswith("/Setgeneral,"):
            os.remove('Settings/General.txt')
            newsettings = request
            newsettings = request.split(",")
            newsettings.pop(0)
            newsettings.pop(len(newsettings)-1)
            with open('Settings/General.txt', 'x') as ing:
                for i in newsettings:
                    e=i
                    if e == "":
                        e=0
                    ing.write(e)
                    ing.write("\n")
                conn.sendall("New settings applied")
                updatesettings = True
        else:
            conn.sendall("We dont know what you mean with "+request+"\n\n\n\n\n\n\n\nYou can call that ERROR 404")
        conn.close()
    except Exception as e:
        if autobright:
            brightness = functions.GetBrightness()
        webmodec+=1
        functions.updatepx(Digits, animationspeed, rgb, rgbd, brightness)
        Digits = functions.MakeDigits(Date[0], Date[1])
        Date = functions.setupTime()
        countfornc += 1
        if countfornc > animationfrequency-1:
            countfornc = 0
            colordata = functions.newc(color)
            rgb = colordata[0]
            color = colordata[1]
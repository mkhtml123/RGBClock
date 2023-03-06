#version1
import machine
import neopixel

p = machine.Pin(2)
Pixels = neopixel.NeoPixel(p, 28)
p = machine.Pin(0)
Dots = neopixel.NeoPixel(p, 2)

import time
import ntptime
def setntptime():
    try:
        ntptime.settime()
    except:
        setntptime()
        
setntptime()

UTC_OFFSET = 1 * 60 * 60

SettingRGB = [0,250,0]
SettingRGBd = [0,0,0]

hostssid = "Clock"
hostpassword = "Clock123"

Numbers = [
  [1, 1, 1, 0, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 0],
  [1, 1, 0, 1, 0, 1, 1],
  [1, 1, 0, 1, 1, 1, 0],
  [1, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [0, 1, 1, 1, 1, 1, 1],
  [1, 1, 0, 0, 1, 0, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0]
]

bootanimation = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1]
]

settext = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1]
]

animated = True
colors = [] 
r=0
with open('Settings/colors.txt', 'r') as colorfile:
    line = colorfile.readlines()
    for i in range(int(len(line))/3):
        temp = [0,0,0]
        for v in range(3):
            temp[v] = int(line[i*3+v])
        colors.append(temp)


animationspeed = 4


def reloadcolors():
    with open('Settings/colors.txt', 'r') as colorfile:
        line = colorfile.readlines()
        for i in range(int(len(line))/3):
            temp = [0,0,0]
            for v in range(3):
                temp[v] = int(line[i*3+v])
            colors.append(temp)


def setupTime():
    actual_time = time.localtime(time.time() + UTC_OFFSET)
    Hours = actual_time[3]
    Minutes = actual_time[4]
    return [Hours, Minutes]

def setupNeopixels():
    return Pixels

def updatecolors(new):
    with open('Settings/colors.txt', 'r') as colorfile:
        line = colorfile.readlines()
        colors = []
        for i in range(int(len(line))/3):
            temp = [0,0,0]
            for v in range(3):
                temp[v] = int(line[i*3+v])
            colors.append(temp)
            
def setupDots():
    return Dots
def GetBrightness():
    f=0
    from machine import Pin, ADC
    Light = ADC(0)
    if int(Light.read()/11)>99:
        f = 99
    elif int(Light.read()/11)<10:
        f = 8
    else:
         f = int(Light.read()/11)
    return int(f/0.8)
    
def newc(color):
    color+=1
    if color == len(colors):
        color = 0
    return [colors[color], color]

def launchWifi(ssid, psk):
    import network
    import time
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=hostssid, password=hostpassword)
    wl = network.WLAN()
    wl.active(1)
    wl.connect(ssid, psk)
    sta_if = network.WLAN(network.STA_IF)
    return sta_if.ifconfig()


def getPage(link):
    import urequests
    response = urequests.get(link)
    return response.text
    response.close()

def checkupdate():
    return getPage("https://Clock.matthiasklaasse.repl.co/SoftwareMax1")

def MakeDigits(Hours, Minutes):
    Hours = str(Hours)
    Minutes = str(Minutes)    
    Digits = [0,0,0,0]
    if len(Minutes) == 1:
        Minutes = "0"+Minutes
    if len(Hours) == 1:
        Hours = "0"+Hours

    DBackup = Digits
    Digits[0] = Minutes[1]
    Digits[1] = Minutes[0]
    Digits[2] = Hours[1]
    Digits[3] = Hours[0]
    return Digits

    

def updatepx(Digits, AnimationSpeed, rgb, rgbd, brightness, animated):
    drgb = [0,0,0]
    for d in range(3):
        drgb[d] = int(rgb[d]/100*brightness)
    speed = brightness/AnimationSpeed+0.1
    Dots[0] = drgb
    Dots[1] = drgb
    for d in range(4):
        for l in range(7):
            Light = Numbers[int(Digits[d])][l]
            pi = (d*7)+l
            newc = list(Pixels[pi])
            if Light == 1:
                for c in range(3):
                    col = rgb[c]/100*brightness
                    if newc[c] < col:
                        if col - newc[c] < speed or animated == False:
                            newc[c] = col
                        else:
                            newc[c]+=speed
                    if newc[c] > col:
                        if newc[c] - col < speed or animated == False:
                            newc[c] = col
                        else:
                            newc[c]-=speed
            else:
                for c in range(3):
                    col = rgbd[c]/100*brightness
                    if newc[c] < col:
                        if col - newc[c] < speed or animated == False:
                            newc[c] = col
                        else:
                            newc[c]+=speed
                    if newc[c] > col:
                        if newc[c] - col < speed or animated == False:
                            newc[c] = col
                        else:
                            newc[c]-=speed
            for t in range(3):
                newc[t] = int(newc[t])
            Pixels[pi] = newc 
    Pixels.write()    
    Dots.write()
    
def sett(br):
    Dots[0] = SettingRGB
    Dots[1] = SettingRGB
    for d in range(4):
        for l in range(7):
            if settext[d][l] == 1:
                Pixels[d*7+l] = (int(SettingRGB[0]/100*br), int(SettingRGB[1]/100*br), int(SettingRGB[2]/100*br))
            else:
                Pixels[d*7+l] = (int(SettingRGBd[0]/100*br), int(SettingRGBd[1]/100*br), int(SettingRGBd[2]/100*br))
    Pixels.write()
    Dots.write()

def fetchssysinfo():
    Response = []
    Response.insert()
import urequests

boot = open("Boot.py", "w") 
boot.write(functions.getPage("https://clock.matthiasklaasse.repl.co/Version-18/Boot.py")) 
boot.close() 

boot = open("main.py", "w") 
boot.write(functions.getPage("https://clock.matthiasklaasse.repl.co/Version-18/main.py")) 
boot.close() 

try:
  err = open("Errorhandler.py", "x") 
  err.write(functions.getPage("https://clock.matthiasklaasse.repl.co/Version-18/Errorhandler.py")) 
  err.close() 
except:
  err = open("Errorhandler.py", "w") 
  err.write(functions.getPage("https://clock.matthiasklaasse.repl.co/Version-18/Errorhandler.py")) 
  err.close()
  
try:
  boot = open("bootscreen.py", "x") 
  boot.write(functions.getPage("https://clock.matthiasklaasse.repl.co/Version-18/bootscreen.py")) 
  boot.close() 
except:
  boot = open("bootscreen.py", "w") 
  boot.write(functions.getPage("https://clock.matthiasklaasse.repl.co/Version-18/bootscreen.py")) 
  boot.close()


functions = open("functions.py", "w") 
response = urequests.get("https://clock.matthiasklaasse.repl.co/Version-18/functions.py")
newf = response.text
functions.write(newf) 
functions.close() 
html = open("Webpage/html/index.html", "w")
response = urequests.get("https://clock.matthiasklaasse.repl.co/Version-18/Webpage/html/general.html")
newf = response.text
html.write(newf) 
html.close() 


print("update done")
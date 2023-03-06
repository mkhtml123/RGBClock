import urequests

boot = open("Boot.py", "w") 
boot.write(functions.getPage("https://clock.matthiasklaasse.repl.co/Version-19/Boot.py")) 
boot.close() 
functions = open("functions.py", "w") 
response = urequests.get("https://clock.matthiasklaasse.repl.co/Version-19/functions.py")
newf = response.text
functions.write(newf) 
functions.close() 
html = open("Webpage/html/index.html", "w")
response = urequests.get("https://clock.matthiasklaasse.repl.co/Version-19/Webpage/html/general.html")
newf = response.text
html.write(newf) 
html.close() 


print("update done")
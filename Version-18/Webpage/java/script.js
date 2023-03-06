var localurl = document.URL
localurl = localurl.substring(0, localurl.length - 12);

var setting = ""
var Savebutton = document.getElementById('save')
var ele = document.getElementById("Inner").children


function httpGet(theUrl){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}
//if (httpGet(localurl+"settings") ==  )
Savebutton.addEventListener("click", () => {
  setting = ""
	for (var i = 0; i < ele.length; i++) {
    if (ele[i].tagName == "INPUT"){
      if (ele[i].type == "checkbox"){
         setting = setting + String(ele[i].checked)
      }
      if (ele[i].type == "number"){
         setting = setting + String(ele[i].value)
      }
    var resp = setting = setting + ","
    }
  }
  httpGet("\Setgeneral,"+setting)
  location.reload()
});


function componentToHex(c) {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
  return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

function Hidetext() {
  document.getElementById("speed").hidden = !document.getElementById("Animate").checked
  document.getElementById("bri").hidden = document.getElementById("AutoBright").checked
  if (document.getElementById("Animate").checked){
    document.getElementById("htext").style.display = "inline"
  }else{
    document.getElementById("htext").style.display = "none"
  }
  if (document.getElementById("AutoBright").checked){
    document.getElementById("btext").style.display = "none"
  }else{
    document.getElementById("btext").style.display = "inline"
  }
  
}
var current = httpGet("/Getgeneral")

var lines = current.split("\n");
var inp = []

var ele = document.getElementById("Inner").children
for (let i = 0; i < ele.length; i++) {
  if (ele[i].tagName == "INPUT"){
    inp[inp.length] = ele[i]
  }
}

for (let i = 0; i < inp.length; i++) {
  if(inp[i].type == "checkbox"){
    if (lines[i]=="true"){
      inp[i].checked = true
    }else{
      inp[i].checked = false
    }
  }
  if(inp[i].type == "text"){
    inp[i].value = lines[i]
  }
  if(inp[i].type == "number"){
    inp[i].value = lines[i]
  }
}

console.log(inp)
Hidetext()



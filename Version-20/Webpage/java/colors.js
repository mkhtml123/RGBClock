var localurl = document.URL
localurl = localurl.substring(0, localurl.length - 12);
var colors = httpGet("/getcolors")
var colors = colors.split("\n");
var savec = document.getElementById('savec')
var newr = document.getElementById('newr')
var newg = document.getElementById('newg')
var newb = document.getElementById('newb')
var remover = document.getElementById('remover')
var removeg = document.getElementById('removeg')
var removeb = document.getElementById('removeb')
var empty = newb.value 
var colorsdiv = document.getElementById('colors').children

function httpGet(theUrl){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

savec.addEventListener("click", () => {
  var req = localurl+"/"
  req = req+"Addcolor"
  if (newr.value != '' && newg.value != '' && newb.value != ''){
    req = req+","
    req = req+newr.value
    req = req+","
    req = req+newg.value
    req = req+","
    req = req+newb.value
  }
  old = httpGet("/getcolors")
  console.log(old)
  old = old.split("\n")
  console.log(old)
  for (let i = 0; i < old.length; i++) {
    //old[i] = old[i].replace("\n", "")
    req = req+","
    console.log(old[i])
    req = req+old[i]
  }
  if (remover.value != '' && removeg.value != '' && removeb.value != ''){
    var searchstring = ""
    searchstring = searchstring+","
    searchstring = searchstring+remover.value
    searchstring = searchstring+","
    searchstring = searchstring+removeg.value
    searchstring = searchstring+","
    searchstring = searchstring+removeb.value
    req = req.replace(searchstring, "")
  }
  console.log(searchstring)
  console.log(req)
  resp = httpGet(req)
  location.reload()
});

function componentToHex(c) {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
  return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}
for (let i = 0; i < colors.length/3; i++) {
  display = document.createElement('div')
  display.className  = "colord"
  display.style.backgroundColor = rgbToHex(parseInt(colors[i*3]), parseInt(colors[i*3+1]), parseInt(colors[i*3+2]))
  col = document.createElement('p')
  col.innerHTML = "Red:"
  col.innerHTML = col.innerHTML+colors[i*3]+"Blue:"
  col.innerHTML = col.innerHTML+colors[i*3+1]+"Green:"
  col.innerHTML = col.innerHTML+colors[i*3+2]
  document.getElementById("colors").appendChild(display)
  display.appendChild(col)
}
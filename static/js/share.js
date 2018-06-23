//javascript for share page
var step = -1;


function nextStep(){
  step++;
  document.getElementById("startButton").style.display = "none";
  var ins =  document.getElementsByClassName('inputHolder');
  for (var i = 0; i < ins.length; i++) {
    ins[i].style.display = "none";
  }
  ins[step].style.display = "block";
  ins[step].getElementsByTagName("input")[0].focus();
}

function enterFunction(event){
	if (event.keyCode == 13 || event.which == 13){{}
    if(step == -1){
      nextStep();
    }
    if (step == 0){
      if (document.getElementById('nBut').disabled == false){
        nextStep();
      }
    }
    if (step == 1){
      if (document.getElementById('cBut').disabled == false){
        nextStep();
      }
    }
    if (step == 2){
      if (document.getElementById('tBut').disabled == false){
        nextStep();
      }
    }
  }
}

function prevStep(){
  step--;
  document.getElementById("startButton").style.display = "none";
  var ins =  document.getElementsByClassName('inputHolder');
  for (var i = 0; i < ins.length; i++) {
    ins[i].style.display = "none";
  }
  ins[step].style.display = "block";
}

function hideButt(){
  var butt = document.getElementsByClassName("buttonHolder");
  for (var i = 0; i < butt.length; i++) {
    butt[i].style.display = "none";
  }
}

function showButt(){
  var butt = document.getElementsByClassName("buttonHolder");
  for (var i = 0; i < butt.length; i++) {
    butt[i].style.display = "block";
  }
}

function nStep(){
  document.getElementById('nBut').disabled = false;
}

//start with the fucntion that shows the stuffs
function cShow(){
  document.getElementById('cDrop').style.display = "block";
  document.getElementById("cEx").style.display = "none";
  //make the seletion disapear
//  document.getElementById("cInput").value = "";
  document.getElementById("cInput").focus();
  //clear some properties
  document.getElementById("cInput").style.removeProperty('background-color');

  document.getElementById('cBut').disabled = true;
  hideButt();

  //re run filterFunction
  cFilter();
}

function cFilter(){
  var rawText = document.getElementById("cInput").value;
  var text = rawText.toUpperCase();
  var div = document.getElementById("cDrop");
  var p = div.querySelectorAll("p"); // list of all p that are in the div
  var match = false;
  for(var i=0; i < p.length; i++) {
    if (p[i].innerHTML.toUpperCase().indexOf(text) == 0 || p[i].innerHTML.toUpperCase().indexOf(" "+text) > -1) {
      // Show it
      p[i].style.display = "block";
    } else {
      // Don't show it
      p[i].style.display = "none";
    }
    if(p[i].innerHTML.toUpperCase() == text){
      match = true;
    }
  }
  //check if a perfect match is found
  var pNew = document.getElementById("cNew");
  if(match == false){
    //then display a create a new thing thing
    pNew.innerHTML = "Add a new Class: " + rawText;
    pNew.style.display = "block";
  } else {
    pNew.style.display = "none";
  }
  if(rawText == ""){
    pNew.style.display = "none";
  }
}

function cClick(ele){
  var inp = document.getElementById("cInput");
  //set the text field to the selection
  var sel = ele.innerHTML;
  inp.value = sel;

  //make it look final
  inp.style.backgroundColor = "blue";
  document.getElementById("cEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('cDrop').style.display = "none";

  showButt();
  document.getElementById('cBut').disabled = false;
}

function cClickNew(){
  //make it look final
  document.getElementById("cInput").style.backgroundColor = "blue";
  document.getElementById("cEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('cDrop').style.display = "none";
  showButt();
  document.getElementById('cBut').disabled = false;
}

function cEr() {
  document.getElementById("cInput").value = "";
  cFilter();
}

//teacher stuf ***************************8

function tShow(){
  document.getElementById('tDrop').style.display = "block";
  document.getElementById("tEx").style.display = "none";
  //make the seletion disapear
  //document.getElementById("tInput").value = "";
  document.getElementById("tInput").focus();
  //clear some properties
  document.getElementById("tInput").style.removeProperty('background-color');

  document.getElementById('tBut').disabled = true;
  hideButt();


  //re run filterFunction
  tFilter();
}

function tFilter(){
  var rawText = document.getElementById("tInput").value;
  var text = rawText.toUpperCase();
  var div = document.getElementById("tDrop");
  var p = div.querySelectorAll("p"); // list of all p that are in the div
  var match = false;
  for(var i=0; i < p.length; i++) {
    if (p[i].innerHTML.toUpperCase().indexOf(text) == 0 || p[i].innerHTML.toUpperCase().indexOf(" "+text) > -1) {
      // Show it
      p[i].style.display = "block";
    } else {
      // Don't show it
      p[i].style.display = "none";
    }
    if(p[i].innerHTML.toUpperCase() == text){
      match = true;
    }
  }
  //check if a perfect match is found
  var pNew = document.getElementById("tNew");
  if(match == false){
    //then display a create a new thing thing
    pNew.innerHTML = "Add a new teacher: " + rawText;
    pNew.style.display = "block";
  } else {
    pNew.style.display = "none";
  }
  if(rawText == ""){
    pNew.style.display = "none";
  }
}

function tClick(ele){
  var inp = document.getElementById("tInput");
  //set the text field to the selection
  var sel = ele.innerHTML;
  inp.value = sel;

  //make it look final
  inp.style.backgroundColor = "blue";
  document.getElementById("tEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('tDrop').style.display = "none";

  showButt();
  document.getElementById('tBut').disabled = false;
}

function tClickNew(){
  //make it look final
  document.getElementById("tInput").style.backgroundColor = "blue";
  document.getElementById("tEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('tDrop').style.display = "none";

  showButt();
  document.getElementById('tBut').disabled = false;
}

function tEr(){
    document.getElementById("tInput").value = "";
    tFilter();
}

//start creating the upload
function createUpload() {
  //some stuff
}

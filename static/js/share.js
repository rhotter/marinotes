//javascript for share page
var step = 0;

function loadFunc(){
  var divs = document.getElementsByClassName('inputHolder');
  for (var i = 0; i < divs.length; i++) {
    divs[i].style.display = 'none';
  }
  divs[0].style.display = 'block';
}

function nameFinal(){
  if (document.getElementById('nInput').value != ""){
    document.getElementById('nInput').style.backgroundColor = "#cccccc";
    document.getElementById('nEx').style.display = "block";
  }
}

function nameOld(){
  document.getElementById('nInput').style.backgroundColor = "white";
    document.getElementById('nEx').style.display = "none";
}

function nextStep(){
  step++;
  var ins =  document.getElementsByClassName('inputHolder');
  for (var i = 0; i < ins.length; i++) {
    ins[i].style.display = "none";
  }
  ins[step].style.display = "block";
  ins[step].getElementsByTagName("input")[0].focus();
}

function enterFunction(event){
	if (event.keyCode == 13 || event.which == 13){
    if (document.getElementsByClassName('inputHolder')[step].getElementsByClassName('nextBut')[0].disabled == false){
      nextStep();
    }
  }
}

function prevStep(){
  step--;
  var divs = document.getElementsByClassName('inputHolder');
  for (var i = 0; i < divs.length; i++) {
    divs[i].style.display = 'none';
  }
  divs[step].style.display = 'block';
}

function hideButt(ide){
  document.getElementById(ide).style.display="none";
}

function showButt(ide){
  document.getElementById(ide).style.display="inline-block";
}

function nStep(){
  document.getElementsByClassName('inputHolder')[step].getElementsByClassName('nextBut')[0].disabled = false;
}

//start with the fucntion that shows the stuffs
function cShow(){
  cDropStyleDown();
  document.getElementById('cDrop').style.display = "block";
  document.getElementById("cEx").style.display = "none";
  //make the seletion disapear
//  document.getElementById("cInput").value = "";
  document.getElementById("cInput").focus();
  //clear some properties
  document.getElementById("cInput").style.removeProperty('background-color');

  //document.getElementById('cBut').disabled = true;
  //hideButt("cBut");
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
  nStep();
  cDropStyleUp();
  var inp = document.getElementById("cInput");
  //set the text field to the selection
  var sel = ele.innerHTML;
  inp.value = sel;

  //make it look final
  inp.style.backgroundColor = "#cccccc";
  document.getElementById("cEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('cDrop').style.display = "none";

  //showButt("cBut");
  //document.getElementById('cBut').disabled = false;
}

function cClickNew(){
  nStep();
  cDropStyleUp();
  //make it look final
  document.getElementById("cInput").style.backgroundColor = "#cccccc";
  document.getElementById("cEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('cDrop').style.display = "none";
  //showButt("cBut");
  //document.getElementById('cBut').disabled = false;
}

function cEr() {
  document.getElementById("cInput").value = "";
  cFilter();
}

function cDropStyleDown(){
  document.getElementById("cInput").style.borderBottomRightRadius = "0px";
  document.getElementById("cInput").style.borderBottomLeftRadius = "0px";
}

function cDropStyleUp(){
  document.getElementById("cInput").style.borderBottomRightRadius = "8px";
  document.getElementById("cInput").style.borderBottomLeftRadius = "8px";
}


//teacher stuf ***************************8

function tShow(){
  tDropStyleDown();
  document.getElementById('tDrop').style.display = "block";
  document.getElementById("tEx").style.display = "none";
  //make the seletion disapear
  //document.getElementById("tInput").value = "";
  document.getElementById("tInput").focus();
  //clear some properties
  document.getElementById("tInput").style.removeProperty('background-color');

  //document.getElementById('tBut').disabled = true;
  //hideButt("tBut");


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
  nStep();
  tDropStyleUp();
  var inp = document.getElementById("tInput");
  //set the text field to the selection
  var sel = ele.innerHTML;
  inp.value = sel;

  //make it look final
  inp.style.backgroundColor = "#cccccc";
  document.getElementById("tEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('tDrop').style.display = "none";

  //showButt("tBut");
  //document.getElementById('tBut').disabled = false;
}

function tClickNew(){
  nStep();
  tDropStyleUp();
  //make it look final
  document.getElementById("tInput").style.backgroundColor = "#cccccc";
  document.getElementById("tEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('tDrop').style.display = "none";

  //showButt("tBut");
  //document.getElementById('tBut').disabled = false;

}

function tEr(){
    document.getElementById("tInput").value = "";
    tFilter();
}

function tDropStyleDown(){
  document.getElementById("tInput").style.borderBottomRightRadius = "0px";
  document.getElementById("tInput").style.borderBottomLeftRadius = "0px";
}

function tDropStyleUp(){
  document.getElementById("tInput").style.borderBottomRightRadius = "8px";
  document.getElementById("tInput").style.borderBottomLeftRadius = "8px";
}


//start creating the upload
function createUpload() {
  //some stuff
}

function inputNotes(){
  var butt = document.getElementsByClassName('inputHolder')[step].getElementsByClassName('nextBut')[0];
  document.getElementById('noteBd').style.display = "none";
  document.getElementById('notePr').style.display = "block";

  var x = document.getElementById("file1");
  var txt = "";
  var nms = [];
  if ('files' in x) {
      if (x.files.length == 0) {
          txt = "Select one or more files.";
          butt.disabled = true;
      } else {
          butt.disabled = false;
          for (var i = 0; i < x.files.length; i++) {
              var file = x.files[i];
              if ('name' in file) {
                  nms.push(file.name);
              }
          }
      }
  }
  else {
      if (x.value == "") {
          txt += "Select one or more files.";
          butt.disabled = true;
      } else {
          butt.disabled = true;
          txt += "The files property is not supported by your browser!";
          txt  += "<br>The path of the selected file: " + x.value; // If the browser does not support the files property, it will return the path of the selected file instead.
      }
  }
  var sorted = nms.sort();
  for (var i = 0; i < sorted.length; i++) {
    txt += sorted[i] + "<br>";
  }
  document.getElementById("notePr").innerHTML = txt;

}

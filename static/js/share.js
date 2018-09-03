//javascript for share page
var step = -1;

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
  // document.getElementById("startButton").style.display = "none";
  var ins =  document.getElementsByClassName('inputHolder');
  // for (var i = 0; i < ins.length; i++) {
  //   ins[i].style.pointerEvents = "none";
  // }
  // for (var i = 0; i <= step; i++){
  //   ins[i].style.pointerEvents = "auto";
  // }
  ins[step].getElementsByTagName("input")[0].focus();
}

function enterFunction(event){
	if (event.keyCode == 13 || event.which == 13){{}
    nextStep();
  }
}

// function prevStep(){
//   step--;
//   document.getElementById("startButton").style.display = "none";
//   var ins =  document.getElementsByClassName('inputHolder');
//   for (var i = 0; i <   ins.length; i++) {
//     ins[i].style.pointerEvents = "none";
//   }
//   ins[step].style.pointerEvents = "auto";
// }

// function hideButt(ide){
//   document.getElementById(ide).style.display="none";
// }

// function showButt(ide){
//   document.getElementById(ide).style.display="inline-block";
// }

// function nStep(){
//   document.getElementById('nBut').disabled = false;
// }

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
  nextStep();
}

function cClickNew(){
  cDropStyleUp();
  //make it look final
  document.getElementById("cInput").style.backgroundColor = "#cccccc";
  document.getElementById("cEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('cDrop').style.display = "none";
  //showButt("cBut");
  //document.getElementById('cBut').disabled = false;
  nextStep();
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
  nextStep();
}

function tClickNew(){
  tDropStyleUp();
  //make it look final
  document.getElementById("tInput").style.backgroundColor = "#cccccc";
  document.getElementById("tEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('tDrop').style.display = "none";

  //showButt("tBut");
  //document.getElementById('tBut').disabled = false;
  nextStep();

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

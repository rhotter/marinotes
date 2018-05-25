//javascript for share page

//start with the fucntion that shows the stuffs
function cShow(){
  document.getElementById('cDrop').style.display = "block";
  document.getElementById("cEx").style.display = "none";
  //make the seletion disapear
  document.getElementById("cInput").value = "";
  document.getElementById("cInput").focus();
  //clear some properties
  document.getElementById("cInput").style.removeProperty('background-color');

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
    pNew.innerHTML = "Create new Class: " + rawText;
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
}

function cClickNew(){
  //make it look final
  document.getElementById("cInput").style.backgroundColor = "blue";
  document.getElementById("cEx").style.display = "block";

  //make dropdown disapearing
  document.getElementById('cDrop').style.display = "none";
}
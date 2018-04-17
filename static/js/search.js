var dropViz = false;
var selection = 0;

function filterFunction() {
	// Get rid of share button
	document.getElementById("shareBut").style.display = "none";

	//used for the arrows
	dropViz = true;

	// Show dropdown border
	document.getElementById("dropDown").style.borderBottom = "1px solid #C1C4C7";
	document.getElementById("dropDown").style.borderRight = "1px solid #C1C4C7";
	document.getElementById("dropDown").style.borderLeft = "1px solid #C1C4C7";

	// Change text field border to make remove round bottom edge
	document.getElementById("myInput").style.borderBottomRightRadius = "0px";
	document.getElementById("myInput").style.borderBottomLeftRadius = "0px";

	var text = document.getElementById("myInput").value.toUpperCase();
	var div = document.getElementById("searchDiv");
	var a = document.getElementsByTagName("a"); // Upper case list
	var match = false;
	for(var i=0; i < a.length-1; i++) { /* remove last a (error).... i also added a thing to hide some things as my mom said */
		if (a[i].innerHTML.toUpperCase().indexOf(text) == 0 || a[i].innerHTML.toUpperCase().indexOf(" "+text) > -1) {
			// Show it
			a[i].style.display = "block";
			match = true;
		} else {
			// Don't show it
			a[i].style.display = "none";
		}
	}

	// Error text
	if (!match && text != "") {
		document.getElementById("error_text").style.display = "block";
	}
	else {
		document.getElementById("error_text").style.display = "none";
		//hightlight the first element
		hiSelection(selection);
	}

}

function erase() {
	//attepmt at fixing the disapearing shit
  var c = window.getComputedStyle(document.getElementById('dropDown')).getPropertyValue('border-top-style');

	//used for arrows
	dropViz = false;

  if (c === 'hidden') {
      //alert('Mouse in box');
			//place cursor back in the input
			document.getElementById('myInput').focus();
  } else {
      //alert('Mouse not in box');
			var a = document.getElementsByTagName("a"); // Upper case list
			for(var i=0; i < a.length; i++) {
				// Don't show it
				a[i].style.display = "none";
			}
			document.getElementById("myInput").style.boxShadow = "";

			// Re-show the share button
			document.getElementById("shareBut").style.display = "block";

			// Hide the border of the div
			document.getElementById("dropDown").style.borderBottom = "none";

			// Put back text field round bottom border
			document.getElementById("myInput").style.borderBottomRightRadius = "8px";
			document.getElementById("myInput").style.borderBottomLeftRadius = "8px";

			//reset hiSelection
			seletion = 0;

  }
}

///the enter enterFunction
function enterFunction(event){
	if (dropViz){
		if (event.keyCode == 13 || event.which == 13){
			//the enter key was pressed
			if (getOptions().length != 0) {
				location.href = getOptions()[selection].href;
			}
		}
	}
}

function arrowFunction(event){
	if (dropViz){
		if (event.keyCode == 40){
			//the down key was pressed
			selection++;
			selection = selRange(selection);
			hiSelection(selection);
		}
		if (event.keyCode == 38){
			//the up key was pressed
			selection--;
			selection = selRange(selection);
			hiSelection(selection);
		}
	}
}



function getOptions(){
	var clList = new Array();
	var toSort = document.getElementsByClassName("options");
	for (var i = 0; i < toSort.length; i++) {
		if (window.getComputedStyle(toSort[i]).getPropertyValue('display') == "block"){
			clList.push(toSort[i]);
		}
	}
	return clList;
}

function selRange(num){
	if (num < 0) {num = 0;}
	if (num > getOptions().length) {num = getOptions().length;}
	return num;
}

function hiSelection(ind){
	if (selection < getOptions().length){
		for (var i = 0; i < getOptions().length; i++) {
			getOptions()[i].style.backgroundColor = "white";
		}
		getOptions()[ind].style.backgroundColor = "#B3B3B3";
	} else {
		selection = 0;
	}
}


function hi(ele){
	selection = getOptions().indexOf(ele);
	for (var i = 0; i < getOptions().length; i++) {
		getOptions()[i].style.backgroundColor = "white";
	}
	ele.style.backgroundColor = "#B3B3B3";
}

/*
function scrolSel(dirct){

}


function lo(){
	selection = 0;
	var stf = document.getElementsByClassName("options")
	for (var i = 0; i < stf.length; i++) {
		stf.style.backgroundColor = "white";
	}
}
*/

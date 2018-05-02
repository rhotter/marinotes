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
	for(var i=1; i < a.length-1; i++) { /* remove last a (error).... i also added a thing to hide some things as my mom said */
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
	}

	if (selection >= getOptions().length) {
		selection = 0;
		//console.log("a");
	}

	hiSelection(selection);

}

function erase() {
	//attepmt at fixing the disapearing shit
  var c = window.getComputedStyle(document.getElementById('dropDown')).getPropertyValue('border-top-style');

	dropViz = false;

  if (c === 'hidden') {
      //alert('Mouse in box');
			//place cursor back in the input
			document.getElementById('myInput').focus();
  } else {
      //alert('Mouse not in box');
			var a = document.getElementsByTagName("a"); // Upper case list
			for(var i=1; i < a.length; i++) {
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
			selection = 0;
			//console.log("c");

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
			viewCenter();
		}
		if (event.keyCode == 38){
			//the up key was pressed
			selection--;
			selection = selRange(selection);
			hiSelection(selection);
			viewCenter();
		}
	}
}


//this function gets all the displayed classes
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


//this function makes sure that the selection is within the bounds
function selRange(num){
	if (num < 0) {num = 0;}
	if (num >= getOptions().length) {num = getOptions().length-1;}
	return num;
}

//highlights selection by arrows
function hiSelection(ind){
	if (selection < getOptions().length){
		for (var i = 0; i < getOptions().length; i++) {
			getOptions()[i].style.backgroundColor = "white";
		}
		getOptions()[ind].style.backgroundColor = "#B3B3B3";
	} else {
		//do nothing
		//selection = 0;
	}
}

//highlights selection by mouse
function hi(ele){
	selection = getOptions().indexOf(ele);
	for (var i = 0; i < getOptions().length; i++) {
		getOptions()[i].style.backgroundColor = "white";
	}
	ele.style.backgroundColor = "#B3B3B3";
}


//erases on reload
function eraseText(){
	document.getElementById("myInput").value = "";
}

function viewCenter(){
	var padDrop = 20;
	var scrollPos = document.getElementById("dropDown").scrollTop;
	var element = document.getElementById('dropDown'),
    	style = window.getComputedStyle(element),
    	dropSize = parseInt(style.getPropertyValue('max-height'));
	var element = document.getElementsByClassName('options')[0],
    	style = window.getComputedStyle(element),
			hegt = parseInt(style.getPropertyValue('height')),
			padd = parseInt(style.getPropertyValue('padding')),
    	classElSize = hegt + (2*padd);

	var newScroll = 0;

	var elePos = selection*classElSize;

	//console.log(scrollPos + dropSize);
	//console.log(elePos);

	if (scrollPos > elePos){
		newScroll = classElSize*(-1);
		//console.log("trger1");
	}
	if ((elePos + classElSize) > (scrollPos + dropSize)){
		newScroll = classElSize;
		//console.log("trger2");
	}

	document.getElementById("dropDown").scrollTop = scrollPos + newScroll;

}

var dropViz = false;
var selection = 0;
var isMobile = false; //initiate as false
// device detection
if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|Android|Silk|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(navigator.userAgent)
    || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(navigator.userAgent.substr(0,4))) {
    isMobile = true;
}

console.log(isMobile);

function filterFunction() {
	// Get rid of share button --> z index takes care of that
	// document.getElementById("shareBut").style.display = "none";

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
	if (selection < getOptions().length && !isMobile){
		for (var i = 0; i < getOptions().length; i++) {
			getOptions()[i].style.backgroundColor = "white";
		}
		getOptions()[ind].style.backgroundColor = "#d9d9d9";
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
	if (!isMobile){
		ele.style.backgroundColor = "#d9d9d9";
	}
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

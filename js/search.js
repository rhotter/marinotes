function filterFunction() {
	// Get rid of share button
	document.getElementById("shareBut").style.display = "none";

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
	for(var i=0; i < a.length-1; i++) { /* remove last a (error) */
		if (a[i].innerHTML.toUpperCase().indexOf(text) > -1) {
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
}

function erase() {
	//attepmt at fixing the disapearing shit
  var c = window.getComputedStyle(document.getElementById('dropDown')).getPropertyValue('border-top-style');

  if (c === 'hidden') {
      //alert('Mouse in box');
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
  }




}

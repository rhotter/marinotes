function filterFunction() {
	var text = document.getElementById("myInput").value.toUpperCase();
	var div = document.getElementById("searchDiv");
	var a = document.getElementsByTagName("a"); // Upper case list
	var match = false;
	for(var i=0; i < a.length-1; i++) { /* remove last a (error) */
		if (text !== "" && a[i].innerHTML.toUpperCase().indexOf(text) > -1) {
			// Show it
			a[i].style.display = "block";
			match = true;
		} else {
			// Don't show it
			a[i].style.display = "none";
		}
	}
	//deals with making the button dispear
	if(text.length != 0) {
		document.getElementById("shareBut").style.display = "none";
		document.getElementById("myInput").style.boxShadow = "none";
	} else {
		document.getElementById("shareBut").style.display = "block";
		document.getElementById("myInput").style.boxShadow = "";
	}
	if (!match && text != "") {
		document.getElementById("error_text").style.display = "block";
		console.log("no match")
	}
	else {
		document.getElementById("error_text").style.display = "none";
	}
}

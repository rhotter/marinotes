function filterFunction() {
	var text = document.getElementById("myInput").value.toUpperCase();
	var div = document.getElementById("searchDiv");
	var a = document.getElementsByTagName("a"); // Upper case list
	
	for(var i=0; i < a.length; i++) {
		if (a[i].innerHTML.toUpperCase().indexOf(text) > -1) {
			// Show it
			a[i].style.display = "";
		} else {
			// Don't show it
			a[i].style.display = "none";
		}
	}
}
//get a list of all the teachers and save to teach array
var teach = ["error"];
function teacherLoad(){
  var tch = document.getElementsByClassName('teacherName');
  for (var i = 0; i < tch.length; i++) {
    if (teach.indexOf(tch[i].innerHTML) > -1){
      //do nothing
    } else {
      teach.push(tch[i].innerHTML);
    }
  }

  for (var i = 1; i < teach.length; i++) {

    var hold = document.createElement("div");

    var div = document.createElement("INPUT");
    div.setAttribute("type", "checkbox");
    div.value = teach[i];
    div.setAttribute("id", teach[i]);
    div.onchange = function(){sortTeach()};

    //div.checked = true; //get them to start checked

    var label = document.createElement('label');
    label.setAttribute("for",teach[i]);
    label.className = "teacher";


    label.innerHTML = teach[i];

    hold.appendChild(div);
    hold.appendChild(label);
    document.getElementById('filtBar').appendChild(hold);
  }
}

function sortTeach(){
  //start by getting the checked ones
  var check = ["not really there"];
  for (var i = 1; i < teach.length; i++) {
    if (document.getElementById(teach[i]).checked == true) {
      check.push(teach[i]);
    }
  }
  //get all the cards note that im using the fact that there r equaly as many
  //teacher name divs as there are cards
  var tch = document.getElementsByClassName('teacherName');

  for (var i = 0; i < tch.length; i++) {
    if (check.indexOf(tch[i].innerHTML) > -1){
      //so it
      document.getElementsByClassName('cardFull')[i].style.display = "block";
    } else {
      document.getElementsByClassName('cardFull')[i].style.display = "none";
    }
  }
}

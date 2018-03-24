//wonderful document that deals with creating and all the shit related to the cards
function cardGenerate(left, top){
  //start by creating the card holder and attributing neccesary properites
  var divCardFull = document.createElement("div");
  divCardFull.setAttribute('class', "cardFull");
  //divCardFull.addEventListener("click", myFunction()); //calls function onClick

  //make it positioned where i want
  divCardFull.style.left = left + "px";
  divCardFull.style.top = top + "px";

  //lets add the picture div
  var divCardPicture = document.createElement("div");
  divCardPicture.setAttribute('class', "cardPicture");

  //now for picture itself
  var imgCard = document.createElement("img");
  imgCard.src = "../photos/note_screenshot.jpg"; //adds picture at location picLoc
  imgCard.style.width = "100%";
  imgCard.style.height = "100%";

  //add image to its continer
  divCardPicture.appendChild(imgCard);

  //info container
  var divCardInfo = document.createElement("div");
  divCardInfo.setAttribute('class', "cardInfo");
  divCardInfo.innerHTML = "someinfor";

  //add image and info to main div
  divCardFull.appendChild(divCardPicture);
  divCardFull.appendChild(divCardInfo);

  document.getElementById("cardHolder").appendChild(divCardFull);

}

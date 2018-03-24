//wonderful document that deals with creating and all the shit related to the cards

var cardWidth = 200;
var cardHeight = 250;
var minPad = 20;
var vertPad = 50;
var maxRows = 10;


function cardCreate(left, top){
  //start by creating the card holder and attributing neccesary properites
  var divCardFull = document.createElement("div");
  divCardFull.setAttribute('class', "cardFull");
  //divCardFull.addEventListener("click", myFunction()); //calls function onClick

  //make it positioned where i want
  divCardFull.style.left = left + "px";
  divCardFull.style.top = top + "px";
  divCardFull.style.height = cardHeight + "px";
  divCardFull.style.width = cardWidth + "px";

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

function cardPlace(num){
  //lets start by getting their sizes and such callculating padding
  var fullWidth = document.getElementById("cardHolder").clientWidth;
  var numRow = Math.floor((fullWidth-minPad)/(cardWidth+minPad));
  var pad = (fullWidth-(numRow*cardWidth))/(numRow+1);
  //keep track of cards placed and break if reacehd desired number
  var cardPlaced = 0
  //loop trhough positions
  for (var j = 0; j < maxRows; j++) {
    var top = vertPad + (cardHeight+vertPad)*j;
    for (var i = 0; i < numRow; i++) {
      cardPlaced ++;
      var left = pad + (cardWidth+pad)*i;
      cardCreate(left, top);
      if (cardPlaced == num) {
        j=maxRows;
        i=numRow;
      }
    }
  }
}

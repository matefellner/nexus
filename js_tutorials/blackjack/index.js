
let hasBlackjack = false;
let log = "";
let isAlive = false;

let messageEl = document.getElementById("message-el");
let sumEl = document.getElementById("sum-el")
// let sumEl = document.querySelector("#sum-el");
let cardsEl = document.getElementById("cards-el");

let cards = [];
let sum = 0;

let player = {
    name : "Macsi",
    chips : 145
}


let PlayerEl = document.getElementById("player-id-el")
PlayerEl.textContent = player.name + ": $" + player.chips;

function randomCard(){
    randomNumber = Math.floor(1 + Math.random()*13);

    if(randomNumber === 1){
        randomNumber = 11;
    }else if(randomNumber > 10){
        randomNumber = 10;
    }
    return randomNumber;
}



function startGame(){

    let firstCard = randomCard();
    let secondCard = randomCard();
    cards = [firstCard, secondCard];
    isAlive = true;

    sum = firstCard + secondCard;
    renderGame();
}

function renderGame(){

    if (sum < 21){
        log = "Do you want to draw a new card?";

    }else if (sum === 21){
        log = "You have got a BlackJack!";
        hasBlackjack = true;

    }else if (sum > 21){
        log = "You are out!";
        isAlive = false;
    }
    messageEl.textContent = log
    sumEl.textContent = "Sum: " + sum
    cardsEl.textContent = "Cards:"
    for(var i = 0; i < cards.length; i++){
        cardsEl.textContent += " " + cards[i];
    }

}

function newCard(){

    if(isAlive && hasBlackjack === false){

        let newCard = randomCard();

        sum += newCard;
        cards.push(newCard);
        renderGame();
    }

}

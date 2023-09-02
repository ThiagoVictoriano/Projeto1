function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function chooseMode(){
  img = document.getElementById('img')
  src = img.getAttribute('src')
  if ( src == "img/darkmode.png"){
    darkMode()
  }

  else {
    whiteMode()
  }
}

function whiteMode(){
  body = document.querySelector('.body')
  body.style.backgroundColor = "#ffffff"  
  input = document.querySelector('input')
  input.style.backgroundColor = "#ffffff"
  textarea = document.querySelector('textarea')
  textarea.style.backgroundColor = "#ffffff"
  img = document.getElementById('img')
  img.src = "img/darkmode.png"
}

function darkMode(){
  body = document.querySelector('.body')
  body.style.backgroundColor = "#515151"  
  input = document.querySelector('input')
  input.style.backgroundColor = "#515151"
  textarea = document.querySelector('textarea')
  textarea.style.backgroundColor = "#515151"
  img = document.getElementById('img')
  img.src = "img/whitemode.png"
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});

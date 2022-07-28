/////// ACTIVITY 11 JS FILE ////////

//example 14
const sBubble = document.querySelector('.sBubble')
const pBubble = document.querySelector('.pBubble')
const aBubble = document.querySelector('.aBubble')
sBubble.addEventListener('click', function(){
  e.stopPropagation()
  alert('SECTION was clicked!')
})
pBubble.addEventListener('click', function(e){
  e.stopPropagation()
  alert('PARAGRAPH was clicked!')
})
aBubble.addEventListener('click', function(e){
  e.stopPropagation()
  alert('ANCHOR was clicked!')
})

//example 13
const qccURL = document.querySelector('#qccURL')
qccURL.addEventListener('click', function(e){
  e.preventDefault();
  alert("QCC website is OFF!")
})

//example 12
const toTop = document.querySelector('.toTop')
window.addEventListener('scroll', function(){
  let pxTop = window.pageYOffset;
  if (pxTop>80){
    toTop.style.display = 'block';
  }
  else{
    toTop.style.display = 'none';
  }
})


//example 11
const display9 = document.querySelector('.display9')
window.addEventListener('scroll', function(){
  let pxTop = window.pageYOffset;
  display9.innerHTML = `Browser window is ${pxTop}px away from the top`
})


//example 10
const inputTxt = document.querySelector('.inputTxt')
inputTxt.addEventListener('keydown', function(e){
  alert(`KEYDOWN! key "${e.key}" was pressed \nThe ASCII code for key "${e.key}" is ${e.which}`)
})

//example 9
const divColor = document.querySelectorAll('.divColor')
for(let eachDiv of divColor){
  eachDiv.addEventListener('mouseout', function(){
    eachDiv.style.backgroundColor = changeColor();
  })
}


//example 7
const colorContainer = document.querySelector('.colorContainer')
const btnColor = document.querySelector('#btnColor')

btnColor.addEventListener('click', function(){
  //change background color of the <div>
  colorContainer.style.backgroundColor = changeColor();
})
function changeColor(){
  //rgb values goes from 0 to 255
  const r = Math.floor(Math.random()*256)
  const g = Math.floor(Math.random()*256)
  const b = Math.floor(Math.random()*256)
  return `rgb(${r},${g},${b})`
}


//example 6
const btn6 = document.querySelector('#btn6')
btn6.addEventListener('mouseout', click1)
btn6.addEventListener('dblclick', click2)

function click1(){
  alert('BUTTON 6 = mouseout')
}
function click2(){
  alert('BUTTON 6 was double clicked')
}

//example 5
const btn5 = document.querySelector('#btn5')
btn5.addEventListener('click', function(){
  alert('BUTTON 5 was clicked!')
})

//example 4
const title = document.querySelector('.title')
title.onmouseout = function(){
  console.log(`The title was hovered on mouseout event`)
}

//example 3
const qcclink = document.querySelector('#qccLink')
qccLink.onclick = function(){
  console.log(`QCC link was clicked!`)
}
qccLink.onmouseover = testing;
function testing(){
  console.log(`QCC link was hovered or mouseover!`)
}

//example 2
const btn2 = document.querySelector('#btn2')
btn2.onclick = function(){
  alert('Hi There!')
}

/*
// another way to create the event
function clickedBtn(){
  alert('Hi There!')
}
btn2.onclick = clickedBtn;
*/

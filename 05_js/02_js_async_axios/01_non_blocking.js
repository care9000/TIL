/*
const nothing = () => {}

console.log('start')
setTimeout(nothing, 3000)
console.log('end')
*/

/*
function sleep_3s() {
  setTimeout(() => {
    console.log('일어나!!!')
  }, 3000)
}

console.log('시작')
sleep_3s()
console.log('끝')
*/

/*
function first(){
  console.log('first')
}

function second() {
  console.log('second')
}

function third() {
  console.log('third')
}

first()
setTimeout(second, 0)
third()
*/

console.log('Hello')

setTimeout(function cb1(){
  console.log('cb1')
}, 5000 )

console.log('ByeBye')
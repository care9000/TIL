// var x = 1
// if (x === 1) {
//   var x = 2
//   console.log(x)
// }
// console.log(x)

// let x = 1
// console.log(x)

// if (x === 1) {
//   let x = 2
//   console.log(x)
// }
// console.log(x)


// const My_FAV

// const My_FAV = 7
// console.log(My_FAV)
// console.log("my favorite number is " + My_FAV)

// function varTest() {
//   var x = 1
//   if (true) {
//     var x = 2
//     console.log(x)
//   }
//   console.log(x)
// }
// varTest()

// function letTest(){
//   let x = 1
//   if (true) {
//     let x = 2
//     console.log(x)
//   }
//   console.log(x)
// }
// letTest()

// var a = 1
// var b = 2

// if (a === 1){
//   var a = 11
//   let b = 22
//   console.log(a)
//   console.log(b)
// }
// console.log(a)
// // console.log(b)
// const memberInfo = {
//   id : 1,
//   password: 12345,
//   gender: 'male'
// }
// console.log(memberInfo)
class User {
  constructor(options) {
    this.name = options.name
  }
}
const good = new User({
  name: 'gyoyoul',
})
console.log(good)
console.log(typeof good)
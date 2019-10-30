// Object & Array



/*
// Array


const numbers = [1, 2, 3, 4,]

console.log(numbers[0]) //1
console.log(numbers[-1]) //undefined
console.log(numbers.length) //4
console.log(numbers[numbers.length-1])

// 원본 파괴
console.log(numbers.reverse())
console.log(numbers)
console.log(numbers.reverse())
console.log(numbers)

// push - 배열의 길이를 return
// 배열 끝에 push

console.log(numbers.push('a'))//5
console.log(numbers)

// pop -배열의 가장 마지막 요소를 제거후 리턴
console.log(numbers.pop())
console.log(numbers)

// unshift - 배열의 가장 첫번째 요소로  push후  배열의 길이를 return
console.log(numbers.unshift('a'))
console.log(numbers)

// shift - 배열 가장 첫번째 요소를 제거하고 return
console.log(numbers.shift())
console.log(numbers)

// 복사본 or 다른값을 return
console.log(numbers.includes(1))
console.log(numbers.includes(0))

console.log(numbers.push('a')) //5
console.log(numbers.push('a')) //6
console.log(numbers)
console.log(numbers.indexOf('a')) //가장 먼저 만난 index리턴
console.log(numbers.indexOf('b')) // 찾고자하는 배열의 요소가 없으면 -1

// join - 
console.log(numbers.join())
console.log(numbers.join('-'))
// 배열의 원본은 변하지 않음
console.log(numbers)
*/

/*
//object - 객체(오브젝트)

const me = {
  name : 'ssafy', //key가 1개의 단어
  'phone number' : '01084848819', // key가 여러 개 단어로 이루어지면 스트링으로 처리
  appleProducts: {
    ipad: '2018pro',
    iphone: '6s+',
    macbook: '2018pro',
  }
}

console.log(me.name) // value를 얻어내는 첫번째 방법
console.log(me['name']) // value를 얻어내는 두번째 방법
console.log(me['phone number']) // 주의! 2개 이상의 단어로 구성된 key는 []로 접근

console.log(me.appleProducts)
console.log(typeof me.appleProducts)
console.log(me.appleProducts.ipad)

*/


/*
//Object Literal (추가된 오브젝트 표현법: ES6+)

const books = ['사서삼경', '천자문' ]

const movies = {
  'Horror':['곤지암' , '겟아웃'],
  'SF':['인셉션', '마션', '인터스텔라', '그레비티']
}

// ES5
const magazines = null

const bookShop = {
  books: books,
  movies: movies,
  magazines: magazines,
}

console.log(bookShop)
console.log(typeof bookShop)

//천자문 가져올려면
console.log(bookShop.books[1])

*/
/*
// ES6+
// object의 key,value가 똑같다면 마치 배열처럼 한번만 작성이 가능
const books = ['사서삼경', '천자문' ]

const movies = {
  'Horror':['곤지암' , '겟아웃'],
  'SF':['인셉션', '마션', '인터스텔라', '그레비티']
}


const magazines = null

const bookShop = {
  books,
  movies,
  magazines,
}

console.log(bookShop)
console.log(typeof bookShop)

//천자문 가져올려면
console.log(bookShop.books[1])
*/

// JSON <-> Object
// JSON -> JS의 object 형태와 유사한 문자열 !!
// 실제 모습만 비슷하고 JS Object로 사용하기 위해서는 변환이 필요하다.

// Object -> String(json)
const jsonData = JSON.stringify({
  coffee : 'Americano',
  iceCream: 'Cookie and cream'
})

console.log(jsonData)
console.log(typeof jsonData)

// String ->Object
const parseData = JSON.parse(jsonData)

console.log(parseData)
console.log(typeof parseData)

//Object - Json의 차이
//Object: JS의 Key-Value pair의 자료구조
// Json: Js의 Object와 비스무리하게 생긴 단순String(그냥 문자열!!)
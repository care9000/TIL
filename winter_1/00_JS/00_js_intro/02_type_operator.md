# 2020-01-12

## type_operator

- primitive(원시)타입

  ```javascript
  const a = 13 
  const b = -5 
  const c = 3.14 
  const d = 2.998e8 // 10^8 
  const e = Infinity
  const f = -Infinity
  const g = NaN // Not a Number
  console.log(a, b, c, d, e, f, g)
  ```

  

- string

  ```javascript
  const sentence1 = 'Ask and go to the blue' // single
  const sentence2 = "Ask and go to the blue" // double
  const sentence3 = `Ask and go to the blue` // backtick
  console.log(sentence1)
  console.log(sentence2)
  console.log(sentence3)
  
  ```

  

- ※ 따옴표를 사용하면 줄바꿈 불가 -> 백틱을 사용하자!

  ```javascript
  
  const word = "안녕
  하세요"
  const word = "안녕\n하세요"
  console.log(word)
  // 이렇게 사용하자(밑에꺼 처럼)
  const word1 = `안녕
  하세요`
  console.log(word1)
  
  ```

  - 백틱 사용 -> 줄바꿈 + 문자열 사이에 변수도 넣을 수 있다!(python - f'string) 단, 이스케이프 문자열은 사용 불가

  ``` javascript
  const word2 = `안녕
  하세요`
  console.log(word2)
  const age = 10 
  const message = `홍길동은 ${age}
  세입니다.`
  console.log(message)
  const happy = 'Will you join us?'
  const hacking = 'Happy' + 'Hacking' + '!'
  console.log(happy, hacking)
  ```

- Boolean - 참, 거짓

  ```javascript
  const truthy = true 
  const falsy = false 
  console.log(truthy, falsy)
  console.log(typeof truthy)
  console.log(typeof falsy)
  ```

- Empty value (JS -> null,  undefined)

  ``` javascript
  let first_name // JS 넣어줌
  console.log(first_name)
  let last_name = null // 의도적으로 값이 없음을 명시함
  console.log(last_name)
  console.log(typeof null)
  console.log(typeof undefined)
  console.log(null == undefined) // 동등 비교 연산자
  console.log(null === undefined) // 일치 연산자
  console.log(!null) // true 
  console.log(!undefined) // true
  //※ undefined 의 타입은 object이다.
  ```

- 연산자

  - 할당연산자

    ```javascript
    let c = 0 
    c += 10 
    console.log(c)
    c -= 3
    console.log(c)
    c += 10 
    console.log(c)
    c++
    console.log(c)
    c--
    console.log(c)
    
    ```

  - 비교연산자(변수 앞에 var, let, const를 명시적으로 붙여주지 않으면 JS 엔진이 자동으로 var를 붙여줌)

    ```javascript
    console.log(3 > 2)
    console.log(3 < 2)
    console.log('A' < 'B')
    console.log('Z' < 'a')
    console.log('가' < '나')
    // ※ 문자열은 아스키 코드로 변환후 비교해주는거 같다!!
    ```

  - 동등 비교 연산자(==) 느슨한 평가이므로 사용을 지양하자!

    ``` javascript
    const a = 1 
    const b = "1"
    console.log(a == b)
    console.log(a != b)
    console.log(a == Number(b))
    ```

  - 자동 형변환 예시

    ```javascript
    console.log(8 * null) // 0 
    console.log("5" - 1) // 4(number)
    console.log("5" + 1) // 51(String)
    console.log("five" * 2) // NaN
    ```

  - 일치 연산자(===) 엄격한 평가

    ```javascript
    const a = 1 
    const b = "1"
    console.log(a === b) // false
    console.log(a === Number(b)) // true
    ```

  - 논리 연산자

    - and

      ```javascript
      console.log(true && false) // false
      console.log(true && true) // true 
      console.log(1 && 0) // 0 
      console.log(0 && 1) // 0 
      console.log(4 && 7) // 7
      // 뒤에꺼 까지 비교후 출력
      ```

    - or

      ```javascript
      console.log(false || true) // true 
      console.log(false || false) // false 
      console.log(1 || 0) // 1
      console.log(0 || 1) // 1 
      console.log(4 || 7) // 4
      // 앞에꺼 비교하고 맞으면 바로출력
      ```

    - not

      ```javascript
      console.log(!true) // false 
      console.log(!false) // true
      ```

    - 삼항 연산자(가장 앞의 boolean 값이 참이면 : 앞의 값이 반환되고 

      반대일 경우에는 : 뒤의 값이 반환)

      ```javascript
      console.log(true ? 1 : 2) // 1
      console.log(false ? 1 : 2) // 2
      console.log('nyapy' ? 'awesome' : 'nice') // awesome
      ```

    - 삼항 연산의 결과를 변수에 할당 할 수 있다!

      ```javascript
      const result = Math.PI > 4 ? "Yep" : "Nope" // Nope
      console.log(result)
      ```

      


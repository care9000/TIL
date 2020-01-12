# 2020-01-12

## 변수와 식별자

- var로 선언된 변수의 범위는 현재 실행 문맥 -> 함수 or 함수 외부 전역 다가능

  ```javascript
  var x = 1
  if (x === 1) {
    var x = 2
    console.log(x)
  }
  console.log(x)
  ```

- let -> 값을 재할당 할 수 있는 변수 선언 키워드 (선언은 한번만, 할당은 여러번 가능합니다.)

  ```javascript
  let x = 1
  console.log(x)
  x = 3
  console.log(x)
  
  let x = 1
  console.log(x)
  
  if (x === 1) {
    let x = 2
    console.log(x)
  }
  console.log(x)
  ```

  

```
var 는 블락 밖에서 선언해도 안 까지 영향을 미침(안에서 변하면 바깥까지)
하지만 let은 안은 바깥을 참조는 할 수 있으나 안에서 선언한 변수가 바깥에 영향을 끼치지는 않는다.
```

- const  -> 상수, 값이 변하지 않는 상수를 선언하는 키워드(상수의 값이 재할당을 통해 바뀔 수없고 재선언 될 수 없다.)

  ```javascript
  const My_FAV
  
  const My_FAV = 7
  console.log(My_FAV)
  // 이렇게 할 시 오류가 뜬다.
  const My_FAV = 7
  console.log(My_FAV)
  console.log("my favorite number is " + My_FAV)
  //그래서 const는 변수 선언 한번만!!
  ```

- let 과 var의 scope 비교

  ```javascript
  // var
  
  function varTest() {
    var x = 1
    if (true) {
      var x = 2
      console.log(x)
    }
    console.log(x)
  }
  varTest()
  // 블락 안에서 선언한 값이 밖에도 영향을 끼침
  // let
  function letTest(){
    let x = 1
    if (true) {
      let x = 2
      console.log(x)
    }
    console.log(x)
  }
  letTest()
  // 블락 안에서 선언한 값이 밖에 절대!! 영향 안끼침
  var a = 1
  var b = 2
  
  if (a === 1){
    var a = 11
    let b = 22
    console.log(a)
    console.log(b)
  }
  console.log(a)
  console.log(b)
  // a는 안에서 바뀐 값이 바깥에도 영향을 끼침 그러나 b는 안에서 설정한 값이 바깥에 영향을 끼치지 못했음 ㅠㅠ
  ```

- js언어(객체, 변수, 함수 -> 카멜 케이스 사용(lower-camel-case)) 

  - ex) memberInfo,myGumi

    ```javascript
    // ex)객체(Object)
    const memberInfo = {
      id : 1,
      password: 12345,
      gender: 'male'
    }
    console.log(memberInfo)
    // ex)배열(배열은 보통 복수형 사용)
    const dogs = []
    // 정규표현식 - 'r'로 시작 
    const rDesc = /ab+c/
    // 함수 
    function getPropertyName() {
      
    }
    // 이벤트 핸들러  - 이벤트 핸들러는 'on'으로 시작 
    const onClick = () => {}
    const onKeyDown = () => {}
    // boolean을 반환하는 함수 -> return 값이 불리언인 함수는 'is'로 시작 
    let isAvailable = false 
    // 파스칼 케이스(Upper-camel-case) - 클래스/생성자
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
    // 대문자 스네이크 케이스 - 상수 
    export const API_KEY = 'SOMEKEY'
    export const MAPPING = {
      key: 'value'
    }
    ```

    
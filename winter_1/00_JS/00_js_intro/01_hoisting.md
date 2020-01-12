# 2020-01-12

## Hoisting!(끌어 올림)

- 나중에 선언된 변수를 참조 할 수 있음
- 함수 or statement 최상단으로 올려지는 것(hosting)
- 변수와 함수를 위한 메모리를 확보하는 과정



```javascript
console.log(a)
var a = 10
console.log(a)
// undefined
// 10 이출력

```

- hoisting 과정(var)
  1. 선언이 최상단으로 올라감( var a)
  2. 선언이 최상단으로 올라갔기 때문에 에러대신 정해지지않은(undefined)가 출력(console.log(a))
     - JS에서는 var 변수를 선언할 때 값을 넣어주지 않으면 undefined를 자동으로 넘겨줌
  3. 할당은 그 뒤에 이루어짐(a = 10)
  4. 최종출력(console.log(a))

- hoisting 과정(let)
  1. 선언이 최상단으로(let b)
  2. 근데 에러(console.lob(b))
  3. 할당(b = 10)
  4. 출력(console.log(b))

```
// var 할당 과정 
//1. 선언 - 초기화 (동시에 진행) --> 처음에는 값이 없기 때문에 JS가 undefined를 할당 
//2. 값의 할당 진행
// let 할당 과정
//1. 선언 -> 초기화 x
//2. TDZ(Temporal Dead Zone) -> 임시적 사각지대 
//3. 초기화 (초기에는 값이 없기 때문에 undefined 할당)
//4. 할당 
```

```javascript
var x // 선언 hosting
var y // 선언 hoisting

// console.log(y)
if (x !== 1) {
  console.log(y)
  var y = 3 
  if (y === 3) {
    var x = 1
  }
  console.log(y)
}
if (x === 1) {
  console.log(y)
}
x = 7 
console.log(x)
```


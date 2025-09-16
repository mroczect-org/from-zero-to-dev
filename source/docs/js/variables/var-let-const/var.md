# var

nah var itu dia karakteristiknay [functionScope](./../variable-scopes.md#function-scope), diajua sia di deklarais ulang tanpa erormaknya ini rawan eror.


contoh pakek var

```js
var x = 20;
console.log(x); // output 20

// di deklarasi ulang

var x = 30;
console.log(x); // output 20

// ----------------------------

function testVarScopetype(){
  var y = "im a y in functions testVarScopetype()";
  console.log(y);
  console.log(x);

  // output
  // im a y in functions testVarScopetype()
};

testVarScopetype();

console.log(x) // 20
console.log(y) // error

var y = x
console.log(y); // 20
```

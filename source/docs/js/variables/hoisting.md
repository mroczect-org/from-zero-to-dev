# hoisting

Hoisting is the process where a variable, function, or class declaration is read first by JavaScript before the code is executed.
It's as if the declaration "rises" to the top of its scope.

## 1. Function Declaration
Can be called before the declaration.
```js
sayHello(); // run

function sayHello() {
console.log("Hello world");
}
````

## 2. Var

Hoisted, but its value defaults to `undefined` until the assignment is executed.

```js
console.log(x); // undefined
var x = 5;
console.log(x); // 5
```

## 3. Let and Const

Also hoisted, but cannot be accessed before the declaration because it enters the **temporal dead zone (TDZ)**.

```js
console.log(y); // ReferenceError
let y = 10;
```

## 4. Class

Behavior is the same as `let/const`.

```js
new Person(); // ReferenceError

class Person {}
```

---

## Conclusion

* Declarations rise to the top, but assignments don't.
* `function` can be called before declaration.
* `var` exists but its value is `undefined`.
* `let`, `const`, `class` error if called before declaration.

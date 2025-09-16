# Variable Declarations in JavaScript

## Introduction

In programming, a **variable** is a symbolic name for a value. Think of it as a box where you can store data that you want to reuse later. In JavaScript, variables are fundamental because they allow developers to store, update, and manipulate values.

Example of a simple variable:

```js
let message = "Hello World!";
console.log(message); // Output: Hello World!
````

---

## How Variables Work

When you declare a variable, you are:

1. **Creating an identifier** (the name of the variable).
2. **Allocating memory space** for a value.
3. **Assigning a value** to it (optional at declaration).

Illustration:

* Variable = a **box** with a label (name).
* Value = the **content** inside the box.

![Variable illustration](https://upload.wikimedia.org/wikipedia/commons/6/64/Computer_variable.svg)

---

## Declaration vs Assignment

* **Declaration**: Introducing the variable name to the program.

  ```js
  let x;
  ```
* **Assignment**: Giving a value to the declared variable.

  ```js
  x = 10;
  ```

You can also declare and assign at once:

```js
let y = 20;
```

---

## Scoping & Lifetime (Basic)

Variables in JavaScript exist within a **scope**:

* **Global scope**: Accessible everywhere in the program.
* **Block scope**: Limited to `{ }` (e.g., inside functions, loops).

Example:

```js
let globalVar = "I am global";

function example() {
  let localVar = "I am local";
  console.log(globalVar); // Works
  console.log(localVar);  // Works
}

console.log(globalVar); // Works
console.log(localVar);  // Error: not defined
```

---

## Common Mistakes

1. **Accessing before declaration**

   ```js
   console.log(a); // ReferenceError
   let a = 5;
   ```
2. **Using the wrong identifier**

   ```js
   let number = 100;
   console.log(numbr); // ReferenceError: numbr is not defined
   ```

---

## Best Practices

* Use **meaningful names**

  ```js
  let age = 25;        // Good
  let x = 25;          // Bad
  ```
* Stick to **camelCase** for naming (e.g., `userName`, `totalAmount`).
* Declare variables as close as possible to where they are used.
* Prefer `const` for values that do not change, `let` for values that will change.

---

## Tips

* Storing values in variables makes code **easier to read and maintain**.
* Instead of hardcoding values everywhere:

  ```js
  console.log("Hello");
  console.log("Hello");
  ```

  Use a variable:

  ```js
  let greeting = "Hello";
  console.log(greeting);
  console.log(greeting);
  ```

---

## See Also

* [MDN Web Docs: Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
* [ECMAScript Language Specification](https://tc39.es/ecma262/#sec-variable-statement)
* [Wikipedia: Variable (computer science)](https://en.wikipedia.org/wiki/Variable_%28computer_science%29)

## Next To

```{toctree}
:maxdepth: 3
:caption: Navigasi
:glob:

var-let-const/router
```

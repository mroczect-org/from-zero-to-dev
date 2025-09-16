# variable-naming-rules

```{tip}
In JavaScript, it is highly recommended to name your variables and functions clearly and descriptively.
Readable names make your code easier to understand and maintain.
````

---

## 1. Use meaningful names

Choose names that describe the purpose or the value stored in the variable.

```js
let countOfCorrectAnswers = 5; // ✅ clear and descriptive
let x = 5;                     // ❌ unclear
```

```{note}
`countOfCorrectAnswers` makes it obvious what the variable is used for.
Using `x` alone can cause confusion later, especially in larger codebases.
```

---

## 2. Prefer camelCase

JavaScript convention uses **camelCase** for variable and function names.
This makes long variable names easier to read.

```js
let userFirstName = "Alice";   // ✅ camelCase
let userfirstname = "Alice";   // ❌ hard to read
```

```{tip}
CamelCase starts with a lowercase letter, and each new word begins with a capital letter.
Example: `firstName`, `totalPrice`, `isLoggedIn`.
```

---

## 3. No spaces allowed

Variable names cannot contain spaces. Use camelCase or underscores if you need separation.

```js
let my name = "Bob";   // ❌ SyntaxError
let myName = "Bob";    // ✅
let my_name = "Bob";   // ✅ (allowed, but less common in JS)
```

```{warning}
Spaces are not valid in identifiers. Always use a consistent naming style instead.
```

---

## 4. Do not start with a number

Variable names cannot begin with a digit.

```js
let 1user = "Tom";  // ❌ invalid
let user1 = "Tom";  // ✅ valid
```

---

## 5. Avoid reserved keywords

JavaScript keywords (like `for`, `let`, `class`) cannot be used as variable names.

```js
let for = 10;      // ❌ SyntaxError
let score = 10;    // ✅ valid
```

---

## 6. Use ALL\_CAPS for constants

By convention, values that should never change are written in uppercase with underscores.

```js
const PI = 3.14159;
const MAX_USERS = 100;
```

---

# Summary

* Use **descriptive names** that reflect purpose (`userScore`, not `x`).
* Stick to **camelCase** for variables and functions.
* No spaces, no starting with numbers, no reserved keywords.
* Use **ALL\_CAPS** for constants.
* Consistency is key: pick one style and use it across your project.

```{tip}
Good naming habits improve readability, reduce bugs, and make teamwork much easier.
```

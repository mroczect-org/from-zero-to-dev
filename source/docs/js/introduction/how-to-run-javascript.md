# How to Run JavaScript

You can execute JavaScript code in several ways. Here are the three most common methods:

---

## 1. Embedding in an HTML File

This is the traditional way to run JavaScript for web pages. You embed your code within an HTML document using the `<script>` tag.

**Example:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My JavaScript Demo</title>
</head>
<body>
  <button type="button" onclick="foobar()">Click Me!</button>

  <script>
    function foobar(){
      alert("Hello from JavaScript!");
    }
  </script>
</body>
</html>
```

**How to Run:**
1.  Save the code above in a file with a `.html` extension (e.g., `index.html`).
2.  Open the file in any web browser (Chrome, Firefox, Edge, etc.).
3.  Click the button to see the `alert` pop up.

---

## 2. Using Node.js
Node.js is a runtime environment that allows you to run JavaScript outside of a web browser, directly on your computer.

**Example:**

Create a file named `foobar.js`:

```js
let name = "foobar";
console.log(name); // Output: foobar
```

**How to Run:**
1.  Ensure you have [Node.js installed](https://nodejs.org/) on your computer.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where your `foobar.js` file is saved.
4.  Run the command


```sh
node foobar.js
```

1.  The output `foobar` will be printed in your terminal.

---

## 3. Using Browser Developer Tools
For quick testing and debugging, you can run JavaScript directly in your browser's developer console.

**How to Run:**
1.  Open any webpage in your browser (e.g., Google.com).
2.  Right-click anywhere on the page and select **"Inspect"** or press `F12` / `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Option+I` (Mac).
3.  Go to the **"Console"** tab.
4.  Type your JavaScript code directly into the console and press `Enter`.

```js
let message = "Hello, Console!";
console.log(message);
```

# variable-scopes

nah pokonta intina scope itu kayak variabel yang kita bikin itu aoakah bsia di panngil sama funcsiatau trigel lainnya oke kayak ini conthnta

kita akab mmebahsa tentang 3 hal

## globl scope

jadi global scope itu intinya variabel kita bisa di panggil di mana aja, berllau untuk `var`, `let`, dan `const` contoh

```js
let letIsGlobalScope = 'im global scope';
var varIsGlobalScope = 'im global scope';
const constIsglobalScope = 'im global scope';

console.log(letIsGlobalScope);
console.log(varIsGlobalScope);
console.log(constIsglobalScope);

function calledGlobalScope() {
  console.log(letIsGlobalScope);
  console.log(varIsGlobalScope);
  console.log(constIsglobalScope);
}

calledGlobalScope();

//output like this
```

```sh
username@host:~path/fo/file/
$ node foo.js
im global scope
im global scope
im global scope
im global scope
im global scope
im global scope
```

```{note}
nah jadi itu lah global scope dia bsia di panggil di mana aja bsua di dalam atau uar fungsi maupun block
```
---


## function scope

nah kalau ini artinya fungsi kita cuman bisa d palggil di dalam `fungsi()` berllau untuk `var` `let` dan `const`

untuk contoh nya gini

```js
function functionScopeExample(){
  var aVarIsFuncitonScope = "im var called on the functions"
  let aLetIsFuncitonScope = "im let called on the functions";
  const aConstIsFuncitonScope = "im const called on the functions";

  console.log(aVarIsFuncitonScope);
  console.log(aLetIsFuncitonScope);
  console.log(aConstIsFuncitonScope);
};

functionScopeExample()

console.log(aVarIsFuncitonScope);
console.log(aLetIsFuncitonScope);
console.log(aConstIsFuncitonScope);
```

and the output like this

```sh
$ node foo.js
im var called on the functions
im let called on the functions
im const called on the functions
/home/username/path/to/filetemp/foo.js:13
console.log(aVarIsFuncitonScope)
            ^

ReferenceError: aVarIsFuncitonScope is not defined
    at Object.<anonymous> (/home/username/path/to/filetemp/foo.js:13:13)
    at Module._compile (node:internal/modules/cjs/loader:1706:14)
    at Object..js (node:internal/modules/cjs/loader:1839:10)
    at Module.load (node:internal/modules/cjs/loader:1441:32)
    at Function._load (node:internal/modules/cjs/loader:1263:12)
    at TracingChannel.traceSync (node:diagnostics_channel:322:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:237:24)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:171:5)
    at node:internal/main/run_main_module:36:49

Node.js v22.19.0
```

```{note}
nah jadi kalau function itu dua variabe ynag kita devsinisakn hanya bsia di jakankan di dalam uncti itu aja di luar funcsi g bsia tapi ada cara lain
```

contoh

```js
function functionScopeExample() {
  var aVarIsFuncitonScope = 'im var called on the functions';
  let aLetIsFuncitonScope = 'im let called on the functions';
  const aConstIsFuncitonScope = 'im const called on the functions';

  return { aVarIsFuncitonScope, aLetIsFuncitonScope, aConstIsFuncitonScope };
}

const result = functionScopeExample();

console.log(result.aVarIsFuncitonScope);
console.log(result.aLetIsFuncitonScope);
console.log(result.aConstIsFuncitonScope);
```

ini bisa

---

## block scope

Block scope artinya variabel hanya hidup di dalam kurung kurawal {} tempat dia didefinisikan. Ini berlaku hanya untuk let dan const, sedangkan var tidak terikat oleh block scope.

```js
if (true) {
  let blockLet = "i'm let in a block";
  const blockConst = "i'm const in a block";
  var blockVar = "i'm var in a block";

  console.log(blockLet);    // i'm let in a block
  console.log(blockConst);  // i'm const in a block
  console.log(blockVar);    // i'm var in a block
}

console.log(blockVar);   // i'm var in a block
console.log(blockLet);   // ReferenceError
console.log(blockConst); // ReferenceError
```
output

```sh
$ node foo.js
i'm let in a block
i'm const in a block
i'm var in a block
i'm var in a block
/home/username/foo.js:11
console.log(blockLet);
            ^

ReferenceError: blockLet is not defined
```

```{warning}
hati-hati, `var` bisa lolos keluar dari block `{}`. Karena itu jarang dipakai lagi di JavaScript modern.
```

---

## local scope

Local scope ini istilah umum untuk variabel yang hidup di dalam ruang lingkup terbatas (fungsi atau blok). Setiap fungsi bisa punya variabel lokal dengan nama yang sama tanpa saling tabrakan.

contoh

```js
function foo() {
  let x = "inside foo";
  console.log(x);
}

function bar() {
  let x = "inside bar";
  console.log(x);
}

foo(); // inside foo
bar(); // inside bar
```

```{tip}
kesimpulan

[Global scope](#globl-scope) → bisa dipanggil di mana saja.

[Function scope](#function-scope) → hidup cuma di dalam fungsi.

[Block scope](#block-scope) → hidup cuma di dalam {} (let & const saja).

[Local scope](#local-scope) → variabel lokal, bebas dipakai ulang di fungsi lain.
```

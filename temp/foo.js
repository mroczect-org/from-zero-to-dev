function functionScopeExample() {
  var aVarIsFuncitonScope = 'im var called on the functions';
  let aLetIsFuncitonScope = 'im let called on the functions';
  const aConstIsFuncitonScope = 'im const called on the functions';

  return
}

functionScopeExample()

console.log(aVarIsFuncitonScope)
console.log(aLetIsFuncitonScope)
console.log(aConstIsFuncitonScope)

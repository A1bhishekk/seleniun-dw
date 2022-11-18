// (0, assert_1.strict)(!!fakeDD);
// a=false
// console.log(!!a);
// declare an object with property x
var obj = { x: 1 };
var aliasToObj = obj;
aliasToObj.x ++;
// alert( obj.x );
console.log(obj.x);
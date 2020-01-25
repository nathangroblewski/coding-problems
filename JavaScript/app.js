let arrangeBy = require('./lib/arrangeBy');

/* 
This module runs the example test case from the document
with additional problematic elements 
*/

const users = [
    { 'name': 'Bob', 'id': 1 },
    { 'name': 'Sally', 'id': 2 }, undefined,
    { 'name': 'Bob', 'id': 3, 'age': 30 }, null, [],
]

const arrangeByName = new arrangeBy('name')
var nameArranged = arrangeByName(users)
console.log(nameArranged)
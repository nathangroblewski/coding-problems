let arrangeBy = require('../lib/arrangeBy');

var mockObjects = [
                { 'name': 'Bob', 'id': 1, 'age': 25 }, undefined,
                { 'name': 'Bob', 'id': 2, 'age': 31 }, null,
                { 'name': 'Jake', 'id': 2, 'age': 46 }, [],
                { 'name': 'Sally', 'id': 5, 'age': 32 },
                { 'id': 5, 'age': 32 },
                { 'name': 'Bob', 'id': 6, 'age': 31 },
                { 'name': 'Jake', 'id': 1, 'age': 68 }
            ]

describe('tests for arrangeBy module',()=> {
    let arrangeByName;
    let nameArranged;

    beforeEach(() => {
        arrangeByName = new arrangeBy('name');
        nameArranged = arrangeByName(mockObjects);
    });

    test('that a function is returned', () => {
        expect(typeof arrangeByName).toBe('function');
    });

    test('that an object is returned when arrangeByName is invoked', () => {
        expect(typeof nameArranged).toBe('object');
    });

    /*
    Testing the num of total keys and num of persons in each grouping validates
    that null, undefined or non object elements were excluded, 
    as well as the object missing the key 
    */

    test('that there are only three grouping keys', () => {
        expect(Object.keys(nameArranged).length).toEqual(3);
    });

    test('that there are three Bobs in the "Bob" grouping', () => {
        expect(nameArranged['Bob'].length).toEqual(3);
    });

    test('that there are two Jakes in the "Jake" grouping', () => {
        expect(nameArranged['Jake'].length).toEqual(2);
    });

    test('that there is one Sally in the "Sally" grouping', () => {
        expect(nameArranged['Sally'].length).toEqual(1);
    });
});

# Advanced JavaScript Concepts with [Fireship.io](https://fireship.io)

- 102

## [🔗 Prototype Chain](https://fireship.io/courses/js/102-prototype-chain/)

Except for the *primitives*, everything in JavaScript is just an **Object**.

- Inheritance between JavaScript Objects

- `{ }`

- `new Object()`

- `.__proto__`

- `Object.setPrototypeOf()`

- `Object.getPrototypeOf()`

![*everyMfinThingIsAnObject](./Resources/memes/everyMfinThingIsAnObject.webp)

```javascript

// animal object
const animal = {
    dna: 'ACGT',
    origin: 'Planet-Earth',
    sleep: () => {
        console.log('...ZZZzzzZZZzzz...')
    }
}

// dog object
const dog = new Object(
    {
        name: 'dwag',
        face: '🐺'
    }
);

// initially, the dog object has no prototype...
console.log(animal.__proto__);       // [Object: null prototype] {}
console.log(dog.__proto__);

// Inherit properties from animal object, yeah! ik...
Object.setPrototypeOf(dog, animal);


// now, the dog object has a prototype...
console.log(dog.__proto__);         // { dna: 'ACGT', origin: 'Planet-Earth', sleep: [Function: sleep] }


console.log(dog.name)        // dwag
console.log(dog.dna)        // ACGT
console.log(dog.sleep())        // ...ZZZzzzZZZzzz...

```

## [🍳 Object {destructuring}](https://fireship.io/courses/js/102-destructuring/)

- DRY code

![*moreExperienceNeeded](./Resources/memes/moreExperienceNeeded.webp)

```javascript
const { name, dna, origin, activate } = starboyObject;
```

`Note:` ***Do Not Repeat Yourself** (*DRY*)

## [👫 ...Spread Operator](https://fireship.io/courses/js/102-spread/)

- `...`

```javascript
const life = [...idk, ...fml]
```

`Note:` where you import *objects* matter, it will **overwrite** the previous values!

## [⛓ Optional Chaining (`?`)](https://fireship.io/courses/js/102-optional-chaining/)

**Error handling* while calling/assigning an object's property that may or may not exist yet!

![*handleThis...](./Resources/memes/handleThis.webp)

```javascript
const starboy = homoSapien?.name;
```

## [🦺 Nullish Coalescing (`??`)](https://fireship.io/courses/js/102-nullish-coalescing/)

*JS* is a weakly typed language, so `types` behave a little different than in other languages!

- **Type Coercion**

- `0` is *falsy* by design in the world of *JS*...

![*welcomeToTheWorldOfJS](./Resources/memes/welcomeToTheWorldOfJS.webp)

```javascript
let reasonsToLive = moments ?? 'None';
```

`Note:` While using `??`, only `null` and `undefined` are considered as **falsy**!

## [🔱 Higher Order Functions ( HOF )](https://fireship.io/courses/js/102-higher-order-functions/)

- A **function** is just an **object** in *JavaScript*, so we can pass functions around like any other object. (*Yeah*! just like a thoughtless child wandering throughout the garden, doin' whatev tf, just living life to its fullest... ;)

### Function Declaration

- *Hoisted*, use anywhere in a file.

- *Global Scope* (*Convention)

![*callTheMfinFunction](./Resources/memes/callTheMfinFunction.webp)

```javascript
function add(x, y) {
    return x + y;
}
```

`Note:` **Call** the *function()*

### Function Expression

- *Ain't created until encountered* in the code.

- Can be *named or anonymous*.

- Can be *assigned to a variable* or *passed as an argument* to another function.

- *Local Scope* (*Convention)

#### Function Expression, Named

```javascript
const addFunc = function sum(x, y) {
    return x + y;
}
```

#### Function Expression, Anonymous

```javascript
const fuckFunc = function(x, y) {
    return x * y;
}
```

### Arrow Function

- *goCrazy, do whatever tf you want...

- Good for quick, short functions.

- `=>` / `() =>`

```javascript
someFunc(value => console.log(value))
```

- `() => {}`

```javascript
const subtract = (x, y) => {
    return x - y;
}
```

### HOF

A **higher order function** is a function that takes a function as an argument, or *returns a function*. They are commonly used in functional programming, and are a powerful tool for abstracting away complexity.

- **Callback***s*

```javascript
// a function that takes a function as an argument...
function hofExample(x, y, func) {
    return func(x, y);
}
```

`Note:` It's damn simple, but the way it's used in *different ways* throughout the language is just... ***brain-fuck!**

`Personal Note:` *JavaScript* is fucked, and i love it ;)

## [🫂 Closures ( notThatOne ;) ...this🥡or📦!](https://fireship.io/courses/js/102-closures/)

A **closure** is a `function + outer states/data` that has access to the **parent scope**, even after the parent function has closed. JS will automatically store the state of a *closure* in the **heap memory**, even after the parent function has returned. This behavior makes them useful for *encapsulating private variables*.

- **Open Expression**, Everything that depends on a *parent to send/receive data*, needs to be closed off in a box (**closure**) before *JIT* compilation.

  - Free Variables (*Parent Scope*)

  - Heap Memory (***Long-lived**)
    - Garbage Collector

  - *More memory, more computation...

    - **Data Encapsulation**

![*Closures](./Resources/memes/closures.webp)

```javascript
// Open Expression/Closure
function closure(moments) {
    let theState = 'fucked';
    // console.log(theState)
    function innerClosure() {
        theState = moments ?? 'fuckedAF...';
        // console.log(theState)
        return theState;
    }
    return innerClosure;    // you can make the function anonymous n' return directly... 
}
```

![*callTheFunction()()](./Resources/memes/againCallTheFunction.jpg)

`Note:` use **closure()()** to call the *function()*

- **Closed Expression**, NO external transactions, *no closure!*   (**self-contained**)

  - **NO Closure**

  - Pure *function()* (**Self-contained**)

  - Stack Memory, Call Stack n' *gone!* (***Short-lived**)

wtf??

```javascript

// Closed Expression/noExternalState/pureFunction()
function pureFun() {
    return 'selfContainedPureFunction';
}
```

## [🍟 Array Tricks](https://fireship.io/courses/js/102-array-tricks/)

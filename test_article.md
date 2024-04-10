---
title: "Folder Encapsulation: Fixing your JavaScript folder structure(auto test)"
description: ""
date: 2024-03-22T14:43:12.773Z
preview: ""
draft: true
tags: []
categories: []
type: default
---

Despite encapsulation and decoupling being common conventions in programming, many developers fail to leverage these concepts effectively in organizing their typescript files and folders. Today, we explore practical strategies for applying these fundamental principles to make your code cleaner, easier to manage and just generally better.

As your codebase starts to get larger, it gets harder to figure out which code goes where and what-does-what in your code. Functionalities start to get entangled and import statements begin to look bulky.


![Meme of work overload](/assets/gif.gif)


We'll solve this problem by first discussing an alternative approach to handling imports and exports in your code. Then we'll discover a major pitfall that exists with this approach.

By simply reorganizing your code using some methods we'll discuss later, we'll uncover a much better way to structure your code while providing a solution to the pitfall.



## Module Encapsulation
Consider the two snippets below;


{% embed https://gist.github.com/paulllllo/49a3484e5c5ffebf406efa91c7539d1d %}


{% embed https://gist.github.com/paulllllo/8c913df513338e64bff431156a73e0c0 %}

Clearly, the second snippet looks much easier to understand and manage despite the fact that they generally do the same thing.

By encapsulating the doingX() and doingY() functions and all related functions, we are able to provide a simple interface to that functionality while adding abstraction to their implementation. This makes the code easy to understand and even easier to debug.

Take a look at the implementation of doingThings.js below;

{% embed https://gist.github.com/paulllllo/2ff8a41f58cb12237c97c4552ec5aacd %}

You will quickly run into difficulty when testing the helper functions in this module since they are not exported. Exporting these functions will expose the functions to the public domain defeating the purpose of the encapsulation.

## The Solution - Folder Encapsulation

To fully gain the benefits of encapsulation in our module while still making our functions available for testing, first, we'll break the module down into multiple sub-modules and then we'll create some abstraction over the helper functions.

### Step 1 - Decoupling

First we are going to separate the functions in the module doingThings.js into different files. Then we'll group the files in a folder like this;


![Folder structure](/assets/Basic%20folder%20module.PNG)

We'll keep the important functions, doingX() and doingY() in the original module-- doingThings.js, and import all the helper functions into that module.

This method already brings clear benefits as it allows for easy importing and usage of functions in test files, resulting in improved code management.

However, this approach has its limitations, as it exposes functions to the global environment, posing challenges in managing multiple files within a growing codebase.

Let's take a step further by adding some encapsulation;

### Step 2 - Encapsulation

Folders with an index.js file can be treated as a module in JavaScript and can be imported directly. We can leverage this by creating an index.js file in the doingThings folder. This file will provide a layer of abstraction while acting as a sentinel to the other modules in the folder. The index.js file will only serve to export the required functions and variables from the module like this;


![Folder structure with index](/assets/Folder%20with%20index.PNG)

{% embed https://gist.github.com/paulllllo/431d09bc46b90dca95545e3ad33cd288 %}

This allows us to import and use the required functions directly from the folder-module like this;

{% embed https://gist.github.com/paulllllo/8c913df513338e64bff431156a73e0c0 %}

Now we can just import the folder same way we imported the module. Only the functions exported from index.js will be available through the sentinel and if we try to import one of the helper functions, we'll get a reference error `Uncaught ReferenceError: usedByDoingX1 is not defined`.

{% embed https://gist.github.com/paulllllo/d11813806469a547d606fad42b18dc72 %}

We can still easily run any tests on the helper functions by importing them directly into test files.

In theory, external code could still access the helper functions. However, by utilizing index.js as a sentinel for the other modules, we minimize the chances of such occurrences.

## Enforcing Folder Encapsulation with ESLint

We can go a step further by adding ESLint rules to enforce this implementation. The rules will ensure other developers don't try to directly access background functions and variables in a module. 

This will be discussed in detail in the part 2 of this article. Stay Tuned!

## Benefits of Folder-level Encapsulation
1. Easier to test
2. Promotes Modular Programming
3. Easier to Manage and Debug
4. Security
5. Scalability

### Conclusion
We've learned how folder encapsulation can make our code more organized and easier to manage. By following methods like proper import/export handling, breaking modules into smaller files for better modularity, and using index files to encapsulate sub-modules, we've discovered ways to create cleaner and more maintainable code. Keep practicing these techniques to improve your coding skills and make your projects more efficient.


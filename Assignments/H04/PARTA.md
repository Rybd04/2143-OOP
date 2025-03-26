# Part A: Conceptual Questions

## 1. Definition

**In your own words, define polymorphism.**

Polymorphism allows methods in classes that are called the same thing to have different outputs depending on the situation.

**Why is polymorphism often considered one of the pillars of OOP?**

Polymorphism is considered a pillar of oop because it leads to better code flexibility, reusability, and extensibility.

## 2. Compile-Time vs. Runtime

**Provide a one-sentence explanation of compile-time polymorphism (method overloading).**

Compile-time polymorphism is when different methods in the same class have the same name.

**Provide a one-sentence explanation of runtime polymorphism (method overriding).**

Runtime polymorphism is when a child class has a specific implementation of a method defined in its parent class.

**Which type requires an inheritance relationship, and why?**

Runtime requires an inheritance relationship because it is when a child class overrides a parent method.

## 3. Method Overloading

**Why might a class have multiple methods with the same name but different parameter lists?**

A class might have multiple methods with the same name but different parameter lists if a method is needed that does the same thing just a little differently. 

**Give a brief example (no full code needed) of how method overloading can simplify user interactions with a class.**

If your class has a print method but you need it to work for doubles as well as integers creating multiple print methods with different parameters will make it easier to use. Intead of calling printInt(45) and printDouble(45.5) you can just call print(45) and print(45.5).

## 4. Method Overriding

**Describe how a derived class overrides a base class’s method to provide specialized behavior.**

A derived class overrides a base class's methods by defining its own version of the method with the same name and parameters as the method in the base class.

**In some languages (e.g., C++), the virtual keyword or annotations are used. Why might this be needed?**

The virtual keyword is needed to enable runtime polymorphism and ensure the correct method is called.
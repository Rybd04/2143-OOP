# Part C: Short Reflection & Discussion

## 1. When to Use Inheritance

**Provide one scenario in which inheritance is clearly beneficial, and one scenario in which inheritance might be overkill or lead to a fragile design.**

Inheritence could be used when you have a parent class vehicle with child classes like car, truck, and motorcycle. Each instance is a vehicle but they are a little different.

## 2. Method Overriding vs Overloading

**Differentiate method overriding (runtime polymorphism) and method overloading (compile-time).**

Method overriding is when a child class uses a different implementation of an inherited method. Method overloading is when multiple methods in the same class have the same name but different parameters.

**Why does inheritance rely heavily on overriding for real flexibility?**

Without overriding the child class would be stuck with the parent classes default behavior.

## 3. Inheritance vs. Interfaces/Abstract Classes

**In some languages, we define abstract classes or interfaces.**

**How does the concept of inheritance differ from implementing an interface (or an abstract base class)?**

In inheritance child classes share both behavior and attributes. In interface only a behavior is shared. 

## 4. Pitfalls of Multiple Inheritance

**Name one potential problem with multiple inheritance (e.g., diamond problem).**

The diamond problem is when a child class inherits from two classes that inherit from the same parent class. This leads to the program not knowing what to run when something specific is called.

**Suggest a strategy or approach (like virtual inheritance in C++ or an interface-based design) to mitigate this issue.**

The best way to to mitigate the diamond problem is to avoid it altogether. 
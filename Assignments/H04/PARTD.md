# Part D: Reflection & Real-World Applications

## 1. Practical Example

**Briefly outline a scenario (in a game, a UI framework, or a simulation) where polymorphism is essential.**

In a game polymorphism could be used if there are animal enimes that all bite. There could be just one bite function that runs based on what animal it is.

**Why does it reduce code duplication or improve design?**

It improves design because you could use one line instead of using if else statements.

## 2. Potential Pitfalls

**List one possible confusion or pitfall when using method overloading.**

One pitfall could be ambiguity especially when drealing with implicit type conversions.

**List one potential pitfall when relying heavily on runtime polymorphism (e.g., performance, debugging complexity).**

Excessive use of virtual functions can slow down execution.

## 3. Checking Understanding

**If a new Triangle class is added to your Shape hierarchy, how does polymorphism help you not modify the existing code that uses Shape references?**

Polymorphism helps because the base class shape should be able to do what it needs to do with any shape.
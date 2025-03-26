# Part C: Overloading vs Overriding Distinctions

## 1. Overloaded Methods

**Imagine a class Calculator that has multiple calculate() methods, each accepting different parameter types (e.g., (int, int), (double, double)).**

**How is compile-time resolution used here?**

Compile-time resolution is used to choose the right method based on the values that are passed in.

## 2. Overridden Methods

**In your Shape example (or another scenario), the draw() method is overridden in derived classes.**

**When does the decision for which method to call occur (compile time or runtime)?**

In the shape example the method decision occurs at runtime.

**Why does this matter for flexible code design?**

It matters because it improves code reusability, makes code simplier and it makes code easier to maintain.
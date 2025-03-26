# Part A: Conceptual Questions

## 1. Inheritance Definition

**In your own words, define inheritance.**

Inheritence is when a new child class acquires properties from an existing parent class.

**How does it differ from composition or aggregation in creating complex objects?**

Inheritance defines a hierarchy and implies that the child class is a specialized version of the parent. Composition & Aggregation allow for building complex objects by including instances of other objects, avoiding rigid hierarchies. 

## 2. Types of Inheritance

**List two forms of inheritance (e.g., single vs. multiple).**

In single inheritance a child class inherits from only one parent class. In multiple inheritence a child inherits from more than one parent class.

**Provide a brief example of when each type might be appropriate.**

Single inheritence would be used if you were making a class for animals to make sound. Each animal will have its own sound but they all make sound. Multiple inheritence would be used if you were making an animal class that had the animals move as well as make sound.

## 3. Overriding Methods

**Explain how method overriding in a derived class helps tailor or extend the base class’s functionality.**

Method overriding allows a derived class to use a specific implementation for a method defined in its base class. This makes the base class's methods more dynamic while remaining consistent.

**Why might you override a method instead of simply adding a new method in the derived class?**

Overriding a method is useful when you can extend existing behavior rather than creating a new functionality. This can make things more streamlined.

## 4. Real-World Analogy

**Describe a real-life scenario (outside of programming) where an item or concept “inherits” characteristics from another.**

The easy example is when a child inherits attributes such as height, hair/eye color, and facial features from their parents.

**Discuss how that real-life example aligns with the OOP concept of inheritance.**

In programming the parent class pass down specific attributes to child classes. In my example parents pass down specific traits.
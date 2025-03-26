# Part C: Reflection & Comparison

## 1. Distilling the Essentials

**In your SavingsAccount class, which data or methods would you hide from direct user calls to maintain a clear public interface?**

**Provide a brief explanation.**

Something like logTransaction. The user does not need to know how the transaction was logged.

## 2. Contrast with Polymorphism

**If BankAccount is abstract, how does a method call on SavingsAccount highlight polymorphism while also showcasing abstraction?**

It showcases abstraction by hiding implementaion details of the methods. It highlights polymorphism because bankAccount is the parent class to savingsAccount.

## 3. Real-World Example

**Briefly name another real-world domain (e.g., gaming or healthcare) where abstraction is crucial for a simpler API design.**

In the healtcare field a system that manages multiple medical devices could define abstract methods like measure() or displayData().
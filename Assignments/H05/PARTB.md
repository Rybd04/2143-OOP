# Part B: Minimal Class Example

## Model a Banking System where you only want certain core operations exposed (like deposit and withdraw), hiding internal complexities (like encryption, logging, or ledger balancing).

**The BankAccount could be an abstract class, specifying only the interface methods (no concrete details).**

**The user interacts with derived classes (like SavingsAccount), which implement the abstract methods but hide the internal mechanics.**

class bankAccount {

protected:

    double balance;

public:

    virtual void deposit() = 0;

    virtual void withdraw() = 0;

};

class savingsAccount : public bankAccount {

public:

    savingsAccount() : bankAccount() {}

    void deposit() override {

    }

    void withdraw() override {

    }

};
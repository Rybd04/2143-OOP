# Part B: Minimal Coding

## 1. Base Class

**Create a simple base class called Vehicle with: A brand attribute (or manufacturer).**

**A method drive() that prints something generic like "Vehicle is driving."**

class vehicle {

    string brand;

public:

void drive() {

    cout << "Vehicle is driving." << endl;

}

};

## 2. Derived Class

**Define a derived class Car that inherits from Vehicle.**

**Add a new attribute (e.g., doors) and override the drive() method to show it’s a car specifically driving.**

class car : public vehicle {

    string doors;

public:

void drive() {

    cout << "Car is driving" << endl; 

}

};

## 3. Short Driver Code

**Demonstrate creating a Vehicle object and a Car object.**

**Call drive() on both to illustrate the difference.**

vehicle v1;

v1.drive():

car c1;

car.drive();

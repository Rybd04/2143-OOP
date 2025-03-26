# Part B: Minimal Demonstration

## 1. Base Class & Derived Classes

**Create a base class Shape with an abstract or virtual method: draw().**

**Create two derived classes, Circle and Rectangle, each overriding draw() to print or return a shape-specific action.**

class shape {

    public:

    virtual void draw() {

        cout << "Shape is drawn." << endl;

    }

};

class circle : public shape {

    void draw override {

        cout << "Circle is drawn." << endl;

    }

};

class rectangle : public shape {

    void draw override {

        cout << "Rectangle is drawn." << endl;

    }

};

## 2. Demonstration

**Show a short snippet where you create a list/array of Shape or references, store both a Circle and a Rectangle, and then call draw() on each.**

shape* shapes[2];

shapes [0] = new circle();

shapes [1] = new rectangle();

for (int i = 0; i < 2; i++) {

    shapes[i]->draw();

}

**Emphasize how the correct draw() method is chosen at runtime.**

THe correct draw() method is chosen because the program knows what type of shape is in the array index at the time of drawing.
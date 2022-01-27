//main.cpp
#include <iostream>
#include "Circle.h"

int main()
{
	//Stack allocated objects
	Circle circ1;//Constructor is called
	Circle circ2;//Constructor is called
	
	
	//Heap allocated objects
	Circle* circPtr = nullptr;
	
	
	//         plicit constructor call
	//pointer = new Type(___);
	circPtr = new Circle();
	
	//pointer->publicMethod()
	circPtr->setRadius(10);
	
	std::cout << circPtr->area() << '\n';
	
	//delete[] is for arrays
	//delete   is for objects
	delete circPtr;
	
}

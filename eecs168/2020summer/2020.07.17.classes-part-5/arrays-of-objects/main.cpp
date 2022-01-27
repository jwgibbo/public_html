#include <iostream>
#include <string>

//for local files, use "" instead of <>
#include "Circle.h"


int main()
{	

	Circle circ(0);
	Circle* cPtr = nullptr;
	
	//Stack allocated array of 4 Circles
	//Calls the zero parameter Constructor 
	//4 times
	Circle circArray[4]; 
	Circle* heapArray = nullptr;
	Circle** arrayOfPointers = nullptr;
	arrayOfPointers = new Circle*[4];
	for(int i=0; i<4; i++)
	{
		arrayOfPointers[i] = new Circle(1);
	}
	//change the radius of the Circle
	//at index 2, to be 77
	arrayOfPointers[2]->setRadius(77);
	
	//Heap allocated array of 4 Circles
	//Calls the zero parameter constructor
	//4 times
	heapArray = new Circle[4];
	
	circArray[0].setRadius(7);
	heapArray[0].setRadius(99);
	
	circ.setRadius(10); //good radius
	
	cPtr = new Circle(33);	
	cPtr->setRadius(5);
	
	
	
	
	delete cPtr;
	
	return(0);
}
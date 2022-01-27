#include <iostream>
//Note " " instead of < >
#include "Triangle.h"


int main()
{
	Triangle tri1(1,2); //Constructor is called
	
	
	//Illegal without parameterless constructor
	//Triangle triArray[5]; //Constructs 5 triangles
	
	Triangle* triPtr = nullptr;
	triPtr = new Triangle(7, 15); //Heap allocated Triangle 
	
	Triangle** heapTriArray = nullptr;
	
	//The following is only possible because 
	//a constructor that takes zero parameters is
	//available
	heapTriArray = new Triangle*[4]; //Heap allocated
								//array of 4 Triangle 
								//objects. 
								
	for(int i=0; i<4; i++)
	{
		heapTriArray[i] = new Triangle(5, 10);
		std::cout << "Base: " << heapTriArray[i]->getBase() << '\n';
		std::cout << "Height: " << heapTriArray[i]->getHeight() << '\n';
	}
	
	//Memory visualization #1
	
	//Board Work
	//Write the code to deallocate everything involved in 
	//heapTriArray
	
	return(0);
}
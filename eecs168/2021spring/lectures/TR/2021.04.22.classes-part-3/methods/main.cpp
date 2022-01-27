
#include "Triangle.h"

void byReferenceFunc(int& num)
{
	num = 99;
}

void heightChanger(Triangle& tri)
{
	tri.setHeight(9001);
}

void heightChangerPtr(Triangle* tri)
{
	tri->setHeight(9001);
}


int main()
{
	Triangle tri1; //Constructor is called

	Triangle* triPtr = nullptr;
	triPtr = new Triangle();
	
	//Accessing our objects
	tri1.setBase(5);
	
	triPtr->setBase(5);
	(*triPtr).setBase(5);
	

	heightChanger(tri1);//FINE
	heightChanger(triPtr);//ERROR
	heightChanger(*triPtr);//FINE
	
	heightChangerPtr(tri1);//ERROR
	heightChangerPtr(triPtr);//FINE
	heightChangerPtr(*triPtr);//ERROR
	
	delete triPtr;//Delete Triangle object
	return(0);
}
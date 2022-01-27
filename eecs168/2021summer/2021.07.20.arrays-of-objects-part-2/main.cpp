//main.cpp
#include <iostream>
#include "Triangle.h"//NOTE: "" not <>

int main()
{	
	Triangle* myTri = nullptr; 
	Triangle* yourTri = nullptr; 
	//Draw stack and heap #1

	//Allocate the Triangle objects
	myTri = new Triangle();
	yourTri = new Triangle(5.5, 7.5);
	//Draw stack and heap #2

	(*myTri).setHeight(10);
	myTri->setBase(15);

	//Let's make an array Triangles
	const int SIZE = 4;
	Triangle* tris[SIZE];
	
	for(int i=0; i<SIZE; i++)
	{
		tris[i] = new Triangle(5, 10);
	}
	
	tris[3].setBase(10);
	tris[3].setHeight(10);
	
	return(0);
}
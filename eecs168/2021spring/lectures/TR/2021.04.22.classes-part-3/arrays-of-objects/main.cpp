
#include "Triangle.h"

int main()
{
	Triangle tri1; //Constructor is called

	Triangle* triPtr = nullptr;
	triPtr = new Triangle();
	delete triPtr;//Delete Triangle object

	//Goal: Make an array of 5 Triangles
	int nums[5];
	Triangle tris[5];
	//set first Triangle's height to 10
	tris[0].setHeight(10);
	
	//Goal: Make a heap allocated array of
	// 		5 Triangles
	int* heapNums = nullptr;
	heapNums = new int[5];
	heapNums[0] = 55;
	delete[] heapNums;
	
	Triangle* heapTris = nullptr;
	heapTris = new Triangle[4];
	//set the first Triangle's height to 10
	heapTris[0].setHeight(10);
	delete[] heapTris;

	return(0);
}
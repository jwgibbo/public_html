
//cpp files for classes are implementation files
//All methods are defined in the cpp file


//First thing to do in cpp is include the header file
#include "Triangle.h"

Triangle::Triangle()
{
	//Assigning base and height initial values
	base = 0;
	height = 0;
}

//This method belongs to the Triangle
double Triangle::area()
{
	//base and height's values will be 
	//determined based on which instance/object
	//is doing the calling
	double ans = 0;
	ans = 0.5*base*height;
	return(ans);
}
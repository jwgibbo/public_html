#include <iostream>

int main()
{
	bool myBool;
	
	myBool = true;
	myBool = false;
	
	//For EEs and CoEs
	myBool = 1; //true
	myBool = 0; //false
	
	std::cout << "myBool =  " << myBool;
	std::cout << std::endl;
	
	
	return(0);
}
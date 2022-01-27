#include <iostream>
#include <string>

int main(int argc, char** argv)
{
	std::string pet="";
	std::string tempCount="";
	int petCount = 0;
	
	//Require 3 command-line arguments
	if(argc >= 3)
	{
		//Get the pet type
		pet = argv[1];

		//Get the pet count
		tempCount = argv[2];
		
		//convert the string to an int
		petCount = std::stoi(tempCount);
	}
	else
	{
		std::cout << "ERROR: Invalid arguments\n";
	}
	
	//You don't have to delete[] argv
	
	return(0);
}

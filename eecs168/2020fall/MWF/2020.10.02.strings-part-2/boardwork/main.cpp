#include <iostream>
#include <string>
#include <limits>

int main()
{
	//Board work: Create a madlib for the user:
	//Get a verb and a place. Then print:
	//"The dog <verb> in the <place>
	//Example: let the verb be eats and the place be house
	//The dog eats in the house
	
	std::string verb="";
	std::string place="";
	
	std::cout << "Enter a verb and a place: ";
	std::cin >> verb >> place;
	
	std::cout << "The dog " << verb << " in the " << place << '\n';
	
	return(0);
}
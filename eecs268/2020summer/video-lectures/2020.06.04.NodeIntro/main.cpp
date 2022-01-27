#include <iostream>
#include "Node.h"

int main()
{
	Node* ptr = nullptr;
	Node* ptr2 = nullptr;
	int userValue = 0;
	
	//Goal: Create a heap allocated node
	//		Let the user pick the value for
	//		Store the value in the node, and then
	//		print it back
	
	std::cout << "Input a value: ";
	std::cin >> userValue;
	
	ptr = new Node(userValue);
	//MEMORY VISUALIZATION #1
	std::cout << "Value in node: " << ptr->getEntry();
	std::cout << std::endl;

	
	
	//Goal: Connect first Node to second Node
	//Memory visualization #3
	ptr2 = new Node(64);
	ptr->setNext(ptr2);
	
	delete ptr;
	ptr = nullptr; //optional
	//MEMORY VISUALIZATION #2
	return(0);
}


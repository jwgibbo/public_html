//main.cpp

#include <iostream>
#include "Node.h"
#include <string>

int main()
{
	Node<std::string>* stringNodePtr = nullptr;
	stringNodePtr = new Node<std::string>("Templating Rocks!");
	
	
	Node<int>* intNodePtr = nullptr;
	intNodePtr = new Node<int>(5);
	
	Node<char>* charNodePtr = nullptr;
	charNodePtr = new Node<char>('?');
	
	
	std::cout << intNodePtr->getEntry() << '\n';
	std::cout << charNodePtr->getEntry() << '\n';
	std::cout << stringNodePtr->getEntry() << '\n';

	//intNodePtr->setNext(charNodePtr);
	//charNodePtr = intNodePtr;
	
	return(0);
}
//main.cpp

#include <iostream>
#include "Node.h"


int main()
{
	Node* first = nullptr;
	Node* temp = nullptr;
	first = new Node(55);
	temp = new Node(32);
	first->setNext(temp);
	
	temp = new Node(27);
	
	first->getNext()->setNext(temp);
	
	return(0);
}
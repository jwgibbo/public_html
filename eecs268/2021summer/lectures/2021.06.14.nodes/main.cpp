//main.cpp

#include <iostream>
#include "Node.h"


int main()
{
	Node* first = nullptr;
	Node* temp = nullptr;
	
	
	first = new Node(5);
	temp = new Node(10);
	
	//link the Node with 5 to 
	//the Node with 10
	first->setNext(temp);
	
	//Allocate the Node with 15
	temp = new Node(15);
	
	//Link the Node with 10 to 
	//the Node with 15
	first->getNext()->setNext(temp);
	
	return(0);
}
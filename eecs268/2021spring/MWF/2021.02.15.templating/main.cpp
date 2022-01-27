

#include "Node.h"

int main()
{
	//Make a node that stores an int
	//When you create the pointer or 
	//call the constructor you now define
	//what T is
	Node<int>* intNode = new Node<int>(5);
	
	//Now make a Node that houses a double
	Node<double>* dubNode = new Node<double>(3.14);
	
	//ILLEGAL
	intNode->setNext( dubNode );
	
}
#include <iostream>
#include "Node.h"

int main()
{
	//Create a heap allocated Node that contains
	//a character
	//T gets defined
	Node<char>* myCharNode = nullptr;
	Node<char>* myCharNode2 = nullptr;
	Node<double>* myDubNode = nullptr;
	
	myCharNode = new Node<char>('Q');
	myCharNode = new Node<char>('R');
	
	myDubNode = new Node<double>(3.14158);
	
	//set the entry to be 'L'
	myCharNode->setEntry('L');
	myCharNode->setNext(myCharNode2);
	
	//ILLEGAL
	//myDubNode->setNext(myCharNode);
	
	//deletes are normal
	delete myCharNode;
	delete myCharNode2;
	delete myDubNode;

	return(0);
}
/*
Update your Node class to be templated.
And get last board work working again. 
Get a compiling/working version on the 
cycle servers
*/

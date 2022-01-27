#include "Node.h"

int main()
{
	Node<int>* ptr = nullptr;
	Node<char>* charPtr = nullptr;
	Queue<double> myQ;
	
	ptr = new Node<int>(5);
	charPtr = new Node<char>('1');
	
	// ptr->setNext(charPtr);  ILLEGAL

	return(0);
}
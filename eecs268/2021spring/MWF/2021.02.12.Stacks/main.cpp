#include "Node.h"


int main()
{
	Node* front = nullptr;
	Node* temp = nullptr;
	
	front = new Node(5);
	temp = new Node(99);
	front->setNext( temp )
	temp = new Node(-7);
	front->getNext()->setNext(temp);
}
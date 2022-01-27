#include "Node.h"

int main()
{
	Node* front = nullptr;
	
	front = new Node(10);
	
	delete front;
	front = nullptr;
	return(0);
}
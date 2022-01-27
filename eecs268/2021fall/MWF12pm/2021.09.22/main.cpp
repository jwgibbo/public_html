#include "Node.h"


int main()
{
	Node<int>* intNode = nullptr;
	Node<bool>* boolNode = nullptr;
	Node<std::string>* strNode = nullptr;
	
	intNode = new Node<int>(55);
	boolNode = new Node<bool>(false);
	strNode = new Node<std::string>("");
	
	intNode->setEntry(99);//no <int>
	boolNode->setEntry(false);
	
	intNode->setNext(boolNode); //ERROR
	
}

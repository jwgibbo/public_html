#include "Node.h"
#include <string>

int main()
{
	Node<bool>* boolNode = nullptr;
	Node<std::string>* strNode = nullptr;

	
	boolNode = new Node<bool>(false);
	strNode = new Node<std::string>("");
	
	
	boolNode->setNext(strNode);//ERROR
	
	
}
#include "Node.h"
#include <iostream>


int main()
{
	//We need to define T
	Node<int>* intNode = nullptr;
	Node<char>* charNode = nullptr;
	
	intNode = new Node<int>(5);
	charNode = new Node<char>('a');
}
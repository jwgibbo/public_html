//main.cpp


//You still include header file
//for templated classes
#include "Node.h"
#include "Stack.h"
int main()
{
	//You choose what T is
	Node<int>* ptrA = new Node<int>(5);
	Node<char>* ptrB = new Node<char>('h');
	
	Stack<double> myStack;
	Stack<bool>* myHeapStack = new Stack<bool>();
	
	int* intPtr = new int[5];
	Elephant* elePtr = nullptr;
	elePtr = intPtr; //Illegal!
	
	
	ptrA->setNext( ptrB );//Illegal!
	
	
}
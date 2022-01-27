#ifndef STACK_H
#define STACK_H

#include "Node.h"

template <typename T>
class Stack
{
	private:
	Node<T>* m_top;
	
	public:
	Stack();
	//don't forget a destructor!
	
	void push(T entry); //add to the top
	void pop(); //remove top entry
	T peek() const;//look at top entry
	bool isEmpty() const;//is it empty?
	
	
};
#include "Stack.cpp"
#endif

/*Board works:
Assume you are in Stack.cpp. Implement...
1) pop - which can thrown exception if the stack
	is empty!
2) peek - which can thrown an exception if the 
	stack is empty
3) isEmpty
*/
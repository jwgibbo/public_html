#ifndef STACK_H
#define STACK_H

#include <stdexcept>
#include "Node.h"

template <typename T>
class Stack
{
	private:
	Node<T>* m_top;
	
	public:
	Stack();
	Stack(const Stack<T>& orig);
	
	void operator= (const Stack<T>& rhs);	
	
	void push(T entry);
	void pop();
	T peek() const;
	bool isEmpty() const;
};

#include "Stack.cpp"
#endif
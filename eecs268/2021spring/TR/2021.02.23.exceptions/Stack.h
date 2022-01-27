#ifndef STACK_H
#define STACK_H

#include "Node.h"
#include <stdexcept>

template <typename T>
class Stack
{
	private:
	Node<T>* m_top;
	
	public:
	Stack();
	void push(T entry);
	void pop();
	T peek() const;
	bool isEmpty() const;
};

#endif
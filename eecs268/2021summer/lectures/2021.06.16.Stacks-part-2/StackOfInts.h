#ifndef STACK_OF_INTS_H
#define STACK_OF_INTS_H

#include "Node.h"
#include <stdexcept>
class StackOfInts
{
	private:
	Node* m_top;
	
	
	public:
	StackOfInts();
	~StackOfInts();
	StackOfInts(const StackOfInts& orig);
	void push(int entry);
	void pop(); //Can throw std::runtime_error
	int peek() const; //Can throw std::runtime_error
	bool isEmpty() const; 
	
};

#endif
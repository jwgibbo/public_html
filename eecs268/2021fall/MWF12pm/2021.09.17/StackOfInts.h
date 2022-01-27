#ifndef STACK_OF_INTS_H
#define STACK_OF_INTS_H

#include "StackInterface.h"
#include "Node.h"

class StackOfInts : public StackInterface<int>
{
	private:
	Node* m_top;
	
	public:
	StackOfInts();
	virtual void push(int entry);
	virtual void pop();
	
};

#endif
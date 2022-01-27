//Stack.h

#include "Node.h"


class Stack
{
	private:
	Node* m_top;
	
	public:
	Stack();
	
	void push(int entry);
	void pop();
	int peek() const;
	bool isEmpty() const;
};
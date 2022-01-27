//Stack.h


#include "Node.h"


class StackOfInts
{
	private:
	Node* m_top;
	//no length!
	public:
	StackOfInts();
	void push(int entry);
	void pop();
	int peek() const;
	bool isEmpty() const;
};
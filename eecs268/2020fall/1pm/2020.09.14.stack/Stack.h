
#include "Node.h"

class StackOfInts
{
	private:
	Node* m_top;
	
	public:
	StackOfInts();
	void push(int entry);
	void pop();
	
	int peek() const;
	bool isEmpty() const;
};
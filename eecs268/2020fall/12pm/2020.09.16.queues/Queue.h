
#include "Node.h"

class QueueOfInts
{
	private:
	Node* m_front;
	Node* m_back;
	
	public:
	QueueOfInts();
	void enqueue(int entry);
	void dequeue();
	int peekFront() const;
	bool isEmpty() const;
	
};

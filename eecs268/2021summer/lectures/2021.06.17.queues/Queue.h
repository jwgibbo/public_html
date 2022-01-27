#ifndef QUEUE_H
#define QUEUE_H

#include "Node.h"

template <typename T>
class Queue
{
	private:
	Node<T>* m_front;
	Node<T>* m_back;
	
	public:
	Queue();
	~Queue();
	Queue(const Queue<T>& orig);
	
	void enqueue(T entry);
	void dequeue();
	T peekFront() const;
	bool isEmpty() const;
	
};

#include "Queue.cpp"

#endif

#ifndef QUEUE_H
#define QUEUE_H

#include <stdexcept>
#include "Node.h"


template <typename T>
class Queue
{
	private:
	Node<T>* m_front;
	Node<T>* m_back;
	
	public:
	Queue();
	Queue(const Queue<T>& orig);
	void operator=(const Queue<T>& rhs);
	
	void enqueue(T entry);
	void dequeue();
	T peekFront() const;
	bool isEmpty() const;
	
};

#include "Queue.cpp"
#endif
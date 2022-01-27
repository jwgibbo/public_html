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
	void enqueue(T entry);
	void dequeue();
	T peekFront() const;
	bool isEmpty() const;
	
};

#include "Queue.cpp"
#endif
//Queue.cpp


#ifndef QUEUE_H
#define QUEUE_H

#include "Node.h"
#include "QueueInterface.h"

template <typename T>
class Queue : QueueInterface<T>
{
	private:
	Node<T>* m_front;
	Node<T>* m_back;
	
	public:
	Queue();
	void enqueue(T entry);
	void dequeue();
	
};


#endif
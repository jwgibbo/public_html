#ifndef QUEUE_H
#define QUEUE_H

#include "QueueInterface.h"
#include "Node.h"

template <typename T>
class Queue : public QueueInterface<T>
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
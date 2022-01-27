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
	void enqueue(T entry);
	bool isEmpty() const;
	/*
	~Queue();
	void dequeue();//can throw exception
	T peekFront() const;
	
	*/
};


#include "Queue.cpp"
#endif
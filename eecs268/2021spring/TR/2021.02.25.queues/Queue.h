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
	
	//Methods we'll need in lab
	~Queue();
	
	//Copy constructor
	Queue(const Queue<T>& orig);
	
	//Assignment operator
	void operator=(const Queue<T>& rhs);
	
	void enqueue(T entry);
	void dequeue();
	T peekFront() const;
	bool isEmpty() const;
	
};

#include "Queue.cpp"
#endif
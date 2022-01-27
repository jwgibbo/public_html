//QueueInterface.h


#ifndef QUEUE_INTERFACE_H
#define QUEUE_INTERFACE_H

template <typename T>
class QueueInterface
{
	public:
	virtual void enqueue(T entry) = 0;
	virtual void dequeue() = 0;
	virtual T peekFront() const = 0;
	virtual bool isEmpty() const = 0;
};

#endif
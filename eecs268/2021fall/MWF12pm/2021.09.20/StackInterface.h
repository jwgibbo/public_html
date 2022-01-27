#ifndef STACK_INTERFACE_H
#define STACK_INTERFACE_H

//The type T are the values of interest
template <typename T>
class StackInterface
{
	public:
	virtual void push(T entry) = 0;
	virtual void pop() = 0;
	virtual T peek() const = 0;
	virtual bool isEmpty() const = 0;
};


#endif
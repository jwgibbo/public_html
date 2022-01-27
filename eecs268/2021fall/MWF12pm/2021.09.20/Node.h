#ifndef NODE_H
#define NODE_H

template <typename T> //#1
class Node
{
	private:
	T m_entry;
	Node<T>* m_next; //#2
	
	public:
	Node(T entry);
	T getEntry() const;
	void setEntry(T entry);
	Node<T>* getNext() const;
	void setNext(Node<T>* next);
};
#include "Node.cpp" //#3
#endif
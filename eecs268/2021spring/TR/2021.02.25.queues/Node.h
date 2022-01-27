#ifndef NODE_H
#define NODE_H

template <typename T>
class Node
{
	private:
	T m_entry;
	Node<T>* m_next;
	
	public:
	Node(T entry);
	void setEntry(T entry);
	T getEntry() const;
	void setNext(Node<T>* next);
	Node<T>* getNext() const;
};
#include "Node.cpp"
#endif
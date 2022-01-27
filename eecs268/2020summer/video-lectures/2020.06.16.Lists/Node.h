//Node.h
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
	T getEntry() const;
	void setEntry(T entry);
	
	Node<T>* getNext() const;
	void setNext(Node<T>* next);
};

//For all templated types, include
//the cpp file at the bottom, just 
//before the #endif
#include "Node.cpp"
#endif
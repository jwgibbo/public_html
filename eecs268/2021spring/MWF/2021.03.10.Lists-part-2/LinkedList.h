#ifndef LINKED_LIST_H
#define LINKED_LIST_H


#include "ListInterface.h"
#include "Node.h"


template <typename T>
class LinkedList : public ListInterface<T>
{
	public:
	LinkedList(); 
	int length() const;
	T getEntry(int index) const;
	//NOTE: We'll work on rest of implementation next class
	
	protected:
	Node<T>* m_front;
	int m_length;

};
#include "LinkedList.cpp"
#endif
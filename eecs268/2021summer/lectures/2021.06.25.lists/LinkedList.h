//LinkedList.h

#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include "ListInterface.h"
#include "Node.h"

template <typename T>
class LinkedList : public ListInterface<T>
{
	
	protected:
	Node<T>* m_front;
	int m_length;
	
	public:
	LinkedList();//Assume front=nullptr, length=0
	T getEntry(int index) const;
	
};


#endif
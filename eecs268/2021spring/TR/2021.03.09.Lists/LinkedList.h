//LinkedList.h

#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include "Node.h"
#include "ListInterface.h"

template <typename T>
class LinkedList : public ListInterface<T>
{
	protected:
	Node<T>* m_front;
	int m_length;
	
	public:
	LinkedList(); //set front to nullptr, length to 0
	int length() const;//returns m_length
	T getEntry(int index) const;//indexing start @ 1
	
	
	
};

#endif

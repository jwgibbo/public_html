/**
*	@file LinkedList.h
*	@author 
*	@date 
*	@brief A header file for templated LinkedList class
*/

#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <iostream>
#include <vector>
#include "Node.h"

template <typename T>
class LinkedList
{
	public:
	/** @pre None.
	*   @post An empty list is created.
	*/
	LinkedList();
	
	/** @pre None.
	*   @post Deletes all nodes in the list.
	*/
	~LinkedList();	

	/** @pre None.
	*   @post None.
	*   @return true if the list is empty, false otherwise.
	*/	
	bool isEmpty() const;

	/** @pre None.
	*   @post None.
	*   @return the number of elements in the list.
	*/	
	int size() const;

	/** @pre the value is a valid T.
	*   @post none.
	*   @return true is the value is in the list, false otherwise.
	*/	
	bool search(T value) const;

	/** @pre None
	*   @post None
	*   @return A standard vector with the contents of the list
	*/	
	std::vector<T> toVector() const;

	/** @pre the value is a valid T.
	*   @post One new element added to the end of the list.
	*   @return none.
	*/	
	void addBack(T value);

	/** @pre the value is a valid T.
	*   @post One new element added to the front of the list.
	*   @return none.
	*/	
	void addFront(T value);

	/** @pre None
	*   @post One element is removed from the back of the list.
	*   @return true if the back element was removed, false if the list is empty.
	*/	
	bool removeBack();	

	/** @pre None
	*   @post One element is removed from the front of the list.
	*   @return true if the front element was removed, false if the list is empty.
	*/	
	bool removeFront();

	private:
	Node<T>* m_front;
	T m_size;
};

#include "LinkedList.hpp"

#endif

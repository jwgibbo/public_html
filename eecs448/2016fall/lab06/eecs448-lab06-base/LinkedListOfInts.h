/**
*	@file LinkedListOfInts.h
*	@author 
*	@date 
*	@brief A header file for Linked List class
*/

#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <iostream>
#include <vector>
#include "List.h"
#include "Node.h"

class LinkedListOfInts : public List<int>
{
	public:
	/** @pre None.
	*   @post An empty list is created.
	*/
	LinkedListOfInts();
	
	/** @pre None.
	*   @post Deletes all nodes in the list.
	*/
	~LinkedListOfInts();	

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
	*   @return true if the value is in the list, false otherwise.
	*/	
	bool search(int value) const;

	/** @pre None
	*   @post None
	*   @return A standard vector with the contents of the list
	*   NOTE: This method is guaranteed to work. It's only one guaranteed though
	*/	
	std::vector<int> toVector() const;

	/** @pre the value is a valid T.
	*   @post One new element added to the end of the list.
	*   @return none.
	*/	
	void addBack(int value);

	/** @pre the value is a valid T.
	*   @post One new element added to the front of the list.
	*   @return none.
	*/	
	void addFront(int value);

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
	Node<int>* m_front;
	int m_size;
};

#endif

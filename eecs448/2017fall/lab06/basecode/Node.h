/**
*	@author
*	@date 
*	@brief A header file for templated Node class
*/

#ifndef NODE_H
#define NODE_H

template <typename T>
class Node
{
	public:

	/** @pre None
	*   @post A node is created and the value is stored
	*/
	Node(T value);

	/**
	*   @pre None
	*   @post None
	*   @return Returns the value stored in the node	
	*/
	T getValue() const;

	/** @pre the value is a valid T.
	*   @post Stores the value in the node
	*   @return None
	*/
	void setValue(T value);


	/**
	*   @pre None
	*   @post None
	*   @return Returns a pointer to the next node, or nullptr if there is no next node.
	*/
	Node<T>* getNext() const;

	/**
	*   @pre Next is a pointer to a valid node or nullptr.
	*   @post Sets the member pointer to point at the object (or nullptr) passed in.
	*   @return None.
	*/
	void setNext(Node<T>* next);

	private:
	T m_value;
	Node<T>* m_next;
};

#include "Node.hpp"

#endif

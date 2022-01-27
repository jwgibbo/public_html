/**
*	@file List.h
*	@author 
*	@date 
*	@brief A List ADT
*/

#ifndef LIST_H
#define LIST_H


template <typename T>
class List
{
	public:
	/** @pre None.
	*   @post Deletes the list.
	*   This is a public virtual destructor with an empty definition. Though odd, it's 
	*	commonly used in interfaces.
	*/
	virtual ~List(){};	

	/** @pre None.
	*   @post None.
	*   @return true if the list is empty, false otherwise.
	*/	
	virtual bool isEmpty() const = 0;

	/** @pre None.
	*   @post None.
	*   @return the number of elements in the list.
	*/	
	virtual int size() const = 0;

	/** @pre the value is a valid T.
	*   @post none.
	*   @return true is the value is in the list, false otherwise.
	*/	
	virtual bool search(T value) const = 0;

	/** @pre the value is a valid T.
	*   @post One new element added to the end of the list.
	*   @return none.
	*/	
	virtual void addBack(T value) = 0;

	/** @pre the value is a valid T.
	*   @post One new element added to the front of the list.
	*   @return none.
	*/	
	virtual void addFront(T value) = 0;

	/** @pre None
	*   @post One element is removed from the back of the list.
	*   @return true if the back element was removed, false if the list is empty.
	*/	
	virtual bool removeBack() = 0;	

	/** @pre None
	*   @post One element is removed from the front of the list.
	*   @return true if the front element was removed, false if the list is empty.
	*/	
	virtual bool removeFront() = 0;

};

#endif 

#ifndef STACKOFCHARS_H
#define STACKOFCHARS_H

class StackOfChars
{
	private:
	Node* m_top;
	
	public:
	
	Stack();
	
	/** Here's an example of a doxygen comment block. Do this for all methods
     * @pre None
     * @post entry is added to top of the stack
     * @param entry, the element to be added to the stack
     * @throw None
     **/
	void push(char entry);
	
	/** Here's an example of a doxygen comment block. Do this for all methods
     * @pre Stack is non-empty
     * @post Top element is removed from the stack
     * @param None
     * @throw None
     **/
	void pop();
	
	char peek() const;
	bool isEmpty() const;

};
#endif
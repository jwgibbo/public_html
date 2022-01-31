#ifndef NODE_H
#define NODE_H

class Node
{
	private:
	char m_entry;
	Node* m_next;
	
	public:
	Node(char entry);
	char getEntry() const;
	void setEntry(char entry);
	Node* getNext() const;
	void setNext(char next);

};
#endif
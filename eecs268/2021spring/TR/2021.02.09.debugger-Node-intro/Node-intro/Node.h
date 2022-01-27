#ifndef NODE_H
#define NODE_H

class Node
{
	private:
	int m_entry;
	Node* m_next;
	
	public:
	Node(int entry);
	void setEntry(int entry);
	int getEntry() const;
	void setNext(Node* next);
	Node* getNext() const;
};

#endif
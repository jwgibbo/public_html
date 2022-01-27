//LinkedList.h


#include "Node.h"
#include "ListInterface.h"


template <typename T>
class LinkedList : public ListInterface<T>
{
	private:
	Node<T>* m_front;
	int m_length;
	
	public:
	LinkedList();
	virtual T getEntry(int index) const;
	
	
};
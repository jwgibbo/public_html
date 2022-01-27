
#include "BNode.h"

template <typename T>
class BST
{
	private:
	BNode<T>* m_root;
	bool recSearch(T target, BNode<T>* subtree) const;
	
	public:
	BST();//Sets root to null
	bool search(T target) const;
};
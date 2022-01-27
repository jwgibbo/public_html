
#include "BNode.h"

template <typename ItemType, typename KeyType>
class BST
{
	private:
	BNode<ItemType>* m_root;
	ItemType recSearch(KeyType key, BNode<ItemType>* subtree) const;
	
	public:
	BST();//Sets root to null
	ItemType search(KeyType key) const;
};
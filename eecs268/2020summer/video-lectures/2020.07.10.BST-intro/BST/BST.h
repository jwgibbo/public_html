
#include "BNode.h"


//ItemType - Type of things in each node
//KeyType - Type of our search terms
template <typename ItemType, typename KeyType>
class BST
{
	private:
	BNode<ItemType>* m_root;
	void add(ItemType entry, BNode<ItemType>* subtree);
	ItemType search(KeyType key, BNode<ItemType>* subtree) const; 
	
	
	public:
	BST();
    ItemType search(KeyType key) const; 
	void add(ItemType entry);
}
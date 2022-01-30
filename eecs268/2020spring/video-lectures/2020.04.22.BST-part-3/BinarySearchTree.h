
#ifndef BST_H
#define BST_H

#include "BinaryNode.h"
#include <stdexcept>

template <typename ItemType, typename KeyType>
class BST : public BinarySearchTreeInterface<ItemType, KeyType>
{
	public:
	BST();
	virtual ItemType search(KeyType key) const;
	virtual void add(ItemType entry);
	
	private:
	ItemType search(KeyType key, BinaryNode<ItemType>* subtree) const;
	void add(ItemType entry, BinaryNode<ItemType>* subtree);
	BinaryNode<ItemType>* m_root;
};

#include "BinarySearchTree.cpp"

#endif
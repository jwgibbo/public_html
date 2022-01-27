

template <typename ItemType, typename KeyType>
class BST : public BinarySearchTreeInterface<ItemType, KeyType>
{
	public:
	BST();
	virtual ItemType search(KeyType key) const;
	virtual void add(ItemType entry);
	
	private:
	ItemType search(KeyType key, BinaryNode<ItemType>* subtree) const;
	void add(ItemType entry, BinaryNode<ItemNode>* subtree);
	BinaryNode<ItemType>* m_root;
}
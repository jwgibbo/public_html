

template <typename ItemType, typename KeyType>
class BST : public BinarySearchTreeInterface<ItemType, KeyType>
{
	public:
	BST();
	virtual ItemType search(KeyType key) const;
	
	private:
	ItemType search(KeyType key, BinaryNode<ItemType>* subtree) const
	BinaryNode<ItemType>* m_root;
}
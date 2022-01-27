
//public search
template <typename ItemType, typename KeyType>
ItemType BST<ItemType, KeyType>::search(KeyType key) const
{
	return(search(key, m_root));
}

//private search
template <typename ItemType, typename KeyType>
ItemType BST<ItemType, KeyType>::search(KeyType key, BinaryNode<ItemType>* subtree) const
{
	if(subtree == nullptr)
	{
		//throw exception
	}
	else if (subtree->getEntry() == key)
	{
		//it's a match! return the entry
	}
	else if(subtree->getEntry() < key)
	{
		//recurse right
	}
	else
	{
		//recurse left
	}
}

//public facing add
template <typename ItemType, typename KeyType>
void BST<ItemType, KeyType>::add(ItemType entry)
{
	//Please see the illustration and video for 
	//help with this!
}

//public facing add
template <typename ItemType, typename KeyType>
void BST<ItemType, KeyType>::add(ItemType entry, BinaryNode<ItemType* subtree)
{
	//DON'T DO THIS!
	//This does NOT change the correct pointer
	if(subtree == nullptr)
	{
		subtree = new Node<Item>(entry);
	}
}

//public add
template <typename ItemType, typename KeyType>
void BinarySearchTree<ItemType, KeyType>::add(ItemType entry)
{
	//check for a completely empty tree
	if(m_root == nullptr)
	{
		m_root = new BinaryNode(entry);
	}
	else
	{
		add(entry, m_root);
	}	
}


//private add
template <typename ItemType, typename KeyType>
void BinarySearchTree<ItemType, KeyType>::add(ItemType entry, BinaryNode<ItemType>* subtree)
{
	//This will NOT work!
	if(subtree == nullptr)
	{
		subtree = new BinaryNode(entry);
	}
	
	//Make sure to ask question if this isn't
	//making sense!
}

//public search
template <typename ItemType, typename KeyType>
ItemType BinarySearchTree<ItemType, KeyType>::search(KeyType key) const
{
	return(search(key, m_root));
}

template <typename ItemType, typename KeyType>
ItemType BinarySearchTree<ItemType, KeyType>::search(KeyType key, BinaryNode<ItemType>* subtree) const
{
	
	//check for nullptr, check for an empty
	if(subtree == nullptr)
	{
		throw(std::runtime_error("Dr. Gibbons says: Item not in tree"));
	}
	else if( subtree->getEntry() == key)
	{
		//Found the object that matches the key
		//e.g. A Student that has a given ID
		return(subtree->getEntry());
	}
	else
	{
		//check the rest of the tree
		//traverse down the appropriate subtree
		if(subtree->getEntry() > key)
		{
			return(search(key, subtree->getLeft());
		}
		else
		{
			return(search(key, subtree->getRight());
		}
	}
}
//public search
template <typename ItemType, typename KeyType>
ItemType BST<ItemType, KeyType>::search(KeyType key) const
{
	return( search(key, m_root) );
}

//private
template <typename ItemType, typename KeyType>
ItemType BST<ItemType, KeyType>::search(KeyType key, BNode<ItemType>* subtree) const
{
	//Board work: finish this definition
	//Assume that ItemType == KeyType
	//				ItemType < KeyType
	//				ItemType > KeyType
	//			are all defined
	if(subtree == nullptr)
	{
		//throw an exception
	}
	else if(subtree->getEntry() == key)
	{
		return(subtree->getEntry());
	}
	else if(subtree->getEntry() < key)
	{
		//go right
	}
	else
	{
		//go left
	}
}

//public facing add
template <typename ItemType, typename KeyType>
void BST<ItemType, KeyType>::add(ItemType entry)
{
	//Deal with the case of adding to empty tree
	if(m_root == nullptr)
	{
		m_root = new BNode<ItemType>(entry);		
	}
	else
	{
		recAdd(entry, m_root);
	}
}

//private recursive add
template <typename ItemType, typename KeyType>
void BST<ItemType, KeyType>::recAdd(ItemType entry, BNode<ItemType>* subtree)
{
	//subtree pointer will ALWAYS be pointing to a BNode object
	
	//Base case 1: entry matches the current node's entry
	//Base case 2&3: The entry should be added to LST/RST and that subtree is empty
	//				  then just add the new entry
	//Recursive case: Go into appropriate subtree
}



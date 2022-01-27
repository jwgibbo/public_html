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
	
}

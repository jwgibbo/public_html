
//public search
template <typename T>
bool BinaryTree<T>::search(T entry)
{
	return( search(entry, m_root) );
}

//public countNodes()
int BinaryTree<T>::countNodes() const
{
	return( countNodes(m_root) );
}

//private countNodes
int BinaryTree<T>::countNodes() const
{
	//board work!	
}

//private search
template <typename T>
bool BinaryTree<T>::search(T entry, BNode<T>* subtree)
{
	//if the subtree is empty
	if(subtree == nullptr)
	{
		return(false);
	}
	//Board work! Finish the definition
}


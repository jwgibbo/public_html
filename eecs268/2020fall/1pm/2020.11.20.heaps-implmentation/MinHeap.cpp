//MinHeap.cpp

template <typename T>
void MinHeap<T>::add(T entry);
{
	//Check if we need more room
	if(m_heapSize == m_arrSize)
	{
		resize();
	}
	
	//Put the new entry at the
	//"lowest left-most" position
	m_arr[m_heapSize] = entry;
	upheap(m_heapSize);
	m_heapSize++;
}

template <typename T>
void MinHeap<T>::remove()
{
	//Make the "lowest right-most
	//node" the temporary root.
	m_heapSize--;
	
	//swapping with index heap size
	//has added benefit if you're doing
	//a sort called "heap sort"
	T temp = m_arr[0];
	m_arr[0] = m_arr[m_heapSize];
	m_arr[m_heapSize] = temp;
	
	downheap(0);
}

template <typename T>
void MinHeap<T>::downheap(int index)
{
	//How many children does this 
	//index have? 
	//If my right child index is 
	//between 0 and heapSize, then
	//then this index has 2 children
	//If ONLY my left child index is
	//is between 0 and heapSize, then
	//this index only have 1 child
}






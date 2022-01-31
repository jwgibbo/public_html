//MinHeap.cpp

template <typename T>
MinHeap<T>::MinHeap()
{
	m_arraySize = 4;
	m_heapSize = 0;
	m_arr = new T[m_size];
}

template <typename T>
void MinHeap<T>::add(T entry)
{
	if(m_arraySize == m_heapSize)
	{
		resize();//make more space
	}
	
	//place new entry such that
	//the tree remains complete
	m_arr[heapSize] = entry;
	upheap(heapSize);
	m_heapSize++;
}
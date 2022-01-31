//MinHeap.cpp

template<typename T>
void MinHeap<T>::add(T entry)
{
	if(heapSize == arraySize)
	{
		resize();//doubles current array size
	}
	
	m_arr[heapSize] = entry;
	upheap(heapSize);
	heapSize++;
}
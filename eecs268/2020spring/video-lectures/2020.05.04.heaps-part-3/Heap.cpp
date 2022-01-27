
template <typename T>
void Heap::add(T entry)
{
	//See if we need more room
	if(m_heap >= m_array)
	{
		resize();
	}
	
	//place new entry at lowest left-most unfilled 
	//position (index heap size)
	m_arr[m_heapSize] = entry;
	
	upheap(m_heapSize);
	
	m_heapSize++;
}
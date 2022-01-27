//MinHeap.cpp

#include "MinHeap.h"

template <typename T>
void MinHeap<T>::add(T entry)
{
	if( m_heapSize == m_arrSize )
	{
		resize(); //gives us more room
	}
	
	//place new entry at the "lowest
	//left-most" position
	m_arr[m_heapSize] = entry;
	upheap(m_heapSize);
	m_heapSize++;
}

template <typename T>
void MinHeap<T>::remove()
{
	//swap the lowest right-most
	//to the root then downheap it
	m_heapSize--;
	m_arr[0] = m_arr[heapSize];
	downheap(0);
}

template <typename T>
void MinHeap<T>::downheap(int index)
{
	//How many children does this index
	//have? I'll need to check heapSize!
	
	//Is the index of my right child within
	//the range 0 to heapSize?
	//If it is, then this "node" has 2 
	//children
	//If I don't have two children, check
	//for having 1 child.
	
}















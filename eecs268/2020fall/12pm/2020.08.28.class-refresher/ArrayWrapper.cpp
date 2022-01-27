#include "ArrayWrapper.h"

ArrayWrapper::ArrayWrapper(int size)
{
	m_arr = new char[size];
	m_size = size;
}

char ArrayWrapper::getEntry(int index)
{
	if(index >= 0 && index < m_size)
	{
		return (m_arr[index]);		
	}
	else
	{
		//what do I return?
	}
}

//CoolString.cpp

#include "CoolString.h"

//Precondition: valid length
CoolString::CoolString(int length)
{
	m_length = length;
	m_arr = new char[m_length];
	
	//initialize array to all '\0'
	for(int i=0; i<m_length; i++)
	{
		m_arr[i] = '\0';
	}
}

CoolString::~CoolString()
{
	//clean up anything our class
	//allocated on the heap
	delete[] m_arr;
}
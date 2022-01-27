//CoolString.cpp

#include "CoolString.h"

bool CoolString::setEntry(int index, char entry)
{
	if( index >= 0 && index < m_length )
	{
		m_arr[index] = entry;
		return(true);
	}
	else
	{
		return(false);
	}
}
	
char CoolString::getEntry(int index) const
{
	return( m_arr[index] );
}

int CoolString::length() const
{
	return(m_length);
}


//Define copy constructor
CoolString::CoolString(const CoolString& orig)
{
	m_arr = new char[orig.m_length];
	m_length = orig.m_length;
	
	//copy each element
	for(int i=0; i<m_length; i++)
	{
		m_arr[i] = orig.m_arr[i];
	}
}

//Precondition: valid length
CoolString::CoolString(int length)
{
	m_length = length;
	m_arr = new char[m_length];
	
	//initialize array to all '\0'
	for(int i=0; i<m_length; i++)
	{
		m_arr[i] = '?';
	}
}

CoolString::~CoolString()
{
	//clean up anything our class
	//allocated on the heap
	delete[] m_arr;
}










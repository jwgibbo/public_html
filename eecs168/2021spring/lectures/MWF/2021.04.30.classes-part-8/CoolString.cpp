//CoolString.cpp

#include "CoolString.h"

CoolString::CoolString(int size)
{
	m_arr = new char[size];
	m_size = size;
}

CoolString::~CoolString()
{
	delete[] m_arr;
}

bool CoolString::setEntry(int index, char symbol)
{
	if( 0 <= index && index < m_size )
	{
		m_arr[index] = symbol;
		return(true);
	}
	else
	{
		return(false);
	}
}

char CoolString::getEntry(int index) const
{
	if( 0 <= index && index < m_size )
	{
		return(m_arr[index]);
	}
	else
	{
		//what do we return if the index
		//isn't valid?
		return('\0');
		//We're learn a better alternative
		//in 268 (spoilers: Exceptions!)
	}
}

int CoolString::getSize() const
{
	return(m_size);
}


bool CoolString::operator==(CoolString rhs) const
{
	if(m_size == rhs.m_size)
	{
		for(int i=0; i<m_size; i++)
		{
			if(m_arr[i] != rhs.m_arr[i])
			{
				return(false);
			}
		}
		return(true);
	}
	else
	{
		return(false);
	}
}

















//CoolString.cpp

#include "CoolString.h"


CoolString::CoolString(int size)
{
	//create the char array
	m_arr = new char[size];
	//store the size
	m_size = size;
}

CoolString::~CoolString()
{
	delete[] m_arr;
}

int CoolString::getSize() const
{
	return(m_size);
}
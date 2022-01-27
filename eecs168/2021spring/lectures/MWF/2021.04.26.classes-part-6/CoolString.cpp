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

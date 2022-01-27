//CoolString.cpp

#include "CoolString.h"

CoolString::CoolString(int size)
{
	m_size = size;
	m_array = new char[m_size];
}


CoolString::~CoolString()
{
	//What do we do?
	//We only need to delete the stuff
	//we "new"-ed 
	delete[] m_array;
}
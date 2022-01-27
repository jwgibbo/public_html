//CoolString.h

#ifndef COOL_STRING_H
#define COOL_STRING_H

class CoolString
{
	private: 
	char* m_arr;
	int m_size;
	
	public:
	CoolString(int size);
	~CoolString();
	int getSize() const;
};

#endif
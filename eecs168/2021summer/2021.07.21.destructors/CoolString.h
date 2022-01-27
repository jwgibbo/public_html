//CoolString.h

#ifndef COOL_STRING_H
#define COOL_STRING_H

class CoolString
{
	private:
	int m_size;
	char* m_array;

	public:
	CoolString(int size);
	~CoolString();
};

#endif
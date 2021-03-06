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
	bool setEntry(int index, char symbol);
	char getEntry(int index) const;
	int getSize() const;
	//Destructor!
	~CoolString();
	
	bool operator==(CoolString rhs) const;
};

#endif

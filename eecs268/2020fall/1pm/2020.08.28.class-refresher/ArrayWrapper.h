#ifndef ARRAY_WRAPPER_H
#define ARRAY_WRAPPER_H

class ArrayWrapper
{
	private:
	char* m_arr;
	int m_size;
	
	public:
	//Create an array of the
	//given size.
	//Assume size is valid
	ArrayWrapper(int size);
	
	~ArrayWrapper();
	
	//assume valid index
	char getEntry(int index) const;
	
	//if the index is valid, store 
	//the value and return true. 
	//Otherwise return false.
	bool setEntry(int index, char value);
};

#endif
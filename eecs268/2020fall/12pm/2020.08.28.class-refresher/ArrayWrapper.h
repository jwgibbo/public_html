#ifndef ARRAY_WRAPPER_H
#define ARRAY_WRAPPER_H

class ArrayWrapper
{
	private:
	char* m_arr;
	int m_size;
	
	public:
	/**
	@pre size is valid
	@post Creates an array of the given size
	*/
	ArrayWrapper(int size);
	
	//return value at an index
	//assume index is valid
	char getEntry(int index);
	
	//assigns the value to the index
	//returns true is successful, false
	//otherwise
	bool setEntry(int index, char value);
	
};

#endif

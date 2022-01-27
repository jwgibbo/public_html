
#ifndef SOMECLASS_H
#define SOMECLASS_H
class SomeClass
{
	public:
	SomeClass(int data);
	void interactWithData(void func(int)) const;
	
	private:
	int m_data;
};
#endif
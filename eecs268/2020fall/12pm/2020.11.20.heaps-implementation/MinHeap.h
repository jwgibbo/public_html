
template <typename T>
class MinHeap
{
	
	public:
	MinHeap();
	void add(T entry);
	void remove();
	
	private:
	T* m_arr;
	int m_arrSize;
	int m_heapSize;
	
	//Assume this works.
	//Assume it doubles the array size
	void resize(); 
	
	//Private, recursive, upheap
	void upheap(int index);
	void downheap(int index);
};
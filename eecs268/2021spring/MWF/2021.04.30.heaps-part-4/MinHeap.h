

template <typename T>
class MinHeap
{
	private:
	T* m_arr;
	int arraySize;
	int heapSize;
	void resize();//makes more room
	void upheap(int index);
	
	public:
	void add(T entry);
	
};
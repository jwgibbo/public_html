
//This does NOT scale with n^2
//It runs in constant time 
//Big-O:  O(1)
for(int i=0; i<10; i++)
{
	//do something	
}


//The number of iterations scales
//with n.
//It scales in a linear way
//Big-O: O(n)
for(int i=0; i<n; i++)
{
	//do something
}	

//The number of iterations scales
//with n.
//It scales in an n^2 (quadratic)
//Big-O==>   O(n^2) 
for(int i=0; i<n; i++)
{
	for(int j=0; j<n; j++)
	{
		//do something
	}
}



//This array's is our n (problem size)
//As size goes up, so does the amount
//of memory we need
//Space complexity: O(n)
char* sequence = new char[size];
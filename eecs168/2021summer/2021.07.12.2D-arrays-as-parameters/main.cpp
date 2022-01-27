#include <iostream>
#include <string>

//Goal: define a function that can 
//		fill a 2D array with -1s
void fill2D(int* array2D[], int rows, int cols)
{
	for(int i=0; i<rows; i++)
	{
		for(int j=0; j<cols; j++)
		{
			array2D[i][j] = -1;
		}
	}
}

int main(int argc, char* argv[])
{
	std::string arg1 = "";
	std::string arg2 = "";
	int num = 0;
	
	if(argc == 3)
	{
		arg1 = argv[1];//copies argument into string
		num = std::stoi(argv[2]);

		std::cout << arg1 << '\n';
		std::cout << (num+10) << '\n';
	}
	else
	{
		std::cout << "Wrong number of command line arguments!\n";
	}
	return(0);
}
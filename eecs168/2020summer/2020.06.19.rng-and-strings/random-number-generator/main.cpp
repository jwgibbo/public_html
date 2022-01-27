#include <iostream>
#include <stdlib.h>
#include <time.h>

int main()
{	
	int lottoNumber = 0;
	int randomNumber = 0;
	
	//seed the random number generator
	srand(time(NULL));
	std::cout << "time: " << time(NULL) << '\n';
	
	//print 10 """random""" number
	for(int i=0; i<5; i=i+1)
	{
		//rand() produces a "random" number
		randomNumber = rand(); 
		std::cout << randomNumber << '\t';
		
		//mod:  n%m  ==> 0<->(m-1)
		lottoNumber = (randomNumber % 30)+1;
		std::cout << lottoNumber << '\n';
	}
	
	return(0);
}
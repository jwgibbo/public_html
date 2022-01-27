#include <iostream>
#include <fstream>

int main()
{
	int days = 0;
	std::cout << "How many days have you been quarantine? ";
	std::cin >> days;
	
	std::cout << "Man, that stinks. " << days;
	std::cout << " is a long time. :*(\n";
	
	//declare an ofstream object
	std::ofstream myOutFile;
	std::ifstream myInFile;
	
	//open a specific file 
	//if the doesn't exist, it creates it
	//if it does exist, it overrides it
	int num=0;
	char symbol='\0';
	double pi=0;
	
	myOutFile.open("diary.txt");
	myInFile.open("data.txt");
	
	//write to the file, like you would write to terminal
	myOutFile << "Hey, dairy\nit's been " << days;
	myOutFile << " days since I last saw milk.\n";
	
	myInFile >> num;
	myInFile >> symbol;
	myInFile >> pi;
	
	std::cout << "Here's what we got from file:\n";
	std::cout << num << ' ' << symbol << ' ' << pi << '\n';
	
	//close the file
	myOutFile.close();
	
	
	return(0);
}
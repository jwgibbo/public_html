#include <string>
#include <iostream>
#include <fstream>

int main()
{
	std::ifstream inFile("pokemon.dat");
	std::string englishName;
	std::string japaneseName;
	int pokedexNumber = 0;

	while(inFile >> englishName >> pokedexNumber >> japaneseName)
	{
		std::cout << englishName << ' ' << pokedexNumber << ' ' << japaneseName << '\n';
	}

	return(0);
}

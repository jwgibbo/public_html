prog: main.o Animal.o Dog.o
	g++ -std=c++11 -Wall -g main.o Animal.o Dog.o -o prog

main.o: main.cpp Animal.h
	g++ -std=c++11 -Wall -g -c main.cpp

Animal.o: Animal.h Animal.cpp
	g++ -std=c++11 -Wall -g -c Animal.cpp

Dog.o: Dog.h Dog.cpp
	g++ -std=c++11 -Wall -g -c Dog.cpp
clean:
	rm *.o prog
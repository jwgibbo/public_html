prog: main.o CoolString.o
	g++ -std=c++11 -g -Wall main.o CoolString.o -o prog

main.o: main.cpp
	g++ -std=c++11 -g -Wall -c main.cpp

CoolString.o: CoolString.h CoolString.cpp
	g++ -std=c++11 -g -Wall -c CoolString.cpp

clean: 
	rm *.o prog
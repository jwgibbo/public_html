prog: main.o CoolString.o
	g++ -std=c++11 -Wall -g main.o CoolString.o -o prog
	
main.o: main.cpp CoolString.h
	g++ -std=c++11 -Wall -g -c main.cpp

CoolString.o: CoolString.h CoolString.cpp
	g++ -std=c++11 -Wall -g -c CoolString.cpp

clean:
	rm *.o prog
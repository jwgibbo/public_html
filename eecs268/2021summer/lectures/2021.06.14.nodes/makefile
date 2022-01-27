prog: main.o Node.o
	g++ -std=c++11 -g -Wall main.o Node.o -o prog
	
main.o: main.cpp
	g++ -std=c++11 -g -Wall -c main.cpp

Node.o: Node.h Node.cpp
	g++ -std=c++11 -g -Wall -c Node.cpp

clean:
	rm *.o prog
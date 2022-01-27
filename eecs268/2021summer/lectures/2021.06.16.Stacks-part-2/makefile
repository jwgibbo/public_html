prog: main.o Node.o StackOfInts.o
	g++ -std=c++11 -g -Wall main.o Node.o StackOfInts.o -o prog
	
main.o: main.cpp
	g++ -std=c++11 -g -Wall -c main.cpp

Node.o: Node.h Node.cpp
	g++ -std=c++11 -g -Wall -c Node.cpp

StackOfInts.o: StackOfInts.h StackOfInts.cpp
	g++ -std=c++11 -g -Wall -c StackOfInts.cpp

clean:
	rm *.o prog
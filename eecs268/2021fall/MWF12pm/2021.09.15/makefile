prog: main.o
	g++ -std=c++11 -g -Wall main.o  -o prog
	
main.o: main.cpp
	g++ -std=c++11 -g -Wall -c main.cpp

clean:
	rm *.o prog
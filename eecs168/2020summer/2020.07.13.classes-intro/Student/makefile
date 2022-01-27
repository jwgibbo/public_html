prog: main.o
	g++ -std=c++11 -Wall -g main.o -o prog
	
main.o: main.cpp Student.h
	g++ -std=c++11 -Wall -g -c main.cpp

clean:
	rm *.o prog
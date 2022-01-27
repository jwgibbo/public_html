prog: main.o Student.o
	g++ -std=c++11 -g -Wall main.o Student.o -o prog

main.o: main.cpp
	g++ -std=c++11 -g -Wall -c main.cpp

Student.o: Student.h Student.cpp
	g++ -std=c++11 -g -Wall -c Student.cpp

clean: 
	rm *.o prog
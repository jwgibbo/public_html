#Goal write a recursive factorial
#4! ==> 4*3*2*1 ==> 4*3!
#3! ==> 3*2*1 ==> 3*2!
#2! ==> 2*1 ==> 2*1!
#1! ==> 1
def rec_fact(n):
    if n <= 1: #base case
        return 1
    else:
        #recursive case
        return n*rec_fact(n-1)

def main():
    answer = rec_fact(3)
    print(answer)

main()

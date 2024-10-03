#Goal: Write a recursive factorial function
# 5! ==> 5*4*3*2*1 ==> 5*4!
# 4! ==>   4*3*2*1 ==> 4*3!
# 3! ==>     3*2*1 ==> 3*2!
# 2! ==>       2*1 ==> 2*1!
# 1! ==>         1

def rec_fact(num):
    if num <= 1:
        return 1
    else:
        num*rec_fact(num-1)

def main():
    answer = rec_fact(2)
    print(answer)
main()

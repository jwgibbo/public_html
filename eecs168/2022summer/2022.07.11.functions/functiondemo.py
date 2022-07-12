#Goal: Write a function that can take
#      a number and calculate what
#       1 more than that number is
def one_more(num):
    ans = num + 1
    return ans

#Goal: Define a function that takes
#       two numbers and returns the
#       larger value
def larger(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


ans = larger(2**8, 8**2)
print(ans)

ans = larger(True, 'catfood') #ERROR
print(ans)

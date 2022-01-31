def my_div(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        raise ZeroDivisionError

def middle_func(num1, num2):
    print("middle_func called")
    ans = 0
    try:
        ans =  my_div(num1,num2)
    except:
        print("Something went wrong, but it's not middle_func's fault. I swear! Don't fire me! I'm needed! I'm important!")
    print("middle_func ending")
    return ans

def main():
    ans = my_div(10, 5)
    print(ans)

    try:
        ans = my_div(20, 5)
        print(ans)
        ans = my_div(20, 0)
        print(ans) 
    except:
        print("Ut oh! Something broke!")

    print(f"ans = {ans}")
    #print("ans = " + str(ans))

main()

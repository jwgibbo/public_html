def user_add():
    #user_num was not a parameter
    #not a locally declared function
    #in this context it's the global
    #variable declared in the global
    #scope. Again, this is discouraged!
    ans = add_one(user_num)
    return ans

def add_one(num):
    ans = num + 1
    return ans

user_num =int(input("Enter a number: "))
print(user_add())

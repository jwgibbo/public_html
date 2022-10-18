def greeting(name):
    print("Oh hello, ", name)
    print("So good to see you!")

def main():
    user_name = input("Enter name: ")
    #when calling a function that
    #does not return a value, it's
    #stand-alone statement
    greeting(user_name)

main()

#functions as arguments

def func_as_parameter_demo(func, value):
    func(value) #func is an alias for the function
                #that was passed in

def excited_print(word):
    print(word+"!!!!!!!")

def main():
    func_as_parameter_demo(excited_print, 'nerds')

main()   

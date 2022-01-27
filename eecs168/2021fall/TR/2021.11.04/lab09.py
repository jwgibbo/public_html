#import standard modules
import random

#import a module (.py file) in the same
#directory as this file
import potpourri

def main():
    potpourri.greeting(first_name='John', last_name='Gibbons')


#at the global scope
#check to see if this was file
#that was the entry point to the program
if __name__ == "__main__":
    main()  

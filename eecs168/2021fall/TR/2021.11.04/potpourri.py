def two_params(param1, param2):
    print("param1 = ", param1, end='\t')
    print("param2 = ", param2)

def default_params(param1=0, param2='apples'):
    print("param1 = ", param1, end='\t')
    print("param2 = ", param2)   

def positional_args(param1, param2, /):
    print("param1 = ", param1, end='\t')
    print("param2 = ", param2)

def keyword_args(*, param1, param2):
    print("param1 = ", param1, end='\t')
    print("param2 = ", param2)

def greeting(*, first_name, last_name):
    welcome = 'Hello! ' + str(last_name) + ', ' + str(first_name)
    print(welcome)

def main():
    greeting(first_name='John', last_name='Gibbons')
    greeting(first_name='Gibbons', last_name='John')
    
    func_name = "keyword_args"
    print(func_name.center(30,'='))
    keyword_args(param1='a', param2='b')
    keyword_args(param2='a', param1='b')
    #keyword_args('a', 'b')
    
    func_name = "positional_args"
    print(func_name.center(30,'='))
    positional_args('a', 'b')
    positional_args('b', 'a')
    #positional_args(param2='a', param1='b')
    
    func_name = "two_params"
    print(func_name.center(30,'='))
    two_params('a', 'b')
    two_params('b', 'a')
    two_params(param1='a', param2='b')
    two_params(param2='a', param1='b')

    func_name = "default_params"
    print(func_name.center(30,'='))
    default_params(5, 'oranges')
    default_params(5)
    default_params()

if __name__ == "__main__":
    main()

def two_params(param1, param2):
    print('param1 = ', str(param1), end='\t')
    print('param2 = ', str(param2))

def default_vals(param1='hello', param2=55):
    print('param1 = ', str(param1), end='\t')
    print('param2 = ', str(param2))

def pos_and_optional(param1, param2, /, param3, param4):
    print('param1 = ', str(param1), end='\t')
    print('param2 = ', str(param2), end='\t')
    print('param3 = ', str(param3), end='\t')
    print('param4 = ', str(param4))

def greeting(*, first_name, last_name):
    print(f'Hello {last_name}, {first_name}')

def main():
    
    func_name = 'calling two_params'
    print(func_name.center(30,'='))
    two_params('a', 'b')
    two_params('b', 'a')
    two_params(param1='a', param2='b')
    two_params(param2='a', param1='b')

    func_name = 'calling default_vals'
    print(func_name.center(30,'='))
    default_vals('cat', 22)
    default_vals('cat')
    default_vals(param2=22)
    
    func_name = 'calling default_vals'
    print(func_name.center(30,'='))
    pos_and_optional('a','b','c','d')
    #pos_and_optional(param2='a',param1='b','c','d')
    pos_and_optional('a','b',param4='c',param3='d')

    func_name = 'calling default_vals'
    print(func_name.center(30,'='))
    greeting(last_name="Gibbons", first_name="John")
    
main()

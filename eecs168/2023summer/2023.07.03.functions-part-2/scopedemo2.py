def num_changer(num):
    print('num before change: ', num)
    num = -1
    print('num after change:', num)

def list_changer(some_list):
    print('list before change:', some_list)
    some_list[0] = 'doody'
    print('list after change:', some_list)

def main():
    num = 5
    num_changer(num)
    print('The num back in main', num)
    #see illustrations 2

    words = ['mic', 'broken', 'why', 'how']
    list_changer(words)
    print('List back in main:', words)
    #see illustration 3

main()

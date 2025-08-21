
def main():
    employee_info = ('John Gibbons', 123456789, '01-01-1901')

    print(employee_info)
    print(type(employee_info))
    print(len(employee_info))

    for elem in employee_info:
        print(elem)

    print('-------')

    print(employee_info[0])
    employee_info[0] = 'Gohn Jibbons'

main()

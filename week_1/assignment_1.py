def diagonal():
    string = input('please inpyt your string:')
    for i in range(len(string)):
        print(f'{" " * i}{string[i]}')
def rev_diagonal():
    string = input('please input your string:')
    for i in range(len(string)):
        print(f'{" " * (len(string) - i)}{string[i]}')
def main():
    a = input('Do you want to get strings in reverse diagonal?(y/n)')
    if (a=='n'):
        diagonal()
    elif(a=='y'):
        rev_diagonal()
    else:
        print('invalid input, please try again')
        main()
main()
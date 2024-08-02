# 1. definition

def foo(values, n):
    n **= 2 
    print(f'inside foo ({id(n)}) n = {n}')

    values.sort(reverse=True)

    print(f'inside foo ({id(values)}) values:{values}')

if __name__ == '__main__':
    
    #  call
    # mutable
    numbers = [1, 4, 6, 2, 3]
    # immutable
    a = 10
    print(f'before numbers ({id(numbers)}):{numbers} a({id(a)}) ={a}')

    foo(numbers, a)

    print(f'after numbers ({id(numbers)}):{numbers} a({id(a)}) ={a}')

    print('---')
# port - global var
port = 1521
# 1. definition
def sum_values(a, b, *args):
    # c - local var
    print(f'type of args:{type(args)} args:{args}')
    c = a + b
    for i in args:
        c += i
    return c


if __name__ == '__main__':
    
    # 2. call
    x, y = 15, 16
    res = sum_values(x, y)
    print(f'{x} + {y} = {res}')

    res = sum_values(4, 7, 5)
    print(f'res2 = {res}')

    res = sum_values(4, 7, 5, 8, 9)
    print(f'res3 = {res}')

    arr = [1, 2, 3, 4, 5]
    
    res = sum_values( 2, 3, *arr)
    print(f'res4={res}')
    print('---')
# port - global var
port = 1521
# 1. definition
def sum_values(a, b):
    # c - local var
    c = a + b
    return c


if __name__ == '__main__':
    
    # 2. call
    x, y = 15, 16
    res = sum_values(x, y)
    print(f'{x} + {y} = {res}')

    res = sum_values(4, 7)
    print(f'res = {res}')

    print('---')
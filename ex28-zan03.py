# port - global var
port = 1521
# 1. definition
def sum_values(a, b, d=None):
    # c - local var
    c = a + b + d if d else a + b
    return c


if __name__ == '__main__':
    
    # 2. call
    x, y = 15, 16
    res = sum_values(x, y)
    print(f'{x} + {y} = {res}')

    res = sum_values(4, 7, 5)
    print(f'res = {res}')

    print('---')
# 1 + 2 + 3 ... + 100 = 5050
# 1. definition

def sum_n(n):
    print(f'n={n}')

    if n > 0:
        return n + sum_n(n-1)
    return 0

if __name__ == '__main__':
    
    #  call
    res = sum_n(3)
    print(f'res = {res}')
    print('---')
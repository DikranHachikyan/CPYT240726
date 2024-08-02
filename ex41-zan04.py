def get_squares(n):
    return [ i ** 2 for i in range(1, n + 1)]

# 1. definition
def generate_squares(n):
    for i in range(1, n+1):
        yield i ** 2

if __name__ == '__main__':
    #  call
    values = get_squares(10)
    print(f'values={values}')

    # 2. assign
    gs = generate_squares(10)

    print(f'types:generate squares is:{type(generate_squares)}, gs is:{type(gs)}')
    
    print(f'1=>{next(gs)}')
    print(f'2=>{next(gs)}')
    print(f'3=>{next(gs)}')
    print(f'4=>{next(gs)}')

    arr = list(gs)
    print(f'arr={arr}')

    # print(f'5=>{next(gs)}')

    gs2 = generate_squares(4)

    for i in gs2:
        print(f'i={i}')

    print('---')
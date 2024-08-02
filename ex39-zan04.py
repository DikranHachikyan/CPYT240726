# 1. definition

if __name__ == '__main__':
    #  call
    pow_xy = lambda x,y: x ** y

    z = pow_xy(2, 4)
    print(f'z={z}')
    
    numbers = [4, 2, 3, 5, 3]
    for i in map( lambda el: el ** 2, numbers ):
        print(f'i={i}')

    print('---')
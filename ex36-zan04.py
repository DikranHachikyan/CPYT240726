# 1. definition

def foo(a=[], b={}):
    print(f'a={a} b={b}')
    print('-' * 30 )

    n = len(a)
    a.append(n)
    b[n] = n

if __name__ == '__main__':
    
    #  call
    foo()

    foo([2, 4, 5], {'z':20})

    foo()
    
    foo([12, 24, 35], {'x':10})

    foo()
    
    print('---')
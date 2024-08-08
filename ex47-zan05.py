
from functools import wraps

def to_upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper._original = func
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper

@to_upper
def concat(*args, **kwargs):
    '''Concatenate args with separator sep'''
    # print(f'args:{args}')
    sep = kwargs.get('sep', ';')
    return sep.join(args)

if __name__ == '__main__':
    #  call
    users = ['anna', 'maria', 'markus', 'jorg']

    print(f'users:{concat(*users)}')
    print(f'users:{concat(*users, sep=", ")}')
    
    values = [11, 23, 45, 6, 2]
    print(f'values={concat(*values, sep="|")}')
    
    # restore original 
    concat = concat._original
    print(f'users:{concat(*users, sep=", ")}')

    
    print('---')

from functools import wraps

def to_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'{v}' for v in args]
        # args = [ str(v) for v in args]
        return func(*args, **kwargs)
    return wrapper


@to_string
def concat(*args, **kwargs):
    '''Concatenate args with separator sep'''
    print(f'args:{args}')
    sep = kwargs.get('sep', ';')
    return sep.join(args)

if __name__ == '__main__':
    #  call
    users = ['anna', 'maria', 'markus', 'jorg']

    print(f'users:{concat(*users)}')
    print(f'users:{concat(*users, sep=", ")}')
    
    values = [11, 23, 45, 6, 2]
    print(f'values={concat(*values, sep="|")}')

    
    print('---')
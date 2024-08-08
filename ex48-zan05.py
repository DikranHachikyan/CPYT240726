
from functools import wraps

def to_upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper._original = func
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    #  call
    users = ['anna', 'maria', 'markus', 'jorg']

    print(*users)

    print = to_upper(print)
    
    print(*users)
    print('hello python')
    print(f'hello python! users:{users}')

    print = print._original

    print(*users)
    print('---')
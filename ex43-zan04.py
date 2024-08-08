# 1
# import time
# print(f'now is:{time.time()}')

# 2
# import time as tm
# print(f'now is:{tm.time()}')

# 3
# from time import time, sleep
# print(f'now is:{time()}')

# 3.1
# from time import time as now, sleep
# print(f'now is:{now()}')

from time import time, sleep
from functools import wraps

# 1. definition
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwarg):
        t = time()
        return func(*args, **kwarg)
        print(f'1 name:{func.__name__} doc str:{func.__doc__} exec time:{time() -t:.3f}s')
    
    return wrapper



@measure_time
def foo(sleep_time=0.5):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)

if __name__ == '__main__':
    #  call

    
    foo()
    
    foo(1)
    
    print(f'2 name:{foo.__name__} doc str:{foo.__doc__}')
    print('---')
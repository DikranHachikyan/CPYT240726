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


def foo(sleep_time=0.5):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)

if __name__ == '__main__':
    #  call

    t = time()
    foo()
    print(f'exec time:{time() - t:.3f}s')    

    t = time()
    foo(1)
    print(f'exec time:{time() - t:.3f}s')    

    print('---')
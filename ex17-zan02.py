
# 2 + 4 + ... + 100 = 2550
# print(f'name is:{__name__}')

if __name__ == '__main__':
    i = 1
    sum_n = 0
    is_interrupted = True

    while i <= 100:
        i += 1

        if i == 5:
            break

        sum_n += i
    else:
        is_interrupted = False
        print('--- else ---')

    print(f'2+4+..+100={sum_n} is interrupted:{is_interrupted}')
    print('---')
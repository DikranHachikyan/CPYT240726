
# 2 + 4 + ... + 100 = 2550
# print(f'name is:{__name__}')

if __name__ == '__main__':
    i = 1
    sum_n = 0

    while i <= 100:
        i += 1

        if (i % 2) != 0:
            continue

        sum_n += i
    else:
        print('--- else ---')

    print(f'2+4+..+100={sum_n}')
    print('---')
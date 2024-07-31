

if __name__ == '__main__':
    
    sqrs = [ i ** 2 for i in range(1, 11) ]
    print(f'values={sqrs}')

    txt = 'Lorem ipsum dolor'

    symb = [ f'-{s}-' for s in txt]

    print(f'symb={"".join(symb)}')

    values = [ f'i={i},j={j}' for i in range(3) for j in range(4)]
    
    # for i in range(3):
    #     for j in range(4):
    #         print(f'i={i},j={j}')

    print(f'values={values}')
    print('---')
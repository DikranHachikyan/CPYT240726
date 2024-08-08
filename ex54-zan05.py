def numeric_input(prompt):

    value = float(input(prompt))

    if value < 1 or value > 10:
        raise ValueError(f'Value out of range:{value}')
    return value


if __name__ == '__main__':
    
    try:
        res = numeric_input('Value=')
        print(f'res = {res}')
        res = numeric_input('Value=')
        print(f'res = {res}')
    except ValueError as e:
        print(f'input error:{e}')
    
    print('---')
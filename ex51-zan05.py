

if __name__ == '__main__':
    actions = {
        '+': lambda a,b: a + b,
        '/': lambda a,b: a / b
    }
    
    while True:
        try:
            op = input('actions (+, /, q-quit):')

            if op == 'q':
                quit()
                # break

            value1 = float(input('first number:'))
            value2 = float(input('second number:'))

            result = actions[op]( value1, value2)

        except KeyError as e:
            print(f'Unsupported operation:{e}')
        except ValueError as e:
            print(f'Invalid number:{e}')
        except KeyboardInterrupt as e:
            print(f'Keyboard interrupt:{e}')
        except Exception as e:
            print(f'Unknown error:{e}')
        # 1. python only
        else:
            print(f'{value1} {op} {value2} = {result}')
            continue
        finally:
            print(f'--- finally ---')

    print('---')
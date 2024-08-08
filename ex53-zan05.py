def print_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
    # или 
    # except:
        # 3. обичайното решение
        raise
        # 2. много лоша идея
        # pass
        
        # 1. лоша идея
        # print(f'Invalid key:{e}')
    
    print('--- end of print key ---')


if __name__ == '__main__':
    conn = {
        'host':'localhost',
        'port':1521,
        'service':'oracle-xe'
    }

    try:
        print_key('host', **conn)
        print_key('ip', **conn)
    except KeyError as e:
        print(f'Unknown key:{e}')
    print('---')
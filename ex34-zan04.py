# 1. definition

def sort_priority( values, pri_group):
    found = False

    def sort_helper(el):
        nonlocal found
        if el in pri_group:
            found = True
            return (0, el)
        return (1, el)

    values.sort( key=sort_helper )
    
    return found


if __name__ == '__main__':
    
    #  call
    numbers = [5, 4, 6, 3, 7, 8, 9]
    group = {8, 3, 5}

    is_found = sort_priority( numbers, group)

    print(f'numbers:{numbers} is found:{is_found}')
    print('---')
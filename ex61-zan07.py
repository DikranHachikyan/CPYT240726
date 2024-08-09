import re

if __name__ == '__main__':
    
    while True:
        names = input('Firstname Lastname:')

        if names == 'q': break
        
        match = re.match(r'\w+\s\w+', names)
        if not match:
            names = None
            continue
        start, end, span = match.start(), match.end(), match.span()
        print(f'names:{names} start:{start} end:{end}') 

    print('--- end ---')
import re

if __name__ == '__main__':
    
    while True:
        names = input('Firstname Lastname:')

        if names == 'q': break
        
        match = re.fullmatch(r'[A-Z][a-z]+.*[A-Z][a-z]+', names)
        if not match:
            names = None
            continue
        start, end, span = match.start(), match.end(), match.span()
        print(f'names:{names[start:end]} start:{start} end:{end}') 

    print('--- end ---')
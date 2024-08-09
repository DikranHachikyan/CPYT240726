import re

if __name__ == '__main__':
    
    while True:
        names = input('Firstname Lastname:')

        if names == 'q': break
        
        names = names.strip()
        match = re.match(r'([A-Z][a-z]+)\s([A-Z][a-z]+)', names)
        if not match:
            names = None
            continue
        start, end, span = match.start(), match.end(), match.span()
        # first, last = match.groups()
        first, last = match.group(1), match.group(2)
        print(f'names:{first} {last} start:{start} end:{end}') 

    print('--- end ---')
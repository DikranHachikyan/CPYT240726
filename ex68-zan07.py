import re

if __name__ == '__main__':
    
    while True:
        names = input('Firstname Lastname:')

        if names == 'q': break
        
        names = names.strip()
        match = re.match(r'(?P<first>[A-Z][a-z]+)\s(?P<last>[A-Z][a-z]+)', names)
        if not match:
            names = None
            continue
        start, end, span = match.start(), match.end(), match.span()
        # first, last = match.groups()
        # first, last = match.group('first'), match.group('last')
        user = match.groupdict()
        print(f'names:{user["first"]} {user["last"]} start:{start} end:{end}') 

    print('--- end ---')
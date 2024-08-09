import re


if __name__ == '__main__':
    
    regex = r'(?P<first>[a-z]+)\s(?P<last>[a-z]+)'
    
    pattern = re.compile(regex, re.I | re.M)

    while True:
        names = input('Firstname Lastname:')

        if names == 'q': break
        
        names = names.strip()
        match = re.match( pattern, names)
        if not match:
            names = None
            continue
        start, end, span = match.start(), match.end(), match.span()
        # first, last = match.groups()
        # first, last = match.group('first'), match.group('last')
        user = match.groupdict()
        print(f'names:{user["first"]} {user["last"]} start:{start} end:{end}') 

    print('--- end ---')
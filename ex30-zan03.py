# port - global var
port = 1521
# 1. definition
def show(title, ver='1.1.1', *args, **kwargs):
    print(f'title (positional):{title}')
    
    print(f'ver (optional): {ver}')

    print('args:')
    for i in args:
        print(i, end=' ')
    print()

    print('kwargs:')
    params = {
        'clr': kwargs.get('color', 'black'),
        'font': kwargs.get('font', 'sans-serif')
    }
    print(f'params:{params}')
    


if __name__ == '__main__':
    
    #  call
    # 1.
    # show('Text Editor')

    # 2.
    # show('Text Editor', '2.0.0')

    # 3.
    show('Text Editor', '2.0.0', 1, 2 ,3, 4)
    
    # 4.
    show('Text Editor', '2.0.0', 1, 2 ,3, 4, color='red', font='monospace')
    show('Text Editor', '2.0.0', 1, 2 ,3, 4, color='red')
    show('Text Editor', '2.0.0', 1, 2 ,3, 4, font='monospace', color='red')
    
    print('---')
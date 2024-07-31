# port - global var
port = 1521
# 1. definition
# problem!!
# def show(title, ver='1.1.1', *args, **kwargs):
def show(title, *args, ver='1.1.1', **kwargs):
    print(f'title (positional):{title}')
    
    print(f'ver (optional key-word only): {ver}')

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
    show('Text Editor', 1, 2 ,3, 4, ver='2.0.0', font='monospace', color='red')
    
    show('Text Editor', 1, 2 ,3, 4, font='monospace', color='red')
    
    print('---')
# port - global var
port = 1521
# 1. definition

def show(title, *, ver='1.1.1', **kwargs):
    print(f'title (positional):{title}')
    
    print(f'ver (optional key-word only): {ver}')


    print('kwargs:')
    params = {
        'clr': kwargs.get('color', 'black'),
        'font': kwargs.get('font', 'sans-serif')
    }
    print(f'params:{params}')
    


if __name__ == '__main__':
    
    #  call
    show('Text Editor', ver='2.0.0', font='monospace', color='red')
    
    show('Text Editor', font='monospace', color='red')
    
    print('---')
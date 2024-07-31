# port - global var
port = 1521
# 1. definition
def show():
    global port
    port = 3306
    print(f'port:{port}')
    


if __name__ == '__main__':
    
    #  call
    print(f'(before) global var port:{port}')
    show()
    print(f'(after) global var port:{port}')

    print('---')
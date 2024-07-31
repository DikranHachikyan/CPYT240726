

if __name__ == '__main__':
    
    tp = 12, 34, 56, 78, 1

    for item in enumerate(tp, start=5):
        index, value = item
        
        print(f'index = {index}, value={value}')

    print('---')
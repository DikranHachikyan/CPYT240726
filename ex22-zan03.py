

if __name__ == '__main__':
    
    users = ['Anna', 'Maria', 'Markus', 'Jorg']
    mails = ['anna@no.com', 'maria@no.com', 'markus@no.com']
    
    for data in zip(users, mails):
        name, mail = data
        print(f'name={name}, mail={mail}')

    print('---')
# %%
conn = dict(
    port=1521,
    db='sales',
    host='localhost',
    keepalive=True
)

print(f'conn={conn}')

print(f'port = {conn["port"]}')

# %%
# !!bad idea!!
conn1 = [1521, 'sales','localhost',True]

print(f'conn1={conn1}')

ports = 22, 222, 3457
# %%
# JSON -> JavaScript Object Notation
user = {
    'first_name': 'Anna',
    'last_name' : 'Smith',
    'age': 34,
    'friends': ['John','Markus'],
    'contacts':{
        'phone': '111-22-33',
        'mail': 'anna@no.com'
    }
}

print(f'user={user}')
# %%
print(user.keys())

# %%

print(user.values())
# %%

print(user.items())
# %%
print('age' in user)
# %%
print( 34 in user.values())

# %%
# Throws KeyError
print(user['address'])
# %%
print(user.get('address'))
# %%

print(user.get('address','Sofia'))
# %%

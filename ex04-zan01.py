# %%

s1 = 'Lorem ipsum dolor sit amet'
s2 = "Lorem ipsum dolor sit amet"

print(s1)
print(s2)
# %%
s3 = '''Lorem
ipsum
dolor sit amet'''

print(s3)
# %%

# Function foo prints Hello
# Python
# created: 26.07.2024
# author: Me
def foo():
    '''Function foo prints Hello
    Python
    created: 26.07.2024
    author: Me
    '''
    print('Hello Python')

# %%
foo()
# %%
print(foo.__doc__)
# %%
print(s1[3])
# %%
print(s1[0:5])
# %%
# start:stop:step
print(s1[0:20:2])
# %%
print(s1.upper())
# %%
print('-' * 20)
# %%

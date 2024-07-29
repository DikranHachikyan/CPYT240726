# %%
tp = (12, 34, 5, 6, 89, 9)

print(f'tp={tp}')
# %%
print(f'tp[1]={tp[1]}')
# %%
# tp[1] = 1
# %%
a, b, c, d, e, f = tp

print(f'a={a}, b={b}, c={c}, d={d}, e={e}, f={f}')

# %%

a, b, c, *_ = tp

print(f'a={a}, b={b}, c={c}')
# %%

*_, a, b, c = tp

print(f'a={a}, b={b}, c={c}')
# %%

tp = 10, 20, 30

print(f'tp={tp} type of tp {type(tp)}')
# %%

tp = 19,
print(f'tp={tp} type of tp {type(tp)}')

# %%

print( 10 in tp)
# %%
print( 10 not in tp)
# %%
print( type(tp) is tuple )
# %%
 
# print( type(tp) == tuple )
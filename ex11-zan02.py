value = float(input('Enter a number:'))
output_txt = ''

if value >= 0:
    output_txt = 'positive'
else:
    output_txt = 'negative'

print(f'{value} is {output_txt} number')

print('---')
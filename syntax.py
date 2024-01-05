a=5

if a > 5:
    print('Bigger than 5') # this is inline comment
elif a>=0:
    print('In Between 0 and 5')
else:
    print('Negative')


# Conversions
num = '10'
result = int(num) + 5
print(result)

# String Concatenation
name = 'Divesh'
message = 'Hello, ' + name
print(message)

# Logical Operators
b = 10
if a > 5 and b < 10:
    print('Case 1')
elif not (a < 0 or  b < 0 ):
    print('Case 2')


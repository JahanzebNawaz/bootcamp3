

# logical operators

# and 

a = 5
b = 6
c = 7

# if a > c and c > b:
#     print('HEllo')


# or 


# if a > c or c > b:
#     print('HEllo')


# not 

# if not(a > c):
#     print('HEllo')



# Identity Operators

# b = a
# print( a, b)
# if a is b:
#     print('THIS')

# if a is not c:
#     print('not equals to c')



# Membership operators

# numbers = [2,3,4,5]

# if 2 in numbers:
#     print('THERE')


# if 6 not in numbers:
#     print('not in numbers')


# print(2 ^ 2)


# Bitwise Operators

# & AND 


a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0


c = a & b   # 12 = 0000 1100

# print(f'{c:08b}')


#  | OR

c = a | b   # 0011 1101

# print(f'{c} =  {c:08b}')


#  ^ XOR  

c = a ^ b  # 0011 0001
 
# print(f'{c} =  {c:08b}')



a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

# ~  NOT 

# c = ~a   #  1100 0011

# print(f'{c} =  {c:08b}')


# <<  Zero fill left shift

# print(f'{a} =  {a:08b}')

# print(f'{2} =  {2:08b}')

# c = a << 2;       # 240 = 1111 0000


# print(f'{c} =  {c:08b}')


# print(f'{a} =  {a:08b}')

# print(f'{2} =  {2:08b}')
# c = a >> 2;       # 15 = 0000 1111
# print(f'{c} =  {c:08b}')
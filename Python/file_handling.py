


# open()  function 

# r for read
#  a for append
#  w for write
#  x for create

# t for text
# b binary

import json
import os 



# if os.path.exists('person/test'):
#     os.rmdir('person/test')
# else:
#     print('file does not exists')




# f = open('data.json', mode='rb')
# f = open('data2.txt', mode='r')
# # f.write('A NEW FILE \n NEW')
# print(f.read())
# f.close()



# for line in f:
#     print(line)

# f.close()

# print(f.read(10))

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())



with open('data.json', mode='r') as f:
    data = json.load(f)
    

print(type(data))
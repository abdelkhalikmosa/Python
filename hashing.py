'''
MD5 hash function accepts a sequence of bytes and returns 
128-bit hash value
'''

from hashlib import md5

name = 'Abdo'
hashed_value = md5(name.encode())
print(hashed_value)
print(hashed_value.digest())
print(hashed_value.hexdigest())


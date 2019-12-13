'''
1. r+ used to do read and write operations both
2. if file is not exist it will through error
'''

fh = open('read_write.txt', 'r+')

# Using readline we can read only line and return in string format
print(fh.readline())

# Using readlines we can read entire file data and return in list format
fh.write('\nTEJA')

# To close a file
fh.close()

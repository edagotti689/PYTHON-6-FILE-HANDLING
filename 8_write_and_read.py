'''
1. w+ used to do write and read operations both
2. if file is not exist it will create a file
'''

fh = open('write_read.txt', 'w+')

# Using readlines we can read entire file data and return in list format
fh.write('TEJA')
fh.write('\nKrishna')

# Before reading data you should bring file handler position to starting position
fh.seek(0)

# read a line after writing 
print(fh.read())


# To close a file
fh.close()

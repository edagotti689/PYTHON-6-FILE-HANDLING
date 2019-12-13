'''
1. Seek is used to bring the file handler position where ever we required
'''

fh = open('names.txt', 'r')

# reading entire data from file
line  = fh.read()

# If you wnat to bring file handler position to starting
print(' FH position Before seek :', fh.tell())
fh.seek(0)
print(' FH position After seek  :', fh.tell())

# If you want to bring file handler to 5th position
print(' FH position Before seek :', fh.tell())
fh.seek(5)
print(' FH position After seek  :', fh.tell())

# To close a file
fh.close()

fh = open('names.txt', 'r')

# Using read we can read entire file data and return in string format
fdata = fh.read()
#fh.write('ok')
# Using readline we can read only line and return in string format
line  = fh.readline()

# Using readlines we can read entire file data and return in list format
lines = fh.readlines()


print(' Lines are \n:', lines)

# Using for loop also we can read FH data, it will iterate line by line
for line in fh:
    print(' For loop :', line)

# To close a file
fh.close()
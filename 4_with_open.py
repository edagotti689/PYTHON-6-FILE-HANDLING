# reading names.txt and writing into names_write.txt
with open('names.txt', 'r') as fr, open('names_write.txt', 'w') as fw:
    fr.write(fr.read())
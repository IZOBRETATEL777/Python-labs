fin = open('src.txt')
fout = open('output.txt', 'w')
for i in fin.readlines():
    if i.strip()[0] != '#':
        fout.write(i)
fin.close()
fout.close()


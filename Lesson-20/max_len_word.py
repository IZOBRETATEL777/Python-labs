fin = open('input.txt')
fout = open('output.txt', 'w')
a = fin.readlines()
print(a)
maxL = 0
for i in a:
    maxL = max(maxL, len(i))
for i in a:
    if maxL == len(i):
        fout.write(i)
fin.close()
fout.close()

fin = open('input.txt')
fout = open('output.txt', 'w')
a = fin.readlines()
rowCnt = 1
for i in range(len(a)):
    a[i] = a[i].split()
    if len(a[i]) == 0:
        continue
    if int(a[i][2]) >= 675:
        fout.write(str(rowCnt) + ' ' + a[i][0] + ' ' + a[i][1] + '\n')
        rowCnt += 1
fin.close()
fout.close()


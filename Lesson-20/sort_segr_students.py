fin = open('input.txt')
fout = open('output.txt', 'w')
rowCnt = 1
a = []
for i in fin.readlines():
    i = i.split()
    if len(i) == 0:
        continue
    if float(i[2]) >= 675:
        a.append(i)
a.sort(key=lambda i: float(i[2]), reverse=True)
for i in a:
    fout.write(str(rowCnt) + ' ' +  i[0] +  ' ' +  i[1] + ' ' + i[2] + '\n')
    rowCnt += 1
fin.close()
fout.close()

fin1 = open('input1.txt')
fin2 = open('input2.txt')
a = []
b = []
for i in fin1.readlines():
    if i:
        a.append(int(i.split()[0]))
for i in fin2.readlines():
    if i:
        b.append(int(i.split()[0]))
fin1.close()
fin2.close()
c = []
p1 = 0
p2 = 0
print(a)
print(b)
while len(c) < len(a) + len(b):
    if p1 < len(a) and (p2 >= len(b) or a[p1] < b[p2]):
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
print(c)
fout = open('output.txt', 'w')
fout.write(str([str(i) + '\n' for i in a]))
fout.close()


def sumDig(n):
    s = 0
    n = abs(n)
    while n > 0:
        s += n % 10
        n //= 10
    return s


fin = open('input.txt')
fout = open('output.txt', 'w')
a = [int(i) for i in fin.readlines()]
print(a)
a = sorted(a, key=lambda n: sumDig(n))
print(a)
fout.write(str([str(i) + '\n' for i in a]))
fin.close()
fout.close()


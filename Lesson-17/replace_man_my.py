def replaceAll(s, wOld, wNew):
    res = ''
    idx = s.find(wOld)
    while idx >= 0:
        res += s[:idx] + wNew;
        s = s[idx + len(wOld):]
        idx = s.find(wOld)
    return res + s


s, w1, w2 = input().split()
print(replaceAll(s, w1, w2))


def replaceAll ( s, wOld, wNew ):
    lenOld = len(wOld)
    res = ""
    while len(s) > 0:
        p = s.find ( wOld )
        if p < 0:
            res = res + s
            return res
        if p > 0: res = res + s[:p]
        res = res + wNew
        if p+lenOld >= len(s):
            s = ""
        else:
            s = s[p+lenOld:]
    return res
s, w1, w2 = input().split()
print(replaceAll(s, w1, w2))



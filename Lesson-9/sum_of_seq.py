def sumSeq():
    n = int(input())
    if n == 0:
        return 0
    return sumSeq() + n
print(sumSeq())

def printMatrix(a):
    for i in a:
        for j in i:
            print(f'{j:3d}', end=' ')
        print()
    print()


def spiral(n, m):    
    a = [[0] * m for _ in range(n)]
    cur = 1
    step = 0
    while n - step > 0 and m - step > 0:
        for row in range(step, m - step):
            if cur > n * m:
                break
            a[step][row] = cur
            cur += 1
        cur -= 1
        for col in range(step, n - step):
            if cur > n * m:
                break
            a[col][m - step - 1] = cur
            cur += 1
        cur -= 1
        for row in range(m - step - 1, step - 1, -1):
            if cur > n * m:
                break
            a[n - step - 1][row] = cur;
            cur += 1
        cur -= 1
        for col in range(n - step - 1, step - 1, -1):
            if col != step:
                a[col][step] = cur;
                cur += 1
                if cur > n * m:
                    break
        step += 1
    print()
    printMatrix(a)


def zigzagDiag(n, m):
    a = [[0] * m for _ in range(n)]
    x = 1
    y = 1
    for val in range(1, n * m + 1):
        a[x - 1][y - 1] = val
        if (x + y) % 2  == 1:
            if y < m:
                y += 1
            else:
                x += 2
            if x > 1:
                x -= 1;
        else:
            if x < n:
                x += 1
            else:
                y += 2
            if y > 1:
                y -= 1
    print()
    printMatrix(a)


def zigzag(n, m):
    a = [[0] * m for _ in range(n)]
    x = 0
    y = 0
    direction = 1
    for val in range(1, n * m + 1):
        a[x][y] = val
        x += direction
        if x == n:
            y += 1
            x = n - 1
            direction *= -1
        elif x == -1:
            y += 1
            x = 0
            direction *= -1
    print()
    printMatrix(a)


n = int(input("Enter N: "))
m = int(input("Enter M: "))
spiral(n, m)
zigzagDiag(n, m)
zigzag(n, m)

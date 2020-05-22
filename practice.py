m= int(input())
def solve(n):
    a = list(str(n))
    if len(a) < 2:
        print(int(a[0]))
    else:
        b = 1
        for i in range(0, len(a)):
            b = b * int(a[i])
        if b < 10:
            print(b)
        else:
            solve(b)
solve(m)









        



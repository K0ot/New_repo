a = [2, 4, 7]

def absoluteValuesSumMinimization(a):
    c = [0] * len(a)
    for i in range(len(a)):
        for j in a:
            c[i] += abs(a[i]-j)
    for i in range(len(c)):
        if c[i] == min(c):
            print(i)


absoluteValuesSumMinimization(a)
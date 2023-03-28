# This is a sample Python script.
# Selection Sort
def sortlist(L,n):
    L2 = []
    counter = 0
    while (counter <n):
        m, idx = searchMinFromList (L,n)
        L2.append(m)
        del L[idx]
        n = n-1

        return L2
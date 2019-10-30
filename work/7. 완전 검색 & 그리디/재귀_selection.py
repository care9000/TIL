def reselection(ary, s, e):
    if s == e:
        return
    else:
        minI = s
        for j in range(s+1, e, 1):
            if ary[j] < ary[minI]:
                minI = j

        ary[s], ary[minI] = ary[minI], ary[s]
        reselection(ary, s+1, e)



A = [0, 5, 89, 6, 46, 25, 96, 11, 37, 7, 6]

reselection(A, 0, len(A))
print(A)
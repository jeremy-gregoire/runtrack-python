L = [ i for i in range(1, 6) ]
print("La liste actuel:", L)

tmp = L[0]
L[0] = L[len(L) - 1]
L[len(L) - 1] = tmp

print("La liste avec les changements:", L)
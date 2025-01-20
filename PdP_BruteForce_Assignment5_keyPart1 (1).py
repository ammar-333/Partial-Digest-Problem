import math
import itertools


def brute_force_pdp(L, n):
    maxItem=max(L)
    My_L=[]
    X=[]
	combination=[]
	for i in range(1,maxItem):
		combination.append(i)

    sets = list(itertools.combinations(combination, n - 2))

    # for all set of (n-2)
    for set_ in sets: # iterate over all the cominations 
        X.append(0)
        X.append(maxItem)

        for i in set_:
            X.append(i)
            X.sort()

        for i in range(len(X)):
            for j in range(i + 1, len(X)):
                My_L.append(X[j] - X[i])
        My_L.sort()

        if L == My_L:
            return X

        del X[:]
        del My_L[:]

    return None




   

L = [2, 2, 3, 4, 5, 7]
    




size_L = len(L)
equation = math.sqrt(1 + 8 * size_L)
n = (1 + equation) / 2

solution = brute_force_pdp(L, int(n))
if solution:
    print("X=",solution)
else:
    print("No solution")
   

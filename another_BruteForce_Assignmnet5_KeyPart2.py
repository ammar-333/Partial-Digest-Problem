def BF_pd(l,n):
  maxitem=max(l)
  x=[]
  sets=list(itertools.combinations(l,n-2))
  newl=[]

  for s in sets :
    x.append(0)
    x.append(maxitem)
    for i in s :
      x.append(i)
      x.sort()
    for i in range(len(x)):
      for j in range(i+1 , len(x)):
        newl.append(abs(x[i]-x[j]))
    newl.sort()
    if newl==l:
      return x
    del x[:]
    del newl[:]
  return None


l=[2,2,3,4,5,7]

sizel=len(l)
equation = math.sqrt(1+8*sizel)
n=(1+equation)/2

x=BF_pd(l,int(n))
print(x)
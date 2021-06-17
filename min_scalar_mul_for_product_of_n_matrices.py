#To find minimum number of scalar multiplication needed to compute product of n matrices.

import sys
 
def Calc(p,i,j):
  if i==j:
    return 0
  m=sys.maxsize
  for k in range(i,j):
    count=(Calc(p,i,k) + Calc(p,k+1,j) + p[i-1] * p[k] * p[j])
    if count<m:
      m=count
  return m

print("Enter dimensions of matrices:",end=" ")
l=[int(i) for i in input().split()]
print("Minimum number of scalar multiplication:",Calc(l,1,len(l)-1))

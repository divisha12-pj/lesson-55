#one algo 3 faces
def fun1(n):
     return n*(n+1)/2
print("sum of numbers is ",fun1(5))


def fun2(n):
     sum=0
     for i in range (1,n+1):
          sum+=i
     return sum
          
print("sum of numbers is",fun2(5))
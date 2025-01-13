N=int(input("enter a number:"))
sum1=0
sum2=0
for i in range(N):#if we give the number n it its count from 0to n-1 so we give n+1
    sum1=sum1+i
print("sum1 is:",sum1)    
print("\n")
for i in range(1,N+1):
    sum2=sum2+i
print("sum2 is:",sum2)
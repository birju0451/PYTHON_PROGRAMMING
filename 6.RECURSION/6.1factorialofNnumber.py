def factorial(n):
    #base case
    if(n==0):
        return 1
    ans=n*factorial(n-1)
    return ans
n=int(input("enter a number:"))
print(factorial(n))
    
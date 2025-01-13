def print_nto1(n):
    #base case
    if(n==0):
        return
     
    print(n)
    #recursive case
    print_nto1(n-1)
n=int(input("enter a number:"))
print_nto1(n)

def print_nto1(n):
    #base case
    if(n==0):
        return
    #recursive case
    print_nto1(n-1)
    print(n)
n=int(input("enter a number:"))
print_nto1(n)

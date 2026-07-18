def fact(num):
    if num==1 or num==0:
        return 1
    ans = num*fact(num-1)
    return ans
    
if __name__ == "__main__":
    pass 

num = int(input())
ans = fact(num)
print(ans)
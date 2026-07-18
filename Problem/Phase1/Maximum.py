a, b, c = map(int,input().split())

if a>b:
    if a>c:
        print("a is greater and value is :",a)
    else:
        print("c is greater and value is :",c)
else:
    if b>c:
        print("b is greater and value is :",b)
    else:
        print("c is greater and value is :",c)
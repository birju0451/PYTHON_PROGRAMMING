#match case:
n1=int(input('enter n1:'))
n2=int(input('enter n2:'))
operator=input('enter operator:')
match operator:
    case"+":
        print('the sum is:',n1+n2)
    case"-":
        print('the sub is:',n1-n2)

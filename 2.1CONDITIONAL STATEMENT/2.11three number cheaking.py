#take three number and cheak which is greater 
n1=int(input('enter n1:'))
n2=int(input('enter n2:'))
n3=int(input('enter n3:'))
if n1>n2 and n1>n3:
    print('n1 is greater')
elif n2>n1 and n2>n3:
    print("n2 is greater")
else:
    print('n3 is greater ')

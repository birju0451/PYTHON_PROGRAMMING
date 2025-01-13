#code:-
eng_marks=int(input('enter english marks:'))
math_marks=int(input('enter math marks:'))
if eng_marks>80 and math_marks>80:
    print("grade A")
elif eng_marks>80 or math_marks>80:
    print('grade B')
else:
    print('grade c')



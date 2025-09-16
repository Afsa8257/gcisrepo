'''
Qn)read the score of the students, 
score>90 A grade, 
score>75 B grade, 
score>65 C grade, 
score>55 D grade, 
else fail
'''

s = int(input("Enter the score: "))

if s > 90:
    print("Grade: A") 
elif s > 75:
    print("Grade: B") 
elif s > 65:
    print("Grade: C") 
elif s > 55:
    print("Grade: D") 
else:
    print("Grade: Fail")
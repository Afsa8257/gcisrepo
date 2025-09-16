'''
Ask the user to input lengths of 3 sides.
Compare the sides and find if the triangle is equilateral, isosceles or scalene.
'''

def triangles():
    s1 = int(input("Enter the length of the first side: "))
    s2 = int(input("Enter the length of the second side: "))
    s3 = int(input("Enter the length of the third side: "))

    if s1 == s2 and s2 == s3:
        print("Equilateral triangle")
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
triangles()
def is_equilateral(a,b,c):
    if a == b and b == c:
        return True
    else:
        return False

s1 = int(input("Enter the length of 1st side: "))
s2 = int(input("Enter the length of 2nd side: "))
s3 = int(input("Enter the length of 3rd side: "))
if is_equilateral(s1,s2,s3)==True:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")

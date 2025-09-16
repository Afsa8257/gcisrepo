'''
Qn) Take 3 int inputs from the user.
 Compare the 3 numbers and the output should show which one is the greatest number.
'''
def numbers():
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = int(input("Enter C: "))

    if a > b and a > c:
        print("A is the greatest number.")
    elif b > a and b > c:
        print("B is the greatest number.")
    elif c > a and c > b:
        print("C is the greatest number.")
    else:
        print("All numbers are equal to each other.")
numbers()
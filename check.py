def even_or_odd(number):
    if number%2==0:
        print("This is an even number.")
    else:
        print("This is an odd number.")
    
def square_cube(integer):
    print("Square of the number=",integer**2)
    print("Cube of the number=",integer**3)

def main():
    input_user=int(input("Enter a number: "))
    even_or_odd(input_user)
    square_cube(input_user)
main()
def even_or_odd(number):
    '''
    This function checks if the number is even or odd.
    If the remainder is zero when the given number is divided by 2, the given number is even. 
    Otherwise it's odd.
    '''
    if number%2==0: #Uses mod function
        print("This is an even number.")
    else:
        print("This is an odd number.")
    
def square_cube(integer):
    '''
    This function displays the square and cube of the given number.
    '''
    print("Square of the number=",integer**2) # Gives the square of the number
    print("Cube of the number=",integer**3) # Gives the cube of the number

def main():
    '''
    Takes an input from the user.
    Checks if the input is even or odd and displays if the input is even or odd.
    Displays the square and cube of the input.
    '''
    input_user=int(input("Enter a number: ")) # Takes an input using input and int functions.
    even_or_odd(input_user) # Calls the even_or_odd function and inputs the user's input.
    square_cube(input_user) # Calls the square_cube function and inputs the user's input.
main() # Calls main function
#Ahmad Yasin 748007669
#Nahomi Tesfaye Duki 433000292
#Afsa Farheen Shaik 432000627


def check_limit(borrowed):
    """
    Determine borrowing status based on the number of books borrowed.
 
                                                                                                       
        borrowed (int): Number of books a student borrowed.

    
        str: A message indicating if the student is within or over the borrowing limit.
    """
    if borrowed < 0:
        return "Error: Invalid number of books"
    elif borrowed <= 3:                                                                                                      
        return "Within limit"
    elif borrowed <= 6:
        return "Over limit: Fine $5"
    else:
        return "Over limit: Fine $10"


    # Get input from the user and validate it
    try:
        borrowed_books = int(input("Enter the number of books borrowed: "))
        result = check_limit(borrowed_books)
        print(result)
    except ValueError:
        # Handles cases where the user doesn't enter a valid number
        print("Error: Please enter a valid integer.")


def process_borrowers(filename):
    """
    Read borrower records from a file and display their borrowing status.

    
        filename: Name of the file containing borrower data from the csv file.
                        
    """
    
    with open(filename, "r") as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split(",")
            if len(parts) >= 2:
                name = parts[0].strip()
                try:
                    books_borrowed = int(parts[1].strip())
                    status = check_limit(books_borrowed)  
                    print(name, ":", status)
                except ValueError:
                    print("Error: Non-numeric value for", name)
        
            else:
                print("Error: Incomplete record found")
    print("\n")
    


def calculate_average_books(filename):
    """
    Calculate and display the average number of books borrowed from a file.


        filename: Name of the file containing borrower data.
    """
    total_books = 0
    count = 0
   
    with open(filename, "r") as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split(",")
            if len(parts) >= 2:
                try:
                    books = int(parts[1].strip())
                    total_books += books
                    count += 1
                except ValueError:
                    # Ignore invalid entries
                    continue
    if count > 0:
        average = total_books / count
        print("Average books borrowed:", average)
    else:
        print("No valid data to calculate average.")



def count_over_limit(filename):
    """
    Count and display how many students borrowed more than 3 books.

        filename: Name of the file containing borrower data.
    """
    count = 0

    with open(filename, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(",")
            if len(parts) >= 2:
                try:
                    book_count = int(parts[1])
                    # Increment if the student is over the limit
                    if book_count > 3:
                        count += 1
                except ValueError:
                    # Skip invalid entries 
                    continue

    print("Number of students over the limit:", count)


def main():
    """
    Main program loop:
     Prompts the user for a filename
     Processes borrower records
     Calculates average borrowed books
     Counts students who exceeded the borrowing limit
    """
    while True:
        try:
            filename = input("Enter a file name: ").strip()
            process_borrowers(filename)
            calculate_average_books(filename)
            count_over_limit(filename)
            break  # Exit the loop after successful processing
        except FileNotFoundError:
            print("File not found. Please enter a file name again.\n")


# Run the main program
main()


#manifesto:
"""

This program processes the data of students borrowing books.

Functions:
- check_limit(borrowed): Task done by Ahmad Yasin.

    Checks if the number of books borrowed is within or over the allowed limit.

- User Input Block: Task done by Ahmad Yasin.

    Asks the user for the number of books they borrowed and displays their status.

- process_borrowers(filename): Task done by Nahomi Tesfaye Duki.

    Reads borrower data from a file and prints each students borrowing status.

- calculate_average_books(filename): Task done by Nahomi Tesfaye Duki.

    Calculates and prints the average number of books borrowed.

- count_over_limit(filename): Task done by Afsa Farheen Shaik.

    Counts how many students borrowed more than the allowed limit.

- main(): Task done by Afsa Farheen Shaik.

    Coordinates the program, handles file input and runs all other functions.
"""


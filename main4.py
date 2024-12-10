import math

def calculate_square_root():
    try:
        # Ask the user for input
        number = float(input("Enter a number to calculate its square root: "))
        
        if number < 0:
            print("Square root of a negative number is not defined in the real number system.")
            return
        
        # Calculate the square root
        square_root = math.sqrt(number)
        
        # Display the result
        print(f"The square root of {number} is {square_root}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    calculate_square_root()

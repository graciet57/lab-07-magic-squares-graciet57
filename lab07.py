""""
Author:         Kaitlyn Theerathorn
Date:           3/4/2026
Assignment:     Magic Square Lab
Course:         CPSC1050
Lab Section:    003

"""


print("Welcome to the Magic Square!")


# Get user input and check if user input for square size is greater than 0
def validate_magic_square(): 

    """
    Prompt user to enter the size of the magic square and check if it is greater than 0.
    
    Returns:
        int: The size of the magic square 
    """

    print('Enter in the magic square size you would like:')

    size = int(input())

    # Keeps prompting until the user enters a positive integer
    while size <= 0:
        
        print('Please enter in a number that is greater than 0')

        print('Enter in the magic square size you would like:')

        size = int(input())

    return size


# Calculate the magic number from user input size 
def validate_magic_number(size):

    """
    Calculate the magic number for a square of the user input size.
    The magic number = sum that each row, column, and diagonal must equal.

    Args:
        size (int): The size of the magic square 

    Returns:
        int: The magic number
    """

    magic_number = (size * (size ** 2 + 1)) // 2

    print(f'The magic number for size {size} is {magic_number}.')

    return magic_number 


# Reads the user input square values and converts them into a 2D list 
def square_spaces(size):

    """
    Read user input of the square values as a single line of space seperated integers,
    then converts them into a 2d list which represents the square.

    Args:
        size (int): The size of the magic square (n)

    Returns:
        list[list[int]]: 2d list representing the magic square
    """

    print('Enter in the values separated by spaces: ')

    values = list(map(int, input().split()))

    square = []

    # Converts 1d list into a 2d list and builds a row of the square for each iteration 
    for i in range(size):

        row = values[i * size:(i +1)* size]

        square.append(row)

    # Print the Magic Square to read 
    print('Your square:')

    for row in square:

        print(*row)
    
    return square


# Checks if the sqaure is valid and tests rows, columns, and diagonals
def validate_square(square, size, magic_number): 

    """
    Check if the square is valid:
    1. Contains all numbers from 1 to n^2
    2. Rows sum to the magic number
    3. Columns sum to the magic number
    4. Diagonals sum to the magic number

    Args:
        square (list[list[int]]): The 2d list representing the square
        size (int): The size of the square
        magic_number (int): The expected sum for rows, columns, diagonals

    Returns:
        bool: True if the square is a magic square, False otherwise
    """

    expected_list = list(range(1, size **2 +1))

    # Creates a temporary list to store all numbers from the square 
    temp_list = []

    # Converts square back to 1d for validation 
    for row in square: 

        for num in row: 

            temp_list.append(num)

    temp_list.sort()

    # Checks that all numbers from 1 to n^2 are present 
    if temp_list != expected_list: 

        print(f'The input cannot be a magic square! There must be one of each value from 1 to {size**2}.')

        return None 

    check_magic_square = True 

    # Checks rows 
    for row in range(size):

        if sum(square[row]) != magic_number: 

            print(f'Row {row} does not work! These are the values in row {row}: ', end = '')

            print( * square [row])

            check_magic_square = False 

    # Checks columns 
    for column in range(size):

        column_val = []

        for r in range(size):

            column_val.append(square[r][column])

        if sum(column_val) != magic_number:

            print(f'Column {column} does not work! These are the values in column {column}: ', end = '')

            print( * column_val)

            check_magic_square = False 

    # Checks first diagonal for top left to bottom right 
    diag1 = []

    for i in range(size):

        diag1.append(square[i][i])


    if sum(diag1) != magic_number:

        print('Diagonal 1 does not work!')

        print('These are the values in diagonal 1:', * diag1)

        check_magic_square = False

    # Checks second diagnoal from bottom left to top right 
    diag2 = []

    for i in range(size):

        diag2.append(square[i][size-1-i])

    if sum(diag2) != magic_number:

        print('Diagonal 2 does not work!')

        print('These are the values in diagonal 2:', * diag2)

        check_magic_square = False

    return check_magic_square

# Creates the main program 
size = validate_magic_square()

magic_number = validate_magic_number(size)

square = square_spaces(size)

result = validate_square(square, size, magic_number)

# Validate the square and print result 
if result == True:  

    print('This is a magic square!')

elif result == False: 

    print('This is not a magic square!')

else: 

    print('This is not a magic square!')


	


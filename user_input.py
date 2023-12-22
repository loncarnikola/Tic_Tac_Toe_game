def row_input():
    passed = [1, 2, 3]
    user_input_row = int(input("Please enter a number, in which row you would like to place 'X': "))

    if user_input_row not in passed:
        second_input = int(input('Please choose 1, 2 or 3 for row number: '))

        while second_input not in passed:
            second_input = int(input('Please choose 1, 2 or 3 for row number: '))

        return second_input

    return user_input_row

def column_input():
    passed = [1, 2, 3]
    user_input_column = int(input("Please enter a number, in which column you would like to place 'X': "))

    if user_input_column not in [1,2,3]:
        second_input = int(input('Please choose 1, 2 or 3 for column number: '))
        while second_input not in passed:
            second_input = int(input('Please choose 1, 2 or 3 for column number: '))
        return second_input
    return user_input_column
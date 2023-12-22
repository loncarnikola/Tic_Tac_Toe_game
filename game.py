import random
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

def display():
    print(row1)
    print(row2)
    print(row3)

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
def display_user_input():

    row_input_number = row_input()
    column_input_number = column_input() - 1

    if row_input_number == 1:
        if row1[column_input_number] == 'X' or row1[column_input_number] == 'O':
            print('Unable to put X here, since this field is already full')
            display_user_input()
        else:
            row1[column_input_number] = 'X'
            print('Human move: ')
            display()
    elif row_input_number == 2:
        if row2[column_input_number] == 'X' or row2[column_input_number] == 'O':
            print('Unable to put X here, since this field is already full')
            display_user_input()
        else:
            row2[column_input_number] = 'X'
            print('Human move: ')
            display()
    elif row_input_number == 3:
        if row3[column_input_number] == 'X' or row3[column_input_number] == 'O':
            print('Unable to put X here, since this field is already full')
            display_user_input()
        else:
            row3[column_input_number] = 'X'
            print('Human move: ')
            display()
    else:
        print("Unable to write X there")
        display_user_input()


def computers_turn():

    def random_row():
        random_row_number = random.randint(1, 3)
        return random_row_number

    def random_column():
        random_column_number = random.randint(1, 3)
        return random_column_number

    row_input_number = random_row()
    column_input_number = random_column() - 1

    if row_input_number == 1:
        if row1[column_input_number] == 'X' or row1[column_input_number] == 'O':
            print(f'Unable to put symbol there, since this field is already full')
            computers_turn()
        else:
            row1[column_input_number] = 'O'
            print('Machine move: ')
            display()
    elif row_input_number == 2:
        if row2[column_input_number] == 'X' or row2[column_input_number] == 'O':
            print('Unable to put symbol there, since this field is already full')
            computers_turn()
        else:
            row2[column_input_number] = 'O'
            print('Machine move: ')
            display()
    elif row_input_number == 3:
        if row3[column_input_number] == 'X' or row3[column_input_number] == 'O':
            print('Unable to put symbol there, since this field is already full')
            computers_turn()
        else:
            row3[column_input_number] = 'O'
            print('Machine move: ')
            display()
    else:
        print("Unable to write X there")


def win_check():
    end = False
    while end == False:
        humans_won = False
        machines_won = False

        # Check rows
        for i in range(0, 2):
            if row1[i] == 'X' and row2[i] == 'X' and row3[i] == 'X':
                humans_won = True
            elif row1[i] == 'O' and row2[i] == 'O' and row3[i] == 'O':
                machines_won = True
            else:
                pass

        # Check colums
        if row1 == ['X', 'X', 'X'] or row2 == ['X', 'X', 'X'] or row3 == ['X', 'X', 'X']:
            humans_won = True
        elif row1 == ['O', 'O', 'O'] or row2 == ['O', 'O', 'O'] or row3 == ['O', 'O', 'O']:
            machines_won = True
        else:
            pass

        # Check diagonal
        if row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X':
            humans_won = True
        elif row1[2] == 'X' and row2[1] == 'X' and row3[0] == 'X':
            humans_won = True
        elif row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O':
            machines_won = True
        elif row1[2] == 'O' and row2[1] == 'O' and row3[0] == 'O':
            machines_won = True
        else:
            pass
            # Print who won
        if humans_won == True and machines_won == True:
            end = True
            print("IT'S A TIE!")
            return end
        elif humans_won == True and machines_won == False:
            print('HUMANS WON!')
            end = True
            return end
        elif humans_won == False and machines_won == True:
            print('THE MACHINES WON!')
            end = True
            return end
        else:
            return end




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
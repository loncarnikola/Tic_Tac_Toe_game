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
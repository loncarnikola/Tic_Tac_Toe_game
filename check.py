def win_check():
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
        print("IT'S A TIE!")
    elif humans_won == True and machines_won == False:
        print('HUMANS WON!')
    elif humans_won == False and machines_won == True:
        print('THE MACHINES WON!')
    else:
        pass


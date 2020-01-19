def initialize():
    board = [
        ['B', 'B', '', '', '', '', '', '', '', '', 'B', 'B'],
        ['B', 'B', '', '', '', '', '', '', '', '', 'B', 'B'],
        ['', '', 'ML-EU-WR', 'UL-CD-NR', 'OA', 'PU', 'AU', 'UR-CU-NL', 'UD-CR-NU', 'SU-SD', '', ''],
        ['', '', 'FL', 'AU', 'BU', '#', 'OA', 'AD', 'KR', 'WD-ER-MU', '', ''],
        ['', '', 'GU', 'OA', 'UD-CR-NU', 'ND-UU-CL', '#A', 'ML-EU-WR', '#A', 'GR', '', ''],
        ['', '', 'YL', 'AL', 'UD-CR-NU', 'SU-SD', 'HU-HD-IL-IR', '#', 'UR-CU-NL', 'UR-CU-NL', '', ''],
        ['', '', 'PL', '#A', 'RL', 'BR', 'SL-SR', 'UR-CU-NL', 'DL', 'RR', '', ''],
        ['', '', '#A', 'FD', 'HU-HD-IL-IR', 'OA', 'ND-UU-CL', 'AR', 'BR', 'OA', '', ''],
        ['', '', 'GU', 'WD-ER-MU', 'TD', 'OA', 'UL-CU-WR', '#A', 'MD-ER-WU', '#A', '', ''],
        ['', '', 'SU-SD', 'OA', '#A', 'ND-UU-CL', 'YD', 'MD-ER-WU', 'AD', 'ND-UU-CL', '', ''],
        ['B', 'B', '', '', '', '', '', '', '', '', 'B', 'B'],
        ['B', 'B', '', '', '', '', '', '', '', '', 'B', 'B'],
    ]
    return board

def is_possible(direction, letter):
    options = letter.split('-')
    for option in options:
        if option[1] == direction:
            return (option[0], True)
    return ('', False)

def update_moves(moves, letter, i, direction):
    move_string = str(i) + '-' + direction
    if letter in moves.keys():
        moves[letter].append(move_string)
    else:
        moves[letter] = [move_string]
    return moves

def parse_possible_moves(board):
    moves = {}

    #Checking all the ups
    for i in range(2, len(board)):
        clue_found = False
        for j in range(2, len(board) - 2):
            # board[j][i] as j goes up goes down a row
            current = board[j][i]
            print current, j, i
            if board[1][i] == '' and not clue_found and current != '':
                letter, valid = is_possible('U', current)
                if valid:
                    moves = update_moves(moves, letter, i, 'U')
                    '''if letter in moves.keys():
                        moves[letter].append(str(i) + '-U')
                    else:
                        moves[letter] = [str(i) + '-U']'''
                clue_found = True

    #Checking all the downs
    for i in reversed(range(len(board) - 2)):
        clue_found = False
        for j in reversed(range(2, len(board) - 2)):
            current = board[j][i]
            if board[10][i] == '' and not clue_found and current != '':
                print current
                letter, valid = is_possible('D', current)
                if valid:
                    moves = update_moves(moves, letter, i, 'D')
                clue_found = True

    #Checking all the lefts
    for i in range(2, len(board)):
        clue_found = False
        for j in range(2, len(board) - 2):
            # board[i][j] as j goes up goes down a row
            current = board[i][j]
            print current, j, i
            if board[1][j] == '' and not clue_found and current != '':
                letter, valid = is_possible('L', current)
                if valid:
                    moves = update_moves(moves, letter, i, 'L')
                clue_found = True

    #Checking all the lefts
    for i in reversed(range(len(board) - 2)):
        clue_found = False
        for j in reversed(range(2, len(board) - 2)):
            current = board[i][j]
            if board[10][j] == '' and not clue_found and current != '':
                print current
                letter, valid = is_possible('R', current)
                if valid:
                    moves = update_moves(moves, letter, i, 'R')
                clue_found = True

    return moves



if __name__ == '__main__':
    board = initialize()
    print parse_possible_moves(board)


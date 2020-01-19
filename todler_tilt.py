def initialize():
    board = [
        ['B', 'B', '', '', '', '', '', '', '', '', 'B', 'B'],
        ['B', 'B', '', '', '', '', '', '', '', '', 'B', 'B'],
        ['', '', 'ML-EU-WR', 'UL-CD-NR', 'OA', 'PU', 'AU', 'UR-CU-NL', 'UD-CR-NU', 'SU-SD', '', ''],
        ['', '', 'FL', 'AU', 'BU', '#', 'OA', 'AD', 'KR', 'WD-ER-MU', '', ''],
        ['', '', 'GU', 'OA', 'UD-CR-NU', 'ND-UU-CL', '#', 'ML-EU-WR', '#', 'GR', '', ''],
        ['', '', 'YL', 'AL', 'UD-CR-NU', 'SU-SD', 'HU-HD-IL-IR', '#', 'UR-CU-NL', 'UR-CU-NL', '', ''],
        ['', '', 'PL', '#', 'RL', 'BR', 'SL-SR', 'UR-CU-NL', 'DL', 'RR', '', ''],
        ['', '', '#', 'FD', 'HU-HD-IL-IR', 'OA', 'ND-UU-CL', 'AR', 'BR', 'OA', '', ''],
        ['', '', 'GU', 'WD-ER-MU', 'TD', 'OA', 'UL-CU-WR', '#', 'MD-ER-WU', '#', '', ''],
        ['', '', 'SU-SD', 'OA', '#', 'ND-UU-CL', 'YD', 'MD-ER-WU', 'AD', 'ND-UU-CL', '', ''],
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

def parse_possible_moves(board):
    moves = {}

    #Checking all the ups
    for i in range(2, len(board)):
        clue_found = False
        for j in range(2, len(board) - 2):
            # board[j][i] as j goes up goes down a row
            current = board[j][i]
            print current
            if board[1][i] == '' and not clue_found and current != '':
                letter, valid = is_possible('U', current)
                if valid:
                    if letter in moves.keys():
                        moves[letter].append(str(i) + '-U')
                    else:
                        moves[letter] = [str(i) + '-U']
                clue_found = True
    return moves



if __name__ == '__main__':
    board = initialize()
    print parse_possible_moves(board)


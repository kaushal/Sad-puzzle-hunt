import sys
import copy

def initialize():
    board = [
        ['B', 'B', '', '', '', '', '', '', '', '', 'B', 'B'],
        ['B', 'B', '', '', '', '', '', '', '', '', 'B', 'B'],
        ['', '', 'ML-EU-WR', 'UL-CD-NR', 'OA', 'PU', 'AU', 'UR-CU-NL', 'UD-CR-NU', 'SU-SD', '', ''],
        ['', '', 'FL', 'AU', 'BU', '#A', 'OA', 'AD', 'KR', 'WD-ER-MU', '', ''],
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

def parse_possible_moves(board, target):
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
                if valid and letter == target:
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
                if valid and letter == target:
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
                if valid and letter == target:
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
                if valid and letter == target:
                    moves = update_moves(moves, letter, i, 'R')
                clue_found = True

    return moves



# schmoovin' to another board state
# eg:
#   parse_possible_moves = {'A': ['6-U'], 'C': ['7-U'], 'E': ['2-U'], 'N': ['8-U'], 'P': ['5-U'], 'S': ['9-U']}
#   move = ['6-U']
def make_move(board, move):
    position, direction = move.split('-')
    position = int(position)
    traunch = 0
    first_non_empty_pos = -1

    if direction == 'U':
        traunch = 0 if board[0][position] == '' else 1
        for i in range(2, len(board) - 2):
            current = board[i][position]
            if board[i][position] != '':
                first_non_empty_pos = i
                board[traunch][position] = current
                board[i][position] = ''
                break
        up_counter = 2
        for i in range(first_non_empty_pos + 1, len(board) - 2):
            board[up_counter][position] = board[i][position]
            board[i][position] = ''
            up_counter += 1

    elif direction == 'D':
        traunch = 11 if board[10][position] == '' else 10
        for i in reversed(range(2, len(board) - 2)):
            current = board[i][position]
            if board[i][position] != '':
                first_non_empty_pos = i
                board[traunch][position] = current
                board[i][position] = ''
                break
        down_counter = 9
        for i in reversed(range(2, first_non_empty_pos)):
            board[down_counter][position] = board[i][position]
            board[i][position] = ''
            down_counter -= 1

    elif direction == 'L':
        traunch = 0 if board[position][0] == '' else 1
        for i in range(2, len(board) - 2):
            current = board[position][i]
            if board[position][i] != '':
                first_non_empty_pos = i
                board[position][traunch] = current
                board[position][i] = ''
                break
        up_counter = 2
        for i in range(first_non_empty_pos + 1, len(board) - 2):
            board[position][up_counter] = board[position][i]
            board[position][i] = ''
            up_counter += 1

    elif direction == 'R':
        traunch = 11 if board[position][10] == '' else 10
        for i in reversed(range(2, len(board) - 2)):
            current = board[position][i]
            if board[position][i] != '':
                first_non_empty_pos = i
                board[position][traunch] = current
                board[position][traunch] = ''
                break
        down_counter = 9
        for i in reversed(range(2, first_non_empty_pos)):
            board[down_counter][position] = board[position][i]
            board[position][i] = ''
            down_counter -= 1
    return board


# That's it. LET'S GET TILTIN'!!
def get_tiltin(input_moves, board):
    # all boards are valid when there are no moves to make. pretty sure.
    if len(input_moves) == 0:
        return board

    # a tiltin' time is only successful if we can make every input move
    # and eventually reach a solution.
    for i in input_moves:
        remaining_moves = input_moves[1:]

        # try every candidate move for this input character
        for m in parse_possible_moves(board, i):
            # make schmooves and see if it leads to a solution. if not, try the next candidate.
            candidate_board = copy.deepcopy(board)
            make_move(candidate_board, m)
            solution = get_tiltin(remaining_moves, candidate_board)
            if solution:
                # dope
                return solution

        # the provided input moves and board state do not lead to a valid solution
        return None

def print_board(board):
    mx = len(max((sub[0] for sub in board),key=len))

    for row in board:
        s = ""
        for column in row:
            if column == "B":
                print '[{0: >15}] '.format("---------------"),
            else:
                print '[{0: >15}] '.format(column),
        print ""
        print ""

# hard code the puzzle input and tilt up a solution. our algoirthm might be bad.
def main():
    input_moves = [ '#', 'A', 'T', 'O', 'A', 'U', 'Y', 'M', '#', 'S', 'O', 'P', 'G', 'R', 'U', 'O', 'N', 'M', 'N', 'B', 'C', 'K', 'W', 'G', 'F', 'E', 'N', 'S', 'B', 'C', 'P', 'R', 'A', 'F', 'U', 'C', 'O', '#', 'I', '#', 'O', '#', 'A', 'S', 'N', 'G', 'E', 'N', '#', 'N', 'B', 'S', 'N', 'O', 'M', 'O', '#', 'Y', 'I', '#', 'A', 'A', 'D', '#' ]

    board = initialize()
    print parse_possible_moves(board, 'A')
    print_board(make_move(board, '6-U'))
    '''solution = get_tiltin(input_moves, board)
    if not solution:
        print "Faild to get tiltin', our algorithm is bad"
        sys.exit(1)

    print "Here is the solution, if it means anything to you: "
    print_print(solution)
    sys.exit(0)
'''

if __name__ == '__main__':
    sys.exit(main())

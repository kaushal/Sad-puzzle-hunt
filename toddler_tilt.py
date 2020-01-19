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



# schmoovin' to another board state
# eg:
#   parse_possible_moves = {'A': ['6-U'], 'C': ['7-U'], 'E': ['2-U'], 'N': ['8-U'], 'P': ['5-U'], 'S': ['9-U']}
#   move = ['6-U']
def make_move(board, move):
    tokens = move.split('-')
    n = int(tokens[0])
    direction = tokens[1]

    candidate_board = copy.deepcopy(board)
    if direction == 'U' or direction == 'D':

    elif direction == 'L' or direction == 'R':

    else:
        sys.exit(42)

    return candidate_board


# That's it. LET'S GET TILTIN'!!
def get_tiltin(input_moves, board):
    for i in input_moves:
        # get moves are possible for the current board state
        moves_by_character = parse_possible_moves(board)
        if not moves_by_character[i]:
            # board has no moves for the next in a bad state, so consider this tiltin' bit a failure
            return None

        # get candidate moves that specifically allow tiltin' input character `i',
        # then calculate the ramining input moves by chopping off the first entry.
        candidate_moves = moves_by_character[i]
        remaining_input_moves = input_moves[1:]

        for m in candidate_moves:
            # make schmooves and see if it leads to a solution. if not, try the next candidate.
            candidate_board = make_move(board, m)
            solution = get_tiltin(remaining_input_moves, candidate_board)
            if solution:
                # dope
                return solution

        # the provided input moves and board state do not lead to a valid solution
        return None


# hard code the puzzle input and tilt up a solution. our algoirthm might be bad.
def main():
    input_moves = [ '#', 'A', 'T', 'O', 'A', 'U', 'Y', 'M', '#', 'S', 'O', 'P', 'G', 'R', 'U', 'O', 'N', 'M', 'N', 'B', 'C', 'K', 'W', 'G', 'F', 'E', 'N', 'S', 'B', 'C', 'P', 'R', 'A', 'F', 'U', 'C', 'O', '#', 'I', '#', 'O', '#', 'A', 'S', 'N', 'G', 'E', 'N', '#', 'N', 'B', 'S', 'N', 'O', 'M', 'O', '#', 'Y', 'I', '#', 'A', 'A', 'D', '#' ]

    board = initialize()
    solution = get_tiltin(input_moves, board)
    if not solution:
        print "Faild to get tiltin', our algorithm is bad"
        sys.exit(1)

    print "Here is the solution, if it means anything to you: ", solution
    sys.exit(0)


if __name__ == '__main__':
    sys.exit(main()has no moves for the next

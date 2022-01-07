# AoC Day 4 2021 part 1

with open('AoC21/data/AoC_4_2021.in') as file:
    # take the input and split it by line break to separate numbers and boards
    numbers, *boards = file.read().split('\n\n')
    # create a list of int in which each element represents one number
    numbers = [int(i) for i in numbers.split(',')]
    # create a list of lists in which each sub-list is one board
    all_boards = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in boards]


# place an 'x' if number called is in board:

def mark_board(number, board):
    for row in board:
        for col in range(0, len(row)):
            if row[col] == number:
                row[col] = 'x'

# sum of all numbers in board which are not 'x'


def sum_board(board):
    sum = 0
    for row in board:
        for num in row:
            if num != 'x':
                sum += num
    return sum

# Check for Bingo winner

def check_winner(board):
    winner = False

    # Check rows for a winnner
    for row in board:
        # returns true as soon as all elements in are 'x'
        winner = all(elem in ['x'] for elem in row)

        if winner: # evalualtes to true as soon as winner = True
            return winner # will terminate the function as soon as True

    # Check for column:
    for col in range(0, 5):

        winner = all(elem in ['x'] for elem in [row[col] for row in board])

        if winner:
            return winner

    return winner

# Part 1 solution:

def part_1():

    boards = all_boards
    for number in numbers:
        for board in boards:
            mark_board(number, board)

            if check_winner(board):
                return sum_board(board) * number


print(f'Result part 1:{part_1()}')

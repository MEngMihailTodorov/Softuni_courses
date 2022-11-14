from collections import deque


def check_for_win():
    player_name, player_symbol = players[0]
    size_board = len(board)

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size_board)])
    second_diagonal_win = all([board[i][size_board - 1 - i] == player_symbol for i in range(size_board)])

    row_win = any([all(True if pos == player_symbol else False for pos in row) for row in board])
    col_win = any([all( True if board[r][c] == player_symbol else False for r in range(size_board)) for c in range(size_board)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{player_name} won!")

        raise SystemExit

    players.append(players.popleft())


def place_symbol(position):
    row, col = (position - 1) // 3, (position - 1) % 3

    board[row][col] = players[0][1]

    check_for_win()

    print_board()
    choose_position()


def choose_position():
    while True:
        position = int(input(f"{players[0][0]} choose a free position [1-9]: "))

        if 1 <= position <= len(board) ** 2:
            break
        else:
            print(f"Please select a valid position!")

    place_symbol(int(position))


def print_board(begin=False):
    if not begin:
        [print(f"| {' | '.join(row)} |" ) for row in board]

    else:
        print(f"This is the numeration of the board: ")
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{players[0][0]} starts first!")


def start():
    player_name_1 = input(f"Player one name:")
    player_name_2 = input(f"Player two name:")

    while True:
        player_one_symbol = input(f"{player_name_1} would you like to play with 'X' or 'O'?").upper()

        if player_one_symbol not in ['X', 'O']:
            print(f"Please, {player_name_1} choose a valid option!")
        else:
            break

    player_two_symbol = "0" if player_one_symbol == "X" else "X"

    players.append([player_name_1, player_one_symbol])
    players.append([player_name_2, player_two_symbol])

    print_board(begin=True)
    choose_position()


players = deque()
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]
print(board)

start()
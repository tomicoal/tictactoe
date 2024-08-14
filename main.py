from random import choice


# Create a dictionary
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board(board):
    print(board['top-L'] + ' | ' + board['top-M']+' | ' + board['top-R'])
    print('---------')
    print(board['mid-L'] + ' | ' + board['mid-M']+' | ' + board['mid-R'])
    print('---------')
    print(board['low-L'] + ' | ' + board['low-M']+' | ' + board['low-R'])


def check_win(board):
    # horizontal check
    if board["top-L"] != " " and board["top-L"] == board["top-M"] == board["top-R"]:
        return True
    elif board["mid-L"] != " " and board["mid-L"] == board["mid-M"] == board["mid-R"]:
        return True
    elif board["low-L"] != " " and board["low-L"] == board["low-M"] == board["low-R"]:
        return True
    # vertical check
    elif board["top-L"] != " " and board["top-L"] == board["mid-L"] == board["low-L"]:
        return True
    elif board["top-M"] != " " and board["top-M"] == board["mid-M"] == board["mid-M"]:
        return True
    elif board["top-R"] != " " and board["top-R"] == board["mid-R"] == board["low-R"]:
        return True
    # diagonal checks
    elif board["top-L"] != " " and board["top-L"] == board["mid-M"] == board["low-R"]:
        return True
    elif board["top-R"] != " " and board["top-R"] == board["mid-M"] == board["low-L"]:
        return True
    else:
        return False

list_keys = []
for key in board.keys():
    list_keys.append(key)

print(f"Board positions are as follows: {", ".join(list_keys)}")

print_board(board)

players = ["X", "O"]

player = choice(players)

game_on = True

# only 8 turns before a draw
move_num = 0


while game_on:
    correct_position = False
    while not correct_position:
        print(f"Board positions are as follows: {", ".join(list_keys)}")
        position_chosen = input(f"Turn for player {player}. Choose position:")
        if position_chosen not in board.keys():
            print(f"Not in board. Choose again.")

        if position_chosen in board.keys():
            board[position_chosen] = player
            correct_position = True

    if check_win(board):
        print(f"{print_board(board)}\nPlayer {player} wins!")
        game_on = False

    print_board(board)

    if player == "X":
        player = "0"
    else:
        player = "X"

    move_num += 1
    if move_num == 9:
        print(f"Game draw")
        game_on = False

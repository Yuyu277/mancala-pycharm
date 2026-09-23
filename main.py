board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]

def print_board(board):
    print("   13    12    11    10    9    8")
    print("-"*35)
    rowB = "     ".join(str(x) for x in board[1:7])
    print("B: " + rowB)
    print(str(board[0]) + "                                  " + str(board[7]))
    rowA = "     ".join(str(x) for x in board[8:14])
    print("A: " + rowA)
    print("-"*35)
    print("   1     2     3     4     5     6")

playerATurn = True
def is_valid_move(move_num):
    if(move_num>=1 and move_num<=6 and playerATurn or move_num>=8 and moveNum<=13 and not playerATurn):
        if(board(move_num) > 0):
            return True
        else:
            return False
    else:
        return False

def move_stones(move_num):
    print("moved")


def take_turn():
    if playerATurn:
        print("Player A's turn: ")
        print("Possible moves: 1, 2, 3, 4, 5, 6")
    else:
        print("Player B's turn: ")
        print("Possible moves: 8, 9, 10, 11, 12, 13")
    users_move = int(input("Your move: "))
    while True:
        if is_valid_move(users_move):
            move_stones(users_move)
            break
        else:
            print("Invalid move! Try again.")
            users_move = int(input("Your move: "))

print_board(board)
take_turn()

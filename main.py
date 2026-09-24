board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]

def print_board(board):
    print("   13    12    11    10    9    8")
    print("-"*35)
    rowB = ("     ".join(str(x) for x in board[8:14]))[::-1]
    print("B: " + rowB)
    print(str(" " + str(board[0])) + "                                  " + str(board[7]))
    rowA = "     ".join(str(x) for x in board[1:7])
    print("A: " + rowA)
    print("-"*35)
    print("   1     2     3     4     5     6")

def is_valid_move(move_num):
    if 1 <= move_num <= 6 and playerATurn or 8 <= move_num <= 13 and not playerATurn:
        if board[move_num] > 0:
            return True
        else:
            return False
    else:
        return False

def move_stones(move_num):
    move_amt = board[move_num]
    board[move_num] = 0
    i = 0
    while move_amt > 0:
        board_on = (move_num + 1 + i) % 14
        if playerATurn and board_on == 0 or not playerATurn and board_on == 7:
            i += 1
            board_on = (move_num + 1 + i) % 14
        board[board_on] += 1
        i += 1
        move_amt -= 1
    #steal
    if board[(move_num + i) % 14] - 1 == 0 and not board[(14 - move_num - i) % 14] == 0 and not (14 - move_num - i) % 14 == 7 and not (14 - move_num - i) % 14 == 0:
        if playerATurn and (move_num + 1) % 14 < 7 or not playerATurn and (move_num + 1) % 14 > 7:
            print("Steal!!!")
            if playerATurn:
                board[7] += board[(move_num + i) % 14] + board[(14 - move_num - i) % 14]
            else:
                board[0] += board[(move_num + i) % 14] + board[(14 - move_num - i) % 14]
            board[(move_num + i) % 14] = 0
            board[(14 - move_num - i) % 14] = 0
    if playerATurn and (move_num + i) % 14 == 7 or not playerATurn and (move_num + i) % 14 == 0:
        print_board(board)
        take_turn()
    print_board(board)


def take_turn():
    if playerATurn:
        print("Player A's turn! ")
        print("Possible moves: 1, 2, 3, 4, 5, 6")
    else:
        print("Player B's turn! ")
        print("Possible moves: 8, 9, 10, 11, 12, 13")
    users_move = int(input("Your move: "))
    while True:
        if is_valid_move(users_move):
            move_stones(users_move)
            break
        else:
            print("Invalid move! Try again.")
            users_move = int(input("Your move: "))

#running
playerATurn = True
print_board(board)
while True:
    take_turn()
    playerATurn = not playerATurn

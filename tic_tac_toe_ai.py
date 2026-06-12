board = [" " for _ in range(9)]

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

for i in range(9):
    print_board()
    move = int(input("Enter position (0-8): "))
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Position already taken")

print_board()
print("Game Over")

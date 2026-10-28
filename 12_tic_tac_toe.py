# Program 12: Tic-Tac-Toe, human X versus computer O
board = [" "] * 9
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def won(mark):
    return any(all(board[i] == mark for i in line) for line in wins)
def show():
    for r in range(3):
        print(" | ".join(board[r*3:r*3+3]))
        if r < 2: print("--+---+--")
def computer_move():
    for mark in ("O", "X"):
        for i in range(9):
            if board[i] == " ":
                board[i] = mark
                result = won(mark)
                board[i] = " "
                if result:
                    board[i] = "O"
                    return
    for i in (4,0,2,6,8,1,3,5,7):
        if board[i] == " ":
            board[i] = "O"
            return
while True:
    show()
    try: move = int(input("Choose cell 1-9: ")) - 1
    except ValueError:
        print("Enter a number."); continue
    if not 0 <= move < 9 or board[move] != " ":
        print("Invalid/occupied cell."); continue
    board[move] = "X"
    if won("X"): show(); print("You win!"); break
    if " " not in board: show(); print("Draw!"); break
    computer_move()
    if won("O"): show(); print("Computer wins!"); break
    if " " not in board: show(); print("Draw!"); break

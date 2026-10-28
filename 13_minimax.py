# Program 13: Minimax algorithm for Tic-Tac-Toe
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def winner(board, mark):
    return any(all(board[i] == mark for i in line) for line in wins)
def minimax(board, maximizing):
    if winner(board, "O"): return 1
    if winner(board, "X"): return -1
    if " " not in board: return 0
    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if maximizing else "X"
            scores.append(minimax(board, not maximizing))
            board[i] = " "
    return max(scores) if maximizing else min(scores)
board = [" "] * 9
while True:
    for r in range(3):
        print(" | ".join(board[r*3:r*3+3]))
        if r < 2: print("--+---+--")
    try: move = int(input("Your move (1-9): ")) - 1
    except ValueError:
        print("Enter a number."); continue
    if not 0 <= move < 9 or board[move] != " ":
        print("Invalid move."); continue
    board[move] = "X"
    if winner(board, "X"): print("You win!"); break
    if " " not in board: print("Draw!"); break
    best_score, best_move = -float("inf"), None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score: best_score, best_move = score, i
    board[best_move] = "O"
    if winner(board, "O"): print("Computer wins!"); break
    if " " not in board: print("Draw!"); break

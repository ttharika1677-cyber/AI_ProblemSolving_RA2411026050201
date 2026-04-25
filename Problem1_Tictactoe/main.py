import math

board = [' ' for _ in range(9)]

def print_board():
    print("\nBoard:")
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def is_full():
    return ' ' not in board

def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

def play_game():
    print("Positions: 0 to 8")
    while True:
        print_board()
        try:
            pos = int(input("Enter your move: "))
        except:
            print("Invalid input")
            continue

        if pos < 0 or pos > 8 or board[pos] != ' ':
            print("Invalid move!")
            continue

        board[pos] = 'X'

        if check_winner('X'):
            print_board()
            print("You win!")
            break

        if is_full():
            print_board()
            print("Draw!")
            break

        ai_move()

        if check_winner('O'):
            print_board()
            print("AI wins!")
            break

play_game()

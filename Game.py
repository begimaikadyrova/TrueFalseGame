T = "T"
F = "F"
EMPTY = " "
Draw = "Draw"
squares = 9
low = 0
high = 9

def instruct():
    print("You are playing true and false,follow bellow instructions:")


def yes_or_no(question):
    answ =99999
    while answ not in ("yes", "no"):
        answ = input(question).lower()
    return answ
    
def number(question):
    answ = 99999
    while answ not in range(low, high):
        answ = int(input(question))
    return answ
    
def who_is_the_best():
    go_first = yes_or_no("Do you wish to do the first move? (yes or no): ")
    if go_first == "yes":
        print("\nOkey,good luck")
        human = T
        computer = F
    else:
        print("\nOkey,do not worry,I will go first.")
        computer = T
        human = F
    return computer, human
    
def new_board():
    board = []
    for i in range(squares):
        board.append(EMPTY)
    return board
    
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def free_moves(board):
    moves = []
    for i in range(squares):
        if board[i] == EMPTY:
            moves.append(i)
    return moves

def winner(board):
    combinations = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))
    for row in combinations:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return Draw
    return None
    
def human_move(board, human):
    free = free_moves(board)
    move = 99999
    print("Free squares: ", free)
    while move not in free:
        move = number("Where will you move? (0-8): ")

        if move not in free:
            print("\nThis square is already occupied. Choose another\n")
    return move
    
def computer_move(board, computer, human):
    board = board[:]
    good_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I will take square number ", end=" ")
    for move in free_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move

        board[move] = EMPTY
    for move in free_moves(board):
        board[move] == human
        if winner(board) == human:
            print(move)
            return move
        
        board[move] = EMPTY
    for move in good_moves:
        if move in free_moves(board):
            print(move)
            return move
def next_turn(turn):
    if turn == T:
        return F
    else:
        return T
        
def congrat_winner(the_winner, computer, human):
    if the_winner != Draw:
        print(the_winner, " won!\n")
    else:
        print("It's a draw!\n")

def main():
    instruct()
    computer, human = who_is_the_best()
    turn = T
    board = new_board()
    display_board(board)
    
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
    
main()
input("The end")


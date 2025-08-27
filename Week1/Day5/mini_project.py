
def initialize_board():
    board = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append("-")
        board.append(row)
    return board


def display_board(board_to_display):
    for row in board_to_display:
        print(" ".join(row))

def player_input(board, player):
    
    max_dimension = 3
    print(f"It's Player {player}'s turn")        
   
    while True:
        row_num= input("Enter row: ")
        column_num = input("Enter column: ")
        try:      
            row_num = int(row_num)
            column_num = int(column_num)

            if (0 < row_num <= max_dimension) and (0 < column_num <= max_dimension):
                if board[row_num-1][column_num-1] == "-":
                    board[row_num-1][column_num-1] = player
                    break
                else:
                    print("This position is occupied.Try again!")
                    display_board(board)
                
            else:
                print(f"Error: The row and column numbers must both be between 1 and {max_dimension}")
                
        except ValueError:
            print("Invalid input.Please enter numbers only")

def flatten_board(board):
    flat_list = []
    for row in board:         
        for element in row:    
            flat_list.append(element)
    return flat_list


def check_win(board,player) -> bool:
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    flat_board = flatten_board(board)
    for coord in win_coord:
        if flat_board[coord[0]] == flat_board[coord[1]] == flat_board[coord[2]] == player:
            return True
    return False   

def play():
    print("**********************")
    print("Welcome to TIC TAC TOE")
    print("**********************")
    board = initialize_board()
    current_player = "X"
    for _ in range(9):
        player_input(board, current_player)
        display_board(board)
        if check_win(board, current_player):
            print(f"Congrats!Player {current_player} won!")
            break
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

    if not check_win(board, current_player): 
        print("It's a tie!")

play()


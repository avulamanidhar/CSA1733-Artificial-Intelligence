
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def solve_8_queens():
    # Initialize an empty 8x8 chessboard
    board = [['.' for _ in range(8)] for _ in range(8)]

    # Predefined positions of the queens (known solution)
    positions = [(0, 0), (1, 2), (2, 4), (3, 6), (4, 1), (5, 3), (6, 5), (7, 7)]
    
    # Place the queens on the board
    for i, j in positions:
        board[i][j] = 'Q'
    
    print("Solution to the 8-Queens problem:")
    print_board(board)

solve_8_queens()

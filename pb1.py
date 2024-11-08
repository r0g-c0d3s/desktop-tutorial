def is_safe(board, row, col, N):
    for i in range(row):
        if (
            board[i][col] == 1 or
            (col - row + i >= 0 and board[i][col - row + i] == 1) or
            (col + row - i < N and board[i][col + row - i] == 1)
        ):
            return False
    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, N):
                return True
            board[row][col] = 0  # Backtrack

    return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens_util(board, 0, N):
        print("No solutions exist.")
        return

    for row in board:
        print(''.join(['Q' if col == 1 else '-' for col in row]))

N = int(input("Enter the number of queens (N): "))
solve_n_queens(N)

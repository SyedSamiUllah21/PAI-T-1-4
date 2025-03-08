def print_solution(board, N):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, left_row, upper_diag, lower_diag, N):
    return not (left_row[row] or upper_diag[row + col] or lower_diag[row - col + N - 1])

def solve_n_queens(board, col, left_row, upper_diag, lower_diag, N, solutions):
    if col >= N:
        solutions.append([row[:] for row in board])
        return
    
    for i in range(N):
        if is_safe(board, i, col, left_row, upper_diag, lower_diag, N):
            board[i][col] = 1
            left_row[i] = upper_diag[i + col] = lower_diag[i - col + N - 1] = True
            solve_n_queens(board, col + 1, left_row, upper_diag, lower_diag, N, solutions)
            board[i][col] = 0
            left_row[i] = upper_diag[i + col] = lower_diag[i - col + N - 1] = False

def n_queens(N):
    board = [[0] * N for _ in range(N)]
    left_row = [False] * N
    upper_diag = [False] * (2 * N - 1)
    lower_diag = [False] * (2 * N - 1)
    solutions = []
    solve_n_queens(board, 0, left_row, upper_diag, lower_diag, N, solutions)
    
    for solution in solutions:
        print_solution(solution, N)
    
    print(f"Total solutions: {len(solutions)}")

N = 8  
n_queens(N)
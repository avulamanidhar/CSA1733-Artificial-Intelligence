import heapq

def print_board(board):
    for row in board: print(' '.join(map(str, row)))
    print()



def manhattan(board, goal):
    return sum(abs(i // 3 - goal.index(board[i]) // 3) + abs(i % 3 - goal.index(board[i]) % 3) for i in range(9) if board[i])

def neighbors(board):
    b, i = board[:], board.index(0)
    shifts = (-1, 1, -3, 3)
    for s in shifts:
        j = i + s
        if 0 <= j < 9 and (i % 3 > 0 or s != -1) and (i % 3 < 2 or s != 1):
            b[i], b[j] = b[j], b[i]
            yield b[:]
            b[i], b[j] = b[j], b[i]

def solve(start, goal):
    start, goal = [num for row in start for num in row], [num for row in goal for num in row]
    pq, seen = [(manhattan(start, goal), 0, start, [])], set()
    while pq:
        _, cost, board, path = heapq.heappop(pq)
        if board == goal: return path + [board], cost
        seen.add(tuple(board))
        for n in neighbors(board):
            if tuple(n) not in seen:
                heapq.heappush(pq, (cost + manhattan(n, goal) + 1, cost + 1, n, path + [board]))
    return None, 0

start = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

solution, cost = solve(start, goal)
if solution:
    for step in solution: print_board([step[i:i+3] for i in range(0, 9, 3)])
    print(f"Total cost (number of moves): {cost}")
else:
    print("No solution found.")

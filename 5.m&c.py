def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left
    
    if (m_left < c_left and m_left != 0) or (m_right < c_right and m_right != 0):
        return False
    return True

def print_solution(path):
    if path:
        print("Solution:")
        for i, state in enumerate(path):
            print(f"Step {i+1}: {state}")
    else:
        print("No solution found.")

def solve_missionaries_and_cannibals(start, goal):
    visited = set()
    queue = [(start, [])]
    while queue:
        state, path = queue.pop(0)
        if state == goal:
            return path + [state]
        if state not in visited:
            visited.add(state)
            for next_state in get_possible_moves(state):
                if next_state not in visited:
                    queue.append((next_state, path + [state]))
    return None

def get_possible_moves(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left
    
    possible_moves = []
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for move in moves:
        m_move, c_move = move
        if boat == 1:
            if m_left >= m_move and c_left >= c_move:
                new_state = (m_left - m_move, c_left - c_move, 0)
                if is_valid(new_state):
                    possible_moves.append(new_state)
        else:  
            if m_right >= m_move and c_right >= c_move:
                new_state = (m_left + m_move, c_left + c_move, 1)
                if is_valid(new_state):
                    possible_moves.append(new_state)
    return possible_moves


start_state = (3, 3, 1)
goal_state = (0, 0, 0)
solution = solve_missionaries_and_cannibals(start_state, goal_state)
print_solution(solution)

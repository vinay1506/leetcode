from collections import deque

class State:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent

def is_valid_position(pos, maze):
    rows = len(maze)
    cols = len(maze[0])
    r, c = pos
    return 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0

def get_neighbors(pos, maze):
    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    neighbors = []
    for dr, dc in moves:
        r, c = pos[0] + dr, pos[1] + dc
        if is_valid_position((r, c), maze):
            neighbors.append((r, c))
    return neighbors

def bfs(maze, start, goal):
    queue = deque()
    visited = set()

    start_state = State(start)
    queue.append(start_state)
    visited.add(start)

    while queue:
        current = queue.popleft()
        if current.position == goal:
            return current

        for neighbor in get_neighbors(current.position, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(State(neighbor, current))

    return None

def get_path(goal_state):
    path = []
    while goal_state:
        path.append(goal_state.position)
        goal_state = goal_state.parent
    return path[::-1]

# Input
maze = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 1, 0]
]

start = (0, 0)
goal = (2, 2)

if not is_valid_position(start, maze) or not is_valid_position(goal, maze):
    print("Start or goal is a wall.")
else:
    result = bfs(maze, start, goal)
    if result:
        print("Path found:", get_path(result))
    else:
        print("No path found.")

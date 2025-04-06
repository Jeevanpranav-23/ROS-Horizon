def create_arena_matrix(obstacles, size=11):
    """
 
    
    Args:
        obstacles (list): List of obstacle positions [N, E, S, W]
        size (int): Size of the arena matrix (default 11x11)
        
    Returns:
        list: 2D matrix with 0s for obstacles and 1s for safe positions
    """
   
    arena = [[1 for _ in range(size)] for _ in range(size)]
    
    # Mark obstacles (0,0 is bottom-left corner)
    for obstacle in obstacles:
        N, E, S, W = obstacle
        
        # Calculate obstacle position relative to start coordinate at (0,0)
        # North increase row index, East increases column index
        # South decreases row index, West decreases column index
        row = N - S
        col = E - W
        
        # Ensure position is within bounds
        if 0 <= row < size and 0 <= col < size:
            arena[row][col] = 0
    
    return arena

def find_shortest_path(arena, start=(0, 0), end=(10, 10)):
    """
    Finds the shortest path from start to end avoiding obstacles using BFS.
    
    Args:
        arena (list): 2D matrix representing the arena
        start (tuple): Starting position (row, col)
        end (tuple): Destination position (row, col)
        
    Returns:
        list: List of positions representing the shortest path
    """
    from collections import deque
    
    rows = len(arena)
    cols = len(arena[0]) if rows > 0 else 0
    
    # Directions: N, S, E, W (no diagonals)
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    queue = deque()
    queue.append(start)
    
    visited = {start: None}  # To reconstruct path
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]  # Reverse to get start->end
        
        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if arena[nr][nc] == 1 and (nr, nc) not in visited:
                    visited[(nr, nc)] = current
                    queue.append((nr, nc))
    
    return []  # No path found

if __name__ == "__main__":
    # Sample obstacles from the problem
    obstacles = [
        [2, 3, 0, 3],
        [5, 1, 0, 2],
        [3, 0, 4, 4],
        [3, 4, 0, 2]
    ]
    

    arena = create_arena_matrix(obstacles)
    print("Arena Matrix (0=obstacle, 1=safe):")
    for row in arena:
        print(row)
    

    path = find_shortest_path(arena)
    if path:
        print("\nShortest Path:")
        for position in path:
            print(position)
    else:
        print("\nNo path found to destination!")

from collections import deque

def node0(arr):
    return arr.index(0)

def move_left(arr):
    pos0 = node0(arr)
    if pos0 % 3 > 0:
        new_arr = arr[:]
        new_arr[pos0], new_arr[pos0 - 1] = new_arr[pos0 - 1], new_arr[pos0]
        return new_arr
    return None

def move_right(arr):
    pos0 = node0(arr)
    if pos0 % 3 < 2:
        new_arr = arr[:]
        new_arr[pos0], new_arr[pos0 + 1] = new_arr[pos0 + 1], new_arr[pos0]
        return new_arr
    return None

def move_up(arr):
    pos0 = node0(arr)
    if pos0 >= 3:
        new_arr = arr[:]
        new_arr[pos0], new_arr[pos0 - 3] = new_arr[pos0 - 3], new_arr[pos0]
        return new_arr
    return None

def move_down(arr):
    pos0 = node0(arr)
    if pos0 < 6:
        new_arr = arr[:]
        new_arr[pos0], new_arr[pos0 + 3] = new_arr[pos0 + 3], new_arr[pos0]
        return new_arr
    return None

def print_board(arr):
    for i in range(0, 9, 3):
        print(arr[i], arr[i+1], arr[i+2])
    print("-----------------------")

def bfs(start, target):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state == target:
            return path
        visited.add(tuple(current_state))

        for move_func, move_name in [(move_up, 'Up'), (move_down, 'Down'), (move_left, 'Left'), (move_right, 'Right')]:
            new_state = move_func(current_state)
            if new_state and tuple(new_state) not in visited:
                queue.append((new_state, path + [move_name]))

    return None



ordenini = [7,1,1,1,1,0,1,1,1]
arrfi = [0,1,1,1,1,1,1,7,1]

#ordenini = [7,2,4,5,0,6,8,3,1]
#arrfi = [1,2,3,4,5,6,7,8,0]

shortest_path = bfs(ordenini, arrfi)
if shortest_path:
    current_state = ordenini.copy()
    print("Estado Inicial:")
    print_board(current_state)
    total_moves = len(shortest_path)
    for move_number, move in enumerate(shortest_path, start=1):
        if move == 'Up':
            current_state = move_up(current_state)
        elif move == 'Down':
            current_state = move_down(current_state)
        elif move == 'Left':
            current_state = move_left(current_state)
        elif move == 'Right':
            current_state = move_right(current_state)
        print(f"Move {move_number} ({move}):")
        print_board(current_state)
    print(f"Total de Movimientos: {total_moves}")
else:
    print("No solution found.")

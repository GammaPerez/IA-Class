import time
import psutil
from collections import deque

# ... Las funciones anteriores y tu código ...
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

# Función para medir el tiempo de ejecución
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución: {end_time - start_time} segundos")
        return result
    return wrapper

# Función para medir el uso de memoria
def measure_memory(func):
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        start_memory = process.memory_info().rss / (1024 * 1024)  # En megabytes
        result = func(*args, **kwargs)
        end_memory = process.memory_info().rss / (1024 * 1024)  # En megabytes
        print(f"Uso de memoria: {end_memory - start_memory} MB")
        return result
    return wrapper

# Decoradores para medir tiempo y memoria
@measure_time
@measure_memory
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

if __name__ == "__main__":
    ordenini = [7,1,1,1,1,0,1,1,1]
    arrfi = [0,1,1,1,1,1,1,7,1]

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

import random

def create_board(width, height):
    board = []
    for _ in range(height):
        row = [
            (random.choice(["P", "N", "K"]), random.randint(1, 5)) if random.random() < 0.2 else None
            for _ in range(width)
        ]
        board.append(row)
    return board


def print_board(board):
    symbols = {"P": "P", "N": "N", "K": "K", None: "."}
    for row in board:
        print(" ".join(f"{symbols[cell[0]]}{cell[1] if cell else ' '}" if cell else " . " for cell in row))

def get_neighbors(x, y, width, height):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height: #aby nie wyjść za tablice
            neighbors.append((nx, ny))
    return neighbors

def resolve_battle(attacker, defender):
    """Rozstrzyga pojedynek między dwoma polami."""
    rules = {"P": "K", "K": "N", "N": "P"}  # Co wygrywa z czym
    if attacker[0] is None or defender[0] is None:
        return attacker, defender
    if rules[attacker[0]] == defender[0]:
        # Defender wins
        return (attacker[0], max(1, attacker[1] - 1)), (defender[0], min(5, defender[1] + 1))
    elif rules[defender[0]] == attacker[0]:
        # Attacker wins
        return (attacker[0], min(5, attacker[1] + 1)), (defender[0], max(1, defender[1] - 1))
    else:
        # Draw
        return attacker, defender

def update_board(board):
    """Aktualizuje planszę na podstawie zasad automatu komórkowego."""
    width, height = len(board[0]), len(board)
    new_board = [[cell for cell in row] for row in board]  # Kopiujemy starą planszę

    for y in range(height):
        for x in range(width):
            if board[y][x] is None:
                continue

            cell_type, strength = board[y][x]
            neighbors = get_neighbors(x, y, width, height)
            nx, ny = random.choice(neighbors)
            neighbor = board[ny][nx]

            if neighbor is None:
                # Zasiedlenie pustego pola
                if strength > 1:
                    new_board[ny][nx] = (cell_type, strength - 1)
            elif neighbor[0] == cell_type:
                # Ten sam typ - nic się nie dzieje
                continue
            else:
                # Pojedynek
                new_cell, new_neighbor = resolve_battle((cell_type, strength), neighbor)
                new_board[y][x] = new_cell
                new_board[ny][nx] = new_neighbor if new_neighbor[1] > 0 else None

    return new_board

def main():
    width, height = 10, 10
    board = create_board(width, height)

    for step in range(10):
        print(f"Krok {step}:")
        print_board(board)
        board = update_board(board)
        print()

if __name__ == "__main__":
    main()

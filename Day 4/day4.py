def ingest_grid(file_path: str) -> list[list[str]]:
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]

def count_accessible_rolls(grid: list[list[str]]) -> int:
    accessible_rolls = 0
    roll_index = [] # Array of tuples (i, j) for each roll
    # A roll is accessible if there are fewer than four rolls in the eight adjacent positions.
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                # Check the eight adjacent positions
                adjacent_rolls = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0:
                            continue
                        # Handle out of bounds
                        if i + di < 0 or i + di >= len(grid) or j + dj < 0 or j + dj >= len(grid[i]):
                            continue
                        if grid[i + di][j + dj] == "@":
                            adjacent_rolls += 1
                if adjacent_rolls < 4:
                    accessible_rolls += 1
                    roll_index.append((i, j))
    return accessible_rolls, roll_index

def remove_rolls(grid: list[list[str]], roll_index: list[tuple[int, int]]) -> list[list[str]]:
    for i, j in roll_index:
        grid[i][j] = "."
    return grid

def main():
    grid = ingest_grid("Day 4/day4.txt")
    accessible_rolls, roll_index = count_accessible_rolls(grid)
    print(f"Part One: {accessible_rolls}")
    # Keep counting and removing rolls until no rolls are accessible
    total_rolls = accessible_rolls
    while accessible_rolls > 0:
        grid = remove_rolls(grid, roll_index)
        accessible_rolls, roll_index = count_accessible_rolls(grid)
        total_rolls += accessible_rolls
    print(f"Part Two: {total_rolls}")

if __name__ == "__main__":
    main()
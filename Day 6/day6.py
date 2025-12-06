import math


def rotate_grid(grid: list[list[str]]) -> list[list[str]]:
    # Rotate the grid 90 degrees counter-clockwise
    if not grid or not grid[0]:
        return []
    
    num_rows = len(grid)
    num_cols = max(len(row) for row in grid)  # Find max columns
    
    new_grid = []
    for col in range(num_cols):
        new_grid_line = []
        for row in range(num_rows - 1, -1, -1):  # Iterate rows in reverse
            if col < len(grid[row]):
                new_grid_line.append(grid[row][col])
            else:
                new_grid_line.append("")  # Handle missing cells
        new_grid.append(new_grid_line)
    return new_grid


def parse_problems_right_to_left(lines: list[str]) -> list[tuple[str, list[int]]]:
    # Preserve spacing to keep column alignment intact
    rows = [line.rstrip("\n") for line in lines]
    if not rows:
        return []

    max_len = max(len(row) for row in rows)
    rows = [row.ljust(max_len) for row in rows]

    operator_row_idx = len(rows) - 1
    col = max_len - 1
    problems: list[tuple[str, list[int]]] = []

    while col >= 0:
        # Skip separator columns made entirely of spaces
        if all(rows[r][col] == " " for r in range(len(rows))):
            col -= 1
            continue

        # Collect contiguous non-empty columns for a single problem
        problem_cols: list[int] = []
        while col >= 0 and not all(rows[r][col] == " " for r in range(len(rows))):
            problem_cols.append(col)
            col -= 1

        op_col = problem_cols[-1]  # leftmost column in this problem
        operator = rows[operator_row_idx][op_col]
        if operator not in {"+", "*"}:
            raise ValueError(f"Expected operator in column {op_col}, found '{operator}'")

        numbers: list[int] = []
        for c in problem_cols:
            digits = "".join(rows[r][c] for r in range(operator_row_idx) if rows[r][c] != " ")
            if digits:
                numbers.append(int(digits))

        problems.append((operator, numbers))

    return problems

def main():
    with open("Day 6/day6.txt", "r") as file:
        lines = file.readlines()

    # Part 1
    grid = []
    for line in lines:
        grid_line = line.strip().split()
        grid.append(grid_line)
    rotated_grid = rotate_grid(grid)
    totals = []
    for row in rotated_grid:
        symbol = row[0]
        digits = row[1:]
        total = 0
        if symbol == "+":
            total = sum(int(digit) for digit in digits)
        elif symbol == "*":
            total = math.prod(int(digit) for digit in digits)
        print(f"Total for {symbol} {digits} is {total}")
        totals.append(total)
    print(sum(totals))

    # Part 2
    problems = parse_problems_right_to_left(lines)
    part2_total = 0
    for operator, numbers in problems:
        if operator == "+":
            part2_total += sum(numbers)
        else:
            part2_total += math.prod(numbers)

    print(part2_total)

if __name__ == "__main__":
    main()
from collections import defaultdict
from pathlib import Path


def count_splits(lines: list[str]) -> int:
    """
    Simulate the downward-moving beam and count how many times it splits.
    Each beam moves straight down until it hits a splitter (^). When a beam
    hits a splitter, it stops and creates two new beams that continue
    downward from the immediate left and right positions.

    Multiple beams that end up in the same cell merge into a single beam;
    we only track presence, not multiplicity, which matches the example
    behavior shown in the puzzle.
    """
    grid = [line.rstrip("\n") for line in lines]
    height = len(grid)
    width = len(grid[0])

    # Find the starting position
    start_row = start_col = None
    for r, row in enumerate(grid):
        if "S" in row:
            start_row = r
            start_col = row.index("S")
            break
    if start_row is None:
        raise ValueError("No starting position 'S' found in the grid.")

    # Track active beam columns as a set (presence only); overlapping beams merge.
    active_beams: set[int] = {start_col}
    split_count = 0

    for r in range(start_row + 1, height):
        next_row_beams: set[int] = set()
        for col in active_beams:
            if col < 0 or col >= width:
                continue  # Beam already left the manifold

            cell = grid[r][col]
            if cell == "^":
                split_count += 1
                if col - 1 >= 0:
                    next_row_beams.add(col - 1)
                if col + 1 < width:
                    next_row_beams.add(col + 1)
            else:
                next_row_beams.add(col)

        active_beams = next_row_beams

    return split_count


def count_timelines(lines: list[str]) -> int:
    """
    Count how many timelines exist when a single particle explores all
    possible paths. Each splitter forks the timeline into left and right
    beams; timelines never merge.
    """
    grid = [line.rstrip("\n") for line in lines]
    height = len(grid)
    width = len(grid[0])

    start_row = start_col = None
    for r, row in enumerate(grid):
        if "S" in row:
            start_row = r
            start_col = row.index("S")
            break
    if start_row is None:
        raise ValueError("No starting position 'S' found in the grid.")

    # Track multiplicity per column; timelines never merge, we just tally counts.
    active_beams: dict[int, int] = {start_col: 1}
    exited = 0  # timelines that have already left the grid

    for r in range(start_row + 1, height):
        next_row: defaultdict[int, int] = defaultdict(int)
        for col, count in active_beams.items():
            if col < 0 or col >= width:
                exited += count
                continue

            cell = grid[r][col]
            if cell == "^":
                # Left branch
                if col - 1 >= 0:
                    next_row[col - 1] += count
                else:
                    exited += count
                # Right branch
                if col + 1 < width:
                    next_row[col + 1] += count
                else:
                    exited += count
            else:
                next_row[col] += count

        active_beams = next_row

    # After the last row, all active beams exit downward.
    return exited + sum(active_beams.values())


def main():
    input_path = Path(__file__).parent / "day7.txt"
    with input_path.open("r") as file:
        lines = file.readlines()

    part1 = count_splits(lines)
    print(part1)

    part2 = count_timelines(lines)
    print(part2)


if __name__ == "__main__":
    main()
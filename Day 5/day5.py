def is_in_range(id: int, range: str) -> bool:
	start, end = map(int, range.split("-"))
	return start <= id <= end

def is_in_ranges(id: int, ranges: list[str]) -> bool:
	for range in ranges:
		if is_in_range(id, range):
			return True
	return False

def main():
	with open("Day 5/day5.txt", "r") as file:
		lines = file.readlines()


	fresh_ingredient_ranges = []
	available_ingredient_ids = []
	for line in lines:
		if line.strip() == "":
			continue
		if line.strip().isdigit():
			available_ingredient_ids.append(int(line.strip()))
		else:
			fresh_ingredient_ranges.append(line.strip())
	
	# Part 1
	count_fresh_ingredient_ids = 0
	for id in available_ingredient_ids:
		if is_in_ranges(id, fresh_ingredient_ranges):
			count_fresh_ingredient_ids += 1
	print(f"Part 1: {count_fresh_ingredient_ids}")

	# Part 2
	# For this we just want the number of ingredients in each range
	# We however need to remove the duplicates
	# Parse all ranges into intervals
	intervals = []
	for range_str in fresh_ingredient_ranges:
		start, end = map(int, range_str.split("-"))
		intervals.append((start, end))
	
	# Sort intervals by start value
	intervals.sort()
	
	# Merge overlapping intervals
	merged = []
	for start, end in intervals:
		if not merged or merged[-1][1] < start - 1:  # No overlap (end < start-1 means not adjacent)
			merged.append([start, end])
		else:
			# Merge with previous interval
			merged[-1][1] = max(merged[-1][1], end)
	
	# Calculate total unique count by summing lengths of merged intervals
	total_unique = sum(end - start + 1 for start, end in merged)
	print(f"Part 2: {total_unique}")

if __name__ == "__main__":
	main()
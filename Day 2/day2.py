def is_invalid_part_one(num: int) -> bool:
	# An invalid ID is made only of some sequence of digits repeated twice
	# So we need to check if the number string can be split in half
	# and the first half equals the second half
	num_str = str(num)
	if len(num_str) % 2 != 0:
		return False
	half = len(num_str) // 2
	return num_str[:half] == num_str[half:]

def is_invalid_part_two(num: int) -> bool:
	# An invalid ID is made only of some sequence of digits repeated at least twice
	# So we need to check if the number string can be divided into equal parts
	# where all parts are the same (at least 2 parts)
	num_str = str(num)
	# Try each possible pattern length from 1 to half the string length
	for pattern_len in range(1, len(num_str) // 2 + 1):
		# Check if the string length is divisible by the pattern length
		if len(num_str) % pattern_len != 0:
			continue
		# Extract the pattern (first pattern_len characters)
		pattern = num_str[:pattern_len]
		# Check if the entire string is made of this pattern repeated
		num_repeats = len(num_str) // pattern_len
		if num_repeats >= 2 and pattern * num_repeats == num_str:
			return True
	return False

def main():
	with open("Day 2/day2.txt", "r") as file:
		lines = file.readlines()

	total = 0
	total_part_two = 0
	for line in lines:
		parts = line.split(",")
		for part in parts:
			parts = part.split("-")
			start = int(parts[0])
			end = int(parts[1])
			for i in range(start, end + 1):
				if is_invalid_part_one(i):
					total += i
				if is_invalid_part_two(i):
					total_part_two += i
	print(f"Part One: {total}")
	print(f"Part Two: {total_part_two}")

if __name__ == "__main__":
	main()
def determine_bank_joltage(numbers: list[int]) -> int:
	# We need to find the first digit
	# For this we can find the largest digit in the list - 1
	largest_digit = max(numbers[:-1])
	print(f"Largest digit: {largest_digit}")
	# Then we need to find the next highest digit that comes after the largest digit
	next_highest_digit = max(numbers[numbers.index(largest_digit) + 1:])
	print(f"Next highest digit: {next_highest_digit}")
	return largest_digit, next_highest_digit


def determine_bank_joltage_part_two(numbers: list[int], count: int) -> int:
	# We need to turn on exactly count batteries in the bank to form the largest number
	# Use greedy algorithm: at each step, select the largest digit we can reach
	# while ensuring we can still select enough remaining digits to reach count total
	
	bank_joltage = []
	current_index = 0
	remaining_to_select = count
	
	while remaining_to_select > 0 and current_index < len(numbers):
		# Calculate how many digits we can skip while still being able to select enough remaining
		# We need to leave at least (remaining_to_select - 1) digits after the one we select
		max_skip = len(numbers) - current_index - remaining_to_select
		
		# Find the maximum digit in the range we can consider
		# We can look from current_index to current_index + max_skip + 1
		search_end = min(current_index + max_skip + 1, len(numbers))
		candidate_range = numbers[current_index:search_end]
		
		if not candidate_range:
			break
		
		# Find the maximum digit in this range
		max_digit = max(candidate_range)
		
		# Find the first occurrence of this max digit in the range
		for i in range(current_index, search_end):
			if numbers[i] == max_digit:
				# Select this digit
				bank_joltage.append(numbers[i])
				current_index = i + 1
				remaining_to_select -= 1
				break
	
	# Convert list of integers to string, then to int
	bank_joltage_str = ''.join(str(d) for d in bank_joltage)
	return int(bank_joltage_str)

def main():
	with open("Day 3/day3.txt", "r") as file:
		lines = file.readlines()

	total = 0
	for line in lines:
		numbers = list(line.strip())
		print(f"Numbers: {numbers}")
		largest, second_largest = determine_bank_joltage(numbers)
		bank_joltage = f"{largest}{second_largest}"
		print(f"Bank joltage: {bank_joltage}")
		total += int(bank_joltage)
	print(f"Part One: {total}")

	total_part_two = 0
	for line in lines:
		numbers = list(line.strip())
		bank_joltage = determine_bank_joltage_part_two(numbers, 12)
		print(f"Bank joltage: {bank_joltage}")
		total_part_two += int(bank_joltage)
	print(f"Part Two: {total_part_two}")

if __name__ == "__main__":
	main()
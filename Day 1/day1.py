# Dial starts at 50
import math

START_POS = 50

def rotate_dial(cur, direction, distance):
	# This function now returns 2 values, the new position and the number of times we passed 0
	# For instance: start 50, L68 -> 82, we passed 0 once
	# Start 50, R1000 -> 50, we passed 0 ten times
	new_pos = (cur - distance) % 100 if direction == "L" else (cur + distance) % 100
	
	# Count zeros during rotation
	# For every full 100 clicks, we pass 0 once
	guaranteed_zero = math.floor(distance / 100)
	rest_to_turn = distance % 100
	# Check if we cross 0 in the remaining distance (but don't end at 0)
	# We cross 0 if we wrap around: left turn where new_pos > cur, or right turn where new_pos < cur
	additional_zero = 0
	if rest_to_turn > 0 and (cur != 0 and new_pos != 0):
		if direction == "L" and new_pos > cur:
			additional_zero = 1
		elif direction == "R" and new_pos < cur:
			additional_zero = 1
	
	total_zeros = guaranteed_zero + additional_zero
	return new_pos, total_zeros

def main():
	with open("day1.txt", "r") as file:
		lines = file.readlines()

	lock_pos = START_POS
	count_zero = 0
	for line in lines:
		direction = line[0]
		distance = int(line[1:])
		lock_pos, passed_zero = rotate_dial(lock_pos, direction, distance)
		if lock_pos == 0:
			passed_zero += 1
		count_zero += passed_zero
	print(count_zero)

if __name__ == "__main__":
	main()
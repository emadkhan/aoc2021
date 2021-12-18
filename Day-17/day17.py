#!/usr/bin/python3

LOWEST = -1000
HIGHEST = 1000

def solve_brute(target_area):
	highest = LOWEST 
	target_hit = 0
	worked = []
	for i in range(LOWEST, HIGHEST):
		for j in range(LOWEST, HIGHEST):
			high = simulate([i, j], target_area)
			if high == LOWEST:
				continue
			worked.append((i, j))
			highest = max(highest, high)
			target_hit += 1
	return (highest, target_hit)


# Tried to be clever. This works for the test input but not for the real input.
def solve(target_area):
	vel_x = find_n_for_sum(target_area['x'][0]) 
	max_x = find_n_for_sum(target_area['x'][1])
	highest = -1
	while vel_x <= max_x:
		vel_y = 0
		while True:
			high = simulate([vel_x, vel_y], target_area)
			if high == LOWEST:
				break
			#print("Vel x: {0}, Vel y: {1}".format(vel_x, vel_y))
			highest = max(high, highest)	
			vel_y += 1
		vel_x += 1
	return highest 

def find_sum_for_n(n):
	return (n**2 + n)/2
	
def find_n_for_sum(sum):
	for n in range(1, int(sum/2)):
		if find_sum_for_n(n) >= sum:
			return n	
		

def simulate(velocity, target_area):
	x = 0
	y = 0
	y_positions = []
	step = 0

	while True:
		# If Velocity is positive and it has already crossed the x upper bound then it is not coming back
		if velocity[0] > 0 and x > target_area['x'][1]:
			#print("x short circuit x velocity > 0")
			#print("X: {0} Y: {1}".format(x, y))
			#print("Velocity", velocity)
			return LOWEST 
	
		# If Velocity x is 0 then if it hasn't already reached target then it never will, it cannot drop into 
		if velocity[0] <= 0 and (x < target_area['x'][0] or x > target_area['x'][1]):
			#print("x short circuit x velocity == 0")
			#print("X: {0} Y: {1}".format(x, y))
			#print("Velocity", velocity)
			return LOWEST 


		# If y is already below the target y lower bound and velocity y < 0 then it cannot come back up
		if y < target_area['y'][0]:
			#print("y short circuit")
			#print("X: {0} Y: {1}".format(x, y))
			#print("Velocity", velocity)
			return LOWEST 
	

		# Evaluate Target 

		if x >= target_area['x'][0] and x <= target_area['x'][1] and y <= target_area['y'][1] and y >= target_area['y'][0]:
			#print("Found")	
			#print("X: {0} Y: {1}".format(x, y))
			#print("Velocity", velocity)
			return max(y_positions)

		# Step
		x += velocity[0]
		y += velocity[1]
		y_positions.append(y)
		#print("X: {0} Y: {1}".format(x, y))
		step += 1	
			
		# Gravity and Drag
	
		if velocity[0] > 0:
			velocity[0] -= 1
		elif velocity[0] < 0:
			velocity[0] += 1
		
		velocity[1] -= 1

def parse_input(filename):
	f = open(filename)
	input = f.read().splitlines()[0].split(' ')

	x_target_start = input[2].split('..')[0].split('=')[1]	
	x_target_end = input[2].split('..')[1][:-1]
	y_target_start = input[3].split('..')[0].split('=')[1]	
	y_target_end = input[3].split('..')[1]

	result = {}
	result['x'] = (int(x_target_start), int(x_target_end))
	result['y'] = (int(y_target_start), int(y_target_end))
	print(result)
	f.close()
	return result 

if __name__ == '__main__':
	#input = parse_input('test_input.txt')
	input = parse_input('input.txt')
	print("Running")
	print(solve_brute(input))


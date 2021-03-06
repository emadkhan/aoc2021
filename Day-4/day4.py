#!/usr/bin/python3

def build_boards(boards_input):
	boards = []
	board = []
	for i in range(0, len(boards_input)):
		if boards_input[i] == '':
			if len(board) > 0:
				boards.append(board)
				board = []
			continue

		row = [{'val': int(val), 'marked': False} for val in boards_input[i].split(' ') if val != '']
		board.append(row)

	return boards

def get_unmarked_numbers_sum(board):
	sum = 0
	for row in board:
		for col in row:
			if col['marked'] == False:
				sum += col['val']
	return sum

def calculate_final_score(draws, boards):
	winner_boards_count = 0
	winner_boards_index = [0 for i in range(0, len(boards))]
	is_first_board_winner = True
	result = {'Part1': {}, 'Part2': {}}
	for draw in draws:
		for idx, board in enumerate(boards):
			for row in board:
				for col in row:
					if col['val'] == draw:
						col['marked'] = True
						if is_board_winner(board):
							if is_first_board_winner:
								result['Part1']['result'] = draw * get_unmarked_numbers_sum(board)
								is_first_board_winner = False
							if winner_boards_count == len(boards) - 1 and winner_boards_index[idx] == 0:
								result['Part2']['result'] = draw * get_unmarked_numbers_sum(board)
								return result 
							if winner_boards_index[idx] == 0:
								winner_boards_index[idx] = 1	
								winner_boards_count += 1

def is_board_winner(board):
	# Check for Row Winner
	for row in board:
		has_won = True
		for col in row:
			if col['marked'] == False:
				has_won = False
				break
		if has_won:
			return True

	# Check for Column winner
	for col in range(0, len(board[0])):
		has_won = True
		for row in range(0, len(board)):
			if board[row][col]['marked'] == False:
				has_won = False
				break
		if has_won:
			return True

	return False
				
def get_draws_and_boards(filename):
	f = open(filename, "r")
	input = f.read().splitlines()
	draws = [int(x) for x in input[0].split(',')]
	boards = build_boards(input[1:])
	f.close()
	return (draws, boards)

if __name__ == "__main__":
	draws_and_boards = get_draws_and_boards("input.txt")
	result = calculate_final_score(draws_and_boards[0], draws_and_boards[1])
	print("Part1: {0}, Part2: {1}".format(result['Part1'], result['Part2']))
	

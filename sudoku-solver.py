# sudoku-solver.py
# with the kings rule: 
#	any space cannot contain a number that is
#	a king's move away

def print_matrix(grid):
	for x in grid:
		print(x)

pi_grid = [	[0, 0, 0, 4, 3, 1, 0, 0, 0], 
			[0, 0, 8, 0, 0, 0, 4, 0, 0],
			[0, 3, 0, 0, 0, 0, 0, 1, 0],
			[2, 0, 0, 0, 0, 0, 0, 0, 5],
			[3, 0, 0, 0, 0, 0, 0, 0, 9],
			[9, 0, 0, 0, 0, 0, 0, 0, 2],
			[0, 7, 0, 0, 0, 0, 0, 6, 0],
			[0, 0, 9, 0, 0, 0, 5, 0, 0],
			[0, 0, 0, 8, 5, 3, 0, 0, 0]	]

def num_poss(x, y, n):
	global pi_grid
	for i in range(0, 9):
		if pi_grid[y][i] == n:
			return False

	for i in range(0, 9):
		if pi_grid[i][x] == n:
			return False

	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0, 3):
		for j in range(0, 3):
			if pi_grid[y0 + i][x0 + j] == n:
				return False
	# [x,y]
	# [x+1,y+1],[x-1,y-1],[x+1,y-1],[x-1,y+1]
	# the king's rule
	for i in range(2, 4):
		for j in range(2, 4):
			if (y + pow(-1, i)) in range(9) and (x + pow(-1, j)) in range(9):
				if pi_grid[y + pow(-1, i)][x + pow(-1, j)] == n:
					return False

	return True

print_matrix(pi_grid)

def solve():
	global pi_grid
	for y in range(9):
		for x in range(9):
			if pi_grid[y][x] == 0:
				for n in range(1, 10):
					if num_poss(x, y, n):
						pi_grid[y][x] = n
						#print()
						#print_matrix(pi_grid)
						solve()
						pi_grid[y][x] = 0
				return
	print()
	print_matrix(pi_grid)
	input("More?")

solve()

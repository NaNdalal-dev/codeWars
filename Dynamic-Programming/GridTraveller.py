count = [0]
def GridTraveller(rows,cols):
	count[0] += 1
	if rows == 1 and cols == 1:
		return 1
	if rows == 0 or cols == 0:
		return 0
	return GridTraveller(rows-1,cols) + GridTraveller(rows,cols-1)	

print(GridTraveller(12,8))
print('Steps Taken Without Memoization:',count[0])

#Using Memoization
countMemo = [0]

def GridTravellerWithMemo(rows, cols, memo={}):
	countMemo[0] += 1
	key = f'{rows},{cols}'
	if key in memo:
		return memo[key]

	if rows == 1 and cols == 1:
		return 1
	if rows == 0 or cols == 0:
		return 0
	memo[key] = GridTravellerWithMemo(rows-1,cols,memo) + GridTravellerWithMemo(rows,cols-1,memo)
	return memo[key]

print(GridTravellerWithMemo(12,8))
print('Steps Taken With Memoization:',countMemo[0])

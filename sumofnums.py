#Link:
#https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/python

def show_sequence(n):
	if n == 0:
		return "0=0"
	elif n < 0:
		return f"{n}<0"
	else:
		nums = [str(i) for i in range(n+1)]
		sum_of_nums = sum([int(i) for i in nums])
		sum_str = '+'.join(nums)
		return sum_str+f' = {sum_of_nums}'
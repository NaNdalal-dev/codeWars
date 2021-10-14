#Link:
#https://www.codewars.com/kata/590e03aef55cab099a0002e8/train/python
def incrementer(nums):
	if nums == []:
		return []
	inc = 1
	inc_nums = []
	for num in nums:
		x = num + inc
		if x > 9:
			x = x%10
		inc_nums.append(x)
		inc += 1
	return inc_nums
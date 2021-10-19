#Link:https://www.codewars.com/kata/5a91a7c5fd8c061367000002/train/python
def minimum_steps(numbers, value):
    count = 0
    numbers = sorted(numbers)

    s = numbers[0]
    if s>value:
    	return count

    for val in numbers[1:]:
    	s += val
    	if s >= value:
    		return count+1
    	
    	count += 1
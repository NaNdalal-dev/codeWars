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
print(minimum_steps([4,6,3], 7))
print(minimum_steps([10,9,9,8], 17))
print(minimum_steps([8,9,10,4,2], 23))
print(minimum_steps([19,98,69,28,75,45,17,98,67], 464))
print(minimum_steps([4,6,3], 2))
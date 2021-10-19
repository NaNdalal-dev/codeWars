#link:https://www.codewars.com/kata/5572392fee5b0180480001ae/train/python
def computer_to_phone(numbers):
    new_nums = ''

    for num in numbers:
    	if num == '7' or num == '8' or num == '9':
    		new_nums += str(int(num) - 6)

    	elif num == '1' or num == '2' or num == '3':
    		new_nums += str(int(num) + 6)
    	
    	else:
    		new_nums += num
    return new_nums

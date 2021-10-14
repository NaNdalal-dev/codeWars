#Link:
#https://www.codewars.com/kata/51689e27fe9a00b126000004/train/python

def format_words(words):
    if words == [''] or words == [] or words == None:
    	return ''
    for i in range(words.count('')):
    	words.remove('')

    sentence = ''
    l = len(words)
    if l == 1:
    	return words[0]
    elif l == 2:
    	return f'{words[0]} and {words[1]}'
    sentence = ', '.join(words[:-1])
    sentence += ' and '+words[-1]

    return sentence
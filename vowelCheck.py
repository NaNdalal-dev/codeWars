#Link
#https://www.codewars.com/kata/5a2b7edcb6486a856e00005b/train/python
check_vowel = lambda string, position: string[position].lower() == 'a' or string[position].lower() == 'e' or string[position].lower() == 'i' or string[position].lower() == 'o' or string[position].lower() == 'u' if position >= 0 and position < len(string) else False
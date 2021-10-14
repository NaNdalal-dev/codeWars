#Link:
#https://www.codewars.com/kata/5a4d303f880385399b000001
def fact(num):
    f = 1
    while num:
        f *= num
        num -= 1
    return f
def strong_num(number):
    xnum = number
    xsum = 0
    while number:
        r = number % 10
        factorial = fact(r)
        xsum += factorial
        number //= 10
    if xsum == xnum:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
# Practice Question 1: Find the sum of digits of a positive number using Recursion.

def sumOfDigits(num):
    assert num >= 0 and int(num) == num, 'Enter Only Positive numbers!!'

    if num == 0:
        return 0
    else:
        return int(num % 10) + sumOfDigits(int(num / 10))

#Example of a number
print(sumOfDigits(5119429))

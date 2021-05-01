# Find the power of a number using recursion

def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base

    return base * power(base, exp - 1)
#Sample Output
print(power(12,2)) #144


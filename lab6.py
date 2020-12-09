n = int(input("Input n..."))

def getsumOfDenominators(num):
    denominator = 1
    sum = 0
    for i in range(1, num):
        while denominator<i:
            if num%denominator==0:
                sum += denominator
            denominator += 1
    return sum

for i in range(1, n):
    sumOfDenominators = getsumOfDenominators(i)
    if (sumOfDenominators == i):
        print(f"Number {i} is perfect")
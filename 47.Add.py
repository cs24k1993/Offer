def Add(num1,num2):
    while num2 != 0:
        sum = num1 ^ num2
        carry = (num1 & num2) << 1
        print carry

        num1 = sum
        num2 = carry
    return num1

print Add(7,9)


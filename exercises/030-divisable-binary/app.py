# Your code here
def divisible_binary(n):
    numbers = n.split(',')
    exit = []
    for i in numbers:
        decimal = int(i, 2)
        if decimal % 5 == 0:
            exit.append(i)

    return ','.join(exit)

divisible_binary("0100,0011,1010,1001")
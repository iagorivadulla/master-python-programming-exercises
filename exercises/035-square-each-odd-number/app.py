# Your code here
def square_odd_numbers(n):
    nums = n.split(',')
    nums = [int(x) for x in nums]
    odds = [x for x in nums if x % 2 != 0]
    return [x**2 for x in odds]

print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))
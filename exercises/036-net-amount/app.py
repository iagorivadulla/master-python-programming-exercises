# Your code here
def net_amount(n):
    sep = n.split(' ')
    nums = sep[1::2]
    char = sep[0::2]
    count = 0
    for idx, i in enumerate(char):
        if i == 'D':
            count += int(nums[idx])
        elif i == 'W':
            count -= int(nums[idx])
    
    return count

print(net_amount("D 300 D 300 W 200 D 100"))


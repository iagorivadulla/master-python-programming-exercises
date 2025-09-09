# Your code here
def all_digits_even():
    lst = []
    for i in range(1000, 3001):
        for j in str(i):
            if int(j) % 2 != 0:
                break
        else:  
            lst.append(i)
    
    return ', '.join(str(i) for i in lst)

print(all_digits_even())
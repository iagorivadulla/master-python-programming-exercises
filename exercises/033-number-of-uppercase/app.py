# Your code here
def number_of_uppercase(n):
    exit = {'UPPERCASE' : 0, 
            'LOWERCASE' : 0}
    for i in n:
        if i.isupper():
            exit['UPPERCASE'] += 1
        elif i.islower():
            exit['LOWERCASE'] += 1
    
    return exit

print(number_of_uppercase("Hello world!"))
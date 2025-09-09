# Your code here
def letters_and_digits(n):
    exit = {'LETTERS' : 0, 
            'DIGITS' : 0}
    for i in n:
        if i.isalpha():
            exit['LETTERS'] += 1
        elif i.isdigit():
            exit['DIGITS'] += 1
    
    return exit

print(letters_and_digits("hello world! 123"))

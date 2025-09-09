# Your code here
def squares_dictionary(n):
    dictionary = {}
    count = range(1, n+1)
    for i in count:
        dictionary.update({i : i*i})
    
    return dictionary

print(squares_dictionary(8))
# Your code here
def two_dimensional_list(n, m):
    exit = [[i * j for j in range(m)] for i in range(n)]
    return exit

print(two_dimensional_list(3,5))
# Your code here
def compute_word_frequency(n):
    exit = {}
    sep = n.split(' ')
    for i in sep:
        if i in exit:
            exit[i] +=1
        else:
            exit[i] = 1

    order = dict(sorted(exit.items()))

    for i , j in order.items():
        print(f'{i} : {j} \n')
     

compute_word_frequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")
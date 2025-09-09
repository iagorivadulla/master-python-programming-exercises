# Your code here
def sequence_of_words(n):
    splt = n.split(',')
    splt = sorted(splt, key=lambda w: w.lower())
    

    return ','.join(splt)


print(sequence_of_words("No,gain,pain"))

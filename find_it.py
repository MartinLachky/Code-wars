def find_it(seq):
    dictionary = {}
    seq_copy = seq[:]
    seq = list(dict.fromkeys(seq))
    for i in seq:
        dictionary.update({i:seq_copy.count(i)})
    print (dictionary)
    for i in dictionary:
        if dictionary.get(i)%2 != 0:
            print (i)
            return i
        else:
            continue






find_it([14, 14, 14, 14, 14, 14, 14])
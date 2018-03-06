import sys
def permutations(word):
    compute_permutations("",word)
    
    
def compute_permutations(prefix, word):
    
    if len(word) == 2:
        print(prefix + word[0] + word[1])
        print(prefix + word[1] + word[0])
        return
    
    for i in range(1, len(word)+1):
        compute_permutations(prefix + word[0], word[1:])
        if i < len(word):
            word = swap(word, 0, i)
            
def swap(word, i, j):
    charList = list(word)
    charList[i], charList[j] = charList[j], charList[i]
    return ''.join(charList)
    

if len(sys.argv) == 2:
    arg = sys.argv[1]
    print("List of all permutations of word: ", arg)
    permutations(arg)
else:
    print("You should give one and only one argument. Please try again!")



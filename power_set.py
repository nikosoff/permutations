import sys

def power_set(array):
    array = list(array)
    dictionary = {}
    subsets(array, dictionary)
    return list(dictionary)

def subsets(array, dictionary):
     dictionary[str(array)] = 1
     if len(array) == 0:
            return
     for i in range(1, len(array)+1):
             if str(array[1:]) not in dictionary:
                subsets(array[1:], dictionary)
             if i < len(array):
                   swap(array, 0, i)
                   
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
                     

arguments = sys.argv
                     
if len(arguments) != 2:
    print("You should give an array as argument, i.e. python power_set.py [a,b,c]")
    sys.exit(0)

input = arguments[1].replace(",",'')
array = set(input[1:len(input)-1])

print("Number of subsets: ", len(power_set(array)))
for subset in power_set(array):
    print(subset)

#######################Exercise 1

words = ['this' , 'is', 'a', 'sentence', '.']
def swap(alist, x, y, z,w,v):
    alist[x], alist[y], alist[z],alist[w],alist[v] = alist[v],alist[w],alist[z], alist[y], alist[x]
    return alist
print(f"Before swap: {words }")
swap(words , 0, 1, 2,3,4)
print(f"After swap: {words }")

#############################Exercise 2
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

a_text.split()
count = {}
for word in a_text.split() :
   if word in count :
      count[word] += 1
   else:
      count[word] = 1
print(count)

###########################Exercise 3
cool_list = [2, 5, 6, 12, 45, 47, 98, 123, 1000]
target = 123
def binary_search(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potential_match = array[middle]
        if target == potential_match:
            return f"The index is....{middle}"
        elif target < potential_match:
            right = middle - 1
        else:
            left = middle + 1
    return -1

def binary_helper(array, target):
    return binary_search(array, target, 0, len(array) -1)

print(binary_helper([2, 5, 6, 12, 45, 47, 98, 123, 1000], 123))
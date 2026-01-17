import sys
import math
from collections import OrderedDict 



db = False
swap_count = 0
heapify_call_count = 0


def reset_counts():
    global swap_count
    swap_count = 0
    global heapify_call_count
    heapify_call_count = 0

    
def swap(A, i, j):
    global swap_count
    swap_count += 1
    #print("-----", swap_count, A[i], A[j], "-----")
    A[i], A[j] = A[j], A[i]
    #print("-----", swap_count, A[i], A[j], "-----")

    
def count_heapify():
    global heapify_call_count
    heapify_call_count += 1

    
def current_counts():
    return {'swap_count': swap_count, 'heapify_call_count': heapify_call_count}

# heaps here are complete binary trees allocated in arrays (0 based)
def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return left(i) + 1

# END DO NOT MODIFY

def heapify(A, i, n=None): #min-heapify(A)
    """Ensure that the tree rooted at element i in the list A is a min-heap,
    assuming that the trees rooted at elements left(i) and right(i) are already
    min-heaps. Obviously, if left(i) or right(i) are >= len(A), then element i simply does
    not have those out-of-bounds children. In order to implement an in-place heap sort,
    we will sometimes need to consider the tail part of A as out-of-bounds, even though
    elements do exist there. So instead of comparing with len(A), use the parameter n to
    determine if the child "exists" or not. If n is not provided, it defaults to None,
    which we check for and then set n to len(A).

    Since the (up to) two child trees are already min-heaps, we just need to find the right
    place for the element at i. If it is smaller than both its children, then nothing
    more needs to be done, it's already a min heap. Otherwise you should swap the root
    with the smallest child and recursively heapify that tree.

    If you determine that the element at i should swap with one of its children nodes,
    MAKE SURE you do this by calling the swap function defined above.
    """

    count_heapify() # This MUST be the first line of the heapify function, don't change it.
    if n is None:
        n = len(A)
    if not(i < n):
        # if asked to heapify an element not below n (the conceptual size of the heap), just return
        # because no work is required
        return

    smallest = 0
    l = left(i)
    r = right(i)
    if l < n and A[l][0] < A[i][0]:
        smallest = l
    else:
        smallest = i
    if r < n and A[r][0] < A[smallest][0]:
        smallest = r
    if smallest != i:
        swap(A, i, smallest)
        heapify(A, smallest, n)
    
    return

def buildHeap(A):
    """Turn the list A (whose elements could be in any order) into a
    heap. Call heapify on all the internal nodes, starting with
    the last internal node, and working backwards to the root."""
    n = len(A)
    for i in range(n//2, -1, -1):
        #print("heapify("+str(A), str(i), str(n)+")")
        heapify(A, i, n)
    


def heapExtractMin(A):
    """Extract the min element from the heap A. Make sure that A
    is a valid heap afterwards. Return the extracted element.
    This operation should perform approximately log_2(len(A))
    comparisons and swaps (heapify calls and swap calls).
    Your implementation should not perform O(n) (linear) work."""
    heapify(A, 0)
                            #print(A)
    min = A[0]
                        #print("min", min)
    max = len(A) - 1
                        #A[0] = A[len(A) - 1]
    swap(A, 0, max)
                        #A = A[:-1] why doesnt this work
                        #print("swapped", str(A))
    A.pop()
    heapify(A, 0, len(A))
                        #printCompleteTree(A)
    return min



def heapInsert(A, v):
    """Insert the element v into the heap A. Make sure that A
    is a valid heap afterwards.
    This operation should perform approximately log_2(len(A))
    comparisons and swaps (swap calls).
    Your implementation should not perform O(n) (linear) work.
    MAKE SURE you swap elements by calling the swap function defined above."""
    A.append(v)
    num = len(A) - 1
    while num > 0 and A[num] < A[parent(num)]:
        swap(A, num, parent(num))
        num = parent(num)
    #heapIncreaseKey(A, len(A) - 1, v)
    



def printCompleteTree(A):
    """ A handy function provided to you, so you can see a
    complete tree in its proper shape."""
    
    height = int(math.log(len(A), 2))
    width = len(str(max(A)))
    for i in range(height + 1):
        print(width * (2 ** (height - i) - 1) * " ", end="")
        for j in range(2 ** i):
            idx = 2 ** i - 1 + j
            if idx >= len(A):
                print()
                break
            if j == 2 ** i - 1:
                print("{:^{width}}".format(A[idx], width=width))
            else:
                print("{:^{width}}".format(A[idx], width=width),
                      width * (2 ** (height - i + 1) - 1) * " ", sep='', end='')
    print()




def file_character_frequencies(file_name):
    charDict = {}
    """with open(file_name) as file:
        while True:
            key =  file.read(1)
            if not key: break
            if key in charDict: charDict[key] += 1
            else: charDict[key] = 1 """
    #with open(file_name) as file:
    file = open(file_name)
     
    data = file.read()
    freqList = [PriorityTuple((data.count(c), c)) 
	        for c in sorted(set(data))]
    file.close()    

        
    return freqList


class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one using double parens e.g. PriorityTuple((x, (y, z))) """
    def __lt__(self, other):
        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]


def buildBodes(freqList, resultDict, code):
    if(isinstance(freqList[1], str)):
        resultDict[freqList[1]] = code
    else:
        buildBodes(freqList[1][0], resultDict, code + "0")
        buildBodes(freqList[1][1], resultDict, code + "1")
        
        
def huffman_codes_from_frequencies(frequencies):
    # ----------- turn dict into list ---------
    """freqList = []
    for item in frequencies.items():
        freqList.append(item)
    freqList = [(t[1], t[0]) for t in freqList]"""

    
    #print("----- before heapify ------")
    #print(freqList)
    buildHeap(frequencies)
    #print(freqList)
    #print("----- after heapify -------")
    
    for i in range(1, len(frequencies)):
        t1 = heapExtractMin(frequencies)
        t2 = heapExtractMin(frequencies)
        t3 = PriorityTuple( ( t1[0] + t2[0] , (t1, t2)) )
        heapInsert(frequencies, t3)
    #print("\nfreqList", heapExtractMin(freqList), "leedle")
    resultDict = {}
    buildBodes(heapExtractMin(frequencies), resultDict, "")
    return resultDict


def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    # Suggested strategy...
    freqs = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(freqs)



def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))


def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))


def main():
    """Provided to help you play with your code."""
    import pprint
    frequencies = file_character_frequencies(sys.argv[1])
    pprint.pprint(frequencies)
    codes = huffman_codes_from_frequencies(frequencies)
    pprint.pprint(codes)


if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()

# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Izveido tukšu masīvu
    zero_arr = np.zeros((n), dtype=int)
    non_value_stack = []

    max_height = 0

    for i, next in np.ndenumerate(parents):
        # print("I: ", i)
        # print("zero_arr: " , zero_arr)
        # print("non_value_stack: " , non_value_stack)
        # print("next: " , next)
        # print("zero_arr[i]: ",  zero_arr[i])
        # print("zero_arr[next]: " , zero_arr[next])
        # print("---===---")
        if next < 0:
            zero_arr[i] = 1
            # print("1")
        
        elif zero_arr[next] < 1:
            # print("parbaude")
            non_value_stack.append(i)
            while zero_arr[next] < 1:
                if next < 0:
                    zero_arr[i] = 1
                    break
                non_value_stack.append(next)
                next = parents[next]
                # print(zero_arr)
                # print(non_value_stack)
                # print(parents)
                # print("Next: ", next)
                
            while non_value_stack:
                priv = non_value_stack.pop()
                zero_arr[priv] = zero_arr[next] + 1
                next = priv
                if zero_arr[priv] > max_height:
                    max_height = zero_arr[priv]
                # print("cikls 2")
                # print("non_value_stack: " , non_value_stack)
                # print("zero_arr: " , zero_arr)
        else:
            # print("nesahaja")
            zero_arr[i] = zero_arr[next] + 1
            if zero_arr[i] > max_height:
                    max_height = zero_arr[i]


        

    return max_height

def main():
    # implement input form keyboard and from files
    text = input("I vai F: ")
    if "I" in text[:1]:
        nr = int(input("cipars: "))
        arr = np.array(list(map(int, input("masivs: ").split())))
        print(compute_height(nr, arr))
    elif "F" in text[:1]:
        filename = "test/" + input("Fails: ")

        file = open(filename, "r")
        nr = int(file.readline())
        print(nr)
        arr = file.readline()
        print(arr)
        arr = np.array(list(map(int, arr.split())))
        print(compute_height(nr, arr))
    # arr[0] = 5

    # arr1 = np.zeros((5), dtype=int)

    # cipars = arr1[0]

    # print(type(cipars))

    # if arr[0] > 0:
    #     print("Jā")

    
    

    # print(arr)
    # print(arr1)
    


    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


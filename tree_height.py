# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Izveido tukšu masīvu
    zero_arr = np.zeros((n), dtype=int)
    non_value_stack = []

    max_height = 0

    # Cikls kurš iet cauri katram masīva elementam. next'ā saglabājas masīva vērtība
    for i, next in np.ndenumerate(parents): 
        
        #Pārbauda vai masīvā zero_arr tekošā elementa vecāka pakāpe nav jau saglabāta
        if zero_arr[next] < 1:
            #Saglabā elementu kuram nav zināma pakāpe
            non_value_stack.append(i)
            #Ciklā meklē elemntu, kura vecāka pakāpe ir zināma
            while zero_arr[next] < 1:
                #Pārbauda vai elements ir koka virsotne
                if next < 0:
                    zero_arr[i] = 1
                    break
                #Saglabā elementu kuram nav zināma pakāpe
                non_value_stack.append(next)
                next = parents[next]
            
            #Saglabā elementu pakāpes, kas ir stekā
            while non_value_stack:
                priv = non_value_stack.pop()
                zero_arr[priv] = zero_arr[next] + 1
                next = priv
                
                #Pārbauda vai tekošā koka elementa pakāpe ir augstākā
                if zero_arr[priv] > max_height:
                    max_height = zero_arr[priv]
        else:
            zero_arr[i] = zero_arr[next] + 1

            #Pārbauda vai tekošā koka elementa pakāpe ir augstākā
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

        # let user input file name to use, don't allow file names with letter a
        if filename not in "a":
            file = open(filename, "r")
            nr = int(file.readline())
            arr = file.readline()
            arr = np.array(list(map(int, arr.split())))
            print(compute_height(nr, arr))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


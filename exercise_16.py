"""
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
"""

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    #Create the tuple
    my_tuple = tuple(integer_list)
    
    #Print the hash of the tuple
    print(hash(my_tuple))
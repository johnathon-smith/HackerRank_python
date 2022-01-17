"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
"""

def count_substring(string, sub_string):
    #Tried using the .count method, but it didn't work for this problem
    #return string.count(sub_string)

    #Count manually
    count = 0
    
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i:(i + (len(sub_string)))] == sub_string:
            count += 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
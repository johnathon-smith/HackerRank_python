"""
Read a given string, change the character at a given index and then print the modified string.
"""

def mutate_string(string, position, character):
    #Convert string to list
    string = list(string)
    
    #Change desired character
    string[position] = character
    
    #Convert list back to a string
    string = ''.join(string)
    
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
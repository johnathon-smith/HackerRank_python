"""
You are given a string s.
Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Output Format:
In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
In the second line, print True if s has any alphabetical characters. Otherwise, print False.
In the third line, print True if s has any digits. Otherwise, print False.
In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
In the fifth line, print True if s has any uppercase characters. Otherwise, print False.

"""

if __name__ == '__main__':
    s = input()
    #Convert to list of characters
    s = list(s)
    
    #Create flag vars
    contains_alnum = False
    contains_alpha = False
    contains_digit = False
    contains_lower = False
    contains_upper = False
    
    #Use a loop to check each character in the sting
    for char in s:
        
        #Check for alphanumeric 
        if contains_alnum == False:
            if char.isalnum() == True:
                contains_alnum = True
        
        #Check for alphabetical 
        if contains_alpha == False:
            if char.isalpha() == True:
                contains_alpha = True
    
        #Check for digits
        if contains_digit == False:
            if char.isdigit() == True:
                contains_digit = True
        
        #Check for lowercase
        if contains_lower == False:
            if char.islower() == True:
                contains_lower = True
        
        #Check for uppercase
        if contains_upper == False:
            if char.isupper() == True:
                contains_upper = True
            
    #Print
    print(contains_alnum)
    print(contains_alpha)
    print(contains_digit)
    print(contains_lower)
    print(contains_upper)
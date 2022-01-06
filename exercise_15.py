"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of N followed by N lines of commands where each command will be of the types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
"""

if __name__ == '__main__':
    N = int(input())
    
    my_list = []
    
    #Create a loop to run through the commands N times
    for _ in range(0, N):
        #Get the new command
        command = input()
        
        #Split the given string
        commands = command.split()
        
        #Check for command 'insert'
        if commands[0] == 'insert':
            my_list.insert(int(commands[1]), int(commands[2]))
        #Check for command 'remove'
        if commands[0] == 'remove':
            my_list.remove(int(commands[1]))
        #Check for command 'append'
        if commands[0] == 'append':
            my_list.append(int(commands[1]))
        #Check for command 'sort'
        if commands[0] == 'sort':
            my_list.sort()
        #Check for command 'pop'
        if commands[0] == 'pop':
            my_list.pop()
        #Check for command 'reverse'
        if commands[0] == 'reverse':
            my_list.reverse()
        #Check for command 'print'
        if commands[0] == 'print':
            print(my_list)
    
"""
Task:
There is an array of n integers. There are also two disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. 
Your initial happiness is 0. For each i integer in the array, if i is in A, you add 1 to your happiness. 
If i is in B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Input Format:
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format:
Output a single integer, your total happiness.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
lengths = raw_input().split()
n = int(lengths[0])
m = int(lengths[1])

array = raw_input().split()
array = list(map(int, array))

set_a = raw_input().split()
set_a = set(map(int, set_a))

set_b = raw_input().split()
set_b = set(map(int, set_b))

happiness = 0

for i in range(0, n):
    if array[i] in set_a:
        happiness += 1
    elif array[i] in set_b:
        happiness -= 1

print(happiness)


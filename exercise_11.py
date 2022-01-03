"""
You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j + k is not equal to n.
Please use list comprehensions rather than multiple loops, as a learning exercise.
"""

#This is how it started on HackerRank
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
#My code began here
new_list = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n]

print(new_list)
"""
Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format:
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format:
Output the symmetric difference integers in ascending order, one per line.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()

m_list = raw_input()
m_list = m_list.split()

m_set = set(map(int, m_list))

n = input()

n_list = raw_input()
n_list = n_list.split()

n_set = set(map(int, n_list))

diff_set = m_set.difference(n_set)

diff_set.update(n_set.difference(m_set))

set_size = len(diff_set)

for num in range(0, set_size):
    print(min(diff_set))
    diff_set.discard(min(diff_set))


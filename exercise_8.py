"""
Task:
Ms. Gabriel Williams is a botany professor at District College. 
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used: Average = Sum of Distinct Heights / Total Number of Distinct Heights

Function Description:
Complete the average function in the editor below.

average has the following parameters:
int arr: an array of integers

Returns:
float: the resulting float value rounded to 3 places after the decimal

Input Format:
The first line contains the integer, N, the size of arr.
The second line contains the N space-separated integers, arr[i].
"""

from __future__ import division

def average(array):
    
    distinct_lengths = set(array)
    
    avg = sum(distinct_lengths) / len(distinct_lengths)

    return avg

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
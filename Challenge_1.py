# Weekly Coding Challenge:
# Pls provide the link to your solution in the comments section not later than Friday morning. 
# Problem Statement
# Write a program that accepts sets of three numbers and prints the second-maximum number among the three.
# Input
# First line contains the number of triples, N.
# The next N lines which follow each have three space separated integers.
# Output
# For each of the N triples, output one new line which contains the second-maximum integer among the three.
# Constraints	
# 1 ≤ N ≤ 6
# 1 ≤ every integer ≤ 10000
# The three integers in a single triplet are all distinct. That is, no two of them are equal.
# Sample Input
# 3
# 1 2 3
# 10 15 5
# 100 999 500
# Sample Output
# 2
# 10
# 500
#============================================

from unittest import result


N = int(input())
L=[]
for i in range(N):
    I1, I2, I3 = map(int, input(). split())

    result = sorted([I1, I2, I3])
    L.append(result[1])
for i in range(len(L)):
    print(L[i])
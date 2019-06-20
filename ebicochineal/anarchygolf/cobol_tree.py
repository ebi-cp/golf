#! /usr/bin/env python3

n=input()
for i in range(n):print['COBOL','*'*(i*2+1)][i<n-1].center(n*2-2).rstrip()
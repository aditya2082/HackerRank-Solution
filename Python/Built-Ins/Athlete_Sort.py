'''
# Athlete Sort

https://www.hackerrank.com/challenges/python-sort-sort

### Problem

You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on).   
You are required to sort the data based on the Kth attribute and print the final resulting table.

**Input Format**

The first line contains N and M separated by a space.   
The next N lines each contain M elements.   
The last line contains K.

**Output Format**

Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

**Sample Input 0**
```
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
```
**Sample Output 0**

```
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
```
'''

import math
import os
import random
import re
import sys

class Main():
    def __init__(self):
        self.n, self.m = map(int, input().split())
        
        self.data = []
        for i in range(self.n):
            self.data.append(list(map(int, input().split())))
            
        self.k = int(input())
        
    def output(self):
        self.data.sort(key = lambda x : x[self.k])
        for li in self.data:
            print(*li, sep=' ')


if __name__ == '__main__':
    obj = Main()
    obj.output()
'''
# ginortS

https://www.hackerrank.com/challenges/ginorts

### Problem

You are given a string S.   
S contains alphanumeric characters only.   
Your task is to sort the string S in the following manner:

- All sorted lowercase letters are ahead of uppercase letters.
- All sorted uppercase letters are ahead of digits.
- All sorted odd digits are ahead of sorted even digits.

**Input Format**

A single line of input contains the string S.

**Output Format**

Output the sorted string S.

**Sample Input 0**

```
Sorting1234
```

**Sample Output 0**

```
ginortS1324
```
'''

def order_function(x):
    if x.islower():
        return (1, x)
    elif x.isupper():
        return (2, x)
    else:
        return (3 if int(x) % 2 == 1 else 4, x)

print(*sorted(input(), key = order_function), sep='')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(input())

phonebook = {}

for i in range(n):
    string = input()
    n = string.split(sep=" ")
    phonebook[n[0]] = n[1]

lines = sys.stdin.readlines()

for i in lines:
    name = i.strip()
    if name in phonebook:
        print(name + '=' + str( phonebook[name] ))
    else:
        print('Not found')

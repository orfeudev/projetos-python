#desafio 1

if __name__ == '__main__':
    print("Hello, World!")


#desafio 2

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0:
        print('Weird')
    elif 2 <= n <= 5:
        print('Not weird')
    elif 6 <= n <= 21:
        print('Weird')
    else: print('Not Weird')



#desafio 3

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)


#desafio 4

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a // b)
print(a / b)

#desafio 5

if __name__ == '__main__':
    n = int(input())
    
for i in range(n):
    print(i ** 2)

#desafio 6

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input())
print(is_leap(year))



#desafio 7

Alternate solution:

if __name__ == '__main__':
    n = int(input())
    print("".join([str(i) for i in range(1,n+1)]))



#desafio 8

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    desafio8 = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]
    print(desafio8)

#desafio 9

n = int(input())
numb = input()
lis = list(map(int, numb.split()))
big, sbig = -6000, -6000
for i in lis:
    if (i > big):
        big, sbig = i, big
    elif (i < big and i > sbig):
        sbig = i
print (sbig)

#desafio 10

n=[]
r=[]
for i in range(int(input())):
    n.append(input())
    r.append(float(input()))
m=min(r)
re=[]
for i in range(len(r)):
    if r[i]==m :r[i]=1000000000
m=min(r)
for i in range(len(r)):
    if r[i]==m:re.append(n[i]) 
re.sort()
for i in re :print(i)

#desafio 11

n=input()
grades={}
for j in xrange(n):
  data=raw_input().strip().split()
  name=data[0]
  gr=map(float,data[1:])
  grades[name]=sum(gr)/len(gr)
student=raw_input().strip()
print "{:0.2f}".format(grades[student])

#desafio 12

N = int(input())
dictionary = {}
for _ in range(N):
    A = input().split()
    name = A.pop(0)
    dictionary[name] = list(map(float, A))
name = input()
print("{0:.2f}".format(sum(dictionary[name]) / len(dictionary[name])))


#desafio 13

my_list = []
N = int(input())

for _ in range(N):
    command = input().split()
    
    if command[0] == "insert":
        my_list.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        print(my_list)
    elif command[0] == "remove":
        my_list.remove(int(command[1]))
    elif command[0] == "append":
        my_list.append(int(command[1]))
    elif command[0] == "sort":
        my_list.sort()
    elif command[0] == "pop":
        my_list.pop()
    elif command[0] == "reverse":
        my_list.reverse()


#desafio 14

n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))

#desafio 15

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#desafio 16

def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#desafio 17

def print_full_name(first, last):
   print(f"Hello {first} {last}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#desafio 18

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


#desafio 19

big_str = input().strip()
small_str = input().strip()
small_len = len(small_str)
count = 0

for i in range(len(big_str) - small_len + 1):
    if big_str[i:i+small_len] == small_str:
        count += 1

print(count)

#desafio 20 

inp = input()
print(any(x.isalnum() for x in inp))
print(any(x.isalpha() for x in inp))
print(any(x.isdigit() for x in inp))
print(any(x.islower() for x in inp))
print(any(x.isupper() for x in inp))

#desafio 21

thickness = int(input())
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

for i in range(thickness + 1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

for i in range((thickness + 1) // 2):
    print((c*thickness*5).center(thickness*6))

for i in range(thickness + 1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#desafio 22

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#desafio 23

N, M = map(int,input().split()) 
for i in range(1,N,2): 
    print((".|."*i).center(M,'-'))
print(("WELCOME".center(M,'-')))
for i in range(N-2,-1,-2): 
    print((".|."*i).center(M,'-'))

#desafio 24

def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#desafio 25~

import sys

stdin = sys.stdin

n = int(stdin.readline())
for i in range(2*n-1):
    d = n-1-abs(n-1-i)
    for j in range(4*n-3):
        if j % 2 == 0 and abs((j-(2*n-2))//2) <= d:
            sys.stdout.write(chr(97+n-1-(d-abs((j-(2*n-2))//2))))
        else:
            sys.stdout.write("-")
    sys.stdout.write("\n")


#desafio 26

n=input()
list1=n.split(' ')
for i in list1:
    print(i.capitalize(),end=' ')


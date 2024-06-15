'''
Problem Statement: 
In the enchanted land of Numeria, Alice is on a quest to find the legendary 
Prime Key to unlock the ancient Vault of Secrets. The vault's guardian, an 
ancient sphinx, presents a multi-step puzzle that Alice must solve to obtain the 
Prime Key. 
The puzzle consists of multiple levels, each requiring Alice to solve a different 
challenge involving prime numbers. To progress through each level, Alice must 
perform the following tasks: 
Level 1: Find the smallest prime number larger than a given integer N. 
Level 2: Calculate the sum of all numbers between N and the smallest 
prime number larger than  N. 
Level 3: Determine if the product of the smallest prime number larger than N 
and the next immediate prime number is also a prime. 
To complete the puzzle and retrieve the Prime Key, Alice must solve these 
challenges in sequence for a given integer N. 
Your task is to write a function that takes an integer N and returns a tuple 
containing the following: - The smallest prime number larger than N (Level 1 result). - The sum of all prime numbers between N and the smallest prime number 
larger than N (Level 2 result). - A boolean indicating whether the product of the smallest prime number 
larger than N and the next immediate prime number is prime (Level 3 result). 
Help Alice navigate through the levels, solve the puzzle, and obtain the Prime 
Key to unlock the Vault of Secrets. 
'''
import math
def isprime(m):
    if m <= 1:
        return False
    if m == 2:
        return True
    if m % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(m)) + 1, 2):
        if m % i == 0:
            return False
    return True

def ancient_Vault(n):
    i=n
    l=[]
    while True:
        i+=1
        if isprime(i) and i>n:
            l.append(i)
            break
    s=[k for k in range(n+1,i)]
    l.append(sum(s))
    j=i
    while True:
        j+=1
        if isprime(j) and j>i:
            l.append(isprime(j*i))
            break
    return tuple(l)
print(ancient_Vault(7))
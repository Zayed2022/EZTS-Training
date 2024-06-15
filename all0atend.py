# add all the 0's in list to the end of the list
# don't add use list methods and TC==O(n)
''' The time complexity of this code is O(n) because it iterates through the array
once to move all non-zero elements to the front of the array. 
The space complexity is O(1) because it does not use any extra space that grows 
with the input size, it only uses a constant amount of extra space.'''
'''
Initialization:

We start with a list of numbers, which includes some zeros.
Two pointers are used: i (to traverse the list) and j (to keep track of the 
position to place non-zero elements).
First Phase (Moving non-zeros):

We traverse the list with pointer i.
Whenever we encounter a non-zero element, we move it to the position
indicated by pointer j and then increment j.
Second Phase (Filling with zeros):

After moving all non-zero elements to the front, pointer j will point to 
the position where zeros should start.
We then fill the rest of the list with zeros from the position j to the end
of the list.
Result:

The list now has all non-zero elements at the beginning, in their original order,
followed by all the zeros at the end.
'''
a=[4,5,0,1,9,0,5,0]
n=len(a)
j=0
for i in range(n):
    if a[i]!=0:
        a[j]=a[i]
        j+=1
while j < n:
    a[j]=0
    j+=1
print(a)










# n=8
# a=[4,5,0,1,9,0,5,0]
# c=a.count(0)
# for i in range(c):
#         a.remove(0)
#         a.append(0)
# print(a)
#a=[4,5,0,1,9,0,5,0]
# a=[1,0,2,0,3,0]
# n=len(a)
# for i in range(n-1):
#     for j in range(i+1,n-1):
#         if a[j]==0:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

# a=[4,5,0,1,9,0,5,0]
# n=len(a)
# l=0
# r=n-1
# def swap(l,r):
#     a[l],a[r] =a[r],a[l]
# while l < r:
#     if a[l]!=0:
#         l+=1
#     if a[r]==0:
#         r-=1
#     swap(l,r)
# print(a)

# def loginandRegister(user, password):
#     if user in d:
#         if password == d[user]:
#             print("Successful login")
#         else:
#             print("Invalid credentials")
#     else:
#         print("User not found")
#         print("Registering user")
#         new_user = input("Enter a new user name: ")
#         new_password = input("Enter a new password: ")
#         d[new_user] = new_password
#         loginandRegister(new_user, new_password)

# if __name__ == "__main__":
#     d = {"zayed": "123", "batman": "125"}
#     user = input("Enter user name: ")
#     password = input("Enter password: ")
#     loginandRegister(user, password)

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



l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
s='a8'
print('black false') if (((l.index(s[0])+1) + int(s[1])) %2==0) else print("true white")
    
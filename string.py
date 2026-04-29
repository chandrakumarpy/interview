# a = 'aaabbbxxdddaaccuuzzz' output = 3a3b2x3d2a2c2u3z
m = ''
count = 1
for i in range(1,len(a)):
    if a[i] == a[i-1]:
        count += 1
    else:
        m += str(count)+a[i-1]
        count = 1
print(m+str(count)+a[-1])

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

# count of ovels in string a = 'potulachandrakumar' output = {'o': 1, 'u': 2, 'a': 4}
d={}
for i in a:
    if i in 'aeiou':
        d[i]=d.get(i, 0)+1
print(d)

# add the ovels in reverse formate a = 'potulachandrakumar' output - patulachandrakumor
import re
remove_ovels = re.sub(r'[^aeiou]', '', a)
revers_ovels = remove_ovels[::-1]
s = ''
count = 0
for i in a:
    if i in 'aeiou':
        s += revers_ovels[count]
        count += 1
    else:
        s += i
print(s)
# if string is not repeated a = 'aabbbcccddd' out put = 2a3b3c3d
data = sorted(set(a))
s = ''
for i in data:
    s = s + str(a.count(i))+i
print(s)

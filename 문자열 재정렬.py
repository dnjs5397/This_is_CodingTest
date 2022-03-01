s = input()
alpha = ''
num = 0
for i in range(len(s)):
    if (s[i] == '0' or s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '4' or
        s[i] == '5' or s[i] == '6' or s[i] == '7' or s[i] == '8' or s[i] == '9') :
        num += int(s[i])
    else:
        alpha += s[i]
        
s = list(alpha)
s.sort()
alpha = ''
for i in range(len(s)):
    alpha += s[i]
alpha += str(num)
print(alpha)
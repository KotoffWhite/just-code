s = input()
flag = True
newline = ''

for c in s:
    if flag:
        newline += c.lower()
    else:
        newline += c.upper()
    flag = not flag

print(newline)

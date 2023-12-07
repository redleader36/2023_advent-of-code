import re
filename="input"
with open(filename) as file:
    lines = [line.rstrip() for line in file]

s = 0
for l in lines:
    num = re.findall(r'\d', l)
    ln = f"{num[0]}{num[-1]}"
    print(ln)
    s+=int(ln)
print(s)

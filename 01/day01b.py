import re
filename="input"
with open(filename) as file:
    lines = [line.rstrip() for line in file]

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

word_digit_pairs = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

s = 0
for l in lines:
    x = []
    # print(l)
    sub = {}
    for word in word_digit_pairs.keys():
        finds = []
        for i in findall(word, l):
            # l = f"{l[0:i]}{digit}{l[i+1:len(l)]}"
            finds.append(i)
            # print(i)
        if finds:
            sub[word]=finds
    # print(sub)
    for w in sub.keys():
        # print(w)
        for n in sub[w]:
            # print(n)
            l = f"{l[0:n]}{word_digit_pairs[w]}{l[n+1:len(l)]}"
    num = re.findall(r'\d', l)
    ln = f"{num[0]}{num[-1]}"
    print(ln)
    s+=int(ln)
print(s)

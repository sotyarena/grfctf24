dist = open('dist.txt', 'r')
flag = open('flag.txt', 'r')

text = ""

for line in dist:
    if line == '\n':
        text += '\n'
        continue
    text += " ".join(word[::-1] for word in line.strip().split(' ')) + "\n"

final = ""

for line in flag:
    index = int(line.strip())
    final += text[index]

print(final)
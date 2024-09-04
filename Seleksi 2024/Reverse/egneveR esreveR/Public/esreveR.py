text = open('poem.txt', 'r')
dist = open('dist.txt', 'w')
flag = open('flag.txt', 'w')

for line in text:
    if line == '\n':
        dist.write('\n')
        continue
    dist.write(" ".join(word[::-1] for word in line.strip().split(' ')) + "\n")


FLAG = "ctfgrf24{REDACTED}"
i = 0

for j, char in enumerate(text.read()):
    if i == len(FLAG):
        break
    if char == FLAG[i]:
        print(FLAG[i], "found!")
        flag.write(f"{j}\n")
        i += 1

dist = open('dist.txt', 'w')
flag = open('flag.txt', 'w')
redacted = open('redacted.txt', 'r')


for line in redacted:
    if line == '\n':
        dist.write('\n')
        continue
    dist.write(" ".join(word[::-1] for word in line.strip().split(' ')) + "\n")


FLAG = "ctfgrf24{C4p7ur3_Th3_F149_24}"
i = 0

for j, char in enumerate(redacted.read()):
    if i == len(FLAG):
        break
    if char == FLAG[i]:
        print(FLAG[i], "found!")
        flag.write(f"{j}\n")
        i += 1

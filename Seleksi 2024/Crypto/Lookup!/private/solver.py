ciph = open('secret.txt', 'r').read()
dist = open('dist.txt', 'r')

lookup_table = []

for line in dist:
    lookup_table.append(eval(line.strip().split(' = ')[1]))

def sub(str, lookup1, lookup2):
    result = ""
    for c in str:
        if not c in lookup1:
            result += c
        else:
            result += lookup2[lookup1.index(c)]
    return result

print(sub(ciph, lookup_table[1], lookup_table[0]))
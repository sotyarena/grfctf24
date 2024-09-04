flag = open("ijazah.txt", "rb").read()

def xor(text, key):
    res = bytearray(b'')
    for i in range(len(text)):
        res.append(text[i] ^ key[i % len(key)])
    return bytes(res)

print(xor(flag, b"CWK"))
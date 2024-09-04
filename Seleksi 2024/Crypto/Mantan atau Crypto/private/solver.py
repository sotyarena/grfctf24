key = b"""
Hai. Sudah XX bulan aku pacaran denganmu.
Aku kira dengan nampanmu yang menawan itu
ternyata hatimu tidak semenawan yang kukira
KAMU BUSUK! KAMU YANG NYAKITIN AKU DULU!!
Mungkin nanti kau akan mengadu ke polisi
namun sebelum itu terjadi, aku telah membuat ini
supaya kau tidak bisa kuliah dan keterima kerja
HAHhHaaAHHAhahAaHahaahAAHAHAHHAHA =D
""".hex()

res = bytearray()
for i,c in enumerate(open('HahHAhahHhah', 'rb').read()):
    res.append(c ^ ord(key[i]))
print(bytes(res).decode())
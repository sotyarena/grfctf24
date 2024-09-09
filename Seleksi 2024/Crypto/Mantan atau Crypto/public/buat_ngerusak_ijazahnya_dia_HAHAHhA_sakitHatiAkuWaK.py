import sys

message = """
Hai. Sudah XX bulan aku pacaran denganmu.
Aku kira dengan nampanmu yang menawan itu
ternyata hatimu tidak semenawan yang kukira
KAMU BUSUK! KAMU YANG NYAKITIN AKU DULU!!
Mungkin nanti kau akan mengadu ke polisi
namun sebelum itu terjadi, aku telah membuat ini
supaya kau tidak bisa kuliah dan keterima kerja
HAHhHaaAHHAhahAaHahaahAAHAHAHHAHA =D
"""

def mampusLuwh(biarin, akuTerlanjurSakitHati):
    iniAkibatnyaKloKamuJhtKeAku = bytearray()
    for pokoknya, gatau in enumerate(biarin):
        rasain = ord(gatau) ^ ord(akuTerlanjurSakitHati[pokoknya])
        iniAkibatnyaKloKamuJhtKeAku.append(rasain)
    return bytes(iniAkibatnyaKloKamuJhtKeAku)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = open(sys.argv[1], 'r')
        content = file.read()
        result = mampusLuwh(content, message.encode().hex())
        open('HahHAhahHhah', 'wb').write(result)
        print("HahHAhahHhah Mampuss:p")
    else:
        print("Pesan dari aku:\n", message)
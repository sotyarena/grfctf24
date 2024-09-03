import string
from math import gcd

pairs = [
    [198, 297], # 99
    [234, 351], # 117
    [218, 327], # 109
    [156, 208], # 52
    [190, 285], # 95
    [204, 306], # 102
    [224, 336], # 112
    [196, 294], # 98
    [570, 665], # 95
    [196, 294], # 98
    [98, 147],  # 49
    [194, 291], # 97
    [230, 345], # 115
    [156, 208], # 52
    [665, 760], # 95
    [208, 312], # 104
    [202, 303], # 101
    [208, 312], # 104
    [102, 153]  # 51
]

def main():
    result = ""
    for index, pair in enumerate(pairs):
        print(f'\n{index+1}. {pair[0]} & {pair[1]}')
        check = input("gcd: ")
        assert any(c in string.digits for c in check), "Invalid input!"
        if int(check) != gcd(pair[0], pair[1]):
            print("\nSalah!")
            exit()
        result += chr(int(check))
    print("\nTerima kasih telah mengerjakan tes ini!")
    print("ctfgrf24{" + result + "}")

        

if __name__ == "__main__":
    main()
import string

pairs = [
    [198, 297],
    [234, 351],
    [218, 327],
    [156, 208],
    [190, 285],
    [204, 306],
    [224, 336],
    [196, 294],
    [570, 665],
    [196, 294],
    [98, 147],
    [194, 291],
    [230, 345],
    [156, 208],
    [665, 760],
    [208, 312],
    [202, 303],
    [208, 312],
    [102, 153]
]

def main():
    test = ""
    for index, pair in enumerate(pairs):
        print(f'\n{index+1}. {pair[0]} & {pair[1]}')
        check = input("gcd: ")
        assert any(c in string.digits for c in check), "Invalid input!"
        test += check + " "
    print(f"\nRekap Jawaban:\n{test}")
    print("\nTerima kasih telah mengerjakan tes ini!")

        

if __name__ == "__main__":
    main()
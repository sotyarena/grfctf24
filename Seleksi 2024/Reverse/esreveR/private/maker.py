import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python maker.py [text_to_reverse]")
        exit()
    if ' ' in sys.argv[1]:
        res = " ".join(word[::-1] for word in sys.argv[1].split(' '))
    else:
        res = sys.argv[1][::-1]
    print("\n" + res)
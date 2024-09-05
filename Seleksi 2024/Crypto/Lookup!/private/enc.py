import random
import string

SECRET = "Pssstt, please don't tell anyone about my secret ==> ctfgrf24{h4ny4_5u67i7u5i_ciph3r_6i454}"

def get_charset():
    chars = list(string.ascii_letters + string.digits)
    random.shuffle(chars)

    return chars

def sub(strings, lookup1, lookup2):
    result = ""
    for c in strings:
        if not c in lookup1:
            result += c
        else:
            result += lookup2[lookup1.index(c)]
    return result

def main():
    global SECRET

    lookup1 = get_charset()
    lookup2 = get_charset()

    result = sub(SECRET, lookup1, lookup2)

    dist = open("dist.txt", "w")
    dist.write(f"lookup1 = {lookup1}\n")
    dist.write(f"lookup2 = {lookup2}")

    secret = open("secret.txt", "w")
    secret.write(result)


if __name__ == "__main__":
    main()
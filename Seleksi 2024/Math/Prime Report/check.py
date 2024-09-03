import hashlib
import time
# from Crypto.Util.number import isPrime

tests = [29, 44, 200, 300, 13, 100, 223, 30, 101, 18, 50, 12, 85, 21, 63, 41, 144, 167, 359, 77]

def main():
    print("Welcome to the prime number test module!")
    print("Colecting numbers...")
    time.sleep(1)
    
    answer = ""
    for num in tests:
        print("\n==>", num)
        inp = input("It's prime? (y/n): ")

        assert len(inp) == 1 and inp in 'yn', "Invalid input!"

        # if isPrime(num):
        if inp == 'y':
            answer += "P"
        else:
            answer += "N"
    
    # print(answer)
    print("\nSaving.....")
    hash_id = hashlib.md5(answer.encode()).hexdigest()
    time.sleep(1)
    print("Report saved!\nHere's your report token ==> GRFCTF{" + hash_id + "}")

if __name__ == '__main__':
    main()

# PNNNPNPNPNNNNNNPNPPN
import sys
import os

###########################################################################################
#                             Welcome to the Shuffle Machine                              #
###########################################################################################
#                                                                                         #
# If you want to try this machine, then type this into your terminal:                     #
#                                                                                         #
# py shuffle_machine.py <file_to_shuffle>                                                 #
#                                                                                         #
# The <file_to_shuffle> argument is optional. If it empty, then you will be in live mode. #
# You can shuffle any string that you inputed. Have fun;)                                 #
#                                                                                         #
###########################################################################################


def pad(string):
    return string + (" " * (5 - len(string)))

def covert2blocks(string):
    res = []
    for i in range(0, len(string), 5):
        res.append(pad(string[i:i+5]))
    return res


def shuffle(string):
    result = []
    blocks = covert2blocks(string)
    for block in blocks:
        tmp = ["" for _ in range(len(block))]
        x = [1, 2, -2, 1, -2] # shuffle
        # x = [2, -1, 2, -2, -1] # reshuffle
        for i in range(len(block)):
            tmp[i + x[i]] = block[i]
        result.append("".join(tmp))
    return "".join(result)

def main():
    while True:
        string = input("\nInput your string: ")
        result = shuffle(string)
        print('>>', result, end='\n')

def processFile(filename):
    if (os.path.exists(filename)):
        string = open(filename, 'r').read()
        open('shuffled.txt', 'w').write(shuffle(string))
        print(f"\n{filename} ===> shuffled.txt")
    else:
        print(f"\nFile {filename} doesn't exist!")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        processFile(sys.argv[1])

# asli      : 12345
# shuffled  : 31524
from datetime import datetime
from time import sleep
import random


def getDatetime():
    now = datetime.now()
    return '\033[34m' + f"[{now.strftime("%H.%M")}, {now.strftime("%m/%d/%Y")}]" + '\033[0m'

def sendFrom(subject):
    return getDatetime() + f"\033[33m {subject}\033[0m: "

def fail():
    failMessage = [
        sendFrom('Anonymous') + "Sorry, your answer is not correct. We'll consider about your position in this community",
        sendFrom('Anonymous') + "Wrong. Your answer make us doubt about your position in this comunity.",
        sendFrom('Anonymous') + "Hmm, your response doesn't quite hit the mark. We might need to reconsider your place here.",
        sendFrom('Anonymous') + "Incorrect answer. We’ll need to evaluate your contribution to the community further.",
        sendFrom('Anonymous') + "That’s not correct. We may need to rethink your involvement with us.",
        sendFrom('Anonymous') + "Not quite right. We’ll be reexamining your role in the community based on this response.",
        sendFrom('Anonymous') + "Looks like that’s not the right answer. We’ll have to assess your position in the community more closely.",
        sendFrom('Anonymous') + "Your answer missed the mark. This will impact how we view your role in our community.",
        sendFrom('Anonymous') + "That's not the right answer. We’ll be taking another look at your involvement here.",
        sendFrom('Anonymous') + "Incorrect. This might affect how we view your participation in the community.",
    ]
    print(random.choice(failMessage))
    sleep(3)
    print(sendFrom('Anonymous') + "Try again next time")
    sleep(2)
    print('\n\033[31mConnection Closed!\033[0m')
    exit()


def main():
    print('\n\033[31mStarting connection...\033[0m')
    sleep(2)
    print('\033[32mConnected!\033[0m\n')
    
    sleep(0.2)
    print(sendFrom('Anonymous') + "Hello newbie! I heard you're a new member of ctfgrf")
    sleep(2)
    print(sendFrom('Anonymous') + "Im staff at ctfgrf Headquarter. I'm not gonna spill to you about my identity until you pass this test")
    sleep(3)
    print(sendFrom('Anonymous') + "I've already sent the image file. Have you received it??")
    sleep(1.5)

    inp = input(sendFrom('Me'))
    sleep(1.5)

    if "yes" in inp.lower():
        print(sendFrom('Anonymous') + "Great! now i'll explain the challenge")
        sleep(2)
    elif "no" in inp.lower() or inp.lower() == "":        
        print(sendFrom('Anonymous') + "Huh, i thought you already had it. Well just download the attachment and i'll explain the challenge")
        sleep(3)
    else:        
        print(sendFrom('Anonymous') + "Im not respect if you being unprofessional")
        sleep(1.5)
        print(sendFrom('Anonymous') + "If you not interested with this challenge, you can leave this community")
        sleep(2)
        print('\n\033[31mConnection Closed!\033[0m')
        exit()

    print(sendFrom('Anonymous') + "You will hunt a flag")
    sleep(3)
    print(sendFrom('Anonymous') + "And the flag is split into several hex fragments")
    sleep(4)
    print(sendFrom('Anonymous') + "I'll give you some example:\nfragment 1: 66 6C 34 67 5F 66 72 61 39\nfragment 2: 6D 65 6E 74 5F 37 65 73 74\nTry to decode the fragments and merge it into one!")
    sleep(1.5)
    
    inp = input(sendFrom('Me'))
    sleep(1.5)

    if inp == "fl4g_fra9ment_7est":
        print(sendFrom('Anonymous') + "Correct! That's how this game work")
        sleep(2)
    else:        
        print(sendFrom('Anonymous') + "False! The right answer was \"fl4g_fra9ment_7est\"")
        sleep(2)

    print(sendFrom('Anonymous') + "You must find all fragment inside the image")
    sleep(3)
    print(sendFrom('Anonymous') + "Then, i'll give you the last fragment as a signature for passing this test")
    sleep(2)
    print(sendFrom('Anonymous') + "The number of fragments you've to search is 3")
    sleep(1.8)
    print(sendFrom('Anonymous') + "So let's start the challenge")
    sleep(1.5)
    print(sendFrom('Anonymous') + "Try to look at the image")
    sleep(3)
    print(sendFrom('Anonymous') + "I put the first fragment on it. Get the decoded fragment!")

    inp = input(sendFrom('Me'))
    sleep(1.5)

    if inp == "r3gistr4tion_":
        print(sendFrom('Anonymous') + "Excelent! Now maybe you wonder about the next fragment")
        sleep(2)
    else:        
        fail()

    print(sendFrom('Anonymous') + "It's \"embed\" inside the information of the image")
    sleep(2)
    print(sendFrom('Anonymous') + "If you know what i mean, try to get the second fragment!")
    sleep(2)

    inp = input(sendFrom('Me'))
    sleep(1.5)

    if inp != "t0_f1nd_":
        print(sendFrom('Anonymous') + "Incorrect. Try to find it again. I'll give you the second chance!")
        sleep(2)

        inp = input(sendFrom('Me'))
        sleep(1.5)

        if inp != "t0_f1nd_":
            fail()

    print(sendFrom('Anonymous') + "Great! Now the last one")
    sleep(2)
    print(sendFrom('Anonymous') + "Maybe it will be a little bit difficult")
    sleep(2.5)
    print(sendFrom('Anonymous') + "I've hidden the third fragment somewhere")
    sleep(2)
    print(sendFrom('Anonymous') + "If you need a hint just tell me. Try to search it!")
    sleep(1.5)

    inp = input(sendFrom('Me'))
    sleep(1.5)

    if any([w in inp for w in ['need', 'hint', 'help']]):
        print(sendFrom('Anonymous') + "Okay, i'll give you a hint, only once!")
        sleep(2)
        print(sendFrom('Anonymous') + "Try to look for the last bytes")
        sleep(2)
        print(sendFrom('Anonymous') + "Send me the decoded fragment if you find it")
        sleep(1.5)

        inp = input(sendFrom('Me'))
        sleep(2)

        if "1QHGhwasONr_Sxg_jMk3Jtqa6wn7iISVx" in inp:
            print(sendFrom('Anonymous') + "Interesting.. you found something")
            sleep(2)
            print(sendFrom('Anonymous') + "As you tought, i keep the third fragment on drive")
            sleep(2)
            print(sendFrom('Anonymous') + "Find a way to open it!")
            sleep(3)
            print(sendFrom('Anonymous') + "Tell me when you got the decoded fragment!")
            sleep(1.5)

            inp = input(sendFrom('Me'))
            sleep(3)

            if inp != "the_b3st_0ne_":
                fail()
        elif inp != "the_b3st_0ne_":
            fail()
    elif "1QHGhwasONr_Sxg_jMk3Jtqa6wn7iISVx" in inp:
        print(sendFrom('Anonymous') + "Interesting.. you found something")
        sleep(2)
        print(sendFrom('Anonymous') + "As you tought, i keep the third fragment on drive")
        sleep(2)
        print(sendFrom('Anonymous') + "Find a way to open it!")
        sleep(3)
        print(sendFrom('Anonymous') + "Tell me when you got the decoded fragment!")
        sleep(1.5)

        inp = input(sendFrom('Me'))
        sleep(3)

        if inp != "the_b3st_0ne_":
            fail()
    elif inp != "the_b3st_0ne_":
        fail()
    
    print(sendFrom('Anonymous') + "You cooked this challenge! As i said before, i'll give you a last fragment")
    sleep(2)
    print(sendFrom('Anonymous') + "61 33 68 76 6A 33 32 71 38")
    sleep(1.5)
    print(sendFrom('Anonymous') + "last decode!")
    sleep(1.5)

    inp = input(sendFrom('Me'))
    sleep(2)

    if inp == "a3hvj32q8":
        print(sendFrom('Anonymous') + "Excelent! Here's your reward")
        sleep(2)
        print(sendFrom('Anonymous') + "ctfgrf24{r3gistr4tion_t0_f1nd_the_b3st_0ne_a3hvj32q8}")
        sleep(2)
        print(sendFrom('Anonymous') + "We'll anounce about your membership in no time;)")
        sleep(1)
        print(sendFrom('Anonymous') + "See you")
        sleep(1.5)
        print('\n\033[31mConnection Closed!\033[0m')
        exit()
    else:        
        fail()


if __name__ == "__main__":
    main()
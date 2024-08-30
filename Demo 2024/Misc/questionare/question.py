print("""Selamat datang di questionare yang teman ku buat, handy ;)
Silahkan jawab pertanyaan - pertanyaan yang ada di bawah ini, andd goodluck!
      """)

def salah():
    print("Wroong!")
    exit("Byee!")

flag = "GRF24{4b4ng_k3b4nyakan_metalc0re_0xdd27e}"

if input("Tell me one of the metalcore band from Britain!:\n").lower() == "architects":
    print("Yeees correct!")
    if input("One of the personel died of cancer? (related to prev question):\n").lower() == "tom searle":
        print("Correct!")
        if input("The name of the album from Architects that has black and white cover:\n").lower() == "all our gods have abandoned us":
            print("Correct!")
            if input("Our eyes are open, but we're not listening\n").lower() == "royal beggars":
                print("Correct!")
                print("Congrats for making to the end of the question!")
                print(flag)
            else:
              salah()
        else:
            salah()
    else:
        salah()
else:
    salah()

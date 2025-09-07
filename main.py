while True:
    print("Selected Your Option : \n\t1)Encrypt\n\t2)Decrypt\n\t3)Exit")
    choice = input("Your Select :")
    if choice == "1":
        plain_text = input("text :")
        encrypted_text = ""
        for ch in plain_text:
            x = ord(ch) * 2 + 5
            encrypted_text = encrypted_text + chr(x)
        print("encrypted text : ", encrypted_text)
        print("*" * 40 + "\n")
    elif choice == "2":
        encrypted_text = input("encrypted text :")
        plain_text = ""
        for ch in encrypted_text:
            x = (ord(ch) - 5) // 2
            plain_text = plain_text + chr(x)
        print("plain text : ", plain_text)
        print("*" * 40 + "\n")
    elif choice == "3":
        print("GoodBye:)")
        break
    else:
        print("Exited!")

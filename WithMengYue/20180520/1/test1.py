
if __name__ == "__main__":
    print("PROGRAM BEGIN!")
    while(1):
        a = input("Input One English Name: ")
        if a == "EXIT":
            print("User have input [EXIT]!")
            break
        if a == "":
            print("User have input [BLANK]!")
            break
        b = ""
        for i in a:
            b = b + i.lower()
        print("[ORIGIN    NAME] : " + a)
        print("[FORMATTED NAME] : " + b[0].upper() + b[1:])
    print("PROGRAM END!")


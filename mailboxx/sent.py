def sent(id_active, ask_pc):
    ct = 0
    with open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\sent\\{id_active}.txt", "r") as x:
        data = x.readlines()
        for line in data:
            if line == "\n":
                ct += 1

    if ct == 0:
        print("\nZero Sent Mails")
    else:
        print("\nNo of sent emails:", ct)
        choice = input("Do you wish to see all sent mails? (y/n): ")
        print()
        if choice.lower() == "y":
            for line in data:
                print(line[:len(line)-1])
        else:
            print()

def drafts(id_active, ask_pc, mailbox, user_info):
    ct = 0
    nlist = []
    with open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\drafts\\{id_active}.txt", "r") as w:
        data = w.readlines()
        for i in range(len(data)):
            if data[i] == "\n":
                ct = ct + 1
                pin = i
                nlist.append(pin)
            else:
                continue

    if ct == 0:
        print("\nZero emails in Drafts")
    else:
        print("\nNo of drafted emails:", ct)
        print("1. View drafts")
        print("2. Send a draft")
        print("Press anything else to exit")
        while True:
            choice = input("\nEnter choice: ")
            print()
            if choice == "1":
                for j in data:
                    print(j[:len(j)-1])
            elif choice == "2":
                print()
                for j in data:
                    print(j[:len(j)-1])
                num = int(input("Enter the No. of the email to send: "))
                data.pop(nlist[num-1])
                nlist.pop(num-1)

                receiver = data[nlist[num-1]+2]
                receiver = receiver[26:]
                receiver = receiver[:len(receiver)-11]
                user = user_info.find_one({"user_name": receiver})
                id_receiver = user["_id"]

                mailbox.update_one({"_id": id_active}, {"$inc": {"sent": 1}})
                mailbox.update_one({"_id": id_receiver}, {"$inc": {"inbox": 1}})

                with open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\sent\\{id_active}.txt", "w") as x:
                    for line in data[:nlist[num-1]] + data[nlist[num-1]+2:]:
                        x.write(line)

                print()
                break
            else:
                exit()

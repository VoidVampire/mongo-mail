def inbox(id_active, ask_pc):
    ct = 0
    nlist = []
    with open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\inbox\\{id_active}.txt", "r") as x:
        data = x.readlines()
        for i in range(len(data)):
            if data[i] == "\n":
                ct = ct + 1
                pin = i
                nlist.append(pin)
            else:
                continue

    if ct == 0:
        print("\nZero Mails in Inbox")
    else:
        print("\nNo of received emails:", ct)
        print("1. View all Mails")
        print("2. View mails by a particular sender")
        print("3. Delete Mails")
        print("Press anything else to exit")
        while True:
            choice = input("\nEnter choice: ")
            if choice == "1":
                print()
                for j in data:
                    print(j[:len(j)-1])
            elif choice == "2":
                print()
                count_sender = 0
                user_list = []
                user_sender = input("Enter username of a sender: ")

                for k in range(len(nlist)):
                    if data[nlist[k]] == "Sender's Email Address: " + user_sender + "@ymail.com" + "\n":
                        count_sender += 1
                        if k == len(nlist) - 1:
                            user_list.append(data[nlist[k]:])
                        else:
                            user_list.append(data[nlist[k]:nlist[k+1]])

                print()
                print("Emails received by " + user_sender + ":", count_sender)
                for m in user_list:
                    print()
                    for n in m:
                        print(n[:len(n)-1])
            elif choice == "3":
                print()
                for j in data:
                    print(j[:len(j)-1])
                num = int(input("Enter the No. of the email to delete: "))
                data.pop(nlist[num-1])
                nlist.pop(num-1)

                with open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\inbox\\{id_active}.txt", "w") as q:
                    for line in data:
                        q.write(line)
                print("Deleted Mail Successfully.....")
            else:
                exit()
def compose(id_active, user_active, ask_pc, db):
    mailbox = db["mailbox"]
    user_info = db["user_info"]

    receiver = input("\nEnter recipient's username: ")
    if user_info.count_documents({"user_name": receiver}) == 0:
        print("Username not found.")
        exit()
    
    user = user_info.find_one({"user_name": receiver})
    id_receiver = user["_id"]
    sub = input("Enter subject: ")
    body = input("Enter body: ")
    sender = "Sender's Email Address: " + user_active + "@ymail.com" + "\n"
    receiver = "Receiver's Email Address: " + receiver + "@ymail.com" + "\n"
    sub = "Subject: " + sub + "\n"
    body = "Body: " + body + "\n"
    message = sender + receiver + sub + body + "\n"
    
    while True:
        print("1. Save as Draft")
        print("2. Send it")
        print("3. Discard")
        confirm = input("\nEnter choice: ")
        if confirm == "1":
            mailbox.update_one({"_id": id_active}, {"$inc": {"drafts": 1}})
            with open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\drafts\\{id_active}.txt","a") as x:
                x.write(message)
                print("Saved in Draft")
                break
        elif confirm == "2":
            mailbox.update_one({"_id": id_active}, {"$inc": {"sent": 1}})
            mailbox.update_one({"_id": id_receiver}, {"$inc": {"inbox": 1}})
            with open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\sent\\{id_active}.txt", "a") as y, open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\inbox\\{id_receiver}.txt", "a") as q:
                y.write(message)
                q.write(message)
                print("Sent successfully...")
                break
        elif confirm == "3":
            print("Discarded")
            break
        else:
            print("Invalid Input")
            choice_2 = input("Press 1 to try again or anything to exit: ")
            if choice_2 == "1":
                continue
            else:
                exit()




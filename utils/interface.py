from mailboxx.compose import compose
from mailboxx.drafts import drafts
from mailboxx.inbox import inbox
from mailboxx.sent import sent
from mailboxx.trash import trash
from utils.close import close

def interface(id_active, user_active, ask_pc, db, mailbox, user_info):
    print("This is Your Mail")
    print("1. Compose email")
    print("2. Inbox")
    print("3. Sent Mails")
    print("4. Drafts")
    print("5. Trash")
    print("6. Exit")
    print("7. CLOSE ACCOUNT")
    while True:
        print()
        choice_3 = input("Enter number what to view (6 - exit):")
        if choice_3 == "1":
            compose(id_active, user_active, ask_pc, db)
        elif choice_3 == "2":
            inbox(id_active, ask_pc, user_info)
        elif choice_3 == "3":
            sent(id_active, ask_pc)
        elif choice_3 == "4":
            drafts(id_active, ask_pc, mailbox, user_info)
        elif choice_3 == "5":
            trash(id_active, ask_pc)
        elif choice_3 == "6":
            exit()
        elif choice_3 == "7":
            close(id_active, user_info)
            break
        else:
            print("Invalid Input")
            choice_4 = input("Press 1 to try again or anything to exit :")
            if choice_4 == "1":
                continue                        
            else:
                exit()

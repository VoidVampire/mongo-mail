from database.database_connection import connect_to_database
from pprint import pprint

db = connect_to_database()
mailbox = db["mailbox"]
user_info = db["user_info"]

def generate_report():
    print("1. Generate Mailbox")
    print("2. Users' info")
    choice = input("Choose: ")
    
    if choice == "1":
        no = mailbox.count_documents({"closing_date": None})
        num = mailbox.count_documents({})
        ch = int(input("Press 1 to get info of 1 user / Press 2 to get info of all users"))
        print("No of active users:", no)    
        print("+-------------------------------------------------------------------------------------------------------------------")
        if ch == 1:
            name = input("Enter id to find: ")
            table = mailbox.find_one({"_id": name})
            pprint(table)
        elif ch == 2:
            table = mailbox.find()
            for row in table:
                pprint(row)        
        print("+-------------------------------------------------------------------------------------------------------------------")
    
    elif choice == "2":
        no = user_info.count_documents({"closing_date": None})
        num = user_info.count_documents({})
        ch = int(input("Press 1 to get info of 1 user / Press 2 to get info of all users"))
        print("No of active users:", no)    
        print("+-------------------------------------------------------------------------------------------------------------------")
        if ch == 1:
            name = input("Enter username to find: ")
            table = user_info.find_one({"user_name": name})
            pprint(table)
        elif ch == 2:
            table = user_info.find()
            for row in table:
                pprint(row)        
        print("+-------------------------------------------------------------------------------------------------------------------")
    
    else:
        exit()

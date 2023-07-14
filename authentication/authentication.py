from database.database_connection import connect_to_database
from datetime import datetime
import getpass
db = connect_to_database();
ask_pc = getpass.getuser()


def login_page():
    user_info = db["user_info"]
    data = list(user_info.find())
    if len(data) == 0:
        print("No accounts are registered yet...")
        exit()
    else:
        while True:
            while True:
                u1 = input("\nEnter Username: ")
                if user_info.count_documents({"user_name": u1}) > 0:
                    break
                else:
                    print("Username not found.")
                    choice_1 = input("Press 1 to try again or anything to exit: ")
                    if choice_1 == "1":
                        continue
                    else:
                        exit()

            user = user_info.find_one({"user_name": u1})
            p1 = getpass.getpass("Enter password: ")
            if p1 == user["password"]:
                t1 = input("Enter Type: ")
                if t1 == user["type"]:
                    id_active = user["_id"]
                    user_active = user["user_name"]
                    passwd_active = user["password"]
                    type_active = user["type"]
                    print("Login Successful\n\n")
                    break
                else:
                    print("Username, password, and type of account don't match.")
            else:
                print("Username and password don't match!")
    return id_active, user_active, passwd_active, type_active

def register_page():
    user_info = db["user_info"]
    mailbox = db["mailbox"]
    
    data = list(user_info.find())
    if len(data) == 0:
        y_id = 1
    else:
        x = data[-1]
        y_id = x["_id"] + 1
        
    fn = input("Enter First Name: ")
    mn = input("Enter Middle Name: ")
    ln = input("Enter Last Name: ")
    dob = input("Enter DOB (yyyy-mm-dd): ")
    un = input("Enter desired username: ")
    pwd = input("Enter password: ")
    ty = input("Enter type of Account (N - Normal/B - Business): ")
    
    user_info.insert_one({
        "_id": y_id,
        "first_name": fn,
        "middle_name": mn,
        "last_name": ln,
        "date_of_birth": dob,
        "user_name": un,
        "password": pwd,
        "type": ty,
        "opening_date": datetime.now(),
        "opening_time": datetime.now(),
        "closing_date": None,
        "closing_time": None
    })
    
    mailbox.insert_one({
        "_id": y_id,
        "inbox": 0,
        "sent": 0,
        "drafts": 0,
        "trash": 0
    })
    
    print("\nAccount Registered Successfully")
    fi = open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\inbox\\{y_id}.txt", "a")
    fi.close()
    fd = open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\drafts\\{y_id}.txt", "a")
    fd.close()
    fs = open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\sent\\{y_id}.txt", "a")
    fs.close()
    ft = open(f"C:\\Users\\{ask_pc}\\OneDrive\\Desktop\\project\\trash\\{y_id}.txt", "a")
    ft.close()

from authentication.authentication import register_page, login_page
from utils.report import generate_report
from utils.interface import interface
from database.database_connection import connect_to_database
import getpass

ask_pc = getpass.getuser()
db = connect_to_database()
mailbox = db["mailbox"]
user_info = db["user_info"]

print("\nWelcome to YMail Services")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Reports Generation")
    print("4. Delete records")
    print("5. Exit")

    choice = input("Enter choice: ")
    
    if choice == "1":
        register_page()
    elif choice == "2":
        id_active, user_active, passwd_active, type_active = login_page()
        interface(id_active, user_active, ask_pc, db, mailbox, user_info)
    elif choice == "3":
        generate_report()
    elif choice == "4":
        name = input("Enter username to delete :")
        idx = input("Enter id to delete :")
        user_info.delete_many({"user_name": name})
        mailbox.delete_many({"_id": idx})
    elif choice == "5":
        print("\nGoodbye!")
        break
    else:
        print("Invalid Input")

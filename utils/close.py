def close(id_active, user_info):
    user_info.update_one({"_id": id_active}, {"$currentDate": {"closing_date": True}})
    user_info.update_one({"_id": id_active}, {"$currentDate": {"closing_time": True}})
    print("\n--- ACCOUNT CLOSED ---")
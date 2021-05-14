user_list = []
import pandas as pd
import hashlib
import csv


class User:
    def __init__(self, username, password, role, flag=1):
        """
        :param username:username
        :param password:password
        :param role:role of user is admin, or....
        :param flag: the user is active or not
        """
        self.username = username
        self.password = password
        self.role = role
        self.flag = flag

    @staticmethod
    def register():
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        lst_username = list(df_account["username"])

        username = input("enter your username:")
        if username in lst_username:
            print("valid username")
        password = input("enter your password:")
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
        obj_user = User(username, hash_password)

        row_account = [[obj_user.username, obj_user.password]]
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)






    def discount_status(self):
        for user in user_list:

            if user.role == "admin":
                discount_status = "admin_discount"
            elif user.role == "student":
                discount_status = "student_discount"
            elif user.role == "employee":
                discount_status = "employee_discount"
            else:
                discount_status = "common_person_discount"
import sys
from user import Admin,Customer,User
from event1 import Event, show_event,choose_event,update_capacity

def main():
    menue()

def menue():
    print("+++++++++++++++++++++++++++++welcome to online sale ticket++++++++++++++++++++++++++++++\n"
          "                                                                                           \n"
          "               1-login:\n"
          "               2-register:\n"
          "               3-exist:\n"
          )
    choice = int(input("please enter your choice :"))
    if choice == 1:
        print("1-admin:\n"
              "2-customer:\n")
        user_menue = int(input("enter your choice :"))
        if user_menue == 1:
            security = input("enter admin security code:")
            if security == "1234":
                admin_menue()
            else:
                print("sorry! your security code is wrong! you can not login as an admin!")
        elif user_menue == 2:
            customer_menue()
        else:
            menue()
    elif choice == 2:
        users = Customer.sign_up()

    elif choice == 3:
        sys.exit()
    else:
        menue()


def admin_menue():
    admin1 = Admin.sign_in()
    menu_admin = int(input("Enter\n"
                            "1-create event\n"
                            "2-show event\n"
                            "3-choose event\n"
                            "4-chang total capacity\n"
                            "5-buy ticket\n "
                            "6-Back to previous menu\n "
                            "Enter here:"))

    if menu_admin == 1:
        event = Event.event_()
    elif menu_admin == 2:
        show_event()
    elif menu_admin == 3:
        event_id = input("Enter id of event you want to select:")
        choose_event(event_id)
    elif menu_admin == 4:
        update_capacity()
    # elif menu_admin == 5:
    #     Customer.buy_ticket()
    elif menu_admin == 6:
        menue()
    else:
        print("The entered option is not correct!!")
        admin_menue()



def customer_menue():
    Customer.sign_in()
    customer_m = int(input("Enter\n"
                            "1-show event\n"
                            "2-buy ticket\n "
                            "6-Back to previous menu\n "
                            "Enter here:"))

    if customer_m == 1:
        show_event()
    # elif customer_m == 2:
    #     user.Customer.buy_ticket()
    # elif customer_m == 3:
    #     menue()
    else:
        print("The entered option is not correct!!")
        customer_menue()



if __name__ == '__main__':
    main()







#
#
#
# def menu():
#     print("*********Welcome to Online sales of tickets***********")
#
#     print("""
#                       A: Sign up
#                       B: Login
#                       Q: Quit
#
#                     """)
#     try:
#         choice = input("Please Enter Choice number:")
#         if choice == 1:
#             if User.register() == True:
#                 menu()
#         elif choice == "B" or choice == "b":
#             try:
#                 user_name, password = User.login()
#                 if user_name == 'Admin':
#                     admin_menu(user_name, password)
#                 else:
#                     user_menu(user_name, password)
#             except TypeError:
#                 menu(import sys
# from user import Admin,Customer,User
# from event1 import Event, show_event,choose_event,update_capacity
#
# def main():
#     menue()
#
# def menue():
#     print("+++++++++++++++++++++++++++++welcome to online sale ticket++++++++++++++++++++++++++++++\n"
#           "                                                                                           \n"
#           "               1-login:\n"
#           "               2-register:\n"
#           "               3-exist:\n"
#           )
#     choice = int(input("please enter your choice :"))
#     if choice == 1:
#         print("1-admin:\n"
#               "2-customer:\n")
#         user_menue = int(input("enter your choice :"))
#         if user_menue == 1:
#             security = input("enter admin security code:")
#             if security == "1234":
#                 admin_menue()
#             else:
#                 print("sorry! your security code is wrong! you can not login as an admin!")
#         elif user_menue == 2:
#             customer_menue()
#         else:
#             menue()
#     elif choice == 2:
#         users = Customer.sign_up()
#
#     elif choice == 3:
#         sys.exit()
#     else:
#         menue()
#
#
# def admin_menue():
#     admin1 = Admin.sign_in()
#     menu_admin = int(input("Enter\n"
#                             "1-create event\n"
#                             "2-show event\n"
#                             "3-choose event\n"
#                             "4-chang total capacity\n"
#                             "5-buy ticket\n "
#                             "6-Back to previous menu\n "
#                             "Enter here:"))
#
#     if menu_admin == 1:
#         event = Event.event_()
#     elif menu_admin == 2:
#         show_event()
#     elif menu_admin == 3:
#         event_id = input("Enter id of event you want to select:")
#         choose_event(event_id)
#     elif menu_admin == 4:
#         update_capacity()
#     # elif menu_admin == 5:
#     #     Customer.buy_ticket()
#     elif menu_admin == 6:
#         menue()
#     else:
#         print("The entered option is not correct!!")
#         admin_menue()
#
#
#
# def customer_menue():
#     Customer.sign_in()
#     customer_m = int(input("Enter\n"
#                             "1-show event\n"
#                             "2-buy ticket\n "
#                             "6-Back to previous menu\n "
#                             "Enter here:"))
#
#     if customer_m == 1:
#         show_event()
#     # elif customer_m == 2:
#     #     user.Customer.buy_ticket()
#     # elif customer_m == 3:
#     #     menue()
#     else:
#         print("The entered option is not correct!!")
#         customer_menue()
#
#
#
# if __name__ == '__main__':
#     main()
#
#
#
#
#
#
#
#
#
#
# def menu():
#     print("*********Welcome to Online sales of tickets***********")
#
#     print("""
#                       A: Sign up
#                       B: Login
#                       Q: Quit
#
#                     """)
#     try:
#         choice = input("Please Enter Choice number:")
#         if choice == 1:
#             if User.register() == True:
#                 menu()
#         elif choice == "B" or choice == "b":
#             try:
#                 user_name, password = User.login()
#                 if user_name == 'Admin':
#                     admin_menu(user_name, password)
#                 else:
#                     user_menu(user_name, password)
#             except TypeError:
#                 menu()
#         elif choice == "Q" or choice == "q":
#             sys.exit()
#         else:
#             raise TypeError
#
#     except TypeError:
#
#         print("just choice A, B and Q")
#         logger.my_logger.error('the choice of menu was entered incorrectly', exc_info=True)
#         menu())
#         elif choice == "Q" or choice == "q":
#             sys.exit()
#         else:
#             raise TypeError
#
#     except TypeError:
#
#         print("just choice A, B and Q")
#         logger.my_logger.error('the choice of menu was entered incorrectly', exc_info=True)
#         menu()
from colorama import Fore
import sys
from user import Admin, Customer, User
import ticket
from event1 import Event, show_event, choose_event, update_capacity


def main():
    menue()


def menue():
    print(Fore.YELLOW+"welcome to online sale ticket\n"
          "                                                                                           \n"
          "               1-login:\n"
          "               2-register:\n"
          "               3-exist:\n"
          )
    choice = int(input("please enter your choice :"))
    if choice == 1:
        print(Fore.YELLOW+"1-admin:\n"
                          "2-customer:\n")
        user_menue = int(input("enter your choice :"))
        if user_menue == 1:
            security = input("enter admin security code:")
            if security == "1234":
                admin1 = Admin.sign_in()
                if admin1 == 0:
                    # print("you have entered wrong password and username")
                    menue()
                else:
                    admin_menu()
            else:
                print(Fore.YELLOW+"sorry! your security code is wrong! you can not login as an admin!")
                menue()
        elif user_menue == 2:
            user = Customer.sign_in()
            if user == 0:
                menue()
            else:
                customer_menue()

        else:
            menue()
    elif choice == 2:
        Customer.sign_up()
        menue()

    elif choice == 3:
        sys.exit()
    else:
        menue()


def admin_menu():

    while True:
        menu_admin = None
        try:
            menu_admin = int(input("Enter\n"
                                    "1-create event\n"
                                    "2-show event\n"
                                    "3-choose event\n"
                                    "4-chang total capacity\n"
                                    "5-buy ticket\n "
                                    "6-Back to previous menu\n "
                                    "Enter here:"))
            assert menu_admin in range(1, 7)
        except ValueError:
            print(Fore.YELLOW+'you should enter a number between 1 to 6.')
        except AssertionError:
            print(Fore.YELLOW+'you should enter a number between 1 to 6.')

        if menu_admin == 1:
            event = Event.event_()
        elif menu_admin == 2:
            show_event()
        elif menu_admin == 3:
            event_id = input("Enter id of event you want to select:")
            choose_event(event_id)
        elif menu_admin == 4:
            update_capacity()
        elif menu_admin == 5:
            ticket.Customer_.buy_ticket()
        elif menu_admin == 6:
            menue()
        else:
            print(Fore.RED+"The entered option is not correct!!")
            admin_menu()


def customer_menue():

    customer_m = int(input("Enter\n"
                            "1-show event\n"
                            "2-buy ticket\n "
                            "3-Back to previous menu\n "
                            "Enter here:"))

    if customer_m == 1:
        show_event()
        customer_menue()
    elif customer_m == 2:
        ticket.Customer_.buy_ticket()
        customer_menue()
    elif customer_m == 3:
        menue()
    else:
        print("The entered option is not correct!!")
        customer_menue()



if __name__ == '__main__':
    main()








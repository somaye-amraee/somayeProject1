import csv
class Person:
    def __init__(self, ticket_Number):
        self.ticket_Number = ticket_Number

    def discount_status(self, user):
        if self.user == "admin":
            discount_status = "admin_discount"
        elif self.user == "student":
            discount_status = "student_discount"
        elif self.user == "employee":
            discount_status = "employee_discount"
        else:
            discount_status = "common_person_discount"

    def __str__(self, ticket_Number):
        return ""

class Admin(Person):
    def __init__(self, ticket_number):
    super().__init__(self, ticket_Number)
    self.ticket_number = ticket_number

    def __str__(self):
        ticket_price = ticket_price * ticket_Number

        return f'ticket_price: {self.ticket_price}'

class Student(Person):
    def __init__(self, ticket_Number):
    super().__init__(self, ticket_Number)
    self.ticket_Number = ticket_Number

class Employee(Person):
    def __init__(self, ticket_Number):
class Common_User(Person):
    def __init__(self, ticket_Number):


class Event:
    def __init__(self, date, time, place, total_capacity, event_title, updated_capacity, bought_tickets = None,
                 ticket_price):
       """"""


        self.date = date
        self.time = time
        self.place = place
        self.total_capacity = total_capacity
        self.bought_tickets = bought_tickets
        self.ticket_price = ticket_price
        self.event_title = event_title
        self.updated_capacity = updated_capacity


        """
            this function prints the number of pages read and the number of pages remaining
            And set progress for every object
        """
        try:
            assert n + self.bought_tickets <= self.total_capacity
            self.bought_tickets += n
            remained_capacity = self.total_capacity - self.bought_tickets

            self.updated_capacity = self.remained_capacity

        except AssertionError:
            print("You can not purchase tickets more than total_capacity.")

        else:
            if self.bought_tickets == self.total_capacity:
                print("Completed")
            else:
                print(f"There is {self.remained_capacity} room from'{self.event_title}'.")


@staticmethod
def get_info():
    """
        this function get info from input for every book and initialize it
        media contain info of book
    """
    title, author, publish_year, pages, language, price = \
        input("*Enter* title| author| publish_year| pages| language| price: \n").split('|')
    media = Book(title, author, publish_year, int(pages), language, price)
    return media


def __str__(self):
    return f'\nTitle : {self.title} \nAuthor(s) : {self.author} \nPublish_year : {self.publish_year}' \
           f'\nPages : {self.pages} \nLanguage : {self.language} \nPrice : {self.price} $'


def __lt__(self, other):
    return self.price < other.price


class Cinema (Event):
    def __init__(self, date, time, place, total_capacity, reminded_capacity,
                 ticket_price, user, movie_genera):

        super().__init__(date, time, place, total_capacity, reminded_capacity,
                 ticket_price, user)
        self.movie_genera = movie_genera




class Theater(Cinema):
    pass
class Concert(Cinema):
    pass

while True:
    choice = input("enter your favorite event from Cinema, Theater and Concert")
    pass

import pandas as pd
import csv

class Event:
    event_list = []
    def __init__(self, id_event, name_event, date_event, time_event, place_event, cost_event, total_capacity,
                 flag_event=1):
        """
        this class create a event buy admin
        id_event:
        name_event: name of event
        date_event: date of event
        time_event: time of event
        place_event: place of event
        cost_event: cost of event
        total_capacity: total capacity
        mod_total_capacity: mod of capacity
        flag_event: event live or not
        """
        self.id_event = id_event
        self.name_event = name_event
        self.date_event = date_event
        self.time_event = time_event
        self.place_event = place_event
        self.cost_event = cost_event
        self.total_capacity = total_capacity
        self.mod_total_capacity = self.total_capacity
        self.flag_event = flag_event


    @staticmethod
    def event_():
        path_file = "event.csv"
        def_event = pd.read_csv(path_file)

        id_event = input(" enter id_event: ")
        name_event = input(" enter name_event: ")
        date_event = int(input(" enter date_event: "))
        time_event = int(input(" enter time_event: "))
        place_event = input("enter place_event: ")
        cost_event = int(input("enter cost_event: "))
        total_capacity = int(input("enter total_capacity: "))
        flag_event = int(input("enter flag_event"))

        obj_event = Event(id_event, name_event, date_event, time_event, place_event, cost_event, total_capacity,
                          flag_event)
        Event.event_list.append(obj_event)
        path_file = "event1.csv"
        row = [[id_event,name_event,date_event,time_event,place_event,cost_event,total_capacity,flag_event]]
        with open(path_file, 'a', newline='') as csv_show_event:
            csv_writer = csv.writer(csv_show_event)
            csv_writer.writerows(row)
        return obj_event

# event1=Event.event_()

def show_event():
    path_file = "event.csv"
    file = open(path_file)
    df_show_event = pd.read_csv(file)
    for index, row in df_show_event.iterrows():
        print(f"id_event :{row['id_event']}\n"
        f"name_event :{row['name_event']}\n"
        f"date_event :{row['date_event']}\n"
        f"time_event :{row['time_event']}\n"
        f"cost_event :{row['cost_event']}\n"
        f"total_capacity :{row['total_capacity']}\n"
        f"flag_event :{row['flag_event']}\n")


# show_event()


def choose_event(item):
    path_file = "event.csv"
    file = open(path_file)
    df_show_event = pd.read_csv(file)
    for index, row in df_show_event.iterrows():
        if row['id_event'] == item:
            print(f"id_event :{row['id_event']}\n"
            f"name_event :{row['name_event']}\n"
            f"date_event :{row['date_event']}\n"
            f"time_event :{row['time_event']}\n"
            f"cost_event :{row['cost_event']}\n"
            f"total_capacity:{row['total_capacity']}\n"
            f"flag_event :{row['flag_event']}\n")


choose = input("Enter\n"
               "1-create event\n"
               "2-show event\n"
               "3-choose event\n"
               "Enter here:")
if choose =='1':
    event1 = Event.event_()
elif choose == '2':
    show_event()
elif choose == '3':
    event_id = input(" Enter id of event you want to select")
    choose_event('id_event')








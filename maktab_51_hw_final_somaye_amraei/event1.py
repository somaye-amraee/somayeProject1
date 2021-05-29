import pandas as pd
import csv

import logger


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
        self.mod_total_capacity = total_capacity
        self.flag_event = 1


    @staticmethod
    def event_():
        path_file = "event.csv"
        df_id_event = pd.read_csv(path_file)
        list_id_event = []
        while True:

            id_event = input(" enter id_event: ")
            if id_event in list_id_event:
                print("the id_event is already taken")
            elif id_event == "":
                print("ERROR: your input id is blank")
            else:
                list_id_event.append(id_event)
                break

        name_event = input(" enter name_event: ")
        date_event = input(" enter date_event: ")
        time_event = input(" enter time_event: ")
        place_event = input("enter place_event: ")
        cost_event = input("enter cost_event: ")
        total_capacity = input("enter total_capacity: ")
        flag_event = 1




        obj_event = Event(id_event, name_event, date_event, time_event, place_event, cost_event, total_capacity,flag_event)
        Event.event_list.append(obj_event)
        # path_file = "event.csv"
        row = [[id_event,name_event,date_event,time_event,place_event,cost_event,total_capacity, obj_event.mod_total_capacity,flag_event]]
        with open(path_file, 'a', newline='') as csv_show_event:
            csv_writer = csv.writer(csv_show_event)
            csv_writer.writerows(row)
        # logger.info_logger.info(f'{name_event} is created')
        return obj_event

# event1=Event.event_()

def show_event():
    path_file = "event.csv"
    # file = open(path_file)
    df_show_event = pd.read_csv(path_file)
    print(df_show_event)



def choose_event(ev_id):
    with open("event.csv", 'r') as reader_obj:
        csv_reader = csv.DictReader(reader_obj)
        # line_count = 0
        for row in csv_reader:
            if row['id_event'] == str(ev_id):
                for key, value in row.items():
                    print(value, end='  ')
                # print(row)





def update_capacity():
    update_total_capacity = pd.read_csv("event.csv")
    print(update_total_capacity)
    location = 0
    eventID = input('Enter the id here:')
    with open("event.csv", 'r') as my_file:
        csv_reader = csv.DictReader(my_file)
        for row in csv_reader:
            if row['id_event'] == eventID:
                capacity = input('Enter capacity:')
                row['total_capacity'] = capacity
                update_total_capacity.loc[location, 'total_capacity'] = capacity
                update_total_capacity.to_csv("event.csv", index=False)
            location += 1








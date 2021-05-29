import pandas as pd
def check_id_event():

    path_file = "event.csv"
    df_id_event = pd.read_csv(path_file)
    list_id_event = list(df_id_event['id_event'])
    print(list(df_id_event['id_event']))
    while True:
        id_event = int(input(" enter id_event: "))

        if id_event in list_id_event:
            print("the id_event is already taken")
        elif id_event == "":
            print("ERROR: your input id is blank")
        else:
            list_id_event.append(id_event)
            break


check_id_event()
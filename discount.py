import csv

class Discount:
    """
    this class is created for presenting discount status according to each user by the admin
    """

    def __init__(self, id_discount, name_discount, percent):
        """
        id_discount: id for discount
        name_discount: name for discount
        percent: percentage of discount
        """
        self.id_discount = id_discount
        self.name_discount = name_discount
        self.percent = percent
id_discount = 0
id_discount +=1
obj_dis = Discount("student_dis", 50)
obj_event = Discount("employ_dis", 1)


def create_discount(self):
    """
    this method create a discount
    return: an object
    """
    file_path = "discount.csv"
    row = [[self.id_discount, self.name_discount, self.percent]]
    with open(file_path, 'a', newline='') as csv_discount:
        # creating a csv writer object
        csv_writer = csv.writer(csv_discount)
        # writing the data row
        csv_writer.writerows(row)

    def __str__(self):
        """
        this method return a successfully message for creation of discount
        return: str
        """
        return "discount possibility is seccessful"
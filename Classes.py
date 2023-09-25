class Order:
    def __init__(self, order_num, coffee_name, coffee_temp, special_requests, coffee_price):
        try:
            self.order_num = int(order_num)
        except TypeError:
            self.order_num = "error_type_required INT"

        try:
            self.coffee_name = str(coffee_name)
        except TypeError:
            self.coffee_name = "error_type_required STRING"

        try:
            self.coffee_temp = str(coffee_temp)
        except TypeError:
            self.coffee_temp = "error_type_required STRING"

        self.special_requests = special_requests

        try:
            self.coffee_price = float(coffee_price)
        except TypeError:
            self.coffee_price = "error_type_required NUMBER"

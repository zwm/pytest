class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print("----------DESCRIBE RESTAURANT---------------")
        print("Name: %s" % self.restaurant_name)
        print("Type: %s" % self.cuisine_type)
        print("Numb: %d" % self.number_served)

    def open_restaurant(self):
        print("%s is OPEN!" % self.restaurant_name)

    def set_number_served(self, number_served=0):
        self.number_served = number_served
        print("Number Served:%d" % self.number_served)

    def increment_number_served(self):
        self.number_served = self.number_served + 1

res1 = Restaurant("McDonald's", "fast-food")
res1.describe_restaurant()
res1.open_restaurant()
res1.set_number_served(100)
res1.describe_restaurant()
res1.increment_number_served()
res1.describe_restaurant()

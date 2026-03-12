class Customer:
    def set_name(self,New_name):
        self.Name=New_name

    def give_name(self):
        print("My name is " + self.Name)

customer=Customer()
customer.set_name("John Doe")
customer.give_name()
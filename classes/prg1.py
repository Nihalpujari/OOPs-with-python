class Customers:
    def identify(self, name):
        print("My name is " + name)
customer=Customers()
customer.identify("John Doe")

# We can call the method using the class name by passing the object manually as 'self'.
Customers.identify(customer,"nihal")
class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to Cart",self.name,self.lastname)

customer1 = Customer()
customer1.name = "Pon"
customer1.lastname = "SaToRu"
customer1.age = 21
customer1.addCart()

customer2 = Customer()
customer2.name = "Tar"
customer2.lastname = "Naga"
customer2.age = 20
customer2.addCart()
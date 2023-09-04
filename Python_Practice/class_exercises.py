#9.1, 9.4

#class Restaurant():

    #def __init__(self, restaurant_name, cuisuine_type):
        #self.restaurant_name = restaurant_name
        #self.cuisine_type = cuisuine_type
        #self.number_served = 0

    #def describe_restaurant(self):
        #print(self.restaurant_name)
        #print(self.cuisine_type)

    #def open_restaurant(self):
        #print(f"{self.restaurant_name} is open!")

    #def read_number_served(self):
        #print(f"This restaurant currently has {self.number_served} customers!")

    #def set_number_served(self):
        #self.number_served = int(input("How many customers has the restaurant served? "))
        #print(f"You have served {self.number_served} customer(s)")

    #def increment_number_served(self, customer):
        #print(f"Busy day! Incrementing {customer} customers!")
        #self.number_served += customer
        


#restaurant = Restaurant("Jack's Diner", "Fish & Chips")
#restaurant.read_number_served()
#restaurant.set_number_served()
#restaurant.read_number_served()
#restaurant.increment_number_served(100)
#restaurant.read_number_served()

#9.2

#restaurant = Restaurant("Jack's Diner", "Fish & Chips")
#print(restaurant.restaurant_name)

#restaurant2 = Restaurant("Other restaurant", "Indian")
#restaurant2.describe_restaurant()

#restaurant3 = Restaurant("Final restaurant", "Fast food")
#restaurant3.describe_restaurant()

#9.3, 9.5

#class User():

    #def __init__(self, first_name, last_name, age, hobby, login_attempts):
        #self.first_name = first_name
        #self.last_name = last_name
        #self.age = age
        #self.hobby = hobby
        #self.full_name = f"{self.first_name} {self.last_name}"
        #self.login_attempts = login_attempts



    #def describe_user(self):
        #print(f"\nUser's full name is: {self.full_name}\nUser's age is: {self.age}\nUser's favourite hobby is: {self.hobby}")


    #def greet_user(self):
        #print(f"\nHello {self.full_name}! Nice to see you again!\n")
    
    #def increment_login_attempts(self, inc):
        #inc = self.login_attempts + 1
        #print(f"\nIncrementing... New login attempt count: {inc}\n")
    
    #def reset_login_attempts(self):
        #self.login_attemps = 0
        #print(f"Reset your login attempts. Your login attempts is now {self.login_attemps}\n")

#new_user = User("Jack", "Dean", 20, "Football", 4)
#new_user2 = User("Ben", "Franklin", 109, "Politics", 2)

        
#new_user.describe_user()
#new_user.greet_user()
#print(f"Login attempt count: {new_user.login_attempts}")
#new_user.increment_login_attempts(1)
#new_user.reset_login_attempts()
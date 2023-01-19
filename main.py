#Functional Prompt flatten and sort list in ascedning order
numbers_tuple = ((1,25,5), (8,12,10), (100,3,11))
result = sorted(sum(numbers_tuple, ()))

print("Original list:", numbers_tuple)
print("Flattened and ascending:", result) #[1, 3, 5, 8, 10, 11, 12, 25, 100]
#Because I used a tuple with round-brackets not a list
#No this is not a pure function, because it has to sort the tuple and put it in ascending order.
#Yes, because we take another function paramter which is sorted.
#Maybe 
#It allows us to simplify what would have been a complex function in Javascript. 

#OOP Prompt
class Podracer:
    def __init__(self, max_speed, condition, price ):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = 'repaired'
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed (*2)

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"



# It encapsulates because it is using a class which groups together methods and variables. 
# It uses the abstract method because we have a declaration of of methods inside a class.
# It uses inheritance because there is a baseclass of Podracer, but we derive a new class while still keeping Podracer's parameters. 
# It uses polymorphism because we use a method where the child method inherits form the parent. 
# No, because its readable and the code can be shared and reused.



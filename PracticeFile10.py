# class Vehicle:
    
#     def __init__(self, speed = None, mil = None):
#         self.max_speed = speed
#         self.mileage = mil


# Honda = Vehicle(100, 10)
# print(Honda.mileage)


# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage


# class Bus(Vehicle):
#     pass



# SchoolBus = Bus("School Bus", 100, 10)
# print(SchoolBus.max_speed)


# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
    
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers."

# class Bus(Vehicle):
    
#     def seating_capacity(self, capacity = 50):
#         return super().seating_capacity(capacity)


# SchoolBus = Bus("School Bus", 100, 100)
# print(SchoolBus.seating_capacity())



# class Vehicle:
#     color = "White"

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# Honda = Car("iuSGDF", 90, 90)
# SchoolBus = Bus("jhsfj", 90, 90)
# print(Honda.color, SchoolBus.color)



# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
    
#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     def fare(self):
#         return super().fare() + super().fare() / 10

# School_Bus = Bus("School Bus", 100, 50)
# print(School_Bus.fare())





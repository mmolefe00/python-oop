"""
This task Object-Oriented Programming task demonstrates inheritance
from a base/parent class to a derived/child class and overriding a method - hence the title 'method_override'

For this example, we gather information about an individual, create a class object with their details and
determine whether they are eligible to write a learner's test. We then output a fitting message based on those details
while accounting for error inputs.
"""


# start

# ===== Parent Class =====
class Adult:
    # create initialising constructor
    def __init__(self, name_, age_, eye_colour_, hair_colour_):
        self.name_ = name_
        self.age_ = age_
        self.eye_colour_ = eye_colour_
        self.hair_colour_ = hair_colour_

    # create method to output that the adult is old enough to drive.
    def can_drive(self):
        print(f"Yay! You're {self.age_}. You can now drive!\n")


# ===== Sub Class =====
class Child(Adult):

    # create initialising constructor
    def __init__(self, name_, age_, eye_colour_, hair_colour_):

        # use super to inherit the initialising constructor from the parent class
        super().__init__(name_, age_, eye_colour_, hair_colour_)


    # overwrite printing output for can_drive method.
    def can_drive(self):
        print(f"\nOh no! You're only {self.age_}. You can't drive yet :(")


# ===== Inputs and Outputs =====

# greeting
greeting = "Welcome to NaTIS Online.\nTo book your Learner's test, we first need your details:\n"
print(greeting)

# data collection - variable inputs from user
name = input('What is your name:\t').capitalize()
eye_colour = input('What colour are your eyes?:\t')
hair_colour = input('What colour is your hair?:\t')

# AGE DETERMINATION - loop age input
while True:

    # if old enough
    try:
        age = int(input('Please enter your age in numbers:\t'))

        if age >= 18:
            # run Adult Class and output that user can drive with can_drive method
            run = Adult(name, age, eye_colour, hair_colour)
            run.can_drive()

            # farewell
            print('Please proceed to the next page to make your appointment...')
            break

        # if not old enough
        elif age < 18:  # if not old enough
            # run Child Class and output that user can drive with can_drive method
            run = Child(name, age, eye_colour, hair_colour)
            run.can_drive()

            # farewell
            print('For you, the system is offline until your 18th birthday.\nGoodbye!')
            break

    # output Error message
    except ValueError:
        print("Oops! Please enter your age in numbers(digits). Eg: 21.")


# end

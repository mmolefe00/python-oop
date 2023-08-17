"""
This task demonstrates an understanding of single inheritance.
A subclass inherits form a parent class and has added methods which are only applicable to the subclass.
These methods are then called and displayed in an output.
"""

# start

# ===== Parent Class =====
class Course:

    # assign variables to values used in the methods
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office = 'Cape Town'

    # Print Contact Website method
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Print Offerings Method
    def offering(self):
        print(f'We offer: {self.name}.')

    # Print Head office Location Method
    def location(self):
        print(f"Head office:\t{self.head_office}\n")


# ===== Subclass of 'Course' =====

class OOPCourse(Course):

    # initialising constructor for 'description',' trainer' and 'course_id'
    def __init__(self, description, trainer, course_id):
        self.description = description                          # don't need to use super because
        self.trainer = trainer                                  # parent class had no initialising constructor,
        self.course_id = course_id                              # however the methods are still inherited

    # Trainer Details Method - to print out the course description and trainer info
    def trainer_details(self):
        print(f"Description:\t{self.description}")
        print(f"Trainer:\t\t{self.trainer}")

    # Show Course ID Method - to print out course id
    def show_course_id(self):
        print(f"Course ID:\t\t#{self.course_id}")


# ===== Outputs =====

# Greeting
greeting = "Welcome to the HyperionDev Training Institute.\n"
print(greeting)

# Create an object of the subclass with values for course description, trainer details and the course id
course_1 = OOPCourse("OOP Course", "Mr Anon A. Mouse", 12345)

# Now call methods to output desired information from subclass
course_1.contact_details()
course_1.offering()
course_1.location()
course_1.trainer_details()
course_1.show_course_id()

# farewell
farewell = '\nRegister now for our next course in August!\nWe hope to see you!'
print(farewell)

# end

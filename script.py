# Methods : A function thats only available to a specific data type and in our case we are focusing on strings 

my_uni = "University of Nairobi Main Campus"

print(my_uni)

# Replace Some Words in My String 
# Syntax : .replace(text_to_be_replaced, text_to_change_it_to)

my_uni = my_uni.replace("Main Campus", "Chiromo Campus")

print(my_uni)

# Change the Case of my String 
#Syntax : .upper() or .lower()

my_surname = "Kai"

print(my_surname)

my_surname = my_surname.lower()

print(my_surname)

# Asssignment : Try running other methods on strings and see what they do

my_sentence = "I am a student at the University of Nairobi"

# Multi Line Strings 

my_paragraph = """I am a student at Zindua School 
I am Learning Data Science
I enjoy working with fellow classmates
I always submit my assignments on time"""

print(my_paragraph)

# Lists 
student_names = ["Brayan", "John", "Jane", "Mary", "Peter"]

print(type(student_names))

print(student_names[3])

# Assignment : Try Acessing multiple elemnts in your list, try acessing alternating values in your list

# Dictionaries 
students_name = ["Kai", "Jemmimah", "Allela", "Mary", "Peter"]
student_id = [100, 201, 304, 407, 595]

students_dict = {"Kai" : 100,
                 "Jemmimah" : 201,
                 "Allela" : 304,
                 "Mary" : 407,
                 "Peter" : 595}

print(students_dict["Kai"])

print(students_dict.keys())

# Assignment : try updating a Value , Add a key value pair to the dictionary

# Sets 

student_colors = {"Blue", "Red", "Green", "Yellow", "Blue"}

# Convert a list into a set

student_name_set = set(students_name)

print(type(student_name_set))

# Tuples 
# They are immutable meaning you cant change add or remove elements from them
# They are orderd
class_locations = ("first floor", "ground floor", "board room")

print(class_locations[2])

# Assigmnet : Write A summary of Data Structures (Lists , Dictionaries, Sets, Tuples). 
# Looking into these aspects; immutability, ordered, Allow duplicates, Syntax, use cases, SubSet them 
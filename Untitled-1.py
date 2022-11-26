# """
# Our first lesson

# """
# type()
# number = 2
# print(number)

# print(type(number))
# number_with_coma = 2.5
# print(number_with_coma)

# name = "Alisa"
# print(nam
# print(type(name))

# name_of_list = ["Alisa", "Bob"]
# print(name_of_list)
# print(type(name_of_list))

# name_of_tuples = ("Alisa", "Bob")
# print(name_of_tuples)
# print(type(name_of_tuples))

# dictinary = {"name":"Alisa","surname":"Nikols"}
# print(dictinary)
# print(type((dictinary))

# name = str(input("Your name? "))
# email = str(input("Your email? "))
# age = int(input("Your age? "))
# height = float(input("Your height? "))
# is_active = bool(
#     input(f"хотите ли вы получать уведомления от сайта da {True} net {False}")
# )

# is_active = bool(
#     input(f"хотите ли вы получать уведомления от сайта da {'Y', True} net {'N', False}")
# )

# length = float(input("Enter length "))
# width = float(input("Enter width "))
# area = length * width
# print(area)

# TRAIN IF-ELIF-ELSE

# user_score = int(input("How much score you earn? "))
# if user_score >= 1:
#     print(f"Not bad man!", user_score)
# elif user_score == 0:
#     print(f"Try again,Loozer your score", user_score)
# else:
#     print("Ti prosto LOX")

# user_gender = input("Print your gender plz, Male/Female. ")
# if user_gender == "Male":
#     print("Hi bro!")
# elif user_gender == "Female":
#     print("Hi bitch)))")
# else:
#     print("You are Girl with dick or boy with pussy?")

# TRAIN WHILE LOOP

# counter = 0
# while counter < 5:
#     user_input = input(">>>>")
#     counter += 1  # counter = counter + 1
#     if user_input == "exit":
#         break
#     else:
#         print(f"Now you write: {user_input}")

# TRAIN TRY EXCEPT

# while True:
#     age = input("How old are you? ")
#     try:
#         age = int(age)
#         if age >= 18:
#             print("Access allowed")
#             break
#         else:
#             print("Access denied")
#             break
#     except ValueError:
#         print(f"{age} is not a number. Please write number!")
#     finally:
#         print("_" * 30)

# is_active = input("Is the user active? ")
# is_admin = input("Is the user administrator? ")
# is_permission = input("Does the user have access? ")

# is_active = True or False
# is_admin = True or False
# is_permission = True or False
# access = bool("is_active, is_admin, is_permission")
# if is_permission or is_active:
#     print("Welcom admin")
# elif is_permission and is_active:
#     print("Welcom user")
# else:
#     print("Access denaid")
# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience > 1 and work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience == 1 or work_experience < 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"
# print(developer_type)

# num = int(input("Enter an integer number: "))

# is_even = "True" if num % 2 else "False"
# print(is_even)
# num = int(input("Enter the integer (0 to 100): "))
# sum = 0 + 1
# i = 1
# while num == 0:
#     i = num + 1

# from re import I


# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))
# if first > second:
#     I = second
# else:
#     I = first
# gcd = I
# print(gcd)

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))
# if first > second:
#     small = second
# else:
#     small = first
# gcd = small

# while first and second % gcd:
#     gcd = gcd - 1

# print(gcd)


# first = 575
# second = 375
# if first > second:
#     small = second
# else:
#     small = first
# gcd = small


# while first % gcd != 0 and second % gcd != 0:
#     print(gcd)
#     gcd = gcd - 1
# print(gcd)

# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     for i in range(num + 1):
#         sum = sum + i


# def invite_to_event(username):
#     return username


# result = f"Dear {username}, we have the honour to invite you to our event"
# print(result)

# def invite_to_event(username):
#     return username


# result = f"Dear {username}, we have the honour to invite you to our event"
# print(result)


# def invite_to_event(username):
#     value = f"Dear {username}, we have the honour to invite you to our event"
#     return value


# def current_milli_time():
#     return round(datetime.now() * 1000)
# base_rate = 40
# price_per_km = 10
# total_trip = 0


# def trip_price(path):
#     global total_trip
#     cost = total_trip * price_per_km + base_rate
#     path = cost
#     return path


# price = 200
# discount = 0.07
# size = price * discount
# price -= size
# print(price)


# def get_fullname(first_name, middle_name="", last_name=""):

#     return f"{first_name} {middle_name} {last_name}"


# print(get_fullname("Anton", "Chigarev"), sep="*")

# string = ("first_name", "middle_name", "last_name", sep=" ")
# print(string)
# print("a", "b", "c",sep ="*")
# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     elif len(string) < length:
#         change = string + " " * length - len(string) // 2
#         return change


# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     elif len(string) < length:
#         change = length - len(string) // 2 + string
#         return change


# def cost_delivery(quantity, *args, discount=0):
#     total = 5

#     for i in range(quantity - 1):
#         total += 2

#     if discount != 0:
#         total = total * discount

#     print(total)
#     return total


# cost_delivery(10, 2, 3, 4, discount=0.5)

# while True:
#     wait_for_number = input("Enter number >>> ")
#     try:
#         wait_for_number = int(wait_for_number)
#     except ValueError:
#         print(f"Your enter is not a number please try again enter number")
#     finally:
# #         print("-" * 20)
# while True:
#     operand = input()
#     a = "="
#     if operand == a:
#         break

# ________4
#
#
from random import randint
import random

random_num = randint(40, 126)


def get_random_password():
    number = 1
    lenght = 8
    random_num = randint(40, 126)
    for x in range(number):
        password = ""
        for i in range(lenght):
            password += random.choice(random_num)
        print(password)

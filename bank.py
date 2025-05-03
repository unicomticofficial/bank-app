import os


def get_customer_info():
    name = input('Enter Name: ')
    address = input('Enter Address: ')
    username = input('Enter Username: ')
    password = input('Enter Password: ')

    return [name, address, username, password]


# def create_customer():
#     customers = get_customer_info()
#     with open("customers.txt", "a") as file:
#         file.write(f"{customers[0]},{customers[1]}\n")

# def create_user():
#     customers = get_customer_info()
#     with open("users.txt", "a") as file:
#         file.write(f"{customers[2]},{customers[3]}\n")

def create_auto_user_id():
    with open("users.txt", "r") as user_file:
        user_id = user_file.readlines()[-1].split(",")[0]
        characters = list(user_id)
        print(characters)

create_auto_user_id()


def create_customer_and_user():
    customers = get_customer_info()
    
    with open("customers.txt", "a") as customer_file, open("users.txt", "a") as user_file:
        customer_file.write(f"{customers[0]},{customers[1]}\n")
        user_file.write(f"{customers[2]},{customers[3]}\n")


# create_customer_and_user()

print("press 1. add customer \n 2. for view all customers")

get_input = int(input("Enter Number: "))

if get_input == 1:
    create_customer_and_user():
elif get_input == 2:











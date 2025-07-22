"""3. Dictionary & User Input Example:
   File: phone_book.py – Add, search, delete contacts
Store all files inside a folder named: basic-python/"""


phone_book = {}

def add_op(name, num):
    phone_book[name] = num
    print(phone_book)

def search_op(name):
    print(phone_book.get(name, "Contact not found."))

def delete_op(name):
    if name in phone_book:
        del phone_book[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print('Phone Book Operation')
    print('1: Add')
    print('2: Search')
    print('3: Delete')
    
    ch = int(input("Enter the operation number: "))

    if ch == 1:
        name = input("Enter the name: ")
        num = int(input("Enter the contact number: "))
        add_op(name, num)

    elif ch == 2:
        name = input("Enter name you are searching: ")
        search_op(name)

    elif ch == 3:
        name = input("Enter the name to delete: ")    
        delete_op(name)

    else:
        print("Invalid operation number")


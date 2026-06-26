import json

# Load data
try:
    with open("lib.json", "r") as file:
        lib = json.load(file)
except FileNotFoundError:
    lib = {}

def addbook():
    book = input("Enter the book name: ")

    if book == "":
        print("Book name can't be empty")
        return
    
    author = input("Enter the name of the author")

    if author =="":
        print("Author can't be empty")
        return

    print("Book Name:", lib[book]["Book name"])
    print("Author Name:", lib[book]["Author name"])

    print("Book added successfully!")

def viewbook():
    book = input("Enter the name of the book: ")

    if book == "":
        print("Book name can't be empty")
        return

    if book in lib:
        print("\nBook Found")
        print("Book Name:", lib[book]["book name"])
    else:
        print("Book not found.")

def view_all_book():
    if not lib:
        print("No Book in LIBARY")
        return
    print("ALL BOOKS ARE:")

    for book in lib:
        print("Book Name =", lib[book]["book name"])
        print("Author =", lib[book]["author name"])
        
        

while True:
    print("\nLIBRARY")
    print("1. Add Book")
    print("2. View Book")
    print("3. View All Books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addbook()

    elif choice == "2":
        viewbook()

    elif choice == "3":
        view_all_book()

    elif choice == "4":
        with open("lib.json", "w") as file:
            json.dump(lib, file, indent=4)

        print("Total Books =", len(lib))
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
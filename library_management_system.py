
import getpass

# Global variables for storing books and users
books = []
users = []
user_credentials = {}  # Dictionary to store username-password pairs

# Function to load data (initialize users and credentials)
def load_data():
    global users, user_credentials
    # Simulate loading from a database or external source
    users_data = [
        {"id": 1, "name": "sana", "email": "alice@example.com", "password": "123"},
        {"id": 2, "name": "hassan", "email": "bob@example.com", "password": "456"}
    ]
    users = users_data[:]
    user_credentials = {user['name']: user['password'] for user in users_data}

# Function to save data
def save_data():
    pass

# Function to display books
def display_books():
    if not books:
        print("No books available in the library.")
        return

    print("\nList of Books:")
    for book in books:
        print(f"Title: {book['title']} | Author: {book['author']} | Genre: {book['genre']} | Available: {book['available']}")

# Function to search for a book by title
def search_book(title):
    found_books = [book for book in books if book['title'].lower() == title.lower()]
    if found_books:
        for book in found_books:
            print(f"Title: {book['title']} | Author: {book['author']} | Genre: {book['genre']} | Available: {book['available']}")
    else:
        print("Book not found")

# Function to borrow a book
def borrow_book(title):
    for book in books:
        if book['title'].lower() == title.lower() and book['available']:
            book['available'] = False
            print(f"You have borrowed '{book['title']}'")
            return
    print("Book not available")

# Function to return a book
def return_book(title):
    for book in books:
        if book['title'].lower() == title.lower() and not book['available']:
            book['available'] = True
            print(f"You have returned '{book['title']}'")
            return
    print("Invalid book title or book already available")

# Function to add a new book
def add_book(title, author, genre):
    new_book = {"title": title, "author": author, "genre": genre, "available": True}
    books.append(new_book)
    print(f"New book '{title}' by {author} (Genre: {genre}) has been added to the library")

# Function to remove a book
def remove_book(title):
    for book in books:
        if book['title'].lower() == title.lower():
            books.remove(book)
            print(f"Book '{title}' has been removed from the library")
            return
    print("Book not found")

# Function to display all users
def display_users():
    if not users:
        print("No users registered.")
        return

    print("\nList of Users:")
    for user in users:
        print(f"ID: {user['id']} | Name: {user['name']} | Email: {user['email']}")

# Function to add a new user
def add_user(name, email, password):
    user_id = len(users) + 1
    new_user = {"id": user_id, "name": name, "email": email, "password": password}
    users.append(new_user)
    user_credentials[name] = password  # Add to user credentials dictionary
    print(f"New user '{name}' with email '{email}' has been added")

# Function to search for a user by name
def search_user(name):
    found_users = [user for user in users if user['name'].lower() == name.lower()]
    if found_users:
        for user in found_users:
            print(f"ID: {user['id']} | Name: {user['name']} | Email: {user['email']}")
    else:
        print("User not found")

# Function to authenticate user login
def login():
    print("\nLogin:")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    if username in user_credentials and user_credentials[username] == password:
        print(f"Welcome, {username}!")
        return username  # Return username for simplicity

    print("Invalid username or password")
    return None

# User menu after successful login
def user_menu(username):
    print(f"Welcome, {username}!")
    while True:
        print("\nUser Menu:")
        print("1. Display all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Add a book")
        print("6. Remove a book")
        print("7. Display all users")
        print("8. Search for a user")
        print("9. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_books()
        elif choice == '2':
            title = input("Enter the title of the book you want to search for: ")
            search_book(title)
        elif choice == '3':
            title = input("Enter the title of the book you want to borrow: ")
            borrow_book(title)
        elif choice == '4':
            title = input("Enter the title of the book you want to return: ")
            return_book(title)
        elif choice == '5':
            title = input("Enter the title of the new book: ")
            author = input("Enter the author of the new book: ")
            genre = input("Enter the genre of the new book: ")
            add_book(title, author, genre)
        elif choice == '6':
            title = input("Enter the title of the book you want to remove: ")
            remove_book(title)
        elif choice == '7':
            display_users()
        elif choice == '8':
            name = input("Enter the name of the user you want to search for: ")
            search_user(name)
        elif choice == '9':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to control the flow of the program
def main():
    load_data()  # Initialize users and user credentials
    
    while True:
        print("\nWelcome to the Library Management System")
        print("1. Login")
        print("2. Register new user")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = login()
            if username:
                user_menu(username)
        elif choice == '2':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = getpass.getpass("Enter your password: ")
            add_user(name, email, password)
        elif choice == '3':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


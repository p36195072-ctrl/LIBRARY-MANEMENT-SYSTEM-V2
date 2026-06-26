Library Management System

A beginner-friendly Python project that demonstrates how to manage a collection of books using JSON files and dictionaries.

📌 Description

This project allows users to:

Add books
Store author names
Search books
View all books
Save data permanently
Load data automatically

All library records are stored in lib.json, ensuring that books remain saved even after the program is closed.

🧠 Concepts Used

Python Functions
Dictionaries
Nested Dictionaries
JSON Storage
File Handling
json.load()
json.dump()
User Input
Loops
Conditional Statements
Data Persistence

✨ Features

✅ Add Books

✅ Store Author Names

✅ Search Books

✅ View All Books

✅ Automatic JSON Saving

✅ Automatic JSON Loading

📂 Files

library_manager.py
lib.json

💻 Stored Information

Each book record contains:

Book Name
Author Name

Example:

{
    "Python Basics": {
        "book name": "Python Basics",
        "author name": "John Smith"
    },
    "Data Structures": {
        "book name": "Data Structures",
        "author name": "Alice Brown"
    }
}

▶️ Example Output

LIBRARY

1. Add Book
2. View Book
3. View All Books
4. Exit
Enter your choice: 1

Enter the book name: Python Basics
Enter the name of the author: John Smith

Book added successfully!
Enter your choice: 2

Enter the name of the book: Python Basics

Book Found
Book Name: Python Basics
Author Name: John Smith

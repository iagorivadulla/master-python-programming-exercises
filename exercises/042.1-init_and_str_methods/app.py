# Your code here

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"# Output: \n#\n# Book Title: {self.title}\n# Author: {self.author}\n# Year: {self.year}"

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print(book1)
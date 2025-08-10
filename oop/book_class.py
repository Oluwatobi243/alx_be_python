class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # destructor: prints when the object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # user-friendly string
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # official representation that can be used to recreate the object
        return f"Book('{self.title}', '{self.author}', {self.year})"
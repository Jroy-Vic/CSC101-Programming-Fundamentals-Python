import math


# Representation of a book.
class Book:
    # Initialize a new Book object.
    # input: the book's authors as a list of strings
    # input: the book's title as a string
    def __init__(self, authors: list[str], title: str):
        self.authors = authors
        self.title = title


    # Provide a developer-friendly string representation of the object.
    # input: Book for which a string representation is desired. 
    # output: string representation
    def __repr__(self):
        return "Book({}, '{}')".format(self.authors, self.title)


    # Compare the Book object with another value to determine equality.
    # input: Book against which to compare
    # input: Another value to compare to the Book
    # output: boolean indicating equality
    def __eq__(self, other):
        return (self is other or
                type(other) == Book and
                self.authors == other.authors and
                self.title == other.title)



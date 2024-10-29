#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # Title property
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        self._title = value

    # Page Count property with validation and error message
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        elif value <= 0:
            print("page_count must be a positive integer")
        else:
            self._page_count = value

    # Method for turning the page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    # Optional: String representation for easier debugging
    def __str__(self):
        return f"'{self.title}', {self.page_count} pages"

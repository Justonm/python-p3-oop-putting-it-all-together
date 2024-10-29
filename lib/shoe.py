#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"  # Default condition

    # Brand property
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string.")
        self._brand = value

    # Size property with validation
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        elif value <= 0:
            raise ValueError("Size must be a positive number.")
        else:
            self._size = value

    # Method for cobbling the shoe
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    # Optional: String representation for debugging
    def __str__(self):
        return f"{self.brand} shoe, Size {self.size}, Condition: {self.condition}"

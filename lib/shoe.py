#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand:str, size:int):
        if type(size) != int:
            print("size must be an integer")
        self.brand= brand
        self.size = size
        self.condition = "New"

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value:int):
        if type(value) == int:
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        if(self.condition == "Old"):
            self.condition = "New"
            print("The shoe has been restored to new condition.")
        else:
            print("Your shoe is as good as new!")
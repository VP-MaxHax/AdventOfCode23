import re

class CubeCounter: 

    def __init__(self):
        self.numbers_list = []
        self.box_list = [[] for _ in range(256)]
        self.current_value = 0
        self.label = ""
        self.operation = ""
        self.focal = 0

    def get_value(self, char):
        self.current_value += ord(char)
        self.current_value *= 17
        self.current_value %= 256

    def do_the_thing(self):
        box = self.box_list[self.current_value]
        is_in = False
        for slot in range(len(box)):
            if self.label == box[slot][0]:
                lens_index = slot
                is_in = True
        if self.operation == "-" and is_in:
            box.pop(lens_index)
        elif self.operation == "=" and is_in:
            box[lens_index] = (self.label, self.focal)
        elif self.operation == "=" and not is_in:
            box.append((self.label, self.focal))

    def count_results(self):
        for box in range(len(self.box_list)):
            for lens in range(len(self.box_list[box])):
                self.numbers_list.append((box+1)*(lens+1)*(self.box_list[box][lens][1]))

    def main_block(self):
        with open('Day15/input.txt', 'r') as file:
            puzzle_input = file.read()
            for char in puzzle_input:
                if char == ",":
                    self.do_the_thing()
                    self.current_value = 0
                    self.label = ""  
                elif char in "=-":
                    self.operation = char
                    #self.get_value(char)
                elif char.isdigit():
                    self.focal = int(char)
                    #self.get_value(char)
                else:
                    self.label += char
                    self.get_value(char)
            self.do_the_thing()
            print(self.box_list)
            self.count_results()
            return sum(self.numbers_list)
            


if __name__ == "__main__":
    numb = CubeCounter()
    print(numb.main_block())


#259536 high
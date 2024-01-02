
class CubeCounter: 

    def __init__(self):
        self.numbers_list = []
        self.current_value = 0


    def main_block(self):
        with open('Day15/input.txt', 'r') as file:
            puzzle_input = file.read()
            for char in puzzle_input:
                if char == ",":
                    self.numbers_list.append(self.current_value)
                    print(self.current_value)
                    self.current_value = 0
                else:
                    self.current_value += ord(char)
                    self.current_value *= 17
                    self.current_value %= 256
            self.numbers_list.append(self.current_value)
            return sum(self.numbers_list)
            


if __name__ == "__main__":
    numb = CubeCounter()
    print(numb.main_block())

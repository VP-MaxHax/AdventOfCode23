import re

class CubeCounter: 

    def __init__(self):
        self.numbers_list = []
        self.id_counter = 1

    def parser(self, line):
        line = line.split(":")
        line = re.split(",|;", line[1])
        print(line)
        valid = True
        green_max = 0
        blue_max = 0
        red_max = 0
        for i in line:     
            number = ""
            if i[1] in "1234567890" and i[2] in "1234567890":
                number += i[1]+i[2]
                number = int(number)
                if i[-3:-1] == "re":
                    if number > red_max:
                        red_max = number
                    if number > 12:
                        valid = False
                if i[-3:-1] == "lu":
                    if number > blue_max:
                        blue_max = number
                    if number > 14:                    
                        valid = False
                if i[-3:-1] == "ee":
                    if number > green_max:
                        green_max = number  
                    if number > 13:
                        valid = False
            else:
                number += i[1]
                number = int(number)
                if i[-3:-1] == "re":
                    if number > red_max:
                        red_max = number
                if i[-3:-1] == "lu":
                    if number > blue_max:
                        blue_max = number
                if i[-3:-1] == "ee":
                    if number > green_max:
                        green_max = number               
        self.numbers_list.append(blue_max*green_max*red_max)
        print(blue_max*green_max*red_max)
        self.id_counter += 1



    def main_block(self):
        with open('Day2/input.txt', 'r') as file:
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            for line in puzzle_input:
                self.parser(line)
            return sum(self.numbers_list)
            


if __name__ == "__main__":
    numb = CubeCounter()
    print(numb.main_block())

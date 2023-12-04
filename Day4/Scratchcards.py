
class Scratcher: 

    def __init__(self):
        self.numbers_list = []
        self.id_counter = 1

    def parser(self, line):
        number = ""
        winning_numbers = []
        your_numbers = []
        winning = True
        for i in line:
            if i in "1234567890":
                number += i
            elif i == " ":
                if winning == True and number != "":
                    winning_numbers.append(int(number))
                    number = ""
                elif winning == False and number != "":
                    your_numbers.append(int(number))
                    number = ""
            elif i == "|":
                winning = False
        your_numbers.append(int(number))
        print(winning_numbers, your_numbers)
        score = 0
        for i in winning_numbers:
            if i in your_numbers and score == 0:
                score = 1
            elif i in your_numbers and score > 0:
                score *= 2
        print(score)
        self.numbers_list.append(score)



    def main_block(self):
        with open('Day4/input.txt', 'r') as file:
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            for line in puzzle_input:
                line = line.split(":")
                print(line[1])
                self.parser(line[1])
            return sum(self.numbers_list)
            


if __name__ == "__main__":
    numb = Scratcher()
    print(numb.main_block())

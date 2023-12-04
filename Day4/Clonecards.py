from datetime import datetime

class Scratcher: 

    def __init__(self):
        self.card_count= [1]*192
        self.numbers_list = []
        self.scratched = 0

    def parser(self, line):
        self.scratched += 1
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
        score = 0
        for i in winning_numbers:
            if i in your_numbers:
                score += 1
        for i in range(score):
            self.card_count[i+1] += 1
        print(len(self.card_count))
        self.numbers_list.append(score)



    def main_block(self):
        with open('Day4/input.txt', 'r') as file:
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            for line in puzzle_input:
                line = line.split(":")
                for _ in range(self.card_count[0]):
                    self.parser(line[1])
                self.card_count.pop(0)
            return self.scratched
            


if __name__ == "__main__":
    numb = Scratcher()
    starttime = datetime.now()
    print(numb.main_block())
    endtime = datetime.now()
    print(f"Program runtime = {endtime-starttime}")
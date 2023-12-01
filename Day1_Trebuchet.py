class NumberPicker:

    def __init__(self):
        self.numbers_list = []

    def parser(self, string):
        number = ""
        for i in range(len(string)):
            if string[i] in "1234567890":
                number += string[i]
                break
            elif string[i] == "o":
                if len(string)-i >= 3 and string[i+1] == "n" and string[i+2] == "e":
                    number += "1"
                    break
            elif string[i] == "t":
                if len(string)-i >= 5 and string[i+1] == "h" and string[i+2] == "r" and string[i+3] == "e" and string[i+4] == "e":
                    number += "3"
                    break
                if len(string)-i >= 2 and string[i+1] == "w" and string[i+2] == "o":
                    number += "2"
                    break
            elif string[i] == "f":
                if len(string)-i >= 4 and string[i+1] == "o" and string[i+2] == "u" and string[i+3] == "r":
                    number += "4"
                    break
                if len(string)-i >= 4 and string[i+1] == "i" and string[i+2] == "v" and string[i+3] == "e":
                    number += "5"
                    break
            elif string[i] == "s":
                if len(string)-i >= 4 and string[i+1] == "i" and string[i+2] == "x":
                    number += "6"
                    break
                if len(string)-i >= 5 and string[i+1] == "e" and string[i+2] == "v" and string[i+3] == "e" and string[i+4] == "n":
                    number += "7"
                    break
            elif string[i] == "e":
                if len(string)-i >= 5 and string[i+1] == "i" and string[i+2] == "g" and string[i+3] == "h" and string[i+4] == "t":
                    number += "8"
                    break
            elif string[i] == "n":
                if len(string)-i >= 4 and string[i+1] == "i" and string[i+2] == "n" and string[i+3] == "e":
                    number += "9"
                    break
            elif string[i] == "z":
                if len(string)-i >= 4 and string[i+1] == "e" and string[i+2] == "r" and string[i+3] == "o":
                    number += "0"
                    break
        for j in range(len(string)):
            i = -j-1
            if string[i] in "1234567890":
                number += string[i]
                break
            elif string[i] == "o":
                if len(string)-i >= 3 and string[i+1] == "n" and string[i+2] == "e":
                    number += "1"
                    break
            elif string[i] == "t":
                if len(string)-i >= 5 and string[i+1] == "h" and string[i+2] == "r" and string[i+3] == "e" and string[i+4] == "e":
                    number += "3"
                    break
                if len(string)-i >= 2 and string[i+1] == "w" and string[i+2] == "o":
                    number += "2"
                    break
            elif string[i] == "f":
                if len(string)-i >= 4 and string[i+1] == "o" and string[i+2] == "u" and string[i+3] == "r":
                    number += "4"
                    break
                if len(string)-i >= 4 and string[i+1] == "i" and string[i+2] == "v" and string[i+3] == "e":
                    number += "5"
                    break
            elif string[i] == "s":
                if len(string)-i >= 4 and string[i+1] == "i" and string[i+2] == "x":
                    number += "6"
                    break
                if len(string)-i >= 5 and string[i+1] == "e" and string[i+2] == "v" and string[i+3] == "e" and string[i+4] == "n":
                    number += "7"
                    break
            elif string[i] == "e":
                if len(string)-i >= 5 and string[i+1] == "i" and string[i+2] == "g" and string[i+3] == "h" and string[i+4] == "t":
                    number += "8"
                    break
            elif string[i] == "n":
                if len(string)-i >= 4 and string[i+1] == "i" and string[i+2] == "n" and string[i+3] == "e":
                    number += "9"
                    break
            elif string[i] == "z":
                if len(string)-i >= 4 and string[i+1] == "e" and string[i+2] == "r" and string[i+3] == "o":
                    number += "0"
                    break
        print(number)
        number = int(number)
        self.numbers_list.append(number)

    def main_block(self):
        with open('trebutchet.txt', 'r') as file:
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            for line in puzzle_input:
                self.parser(line)
            return sum(self.numbers_list)
            


if __name__ == "__main__":
    numb = NumberPicker()
    print(numb.main_block())

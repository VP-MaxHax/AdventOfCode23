class NumberPicker:

    def __init__(self):
        self.numbers_list = []

    def parser(self, string):
        number = ""
        for i in string:
            if i in "1234567890":
                number += i
                break
        for i in range(len(string)):
            j = -i-1
            if string[j] in "1234567890":
                number += string[j]
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

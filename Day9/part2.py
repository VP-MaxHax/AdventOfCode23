
class Pinäärijoptaijotain: 

    def __init__(self):
        self.numbers_list = []
        self.id_counter = 1

    def barse(self, line):
        number = ""
        newline = []
        minus = False
        for i in line:
            if i.isdigit():
                number += i
            elif i == "-":
                minus = True
            else:
                if number != "":
                    if minus == True:
                        number = int(number)
                        number = -number
                        newline.append(number)
                    else:
                        newline.append(int(number))
                number = ""
                minus = False
        if minus == True:
            number = int(number)
            number = -number
            newline.append(number)
        else:
            newline.append(int(number))
        return newline

    def binaare(self, line):
        line = self.barse(line)
        tree = [line]
        while tree[-1].count(0)!=len(tree[-1]):
            temp_line = []
            for i in range(len(tree[-1])-1):        
                temp_line.append(tree[-1][i+1]-tree[-1][i])
            #print(temp_line, len(temp_line))
            tree.append(temp_line)
        for i in range(len(tree)-1):
            tree[-i-2].insert(0, tree[-i-2][0]-tree[-i-1][0]) 
        for i in tree:
            print(i, len(i))
        self.numbers_list.append(tree[0][0])

    def main_block(self):
        with open('Day9/input.txt', 'r') as file:
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            for line in puzzle_input:
                self.binaare(line)
            #print(len(self.numbers_list))
            return sum(self.numbers_list)
            


if __name__ == "__main__":
    numb = Pinäärijoptaijotain()
    print(numb.main_block())

#914358946 too high

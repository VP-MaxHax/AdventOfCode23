class CubeCounter: 

    def __init__(self):
        self.numbers_list = []
        self.matrise = self.get_matrise()
        self.merkki = False

    def get_matrise(self):
        with open('Day3/input.txt', 'r') as file:
            matrise = []
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            for i in puzzle_input:
                lista = []
                for j in i:
                    lista.append(j)
                matrise.append(lista)
            return matrise

    def print_matrise(self):
        for i in self.matrise:
            print(i)

    def surroundings_check(self, i, j):
        if self.matrise[max(i-1, 0)][max(j-1, 0)] not in "1234567890." or\
        self.matrise[max(i-1, 0)][j] not in "1234567890." or\
        self.matrise[max(i-1, 0)][min(j+1, len(self.matrise[0])-1)] not in "1234567890." or\
        self.matrise[i][max(j-1, 0)] not in "1234567890." or\
        self.matrise[i][min(j+1, len(self.matrise[0])-1)] not in "1234567890." or\
        self.matrise[min(i+1, len(self.matrise)-1)][max(j-1, 0)] not in "1234567890." or\
        self.matrise[min(i+1, len(self.matrise)-1)][j] not in "1234567890." or\
        self.matrise[min(i+1, len(self.matrise)-1)][min(j+1, len(self.matrise[0])-1)] not in "1234567890.":
            self.merkki = True

    def matrise_runner(self):
        self.print_matrise()
        number = ""
        for i in range(len(self.matrise)):
            for j in range(len(self.matrise[0])):
                if self.matrise[i][j] in "1234567890":
                    number += self.matrise[i][j]
                    self.surroundings_check(i, j)
                else:
                    if number != "" and self.merkki == True:
                        self.numbers_list.append(int(number))
                    number = ""
                    self.merkki = False
        print(self.numbers_list)
        return sum(self.numbers_list)

if __name__ == "__main__":
    numb = CubeCounter()
    print(numb.matrise_runner())

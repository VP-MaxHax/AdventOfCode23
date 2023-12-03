class CubeCounter: 

    def __init__(self):
        self.numbers_list = []
        self.numbers_dict = {}
        self.matrise = self.get_matrise()
        self.merkki = False
        self.entry = ""
        self.entry_got = False

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
        entry = ""
        if self.matrise[max(i-1, 0)][max(j-1, 0)] == "*":
            entry += str(max(i-1, 0))
            entry += str(max(j-1, 0))
            self.merkki = True
            return entry
               
        elif self.matrise[max(i-1, 0)][j] == "*":
            entry += str(max(i-1, 0))
            entry += str(j)
            self.merkki = True
            return entry
        
        elif self.matrise[max(i-1, 0)][min(j+1, len(self.matrise[0])-1)] == "*":
            entry += str(max(i-1, 0))
            entry += str(min(j+1, len(self.matrise[0])-1))
            self.merkki = True
            return entry
        
        elif self.matrise[i][max(j-1, 0)] == "*":
            entry += str(i)
            entry += str(max(j-1, 0))
            self.merkki = True
            return entry
    
        elif self.matrise[i][min(j+1, len(self.matrise[0])-1)] == "*":
            entry += str(i)
            entry += str(min(j+1, len(self.matrise[0])-1))
            self.merkki = True
            return entry
        
        elif self.matrise[min(i+1, len(self.matrise)-1)][max(j-1, 0)] == "*":
            entry += str(min(i+1, len(self.matrise)-1))
            entry += str(max(j-1, 0))
            self.merkki = True
            return entry
    
        elif self.matrise[min(i+1, len(self.matrise)-1)][j] == "*":
            entry += str(min(i+1, len(self.matrise)-1))
            entry += str(j)
            self.merkki = True
            return entry
    
        elif self.matrise[min(i+1, len(self.matrise)-1)][min(j+1, len(self.matrise[0])-1)] == "*":
            entry += str(min(i+1, len(self.matrise[0])-1))
            entry += str(min(j+1, len(self.matrise[0])-1))
            self.merkki = True
            return entry

    def matrise_runner(self):
        self.print_matrise()
        number = ""
        self.entry_got = False
        for i in range(len(self.matrise)):
            for j in range(len(self.matrise[0])):
                if self.matrise[i][j] in "1234567890":
                    number += self.matrise[i][j]
                    entry_maybe = self.surroundings_check(i, j)
                    if self.entry_got == False and entry_maybe not in ("", None):
                        self.entry = entry_maybe
                        self.entry_got = True
                else:
                    if number != "" and self.merkki == True:
                        if self.entry not in self.numbers_dict:
                            self.numbers_dict[self.entry] = [int(number)]
                        else:
                            self.numbers_dict[self.entry].append(int(number))
                    self.entry = ""
                    self.entry_got = False
                    number = ""
                    self.merkki = False
        for key, value in self.numbers_dict.items():
            print(f"{key}: {value}")
            if len(value) == 2:
                self.numbers_list.append(value[0]*value[1])
        return sum(self.numbers_list)

if __name__ == "__main__":
    numb = CubeCounter()
    print(numb.matrise_runner())

class SpaceSpacer: 

    def __init__(self):
        self.numbers_list = []
        self.id_counter = 1
        self.puzzle_input = []
        self.puzzle_size = 0
        self.planets = []

    def empty_space(self):
        self.puzzle_size = len(self.puzzle_input)
        for i in range(self.puzzle_size):
            if "#" not in self.puzzle_input[i]:
                self.puzzle_input[i] = ["w"]*self.puzzle_size
        for i in range(self.puzzle_size):
            empty_space = True
            for j in range(self.puzzle_size):
                if self.puzzle_input[j][i] == "#":
                    empty_space = False
            if empty_space == True:
                for j in range(self.puzzle_size):
                    self.puzzle_input[j][i] = "w"

    def planet_placer(self):
        y = 0
        for i in self.puzzle_input:
            x = 0
            if "#" not in i:
                y += 999999
            else:
                for j in i:
                    if j == "w":
                        x += 999999
                    elif j == "#":
                        self.planets.append((x, y))
                    x += 1
            y += 1

    def distance_calc(self):
        while len(self.planets) > 1:
            current = self.planets.pop(0)
            for i in self.planets:
                distance = abs(current[0]-i[0])+abs(current[1]-i[1])
                self.numbers_list.append(distance)

    def main_block(self):
        with open('Day11/input.txt', 'r') as file:
            puzzle_input = file.read()
            self.puzzle_input = puzzle_input.splitlines()
            for line in range(len(self.puzzle_input)):
                self.puzzle_input[line] = list(self.puzzle_input[line])
            self.empty_space()
            for line in self.puzzle_input:
                print(line)
            self.planet_placer()
            self.distance_calc()
            return sum(self.numbers_list)
            

if __name__ == "__main__":
    numb = SpaceSpacer()
    print(numb.main_block())

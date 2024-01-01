
class Mazerunner:
    def __init__(self):
        self.labyrith = []
        self.row = 0
        self.start = (0, 0)
        self.ways_to_go = []
        self.visited = []
        self.longest = 0

    def parser(self, line):
        row = []
        for i in range(len(line)):
            row.append(line[i])
            if line[i] == "S":
                self.start = (self.row, i)
                self.ways_to_go.append((self.start, 0))
        self.labyrith.append(row)
        self.row += 1

    def check_right(self, location):
        return len(self.labyrith[location[0]])>=location[1]+1 and self.labyrith[location[0]][location[1]+1] in  "-J7"
    
    def check_left(self, location):
        return 0<=location[1]-1 and self.labyrith[location[0]][location[1]-1] in  "-LF"
    
    def check_bottom(self, location):
        return len(self.labyrith)>=location[0]+1 and self.labyrith[location[0]+1][location[1]] in  "|LJ"
    
    def check_top(self, location):
        return 0<=location[0]-1 and self.labyrith[location[0]-1][location[1]] in  "|7F"
    
    def traverser(self):
        while len(self.ways_to_go)>0:
            standing = self.ways_to_go.pop(0)
            location = standing[0]
            steps = standing[1]
            if location not in self.visited:
                self.visited.append(location)

                if steps > self.longest:
                    self.longest = steps

                if self.labyrith[location[0]][location[1]] == "S":
                    if self.check_right(location):
                        self.ways_to_go.append(((location[0],location[1]+1), steps+1))
                    if self.check_left(location):
                        self.ways_to_go.append(((location[0],location[1]-1), steps+1))
                    if self.check_bottom(location):
                        self.ways_to_go.append(((location[0]+1,location[1]), steps+1))
                    if self.check_top(location):
                        self.ways_to_go.append(((location[0]-1,location[1]), steps+1))

                if self.labyrith[location[0]][location[1]] == "|":
                    if self.check_bottom(location):
                        self.ways_to_go.append(((location[0]+1,location[1]), steps+1))
                    if self.check_top(location):
                        self.ways_to_go.append(((location[0]-1,location[1]), steps+1))

                if self.labyrith[location[0]][location[1]] == "-":
                    if self.check_right(location):
                        self.ways_to_go.append(((location[0],location[1]+1), steps+1))
                    if self.check_left(location):
                        self.ways_to_go.append(((location[0],location[1]-1), steps+1))

                if self.labyrith[location[0]][location[1]] == "L":
                    if self.check_top(location):
                        self.ways_to_go.append(((location[0]-1,location[1]), steps+1))
                    if self.check_right(location):
                        self.ways_to_go.append(((location[0],location[1]+1), steps+1))

                if self.labyrith[location[0]][location[1]] == "J":                
                    if self.check_top(location):
                        self.ways_to_go.append(((location[0]-1,location[1]), steps+1))     
                    if self.check_left(location):
                        self.ways_to_go.append(((location[0],location[1]-1), steps+1))

                if self.labyrith[location[0]][location[1]] == "7": 
                    if self.check_left(location):
                        self.ways_to_go.append(((location[0],location[1]-1), steps+1))
                    if self.check_bottom(location):
                        self.ways_to_go.append(((location[0]+1,location[1]), steps+1))

                if self.labyrith[location[0]][location[1]] == "F": 
                    if self.check_bottom(location):
                        self.ways_to_go.append(((location[0]+1,location[1]), steps+1))
                    if self.check_right(location):
                        self.ways_to_go.append(((location[0],location[1]+1), steps+1))

    def main_block(self):
        with open('Day10/input.txt', 'r') as file:
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            for line in puzzle_input:
                self.parser(line)
            self.traverser()
            return self.longest
        
if __name__ == "__main__":
    numb = Mazerunner()
    print(numb.main_block())

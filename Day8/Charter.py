
class Node:

    def __init__(self, left_node, right_node):
        self.left = left_node
        self.right = right_node

class Charter: 

    def __init__(self):
        self.numbers_list = []
        self.id_counter = 1
        self.directions = ""
        self.nodes = {}

    def traverser(self):
        location = "AAA"
        steps = 0
        while True:
            for i in self.directions:
                if i == "L":
                    location = self.nodes[location].left
                elif i == "R":
                    location = self.nodes[location].right
                steps += 1
                if location == "ZZZ":
                    return steps
            

    def main_block(self):
        with open('Day8/input.txt', 'r') as file:
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            directions = False
            skipline = True
            for line in puzzle_input:
                if directions == False:
                    self.directions = line
                    directions = True
                elif skipline == True:
                    skipline = False
                else:
                    self.nodes[line[:3]] = Node(line[7:10], line[12:15])
            #for i,j in self.nodes.items():
            #    print(i,j.left,j.right)
            steps = self.traverser()
            return steps
            
            
if __name__ == "__main__":
    numb = Charter()
    print(numb.main_block())

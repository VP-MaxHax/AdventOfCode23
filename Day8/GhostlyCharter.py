from math import gcd

# Funktio laskemaan kahden luvun LYN:n
def laske_lynn(a, b):
    return abs(a * b) // gcd(a, b)

def usean_numeron_lynn(*args):
    if len(args) < 2:
        raise ValueError("Tarvitaan vähintään kaksi lukua")
    
    lynn = args[0]
    for i in range(1, len(args)):
        lynn = laske_lynn(lynn, args[i])
    
    return lynn

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
        self.starts = []
        self.loop_legths = []
        self.first = []

    def loop_legth(self):
        for i in self.starts:
            last = 0
            steps=0
            first_time = True
            last_check = (0, "")
            checker = (0,"")
            loop = True
            position = i
            while loop:
                for j in self.directions:
                    if j == "R":
                        position = self.nodes[position].right
                    if j == "L":
                        position = self.nodes[position].left
                    steps += 1
                    if position[2] == "Z":
                        print(i, position)
                        checker = (steps-last, position)
                        if checker != (0, "") and not first_time:
                            loop = False
                            print(checker)
                            self.loop_legths.append(checker[0])
                            break
                        if first_time == True:
                            first_time = False
                            self.first.append((steps, i, position))
                        last = steps
                    #print(self.loop_legths)
                

    def traverser(self):
        old_steps = 0
        steps = 6340031855
        self.starts = ['VBT', 'PNJ', 'HCT', 'HMG', 'CDH', 'DCD']
        while True:
            for i in self.directions:
                temp_starts = []
                goal_reached = True
                for j in self.starts:
                    if i == "L":
                        next_node = self.nodes[j].left
                        temp_starts.append(next_node)
                        if next_node[2] != "Z":
                            goal_reached = False
                    elif i == "R":
                        next_node = self.nodes[j].right
                        temp_starts.append(next_node)
                        if next_node[2] != "Z":
                            goal_reached = False
                steps += 1
                if goal_reached:
                    return steps
                self.starts = temp_starts
            if steps-old_steps > 10000000:
                old_steps = steps
                with open('Day8/latest.txt', 'a') as latest:
                    latest.write(f'Current position: {self.starts}, Current step: {steps}\n')
            

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
                    if line[2] == "A":
                        self.starts.append(line[:3])
            self.loop_legth()
            print(self.first)
            value = 1
            yhteinen_lynn = usean_numeron_lynn(*self.loop_legths)
            return yhteinen_lynn
            #for i,j in self.nodes.items():
            #    print(i,j.left,j.right)
            #steps = self.traverser()
            #return steps

    def paths_converse(self):
        p1 = self.loop_legths[0]*2
        p2 = self.loop_legths[1]*2
        p3 = self.loop_legths[2]*2
        p4 = self.loop_legths[3]*2
        p5 = self.loop_legths[4]*2
        p6 = self.loop_legths[5]*2
        solid1 = self.loop_legths[0]
        solid2 = self.loop_legths[1]
        solid3 = self.loop_legths[2]
        solid4 = self.loop_legths[3]
        solid5 = self.loop_legths[4]
        solid6 = self.loop_legths[5]
        while True:
            if p1==p2 and p2==p3 and p3==p4 and p5==p6:
                return p3
            else:
                if min(p1,p2,p3,p4,p5,p6) == p1:
                    p1 += solid1
                if min(p1,p2,p3,p4,p5,p6) == p2:
                    p2 += solid2
                if min(p1,p2,p3,p4,p5,p6) == p3:
                    p3 += solid3
                if min(p1,p2,p3,p4,p5,p6) == p4:
                    p4 += solid4
                if min(p1,p2,p3,p4,p5,p6) == p5:
                    p5 += solid5
                if min(p1,p2,p3,p4,p5,p6) == p6:
                    p6 += solid6

                
            
if __name__ == "__main__":
    numb = Charter()
    print(numb.main_block())

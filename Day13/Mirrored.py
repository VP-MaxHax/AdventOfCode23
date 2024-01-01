
class Mirror: 

    def __init__(self):
        self.numbers_list = []
        self.id_counter = 1
        self.block = []
        self.v_check = False

    def check_block(self):
        self.v_check = False
        for i in range(1, len(self.block)):
            self.v_check = self.check_h_mirror(i, 0)
        if self.v_check == False:
            for i in range(1, len(self.block[0])):
                self.check_v_mirror(i, 0)

    def check_h_mirror(self, index, stage):
        print(self.block[index+stage])
        print(self.block[index-1-stage])
        if self.block[index+stage] == self.block[index-1-stage] and index-1-stage >= 0:
            try:
                self.check_h_mirror(index, stage+1)
            except IndexError:
                self.numbers_list.append(index*100)
                return True
        elif index-1-stage < 0:
            self.numbers_list.append(index*100)
            return True
        return False
        
    def check_v_mirror(self, index, stage):
        comp_1 = []
        comp_2 = []
        for i in range(len(self.block)):
            comp_1.append(self.block[i][index+stage])
            comp_2.append(self.block[i][index-1-stage])
        if comp_1 == comp_2 and index-1-stage >= 0:
            try:
                self.check_v_mirror(index, stage+1)
            except IndexError:
                self.numbers_list.append(index)
        elif index-1-stage < 0:
            self.numbers_list.append(index)





    def main_block(self):
        with open('Day13/input.txt', 'r') as file:
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            blocks= 0
            for line in puzzle_input:
                if line != "":
                    self.block.append(line)
                else:
                    blocks += 1
                    self.check_block()
                    print(len(self.numbers_list))
                    self.block = []
            self.check_block()
            print(blocks)
            print(self.numbers_list, len(self.numbers_list))
            return sum(self.numbers_list)
            


if __name__ == "__main__":
    numb = Mirror()
    print(numb.main_block())


# 28528 low
# 34805 High
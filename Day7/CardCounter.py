
class CardCounter: 

    def __init__(self):
        self.result = 0
        self.convert_table = {"T": 10, "J": 0, "Q": 12, "K": 13, "A": 14}
        self.five_of_a_kind = []
        self.four_of_a_kind = []
        self.fullhouse = []
        self.three_of_a_kind = []
        self.two_pair = []
        self.one_pair = []
        self.high_card = []

    def hand_checker(self, given_hand):
        current_hand = {}
        card_numb = 0
        jonglers = 0
        hand = [0,0,0,0,0,0]
        for i in given_hand[:5]:
            if i == "J":
                jonglers += 1
            if i in self.convert_table:
                hand[card_numb] = self.convert_table[i]
            else:
                hand[card_numb] = int(i)
            if i not in current_hand:
                current_hand[i] = 1
            else:
                current_hand[i] += 1
            card_numb += 1
        #print(given_hand[6:])
        hand[5] = int(given_hand[6:])
        if len(current_hand) == 1:
            self.five_of_a_kind.append(hand)
        elif len(current_hand) == 2:
            highestvalue = 0
            for key, value in current_hand.items():
                if value > highestvalue:
                    highestvalue = value
            if highestvalue == 4:
                if jonglers in (4, 1):
                    self.five_of_a_kind.append(hand)
                else:
                    self.four_of_a_kind.append(hand)
            else:
                if jonglers in (3, 2):
                    self.five_of_a_kind.append(hand)
                else:
                    self.fullhouse.append(hand)
        elif len(current_hand) == 3:
            highestvalue = 0
            for key, value in current_hand.items():
                if value > highestvalue:
                    highestvalue = value
            if highestvalue == 3:
                if jonglers in (3, 1):
                    self.four_of_a_kind.append(hand)
                else:
                    self.three_of_a_kind.append(hand)
            else:
                if jonglers == 2:
                    self.four_of_a_kind.append(hand)
                elif jonglers == 1:
                    self.fullhouse.append(hand)
                else:
                    self.two_pair.append(hand)
        elif len(current_hand) == 4:
            if jonglers in (2, 1):
                self.three_of_a_kind.append(hand)
            else:
                self.one_pair.append(hand)
        else:
            if jonglers == 1:
                self.one_pair.append(hand)
            else:
                self.high_card.append(hand)
        jonglers = 0

    def hand_sorter(self):
        self.five_of_a_kind.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))
        self.four_of_a_kind.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))
        self.fullhouse.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))
        self.three_of_a_kind.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))
        self.two_pair.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))
        self.one_pair.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))
        self.high_card.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))

    def main_block(self):
        with open('Day7/input.txt', 'r') as file:
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            for line in puzzle_input:
                self.hand_checker(line)
            #print(self.five_of_a_kind)
            #print(self.four_of_a_kind)
            #print(self.fullhouse)
            #print(self.three_of_a_kind)
            #print(self.two_pair)
            #print(self.one_pair)
            #print(self.high_card)
            self.hand_sorter()
            rank = 1
            for i in self.high_card:
                #print(i)
                self.result += i[5]*rank
                rank +=1
            for i in self.one_pair:
                #print(i)
                self.result += i[5]*rank
                rank +=1
            for i in self.two_pair:
                self.result += i[5]*rank
                rank +=1
            for i in self.three_of_a_kind:
                self.result += i[5]*rank
                rank +=1
            for i in self.fullhouse:
                self.result += i[5]*rank
                rank +=1
            for i in self.four_of_a_kind:
                #print(i)
                self.result += i[5]*rank
                rank +=1
            for i in self.five_of_a_kind:
                #print(i)
                self.result += i[5]*rank
                rank +=1
            return self.result
            


if __name__ == "__main__":
    numb = CardCounter()
    print(numb.main_block())

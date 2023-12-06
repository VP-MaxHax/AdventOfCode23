class CubeCounter: 

    def __init__(self):
        self.scorecard = []

    def main_block(self, times, distance):
        for i in range(len(times)):
            speed = 0
            timer = 0
            winningways = 0
            for j in range(0, times[i]):
                if (times[i]-timer)*speed > distance[i]:
                    winningways += 1
                speed += 1
                timer += 1
            self.scorecard.append(winningways)
        final_tally = 0
        for i in self.scorecard:
            if final_tally == 0:
                final_tally = i
            else:
                final_tally *= i
        return final_tally

if __name__ == "__main__":
    numb = CubeCounter()
    times1 = [35, 93, 73, 66]
    distance1 = [212, 2060, 1201, 1044]
    times2 = [35937366]
    distance2 = [212206012011044]
    print(numb.main_block(times2, distance2))

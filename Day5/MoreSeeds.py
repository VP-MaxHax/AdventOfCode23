class Seeder: 

    def __init__(self):
        self.countdown = 0
        self.bestloc = 0
        self.start = 9999999999999999
        self.stop = 0
        self.numbers_list = []
        self.id_counter = 1
        self.best = 99999999999999999999999
        self.more_seeds = []
        self.seeds = []
        self.soils = []
        self.fert = []
        self.water = []
        self.light = []
        self.temp = []
        self.hum = []
        self.loc = []



    def main_block(self):
        with open('Day5/input.txt', 'r') as file:
            puzzle_input = file.read()
            puzzle_input = puzzle_input.splitlines()
            typecount = 0
            for line in puzzle_input:
                if line[-3:-1] == "ap":
                    typecount += 1
                if typecount == 0 and line != "" and line[0] in "1234567890":
                    templist = []
                    number = ""
                    for i in line:
                        if i in "1234567890":
                            number += i
                        else:
                            templist.append(int(number))
                            number = ""
                    templist.append(int(number))
                    self.seeds.append(templist)
                if typecount == 1 and line != "" and line[0] in "1234567890":
                    templist = []
                    number = ""
                    for i in line:
                        if i in "1234567890":
                            number += i
                        else:
                            templist.append(int(number))
                            number = ""
                    templist.append(int(number))
                    self.soils.append(templist)
                if typecount == 2 and line != "" and line[0] in "1234567890":
                    templist = []
                    number = ""
                    for i in line:
                        if i in "1234567890":
                            number += i
                        else:
                            templist.append(int(number))
                            number = ""
                    templist.append(int(number))
                    self.fert.append(templist)
                if typecount == 3 and line != "" and line[0] in "1234567890":
                    templist = []
                    number = ""
                    for i in line:
                        if i in "1234567890":
                            number += i
                        else:
                            templist.append(int(number))
                            number = ""
                    templist.append(int(number))
                    self.water.append(templist)
                if typecount == 4 and line != "" and line[0] in "1234567890":
                    templist = []
                    number = ""
                    for i in line:
                        if i in "1234567890":
                            number += i
                        else:
                            templist.append(int(number))
                            number = ""
                    templist.append(int(number))
                    self.light.append(templist)
                if typecount == 5 and line != "" and line[0] in "1234567890":
                    templist = []
                    number = ""
                    for i in line:
                        if i in "1234567890":
                            number += i
                        else:
                            templist.append(int(number))
                            number = ""
                    templist.append(int(number))
                    self.temp.append(templist) 
                if typecount == 6 and line != "" and line[0] in "1234567890":
                    templist = []
                    number = ""
                    for i in line:
                        if i in "1234567890":
                            number += i
                        else:
                            templist.append(int(number))
                            number = ""
                    templist.append(int(number))
                    self.hum.append(templist)
                if typecount == 7 and line != "" and line[0] in "1234567890":
                    templist = []
                    number = ""
                    for i in line:
                        if i in "1234567890":
                            number += i
                        else:
                            templist.append(int(number))
                            number = ""
                    templist.append(int(number))
                    self.loc.append(templist)
            for i in range(int(len(self.seeds[0])/2)):
                self.more_seeds.append((self.seeds[0][i*2], self.seeds[0][i*2+1]+self.seeds[0][i*2]))
            for i in self.more_seeds:
                self.start = min(i[0], self.start)
                self.stop = max(i[0]+i[1], self.stop)
            self.countdown = self.stop-self.start
            self.seed_sorter()
            return self.best
    
    def seed_sorter(self):
        intcount = 0
        for j in self.more_seeds:
            progress = len(self.more_seeds)-intcount         
            self.start = 0
            self.stop = j[1]
            self.countdown = self.stop
            for i in range(j[0],j[1], 10000):
                self.countdown -= 10000
                print(self.best, self.bestloc, progress)
                soil = self.seed_to_soil(i)
                fert = self.soil_to_fert(soil)
                water = self.fert_to_water(fert)
                light = self.water_to_light(water)
                temp = self.light_to_temp(light)
                hum = self.temp_to_hum(temp)
                loc = self.hum_to_loc(hum)
                if loc < self.best:
                    self.best = loc
                    self.bestloc = i
        for i in range(self.bestloc-1000000, self.bestloc+1000000):
            print(self.best, self.bestloc)
            soil = self.seed_to_soil(i)
            fert = self.soil_to_fert(soil)
            water = self.fert_to_water(fert)
            light = self.water_to_light(water)
            temp = self.light_to_temp(light)
            hum = self.temp_to_hum(temp)
            loc = self.hum_to_loc(hum)
            if loc < self.best:
                self.best = loc
                self.bestloc = i

            intcount += 1
        return
    
    def seed_to_soil(self, seed):
        valuefound = False
        value = 999999999999999999999
        for i in self.soils:
            if seed > i[1] and seed < i[1]+i[2]:
                valuefound = True
                tempvalue = i[0]+(seed-i[1])
            if valuefound and tempvalue < value:
                value = tempvalue
        if valuefound == False:
            return seed
        if valuefound == True:
            return value
        
    def soil_to_fert(self, soil):
        valuefound = False
        value = 999999999999999999999
        for i in self.fert:
            if soil > i[1] and soil < i[1]+i[2]:
                valuefound = True
                tempvalue = i[0]+(soil-i[1])
            if valuefound and tempvalue < value:
                value = tempvalue
        if valuefound == False:
            return soil
        if valuefound == True:
            return value
        
    def fert_to_water(self, fert):
        valuefound = False
        value = 999999999999999999999
        for i in self.water:
            if fert >= i[1] and fert <= i[1]+i[2]-1:
                valuefound = True
                tempvalue = i[0]+(fert-i[1])
            if valuefound and tempvalue < value:
                value = tempvalue
        if valuefound == False:
            return fert
        if valuefound == True:
            return value
        
    def water_to_light(self, water):
        valuefound = False
        value = 999999999999999999999
        for i in self.light:
            if water >= i[1] and water <= i[1]+i[2]-1:
                valuefound = True
                tempvalue = i[0]+(water-i[1])
            if valuefound and tempvalue < value:
                value = tempvalue
        if valuefound == False:
            return water
        if valuefound == True:
            return value
        
    def light_to_temp(self, light):
        valuefound = False
        value = 999999999999999999999
        for i in self.temp:
            if light >= i[1] and light <= i[1]+i[2]-1:
                valuefound = True
                tempvalue = i[0]+(light-i[1])
            if valuefound and tempvalue < value:
                value = tempvalue
        if valuefound == False:
            return light
        if valuefound == True:
            return value
        
    def temp_to_hum(self, temp):
        valuefound = False
        value = 999999999999999999999
        for i in self.hum:
            if temp >= i[1] and temp <= i[1]+i[2]-1:
                valuefound = True
                tempvalue = i[0]+(temp-i[1])
            if valuefound and tempvalue < value:
                value = tempvalue
        if valuefound == False:
            return temp
        if valuefound == True:
            return value
        
    def hum_to_loc(self, hum):
        valuefound = False
        value = 999999999999999999999
        for i in self.loc:
            if hum >= i[1] and hum <= i[1]+i[2]-1:
                valuefound = True
                tempvalue = i[0]+(hum-i[1])
            if valuefound and tempvalue < value:
                value = tempvalue
        if valuefound == False:
            return hum
        if valuefound == True:
            return value    


if __name__ == "__main__":
    numb = Seeder()
    print(numb.main_block())
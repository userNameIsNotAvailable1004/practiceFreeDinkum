#satisFactoryCa

class Recipe():
    def __init__(self, name:str, output, mats:list, qtys:list):
        self.name = name
        self.output = output
        self.mats = mats
        self.qtys = qtys

    def makeAmount(self, amount):
        ans = []
        for qty in self.qtys:
            ans.append(amount/(self.output/qty))
        return ans
    
    def bindOne(self, recipeslist:list):
        ans = []
        for i in range(len(self.mats)):
            use = list( filter( lambda r : r.name == self.mats[i], recipeslist) )
            if(len(use) != 0):
                use = use[0]##각종 검정식 추천
                ans.append(use.makeAmount(self.qtys[i]))
                use.printBindings()
        return ans
    def printBindings(self):
        print(self.mats)
        print(self.qtys)


receipes = [Recipe("보강된 철판", 5, ["철판", "나사"], [30, 60])]
receipes.append(Recipe("철판", 20, ["철 주괴"], [30]))
receipes.append(Recipe("철봉", 15, ["철판"], [15]))
receipes.append(Recipe("나사", 40, ["철봉"], [10]))

userCube = []

# print(receipes[3].mats, receipes[3].makeAmount(60))
# # print(receipes[0].mats, receipes[0].makeAmount(1))
# print(receipes[1].mats, receipes[1].makeAmount(30))
print(receipes[0].bindOne([receipes[1],receipes[2],receipes[3]]))
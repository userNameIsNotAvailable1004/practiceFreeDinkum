###tenspape search algo

class TenBlock():
    def __init__(self, block_w, block_h):
        self.block_w = block_w
        self.block_h = block_h
        self.del_count = 0
        self.blockfiller = []

        for b in range(self.block_w):
            bf2 = []
            for bh in range(self.block_h):
                bf2.append(0)
            self.blockfiller.append(bf2)
        
    def notInRange(self, x, y):
        return (x <= 0 or y <= 0 or x >= self.block_w-1 or y >= self.block_h-1)

    def thereBlocked(self, x,y):
        return self.notInRange(x, y) or (not self.excepHorz(x,y) and (self.blockfiller[x][y] > 0))
    def thereSubBlocked(self, x,y):
        return (not self.excepHorz(x,y) and (self.blockfiller[x][y] == 1))


    """
        4방향 검색
    """

    def horc(self, x,y):
        ans = self.thereBlocked(x,y-1) and self.thereBlocked(x,y+1) and self.thereBlocked(x-1,y) and self.thereBlocked(x+1,y)
        return ans #십자상에 모두 블럭이 있을 시 or 블럭이 0과 인접해있을시 True
    
    def horcOne(self, x,y):
        ans = self.thereSubBlocked(x,y-1) and self.thereSubBlocked(x,y+1) and self.thereSubBlocked(x-1,y) and self.thereSubBlocked(x+1,y)
        return ans #십자상에 모두 서브블럭이 있을 시 or 블럭이 0과 인접해있을시 True
    
    def acrossOne(self, x, y):
        ansC= 0
        if(self.thereSubBlocked(x-1,y-1)):
            ansC += 1
        if(self.thereSubBlocked(x-1,y+1)):
            ansC += 1
        if(self.thereSubBlocked(x+1,y-1)):
            ansC += 1
        if(self.thereSubBlocked(x+1,y+1)):
            ansC += 1
        return ansC


    """
        대각선 검색
    """

    def across(self, x,y):
        ans = self.thereBlocked(x-1,y-1) and self.thereBlocked(x-1,y+1) and self.thereBlocked(x+1,y-1) and self.thereBlocked(x+1,y+1)
        return ans #대각선상에 모두 블럭이 있을 시 True
    
    def acrossTwo(self, x,y):
        if(not self.excepHorz(x, y) and (self.blockfiller[x+1][y-1] == 2 or self.blockfiller[x-1][y+1] == 2 or self.blockfiller[x-1][y-1] == 2 or self.blockfiller[x+1][y+1] == 2)):
            return True

    def acrossZero(self, x,y):
        if(not self.excepHorz(x, y) and (self.blockfiller[x+1][y-1] == 0 or self.blockfiller[x-1][y+1] == 0 or self.blockfiller[x-1][y-1] == 0 or self.blockfiller[x+1][y+1] == 0)):
            return True
    

    """
        블럭 삭제관련
    """

    def delhorc(self, x,y):
        self.blockfiller[x][y]   = 0
        self.blockfiller[x][y-1] = 0 
        self.blockfiller[x][y+1] = 0
        self.blockfiller[x-1][y] = 0
        self.blockfiller[x+1][y] = 0
        self.del_count += 1

    def delnearhorc(self, x,y):
        if(self.excepHorz(x,y)):
            return
        if(self.blockfiller[x][y] == 0):
            return
        if(self.blockfiller[x][y-1] >= 2):
            self.delhorc(x,y-1)
        elif(self.blockfiller[x][y+1] >= 2):
            self.delhorc(x,y+1)
        elif(self.blockfiller[x-1][y] >= 2):
            self.delhorc(x-1,y)
        elif(self.blockfiller[x+1][y] >= 2):
            self.delhorc(x+1,y)

    def dellercomfortable(self, x, y):
        count += 1
        if(self.excepHorz(x,y)):
            return 0
        if(self.thereBlocked(x,y-1)):
            count+=1
        elif(self.thereBlocked(x,y+1)):
            count+=1
        elif(self.thereBlocked(x-1,y)):
            count+=1
        elif(self.thereBlocked(x+1,y)):
            count+=1
        return count



    def checker(self, x, y):
        """
            x, y 인접한 4방향(블럭 단위)이 모두 차 있을 시 TRUE를 반환합니다
        """
        if(self.excepHorz(x, y)):
            return False
        elif(self.blockfiller[x][y] > 0 or self.blockfiller[x][y-1] > 0 or self.blockfiller[x][y+1] > 0 or self.blockfiller[x-1][y] > 0 or self.blockfiller[x+1][y] > 0):
            return False
        else:
            return True
    
    def __inserter__(self, x, y):
        """
            삽입 구문 삭제 없이 사용하지 말 것
        """
        if(self.checker(x,y)):
            self.blockfiller[x][y] = 2
            self.blockfiller[x][y-1] = 1
            self.blockfiller[x][y+1] = 1 
            self.blockfiller[x-1][y] = 1 
            self.blockfiller[x+1][y] = 1
            return True
        else: return False

    def deleteAndInsert(self, bw, bh):
        try:
            self.delnearhorc(bw,bh)
            self.delnearhorc(bw-1,bh)
            self.delnearhorc(bw+1,bh)
            self.delnearhorc(bw,bh-1)
            self.delnearhorc(bw,bh+1)
            self.__inserter__(bw, bh)
            return bw, bh
        except:
            print("reangeOut",bw,bh)

    def logblock(self):
        print("=====================================")
        for b in range(self.block_h):
            mistersee = ""
            for bh in range(self.block_w):
                if(self.blockfiller[bh][b]==0):
                    mistersee += "   "
                elif(self.blockfiller[bh][b]==1):
                    mistersee += " # "
                else:
                    mistersee += " @ "
            print("l", mistersee, "l")
            
        print("=====================================")

    
    def roundZero(self, x, y): #0이 다른 블럭에 의해 둘러쌓임
        if(not self.excepHorz(x, y) and self.blockfiller[x][y] == 0 and (self.horc(x,y) and self.across(x,y))):
            return True
    def roundZero22(self, x,y): #다른 블럭에 완전히 둘러쌓임
        if(not self.excepHorz(x, y) and (self.horc(x,y) and self.across(x,y))):
            return True
        else:
            return False
    def roundTwo(self,x,y):
        if(not self.excepHorz(x, y) and self.blockfiller[x][y] == 2 and (self.horc(x,y) and self.across(x,y))):
            return True
        elif(mainBlock.inroundzero(x,y) and mainBlock.roundZero(x,y)):
            return True
        else:
            return False

    def inroundzero(self, x, y): #[0]에 소속되지 않음
        if(x >= self.block_w - 1 or x <= 0 or y >= self.block_h- 1 or y <= 0):
            return True
        else: return False
        
    # def roundedone():
    def excepHorz(self, x, y):
        if(x <= 0 or y <= 0 or y >= self.block_h-1 or x >= self.block_w-1):
            return True
        else: return False
    def horizGetThanks(self, x,y):
        return (self.roundTwo(x+1,y) or self.roundTwo(x,y-1) or self.roundTwo(x,y+1) or self.roundTwo(x-1,y))
    def horzisGetWorse(self, x,y):
        return ((self.roundZero22(x+1,y) or self.roundZero22(x,y-1) or self.roundZero22(x,y+1) or self.roundZero22(x-1,y)) and not self.horizGetThanks(x,y))
    def acrossGetThanks(self, x,y):
        return (self.roundTwo(x+1,y+1) or self.roundTwo(x-1,y-1) or self.roundTwo(x+1,y-1) or self.roundTwo(x-1, y+1))
    def acrossGetWorse(self, x,y):
        return ((self.roundZero(x+1,y+1) or self.roundZero(x-1,y-1) or self.roundZero(x+1,y-1) or self.roundZero(x-1, y+1)) and not self.acrossGetThanks(x,y))

                
    def mostRoundZero(self, x, y):
        count = 0
        axis = yeiAcro(x,y)
        axis2 = yeihorc(x,y)
        for i in range(4):
            axisX, axisY = next(axis)
            axis2X, axis2Y = next(axis2)
            if(self.thereisZero(axisX, axisY)):
                count+=1
            if(self.thereisZero(axis2X, axis2Y)):
                count+=1
        return count
    
    def thereisZero(self, x, y):
        return not self.excepHorz(x,y) and ((self.blockfiller[x][y] > 0))
    


    def getBlockfiller(self, x, y):
        if(self.block_w > x and 0 < x and self.block_h > y and 0 < y):
            return self.blockfiller[x][y]
        else: return -1
    

    def setBlock(self, temp):
        self.blockfiller = temp
    
    def coppySelf(self):
        copy = []
        for i in self.blockfiller:
            copyTemp = []
            for j in i:
                copyTemp.append(j)
            copy.append(copyTemp)
        ans = TenBlock(self.block_w, self.block_h)
        ans.setBlock(copy)
        return ans

    
    


    # def acrossBlockNotInRange(self, x,y):
    #     if(self.notInRange(x+1,y+1) or self.notInRange(x-1,y-1) or self.notInRange(x+1,y-1) or self.notInRange(x-1, y+1)):
    #         return True
    
    # def sureImDelete(self, x, y):
    #     temp = self.acrossTwoMainBlock(x, y)
    #     if(len(temp) >= 2):
    #         tAxisX, tAxisY = self.getMostZero(temp)
    #         self.delnearhorc(tAxisX, tAxisY)
  
            
            
    # def acrossTwoMainBlock(self, x, y):
    #     twoContainAxisList = []
    #     if(self.excepHorz(x, y)):
    #         return []
    #     axis = yeiAcro(x,y)
    #     for i in range(4):
    #         a, b = next(axis)
    #         if(self.getBlockfiller(a, b) == 2):
    #             twoContainAxisList.append((a, b))
    #     return twoContainAxisList
    
    # def getMostZero(self, twoContainAxisList):
    #     a,b = 0, 0
    #     max = 0
    #     for x, y in twoContainAxisList:
    #         newt = self.mostRoundZero(x,y)
    #         if (max < newt):
    #             max = newt
    #             a,b = x,y

    #     return a,b

        

        


def yeihorc(x,y):
    yield x, y-1
    yield x, y+1
    yield x-1, y
    yield x+1, y
    
def yeiAcro(x,y):
    yield x-1, y-1
    yield x-1, y+1
    yield x+1 , y-1
    yield x+1, y+1







# def futureRoundHole():

    
# def canPass(x,y):
#     return not roundZero(x,y)

def getMax(point:list):
    max = point[1]
    for i in point:
        if(max < i):
            max = i 
    return max

def horzcalla(x,y ,ox, oy,bx,by):
    point = [checkPoint(x, y, ox, oy, bx, by, x,y),checkPoint(x+1, y, ox, oy, bx, by, x,y),checkPoint(x,y-1, ox, oy, bx, by , x,y),checkPoint(x, y+1, ox, oy, bx, by , x,y ),checkPoint(x-1, y, ox, oy, bx,by, x,y)]
    maxPoint = getMax(point)
    # print(point)
        
    if(point[1] == maxPoint and ( ox != x+1 and y != oy and bx != x+1 and by != y) and not mainBlock.inroundzero(x+1, y)):
        return x+1, y , point[1]
    if(point[2] == maxPoint and ( ox != x and y-1 != oy and bx != x and by != y-1 ) and not mainBlock.inroundzero(x, y-1)):
        return x, y-1 , point[2]
    if(point[3] == maxPoint and ( ox != x and y+1 != oy and bx != x and by != y+1) and not mainBlock.inroundzero(x, y+1)):
        return x, y+1 , point[3]
    if(point[4] == maxPoint and ( ox != x-1 and y != oy and bx != x-1 and by != y) and not mainBlock.inroundzero(x-1, y)):    
        return x-1, y , point[4]
    
    return -1, -1, -100
    


def checkPoint(x, y, ox, oy, bx, by, x2,y2): #우선순위 탐색
    point = 0
    #포인트가 배치 안 되는 쪽이 점수 더 먹으니까..........
    testCopy = getCopyToTest(x,y)
    #
    # if(mainBlock.inroundzero(x,y)):
    #     return -100
    if(mainBlock.getBlockfiller(x2,y2) == 1):
        point -= 4
    if(testCopy.acrossTwo(x,y)):
        point -= 2
    if(mainBlock.acrossTwo(x,y)):
        point -= 1
    if(mainBlock.roundZero22(x,y)):
        point -= 4
    if(mainBlock.horzisGetWorse(x,y)):
        point -= 1
    if(testCopy.acrossGetWorse(x,y)):
        point -= 2
    if(testCopy.horzisGetWorse(x,y)):
        point -= 2
    point -= testCopy.del_count
    # if(mainBlock.getBlockfiller(x2+x2-bx, y2+y2-by)==0):
    #     print("dd")
    # if(bx==9 and by== 10):
    #     print(point,"Tlt", x, y)
    if(testCopy.horizGetThanks(x,y)):
        point += 3
    if(testCopy.acrossGetThanks(x,y)):
        point += 3
    point += testCopy.acrossOne(x,y)/2
    if(mainBlock.checker(x, y)):
        point += 4
    
    point += ((mainBlock.mostRoundZero(x,y)) - testCopy.mostRoundZero(x,y))/4

    return point


def getCopyToTest(x,y):
    copy = mainBlock.coppySelf()
    copy.deleteAndInsert(x,y)
    
    return copy

def acrossHolePort(x,y):
    # print("기준",x,y)
    wow = []

    if(not mainBlock.inroundzero(x-1, y+1) and mainBlock.getBlockfiller(x-1, y+1) == 0):
        a,b,p = horzcalla(x-1, y+1, x+1, y-1 ,x, y)
        if(not mainBlock.inroundzero(a,b)):
            wow.append([a,b,p])
    if(not mainBlock.inroundzero(x+1, y+1) and mainBlock.getBlockfiller(x+1, y+1) == 0):
        a,b,p = horzcalla(x+1, y+1, x-1, y-1,x, y)
        if(not mainBlock.inroundzero(a,b)):
            wow.append([a,b,p])
    if(not mainBlock.inroundzero(x+1, y-1) and mainBlock.getBlockfiller(x+1, y-1) == 0):
        a,b,p = horzcalla(x+1, y-1, x-1, y+1, x, y)
        if(not mainBlock.inroundzero(a,b)):
            wow.append([a,b,p])
    if(not mainBlock.inroundzero(x-1, y-1) and mainBlock.getBlockfiller(x-1, y-1) == 0):
        a,b,p = horzcalla(x-1, y-1, x+1, y+1,x, y)
        if(not mainBlock.inroundzero(a,b)):
            wow.append([a,b,p])
    
    if(len(wow)==0):
        return -1, -1

    max = [0,0,-100]
    for w in wow:
        if(w[2]>max[2]):
            max = w
    return max[0],max[1]


def oneMoreThings(x,y):
    a,b = acrossHolePort(x,y)
    if(a == -1):
        return True
    else:
        # print(a,b)
        mainBlock.deleteAndInsert(a,b)
        # mainBlock.logblock()
        return False
def filtsecondaryround():
    for bh in range(mainBlock.block_h):
        for bw in range(mainBlock.block_w):
            if(not mainBlock.roundZero22(bw,bh)):
                if(mainBlock.blockfiller[bw][bh] == 2 and not mainBlock.inroundzero(bw,bh)):
                    ahTT = oneMoreThings(bw,bh)
                    if(ahTT == False):
                        return True 
                
    return False


def searchdrone():
    count = 0
    mainBlock.deleteAndInsert(1,1)

    try:
        while(True):
            ah = filtsecondaryround()
            count += 1
            if(count > 30):
                print("Notice Stop : count Range Over cause count :",count,"range Out")
                break
            if(ah == False):
                print("Notice Stop : nothing can Searchable")
                break
    except:
        print("예상치 못 한 오")
    mainBlock.logblock()
    print("end")



block_w = 11
block_h = 15

mainBlock = TenBlock(block_w, block_h)

searchdrone()



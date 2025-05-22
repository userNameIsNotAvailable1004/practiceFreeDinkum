#CropsCa
# cropsList = 
# [{"name":"식물이름",
# "seed":씨앗가격(int),
# "BaseSelling":기본 판매가(int)}]

#shella = 2.5 쉘라의 곱셈 판매가격
#commerce = [5, 10, 15] 자격증의 곱셈 판매가격
#연산은 모두 곱한 후 int로 바뀌어짐 
# 반올림이 됨은 확인 반내림은 확인 필요

import re
import math

shella = 2.5 #쉘라의 곱셈 판매가격

commerce = [5, 10, 15] #자격증의 곱셈 판매가격

cropsList = [
    {"name": "Beetroot", "seed" : 570, "BaseSelling" : 1425, "days" : 7, "regrow":0},
    {"name": "Cabbage", "seed" : 700, "BaseSelling" : 1750, "days" : 7, "regrow":0},
    {'name': 'Carrot', 'seed': 570, 'BaseSelling': 475, 'days': 6, 'regrow': 0, 'minimumY':3},
    {"name": "Sugar Cane", "seed" :400, "BaseSelling" : 840, "days" : 11, "regrow":0},
    {'name': 'Corn', 'seed': 1100, 'BaseSelling': 358, 'days': 10, 'regrow': 5, 'minimumY':2},
    {'name': 'Green Bean', 'seed': 1360, 'BaseSelling': 295, 'days': 10, 'regrow': 5, 'minimumY':3},
    {'name': 'Kale', 'seed': 760, 'BaseSelling': 1520, 'days': 5, 'regrow': 0},
    {'name': 'Onion', 'seed': 540, 'BaseSelling': 450, 'days': 7, 'regrow': 0, 'minimumY':3},
    {'name': 'Potato', 'seed': 640, 'BaseSelling': 640, 'days': 9, 'regrow': 0, 'minimumY':3},
    {'name': 'Pumpkin', 'seed': 780, 'BaseSelling': 3120, 'days': 11, 'regrow': 7},
    {'name': 'Rice', 'seed': 120, 'BaseSelling': 144, 'days': 9, 'regrow': 0},
    {'name': 'Tomato', 'seed': 1620, 'BaseSelling': 351, 'days': 10, 'regrow': 5, 'minimumY':3},
    {'name': 'Watermelon', 'seed': 770, 'BaseSelling': 3080, 'days': 10, 'regrow': 6},
    {'name': 'Wheat', 'seed': 360, 'BaseSelling': 216, 'days': 9, 'regrow': 0, 'minimumY':2},
    {'name': 'Hope Wheat', 'seed': 360, 'BaseSelling':1080, 'days': 9, 'regrow': 0}
    ]

regrowcrops = ['Corn', 'Green Bean', 'Tomato']

def printTotalLog(cropsList):
    name , max, days = "",0, 1
    name2 , max2, days2 = "",0,1
    for c in cropsList:
        totalPrice = c["BaseSelling"]
        minimumY = c.get('minimumY')
        if(minimumY != None):
            totalPrice *= minimumY
        maxPrice = round(totalPrice*((commerce[2]+100)/100)*shella)
        if(c["regrow"]==0):
            if(max < maxPrice):
                name, max, days = c["name"], maxPrice, c["days"]
            if(max2/days2 < maxPrice/c["days"]):
                name2, max2, days2 = c["name"], maxPrice, c["days"]
            
        print("============================================")
        print("종자 : ",c["name"]," 씨앗 가격 : ",c["seed"], " 재배기간 : ", c["days"])
        print("최고 판매가격 : ",maxPrice," 씨앗 차액 : ", maxPrice - c["seed"])
        print("기본 판매가격 : ",totalPrice," 기본 판매가격 - 씨앗 차액 : ", totalPrice  - c["seed"])
       
    print("====== 추가 재배 가능 품목 제외 =======")
    print("최고 이득 종목 : ",name,"최고가 : " ,max," 일별 : ",max/days)
    print("날짜 기반 최고 이득 종목  : ",name2," 최고가 : " ,max2, " 일별 : ",max2/days2)
    print("====== 추가 재배 가능 품목 =======")
    moreRegrowCa(cropsList)
    print("=============================================")


def moreRegrowCa(cropsList):
    temp = list(filter(localFinder ,cropsList))
    for t in temp:
        maxdays = 58 - t["days"]
        availableTime = math.floor(maxdays /  t["regrow"]) + 1
        maxPrice = availableTime*t["minimumY"]*((commerce[2]+100)/100)*shella*t["BaseSelling"]
        print("종자 : ", t["name"], " 의 최고 수익" ,maxPrice)
        

def localFinder(c):
    for r in regrowcrops:
        if r == c["name"]:
            return True

printTotalLog(cropsList)

# text = """
#  Carrot	 570	Winter	6 days	4	3	
#  +5

#  +5

#  475
# """

def incodeCrops(text):
    text = text.replace(",","")
    text = text.replace("\t","")
    listte = re.split(r'(\d+)', text)
    listte = [i.strip() for i in listte]
    filtCrops(listte)

def filtCrops(listte):
    cropTemp = {"name":listte[0],"seed":int(listte[1]),"BaseSelling":int(listte[-2]),"days":int(listte[3])}
    regrow = isReGrow(listte)
    if(regrow != -1): 
        cropTemp["regrow"] = int(listte[regrow-1])
    else : cropTemp["regrow"] = 0
    print(cropTemp)

def isReGrow(listte):
    for c in listte:
        if c.count("regrow") > 0:
            return listte.index(c)
    return -1

# incodeCrops(text)
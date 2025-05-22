import math

"""
이자는 1/7% 즉 0.(1/7) 1/700가 하루후에 발생함
복리임
소수점은 반내림 함
10억 이후  1428571
"""
print("1. 원하는 금액에 도달하기 위해 필요한 일수 계산")
print("2. 원하는 일수가 지난 후에 통장에 들어있는 돈")

def flowans(a):
    return math.floor(a/700)

selectplayer = input("=>")


print("입금액 입력")
firstInner = int(input("숫자만 입력하세요. 검증과정 없습니다 =>"))

if firstInner > 999999000:
    print("이자가 필요있는 양심이 아닙니다.")
    selectplayer = "1234"
elif firstInner < 700:
    print("이자가 발생할 수 있는 양심이 아닙니다.")
    selectplayer = "1234"

if selectplayer == "1":
    finalans = int(input("원하는 금액 입력 검증과정 없습니다 =>"))
    extra = 0
    nowc = firstInner
    count = 0
    if finalans > 1000000000:
        extra = int(finalans-1000000000)
        finalans = 1000000000        
        extra = round(extra/1428571)
    while (finalans >= nowc):
        nowc += flowans(nowc)
        count += 1
    # ans = math.log(finalans/firstInner, 701/700)
    print(count +extra)

elif selectplayer == "2":
    finalans = int(input("원하는 일수 입력 검증과정 없습니다 =>"))
    for i in range(finalans):
        firstInner += flowans(firstInner)
    print(firstInner)
        
    
else: print("유효한 입력값이.. 중대장은 실망했다...")


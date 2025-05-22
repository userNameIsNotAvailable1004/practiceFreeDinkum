def autosumself():
    text = input("self.)")
    textList  = text.split(",")
    textList = [i[:(i.index("="))] for i in textList]
    textList = [i.strip() for i in textList] 
    output = []
    for i in textList:
        output.append("self."+ i + " = " + i)
        
    print("========절취선==========")
    for o in output:
        print(o)
    print("========절취선==========")
autosumself()
#supporter

a="""8  Brick Fence	2  Stone
1  Bag of Cement	
Base Price
 4
Commerce 1
 4
Commerce 2
 4
Commerce 3
 5
2  Brick Flower Bed	2  Bag of Cement
1  Stone	
Base Price
 19
Commerce 1
 20
Commerce 2
 21
Commerce 3
 22"""

a, b = a[:a.find("Base Price")] ,a[a.find("Commerce 3"):]
print(a)
b = b[b.find("\n",12):]
print(b)


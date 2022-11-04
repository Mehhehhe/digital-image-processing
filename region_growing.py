# Simple region growing

class Point:
    def __init__(self, dataVal, next = None):
        self.dataVal = dataVal
        self.rightVal = None
        self.topVal = None
        self.leftVal = None
        self.bottomVal = None
        self.nextFirstSubArrVal = None
    
    def nextVal(self):
        return self.rightVal if self.rightVal != None else self.nextFirstSubArrVal
    
    def allDirectionVals(self):
        return {
            "center": self.dataVal,
            "right": self.rightVal,
            "top": self.topVal,
            "left": self.leftVal,
            "bottom": self.bottomVal
        }
    
    def setRight(self, right):
        newRight = Point(right)
        self.rightVal = newRight
    
    def setTop(self, top):
        newTop = Point(top)
        self.topVal = newTop
    
    def setLeft(self, left):
        newLeft = Point(left)
        self.leftVal = newLeft
    
    def setBottom(self, bottom):
        newBottom = Point(bottom)
        self.bottomVal = newBottom
    
    def setNext(self, nextLine):
        newNext = Point(nextLine)
        self.nextFirstSubArrVal = newNext


def setNeighbor(data: list):
    temp = [[None for _ in range(len(data[0]))] for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            temp[i][j] = Point(data[i][j])
            # Set directions
            temp[i][j].setRight(data[i][j+1] if j+1 < len(data[0]) else None)
            temp[i][j].setTop(data[i-1][j] if i-1 >= 0 else None)
            temp[i][j].setLeft(data[i][j-1] if j-1 >= 0 else None)
            temp[i][j].setBottom(data[i+1][j] if i+1 < len(data) else None)
            if j == len(data[0]) - 1 :
                temp[i][j].setNext(data[i+1][0] if i+1 < len(data) else None)
    return temp

def region_growing(data, delta):
    temp_col = []
    temp_row = []
    temp_div = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            # Column checking
            temp_col.append(data[i][j].dataVal)
            if data[i][j].rightVal.dataVal is None:
                break
            if abs(data[i][j].rightVal.dataVal - data[i][j].dataVal) >= delta:
                temp_col.append(0)
            # Check below point if equal or exceed delta
            if data[i][j].bottomVal.dataVal != None:
                if abs(data[i][j].dataVal - data[i][j].bottomVal.dataVal) >= delta:
                    temp_div.append(".")
                else:
                    temp_div.append("-")
        temp_row.append(temp_col)        
        temp_row.append(temp_div)
        temp_div = []
        temp_col = []
    return temp_row

test = [
    [90, 99, 93, 89, 105, 110, 109, 109],
    [97, 92, 94, 88, 99, 100, 105, 100],
    [95, 88, 90, 82, 92, 93, 101, 102],
    [89, 90, 101, 107, 103, 105 ,111, 113],
    [87, 92, 105, 109, 100, 107, 105, 105],
    [89, 90, 101, 109, 108, 101, 102, 101]
]

ps = setNeighbor(test)
rg = region_growing(ps, 10)

for i in range(len(rg)):
    print(rg[i])
# Simple split_merge by Pakin

import math

class Segment:
    def __init__(self, name, data):
        self.group_name = name
        self.pixels = data

        self.mean = self.get_mean()
        self.variance = self.get_variance()
    
    def get_mean(self):
        sum = 0
        for i in self.pixels:
            sum += i
        return sum/len(self.pixels)
    
    def get_variance(self):
        sum = 0
        for i in self.pixels:
            sum += (i - self.mean)**2
        return math.sqrt(sum/len(self.pixels))

def split(data):
    seg_list = []
    segA = []
    segB = []
    segC = []
    segD = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if i < len(data)//2 and j < len(data[0])//2:
                segA.append(data[i][j])
            elif i < len(data)//2 and j >= len(data[0])//2:
                segB.append(data[i][j])
            elif i >= len(data)//2 and j < len(data[0])//2:
                segC.append(data[i][j])
            elif i >= len(data)//2 and j >= len(data[0])//2:
                segD.append(data[i][j])
    return [Segment("A", segA), Segment("B", segB), Segment("C", segC), Segment("D", segD)]

def sub_split(data, variance):
    arr_need_to_split = []
    if data.variance > variance:
        arr_need_to_split.append(data.pixels)
    # Transform into 2d array
    temp = []
    temp_left = []
    temp_right = []
    isLeftSide = True; isRightSide = False
    for i in range(len(arr_need_to_split)):
        for j in range(0,len(arr_need_to_split[0]), 2):
            if j+2 >= len(arr_need_to_split[0]):
                temp_right.append(arr_need_to_split[i][j:j+2])
                isLeftSide = True; isRightSide = False
            else:
                if isLeftSide:
                    temp_left.append(arr_need_to_split[i][j:j+2])
                    isLeftSide = False
                    isRightSide = True
                elif isRightSide:
                    temp_right.append(arr_need_to_split[i][j:j+2])
                    isLeftSide = True
                    isRightSide = False
    
    temp = [
        Segment("E", [left_sub for left in temp_left for left_sub in left]),
        Segment("F", [right_sub for right in temp_right for right_sub in right])
        ]
    return temp

test2 = [
    [90, 99, 93, 89, 105, 110, 109, 109],
    [97, 92, 94, 82, 95, 104, 105, 98],
    [95, 88, 90, 89, 99, 94, 101, 102],
    [89, 90, 101, 107, 103, 105 ,111, 113],
    [87, 92, 105, 109, 100, 107, 105, 105],
    [89, 90, 101, 109, 108, 101, 102, 101]
]

VARIANCE = 6
MEAN = 3

segment_split = split(test2)

#       |
#   A   |   B   
# --------------
#   C   |   D
#       |

print("<------------- Group list -------------->")
for sg in segment_split:
    print("Group: ",sg.group_name," = \t",sg.pixels, "\t",sg.mean, "\t",sg.variance)

# Group C needs to split again if using variance = 6, so
segment_split2 = sub_split(segment_split[2], VARIANCE)
segment_split.pop(2)

#       |
#   A   |   B   
# --------------
#  E|  F|   D
#  |    |
print("\nSplitting C ... \n")
for sg in segment_split2:
    print("Group: ",sg.group_name," = \t",sg.pixels, "\t\t\t\t",sg.mean, "\t",sg.variance)
    segment_split.append(sg)

print("C is splitted into E and F\n\nConnections:")
temp_seg = 0
for index in range(len(segment_split)):
    # print("Group: ",sg.group_name," = \t",sg.pixels, "\t",sg.mean, "\t",sg.variance)
    if index + 1 < len(segment_split):
        if abs(segment_split[index].mean - segment_split[index+1].mean) <= MEAN:
            print("Group ", segment_split[index].group_name , " can connect with ", segment_split[index+1].group_name)
    if index + 2 < len(segment_split):
        if abs(segment_split[index].mean - segment_split[index+2].mean) <= MEAN:
            print("Group ", segment_split[index].group_name , " can connect with ", segment_split[index+2].group_name)
    if index + 3 < len(segment_split):
        if abs(segment_split[index].mean - segment_split[index+3].mean) <= MEAN:
            print("Group ", segment_split[index].group_name , " can connect with ", segment_split[index+3].group_name)
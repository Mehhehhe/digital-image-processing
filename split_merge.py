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



test = [
    [90, 99, 93, 89, 105, 110, 109, 109],
    [97, 92, 94, 88, 99, 100, 105, 100],
    [95, 88, 90, 82, 92, 93, 101, 102],
    [89, 90, 101, 107, 103, 105 ,111, 113],
    [87, 92, 105, 109, 100, 107, 105, 105],
    [89, 90, 101, 109, 108, 101, 102, 101]
]

test2 = [
    [90, 99, 93, 89, 105, 110, 109, 109],
    [97, 92, 94, 82, 95, 104, 105, 98],
    [95, 88, 90, 89, 99, 94, 101, 102],
    [89, 90, 101, 107, 103, 105 ,111, 113],
    [87, 92, 105, 109, 100, 107, 105, 105],
    [89, 90, 101, 109, 108, 101, 102, 101]
]

segment_split = split(test2)
print(segment_split[0].pixels, segment_split[0].mean, segment_split[0].variance)
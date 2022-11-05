# Simple histogram & equalization by Pakin

import matplotlib.pyplot as plt

# Total pixel from level 0 to 15
test_pic1 = [8060, 7091, 11228, 13397, 15715, 5544, 2628, 1290, 362, 221, 0, 0, 0, 0, 0, 0]
test_pic2 = [7767, 4880, 4690, 8878, 9177, 10493, 8945, 4718, 4417, 1571, 0, 0, 0, 0, 0, 0]

GREY_LEVEL = range(0,16)

# plt.plot(GREY_LEVEL, test_pic1)
# plt.plot(GREY_LEVEL, test_pic2)
# plt.bar(GREY_LEVEL, test_pic1)
# plt.bar(GREY_LEVEL, test_pic2)
# plt.show()

class Equalize:
    def __init__(self, data, grey_level = GREY_LEVEL):
        self.origin_pixels_list = data
        self.total_sum = self.sum_on_each_level()
        self.grey_levels = list(grey_level)
        self.norm_list = self.normalize()
        self.new_pixs = self.new_number_of_pixels()
    
    def sum_on_each_level(self):
        temp = [];sum = 0
        for i in range(len(self.origin_pixels_list)):
            if self.origin_pixels_list[i] == 0:
                sum += 0
                temp.append(0)
            else:
                sum += self.origin_pixels_list[i]
                temp.append(sum)
        return temp

    def normalize(self):
        total_pixs = sum(self.origin_pixels_list)
        norm = []
        for i in self.total_sum:
            norm.append(int((i/total_pixs) * self.grey_levels[len(self.grey_levels) - 1]))
        return norm

    def new_number_of_pixels(self):
        new_pixs = [None] * len(self.norm_list)
        previous = 10000
        current = 0
        for i in self.norm_list:
            current = self.norm_list.index(i) if current != previous else current + 1
            if current > len(self.norm_list) - 1:
                break
            if self.norm_list.count(i) > 1 and i != 0:
                ind_list = [ind for ind, item in enumerate(self.norm_list) if item == i]
                sum_t = 0
                for target in ind_list:
                    sum_t += self.origin_pixels_list[target]
                for t in ind_list:
                    new_pixs[t] = sum_t
            else:
                new_pixs[current] = self.origin_pixels_list[current]
            previous = current
        return new_pixs

img1 = Equalize(test_pic1)
print("Each level summations: ", img1.total_sum, "\n\nNormalized: ", img1.norm_list, "\n\nNew pixels: ", img1.new_pixs)
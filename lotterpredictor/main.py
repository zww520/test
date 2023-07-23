import os;
import rule;
import random;
import crawler;

def getCombinationNun(a, b):  # C(a, b) C(5, 35)
    res = 1
    for i in range(b-a+1, b):
        res = res * i
    return res

def NoC(a, b):
    return getCombinationNun(a, b)

def test():
    result_map = dict()
    num = 100
    for iter in range(0, num):
        random_num = []  
        random_digit = []  
        random_digit.extend(random.sample(range(1, 36), 5))
        random_digit.extend(random.sample(range(1, 13), 2))
        for val in random_digit:
            random_num.append(str(val).zfill(2))
        random_num = ' '.join(random_num)  
        print(random_num)
        level = rule.getWinningLotterLevel(random_num, "10	26	29	32	33	03	11")
        if level in result_map:
            result_map[level] += 1
        else:
            result_map[level] = 1   
    # print(result_map)
    total_income = -2 * num
    for k in result_map.keys():
        total_income += rule.getPrizeAmount(k) * result_map[k]
        print("level {} : {}".format(k, result_map[k]))
    print("total income {}".format(total_income))
    x = 2
    y = 1
    print((NoC(x, 5) * NoC(5-x, 30) * NoC(y, 2) * NoC(2-y, 10))/(NoC(5, 35)* NoC(2, 12)))

    x = 3
    y = 0
    print((NoC(x, 5) * NoC(5-x, 30) * NoC(y, 2) * NoC(2-y, 10))/(NoC(5, 35)* NoC(2, 12)))

    x = 0
    y = 2
    print((NoC(x, 5) * NoC(5-x, 30) * NoC(y, 2) * NoC(2-y, 10))/(NoC(5, 35)* NoC(2, 12)))
    print(NoC(5-x, 30) / (NoC(5, 35)))

if __name__ == '__main__':
    crawler.crawData()




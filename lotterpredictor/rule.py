def isValidNumber(num : str) -> bool:
    num_list = str(num).split(' ')
    ret = False
    if len(num_list) == 7:
        ret = True
        for i in range(0, 5):
            ret &= isValidAnteriorRegionNumber(int(num_list[i]))
        for i in range(5, 7):
            ret &= isValidPosteriorRegionNumber(int(num_list[i]))        
    return ret


def isValidAnteriorRegionNumber(num : int) -> bool:
    ret = True
    if num < 1 or num > 35:
        ret = False
    return ret

def isValidPosteriorRegionNumber(num : int) -> bool:
    ret = True
    if num < 1 or num > 12:
        ret = False
    return ret

def getWinningLotterLevel(buy_num : str, win_num :str) -> int:
    win_num = win_num.replace('	', ' ')
    if isFirstPrizeNum(buy_num, win_num):
        return 1
    elif isSecondPrizeNum(buy_num, win_num):
        return 2
    elif isThirdPrizeNum(buy_num, win_num):
        return 3
    elif isFourthPrizeNum(buy_num, win_num):
        return 4
    elif isFifthPrizeNum(buy_num, win_num):
        return 5
    elif isSixthPrizeNum(buy_num, win_num):
        return 6
    elif isSeventhPrizeNum(buy_num, win_num):
        return 7 
    elif isEighthPrizeNum(buy_num, win_num):
        return 8  
    elif isNinthPrizeNum(buy_num, win_num):
        return 9  
    else:                                                           
        return 0
def isFirstPrizeNum(buy_num : str, win_num :str) -> bool:
    buy_num_list = str(buy_num).split(' ')
    win_num_list = str(win_num).split(' ')
    pri_cnt = 0
    post_cnt = 0
    for i in range(0, 5):
        num1 = int(buy_num_list[i])
        for j in range(0, 5):
            num2 = int(win_num_list[j])
            if num1 == num2:
                pri_cnt += 1
                break
    for i in range(5, 7):
        num1 = int(buy_num_list[i])
        for j in range(5, 7):
            num2 = int(win_num_list[j])
            if num1 == num2:
                post_cnt += 1
                break    
    return (pri_cnt == 5) & (post_cnt == 2)        

def isSecondPrizeNum(buy_num : str, win_num :str) -> bool:
    buy_num_list = str(buy_num).split(' ')
    win_num_list = str(win_num).split(' ')
    pri_cnt = 0
    post_cnt = 0
    for i in range(0, 5):
        num1 = int(buy_num_list[i])
        for j in range(0, 5):
            num2 = int(win_num_list[j])
            if num1 == num2:
                pri_cnt += 1
                break
    for i in range(5, 7):
        num1 = int(buy_num_list[i])
        for j in range(5, 7):
            num2 = int(win_num_list[j])
            if num1 == num2:
                post_cnt += 1
                break    
    return (pri_cnt == 5) & (post_cnt == 1)     

def isThirdPrizeNum(buy_num : str, win_num :str) -> bool:
    buy_num_list = str(buy_num).split(' ')
    win_num_list = str(win_num).split(' ')
    pri_cnt = 0
    post_cnt = 0
    for i in range(0, 5):
        num1 = int(buy_num_list[i])
        for j in range(0, 5):
            num2 = int(win_num_list[j])
            if num1 == num2:
                pri_cnt += 1
                break
    for i in range(5, 7):
        num1 = int(buy_num_list[i])
        for j in range(5, 7):
            num2 = int(win_num_list[j])
            if num1 == num2:
                post_cnt += 1
                break    
    return (pri_cnt == 5) & (post_cnt == 0)      

def isFourthPrizeNum(buy_num : str, win_num :str) -> bool:
    buy_num_list = str(buy_num).split(' ')
    win_num_list = str(win_num).split(' ')
    pri_cnt = 0
    post_cnt = 0
    for i in range(0, 5):
        num1 = int(buy_num_list[i])
        for j in range(0, 5):
            num2 = int(win_num_list[j])
            if num1 == num2:
                pri_cnt += 1
                break
    for i in range(5, 7):
        num1 = int(buy_num_list[i])
        for j in range(5, 7):
            num2 = int(win_num_list[j])
            if num1 == num2:
                post_cnt += 1
                break    
    return (pri_cnt == 4) & (post_cnt == 2)      

def isFifthPrizeNum(buy_num : str, win_num :str) -> bool:
    buy_num_list = str(buy_num).split(' ')
    win_num_list = str(win_num).split(' ')
    pri_cnt = 0
    post_cnt = 0
    for i in range(0, 5):
        num1 = int(buy_num_list[i])
        for j in range(0, 5):
            num2 = int(win_num_list[j])
            if num1 == num2:
                pri_cnt += 1
                break
    for i in range(5, 7):
        num1 = int(buy_num_list[i])
        for j in range(5, 7):
            num2 = int(win_num_list[j])
            if num1 == num2:
                post_cnt += 1
                break    
    return (pri_cnt == 4) & (post_cnt == 1)      

def isSixthPrizeNum(buy_num : str, win_num :str) -> bool:
    buy_num_list = str(buy_num).split(' ')
    win_num_list = str(win_num).split(' ')
    pri_cnt = 0
    post_cnt = 0
    for i in range(0, 5):
        num1 = int(buy_num_list[i])
        for j in range(0, 5):
            num2 = int(win_num_list[j])
            if num1 == num2:
                pri_cnt += 1
                break
    for i in range(5, 7):
        num1 = int(buy_num_list[i])
        for j in range(5, 7):
            num2 = int(win_num_list[j])
            if num1 == num2:
                post_cnt += 1
                break    
    return (pri_cnt == 3) & (post_cnt == 1)      

def isSeventhPrizeNum(buy_num : str, win_num :str) -> bool:
    buy_num_list = str(buy_num).split(' ')
    win_num_list = str(win_num).split(' ')
    pri_cnt = 0
    post_cnt = 0
    for i in range(0, 5):
        num1 = int(buy_num_list[i])
        for j in range(0, 5):
            num2 = int(win_num_list[j])
            if num1 == num2:
                pri_cnt += 1
                break
    for i in range(5, 7):
        num1 = int(buy_num_list[i])
        for j in range(5, 7):
            num2 = int(win_num_list[j])
            if num1 == num2:
                post_cnt += 1
                break    
    return (pri_cnt == 3) & (post_cnt == 0) 

def isEighthPrizeNum(buy_num : str, win_num :str) -> bool:
    buy_num_list = str(buy_num).split(' ')
    win_num_list = str(win_num).split(' ')
    pri_cnt = 0
    post_cnt = 0
    for i in range(0, 5):
        num1 = int(buy_num_list[i])
        for j in range(0, 5):
            num2 = int(win_num_list[j])
            if num1 == num2:
                pri_cnt += 1
                break
    for i in range(5, 7):
        num1 = int(buy_num_list[i])
        for j in range(5, 7):
            num2 = int(win_num_list[j])
            if num1 == num2:
                post_cnt += 1
                break    
    return ((pri_cnt == 3) & (post_cnt == 1)) | ((pri_cnt == 2) & (post_cnt == 2)) 

def isNinthPrizeNum(buy_num : str, win_num :str) -> bool:
    buy_num_list = str(buy_num).split(' ')
    win_num_list = str(win_num).split(' ')
    pri_cnt = 0
    post_cnt = 0
    for i in range(0, 5):
        num1 = int(buy_num_list[i])
        for j in range(0, 5):
            num2 = int(win_num_list[j])
            if num1 == num2:
                pri_cnt += 1
                break
    for i in range(5, 7):
        num1 = int(buy_num_list[i])
        for j in range(5, 7):
            num2 = int(win_num_list[j])
            if num1 == num2:
                post_cnt += 1
                break    
    return ((pri_cnt == 3) & (post_cnt == 0)) or ((pri_cnt == 2) & (post_cnt == 1)) or ((pri_cnt == 1) & (post_cnt == 2))    

def getPrizeAmount(level, base_found = 1e9) -> int:
    if level == 1:
        return 8*1e7
    elif level == 2:
        return 5*1e7
    elif level == 3:
        return 1*1e4
    elif level == 4:
        return 3*1e3
    elif level == 5:
        return 3*1e2
    elif level == 6:
        return 2*1e2
    elif level == 7:
        return 1*1e2
    elif level == 8:
        return 15
    elif level == 9:
        return 5
    else:
        return 0

import random


def generateLottoNumber() -> str:
    random_num = []    
    for i in range(0,5):
        val = str(random.randint(1, 35)).zfill(2)
        # if val in "07 02 09 16 30":
        #     val = str(random.randint(1, 35)).zfill(2)
        if val in random_num:
            val = str(random.randint(1, 35)).zfill(2)                
        random_num.append(val)
    for i in range(0,2):
        val = str(random.randint(1, 12)).zfill(2)
        # if val in "01 11":
        #     val = str(random.randint(1, 23)).zfill(2)
        if val in random_num:
            val = str(random.randint(1, 12)).zfill(2)      
        random_num.append(val) 
    random_num = ' '.join(random_num)  
    return random_num
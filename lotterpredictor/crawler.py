import requests;
craw_url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=120&isVerify=1&pageNo=1'

def crawData():
    response = requests.get(craw_url)
    result_json = response.json()['value']['list']
    lottery_list = []
    for item in result_json:
        lotter_obj = {}
        lotter_obj['lotteryDrawNum'] = item['lotteryDrawNum']
        lotter_obj['lotteryDrawResult'] = item['lotteryDrawResult']
        lottery_list.append(lotter_obj)
    for item in lottery_list:
        print(item)
    print(len(lottery_list))
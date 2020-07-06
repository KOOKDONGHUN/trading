import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

codeList = instCpCodeMgr.GetStockListByMarket(1) # 1을 넣는 이유 -> 유가증권시장 종목코드를 파이썬의 튜플 형태로 반환받을 수 있다.
print(codeList)

f = open('./data/csv/kospi.csv', 'w')
for key, value in kospi.items():
    f.write(f'{key},{value}\n')
f.close()

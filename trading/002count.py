import win32com.client

instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

# 코드종목의 수 확인하기
print(instCpStockCode.GetCount()) # 3252

# 0 : 종목코드, 1 : 종목명, 2 : FullCode
print(instCpStockCode.GetData(0, 0))
print(instCpStockCode.GetData(1, 0))

stockNum = instCpStockCode.GetCount()

for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == 'NAVER':
        print(instCpStockCode.GetData(0, i))
        print(instCpStockCode.GetData(1, i))

naverCode = instCpStockCode.NameToCode('NAVER')
naverIndex = instCpStockCode.CodeToIndex(naverCode)

print(naverCode)
print(naverIndex)
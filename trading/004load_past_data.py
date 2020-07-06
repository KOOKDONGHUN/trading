import win32com.client

instStockChart = win32com.client.Dispatch('CpSysDib.StockChart')

# ord() ->  문자열을 아스키코드로 변환

instStockChart.SetInputvalue(0, "A003540") # 0 -> 종목코드를 사용하겠다 , A003540 -> 대신증권의 종목코드
instStockChart.SetInputvalue(1, ord('2')) # 조회할 기간 입력 기간으로 입력해서 반환받으려면 1, 개수로 요청할 때는 2를 입력, ord()함수 이용 -> 아스키코드 변환 
instStockChart.SetInputvalue(4, 10) # 데이터 요청개수 입력 // 4 -> 요청개수라는 타입을 의미한다. // 10 -> 실제로 요청할 데이터의 개수를 의미한다. // 10은 최근 거래일로부터 10일치에 해당한다.
instStockChart.SetInputvalue(5, 5) # 요청할 데이터의 종류 // 5 -> 종가 
instStockChart.SetInputvalue(6, ord('D')) # 차트의 종류 일봉 주봉 월봉 이런거 말하는 듯 조금 다른것 같기도 하고 // ord('D') -> 일단위 데이터를 가져오겠다.
instStockChart.SetInputvalue(9, ord('1')) # 수정 주가의 반영 여부에 대한 것 // ord('1') -> 수정주가를 의미한다 // 수정 주가란 유 or 무증상자(?), 액면분할 등에 따른 주식 수 변화를 반영해 비교할 수 있는 주가다. 특히 현금배당을 포함한 수정주가는 주가 움직임 분 아니라 투자자의 실질 수익을 추적할 수 있는 것이 특징이다.

instStockChart.BlockRequest() # 모든 어플을 관리자 권한으로 실행 할것 !!

# numData = instStockChart.GetHeaderValue(0) # 종목코드
# numData = instStockChart.GetHeaderValue(1) # 뭔지모름 1나옴
# numData = instStockChart.GetHeaderValue(2) # '종가' 출력됨
numData = instStockChart.GetHeaderValue(3) # 10일치를 요청했으므로 10이여야한다... (3) -> 이유? 모르겠음 
# print(numData) 

# 대신증권의 최근 10일치의 종가 
for i in range(numData):
    print(instStockChart.GetDataValue(0, i))

'''
타입 // 입력 데이터의 종류   // 값(value)
0    // 종목코드            // 요청할 종목의 종목 코드
1    //
'''
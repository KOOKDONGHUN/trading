import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

codeList = instCpCodeMgr.GetStockListByMarket(1) # 1을 넣는 이유 -> 유가증권시장 종목코드를 파이썬의 튜플 형태로 반환받을 수 있다.
print(codeList)


# 부 구분코드 받아오기
for i, code in enumerate(codeList):
    secondCode = instCpCodeMgr.GetStockSectionKind(code)
    name = instCpCodeMgr.CodeToName(code)
    print(i, code, secondCode, name)

# ETN -> Exchange Traded Note 
# Exchange Traded Note는 보험 회사가 발행 한 선임의 무담보 채무 증권, 만기일이 있음 , 발행자의 신용으로만 뒷받침 된다

# ETF -> Exchange Traded Fund
# Exchange Traded Fund는 상장지수펀드 또는 상장지수투자신탁을 주식시장에서 거래가 가능한 거래 목적의 투자신탁 상품이다.
# 주식, 원자재, 채권등 자산으로 구성되며 거래되면서 순자산으로 수렴(인정?을 말하는 건가?)
import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

codeList = instCpCodeMgr.GetStockListByMarket(1)
print(codeList)
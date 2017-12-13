import requests
from raiMain import *

payload = {'limit': '2000'}
r = requests.get('https://raiblocks.net/page/frontiers.php', payload)
#print(r.text)
text = r.text

stringList = text.split('https://raiblocks.net/account/index.php?acc=')
raiAcc = []
for i in range(1, len(stringList)):
	print(stringList[i][0:64])
	raiAcc.append(stringList[i][0:64])
	
percentSum = 0
totalSupply = 133248290

for i in range(0, len(raiAcc)):
	thisBalance = mrai_account_balance(raiAcc[i], "pending")
	percentSum = percentSum + thisBalance/totalSupply
	print("Richlist number:",i+1, "  MXRB in account:", thisBalance, "  Accumulated percentage:", percentSum)

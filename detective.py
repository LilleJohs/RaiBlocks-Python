import requests
from raiMain import *
from operator import itemgetter

bitgrail1 = "xrb_39ymww61tksoddjh1e43mprw5r8uu1318it9z3agm7e6f96kg4ndqg9tuds4"
bitgrail2 = "xrb_31a51k53fdzam7bhrgi4b67py9o7wp33rec1hi7k6z1wsgh8oagqs7bui9p1"
test = "xrb_31htz7djdd9p7sapfyrjfncjgnw5iz5ys3mqckd3yxkxt61qsajdzyicuy6p"

def totalReceived(account):
	allReceive = account_history(account, type = "receive")
	totalReceive = 0
	for i in range(0, len(allReceive)):
		totalReceive = totalReceive + float(allReceive[i]['amount'])/10**30
	return totalReceive
	
def totalReceivedFromBitgrail(account):
	allReceive = account_history(account, type = "receive")
	totalReceive = 0
	for i in range(0, len(allReceive)):
		if allReceive[i]['account'] == bitgrail1 or allReceive[i]['account'] == bitgrail2:
			totalReceive = totalReceive + float(allReceive[i]['amount'])/10**30
	return totalReceive
	
def getTime(hash):
	r = requests.get('https://raiblocks.net/block/index.php?h=' + hash)
	text = r.text
	stringList = text.split('<strong>Date</strong></th><td class="explorer-right" >')
	return stringList[1][0:26]

allReceive1 = account_history(bitgrail1, type = "send")
allReceive2 = account_history(bitgrail2, type = "send")
allReceive = allReceive1 + allReceive2

print(len(allReceive));
count = 0
accountDictList = list()
print("----------------------------------------------")
print("-----------------New Search-------------------")
#Going through all receive send blocks sent out from bitgrail 1 and 2
for i in range(0, len(allReceive)):
	#If this receive block is over 100 000 Nano
	if float(allReceive[i]['amount'])/10**30 > 100000:
		#If the receive block didn't come from another Bitgrail account
		if allReceive[i]['account'] != bitgrail2 and allReceive[i]['account'] != bitgrail1:
			accountDict = {}
			print("New address!")
			#print(float(allReceive[i]['amount'])/10**30)
			thisAccount = allReceive[i]['account']
			#print(thisAccount)
			#print(allReceive[i]['hash'])
			
			#print(getTime(allReceive[i]['hash']))
			#print("")
			
			count = count + 1
			#Checking if the receiving account is already in the list
			inList = False
			for k in range(0, len(accountDictList)):
				if thisAccount in accountDictList[k]['account']:
					print("Already in list")
					inList = True
					break
			
			if inList == False:
				totalReceive = totalReceived(allReceive[i]['account'])
				#print("Received a total of")
				#print(totalReceive)
				#print("")
				
				#print("Received from Bitgrail Rep 1 or 2 a total of")
				totalReceivedBitgrail = totalReceivedFromBitgrail(allReceive[i]['account'])
				#print(totalReceivedBitgrail)
				#print("")
				accountDict['account'] = allReceive[i]['account']
				accountDict['receivedBitgrail'] = totalReceivedBitgrail
				accountDict['ratio'] = totalReceivedBitgrail/totalReceive
				accountDictList.append(accountDict)

print("")
print("Number transactions over 100,000:" , count)
print("Number of accounts that have received one or more 100 000+ Nano transactions from Bitgrail:",len(accountDictList))

sortedDictList = sorted(accountDictList, key=itemgetter('receivedBitgrail'), reverse = True) 
	
for i in range(0,len(sortedDictList)):
	thisDict = sortedDictList[i]
	print("Account:", thisDict['account'], "| NANO:" , thisDict['receivedBitgrail'], "| Block count:", account_block_count(thisDict['account']), "| Ratio received from Bitgrail:", str(int(thisDict['ratio']*1000)/10) + "%")

import json, requests
from time import sleep

localHost = 'http://localhost:7076'

def rpc(json, key):
	try:
		r = requests.post(localHost, json=json).json()
		if 'error' not in r:
			return(r[key])
		else:
			print(r['error'])
			return(r['error'])
	except requests.exceptions.ConnectionError as e:
		sleep(7.5)
		r = requests.post(localHost, json=json).json()
		if 'error' not in r:
			return(r[key])
		else:
			print(r['error'])
			return(r['error'])
	except Exception as e:
		sleep(0.5)
		r = requests.post(localHost, json=json).json()
		if 'error' not in r:
			return(r[key])
		else:
			print(r['error'])
			return(r['error'])

def raw_account_balance(account, type = "balance"): #Gets the balance of the account in the native unit raw
	#Differs between pending and balance
	assert(type == "balance" or type == "pending")
	r = rpc({"action": "account_balance", "account": account}, 'balance')
	try:
		balance = int(r)
	except ValueError as e:
		balance = 0
	return(balance)
	
def mrai_account_balance(account, type = "balance"): #Gets the balance of the account in Mrai and XRB
	#Differs between pending and balance
	assert(type == "balance" or type == "pending")
	return raw_account_balance(account, type)/10**30
	
def account_block_count(account): #Returns all
	r = rpc({"action": "account_block_count", "account": account}, "block_count")
	try:
		block_count = int(r)
	except ValueError as e:
		block_count = 0
	return (block_count)
	
def account_history(account, type = "all"): #Returns a list of all transactions for an account
	#type tells which kind of transactions you want: send or receive or both(all)
	#Each entry in the array is on the form (hash, type, account, amount)
	assert(type == "all" or type == "send" or type == "receive")
	r = rpc({"action": "account_history", "account": account, "count": 10**10}, "history")
	if type == "all":
		#Return all transactions
		if len(r) == 0:
			return 0
		return r
	else:
		#Return only receive or send transactions
		all_trx = []
		for trx in r:
			if trx['type'] == type:
				all_trx.append(trx)
		if len(all_trx) == 0:
			return 0

		return all_trx
		
	
def account_public_key(account): 
	r = rpc({"action": "account_key", "account": account}, "key")
	return (r)

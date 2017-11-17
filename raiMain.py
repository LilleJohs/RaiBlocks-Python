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

def raw_account_balance(account):
	r = rpc({"action": "account_balance", "account": account}, 'balance')
	try:
		balance = int(r)
	except ValueError as e:
		balance = 0
	return(balance)
	
def mrai_account_balance(account):
	return raw_account_balance(account)/10**24
	

print("Balance:", mrai_account_balance('xrb_3t6k35gi95xu6tergt6p69ck76ogmitsa8mnijtpxm9fkcm736xtoncuohr3'));
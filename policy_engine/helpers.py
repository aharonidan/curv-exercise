import requests

def btc_to_usd(btc_amount):
	ticker = requests.get('https://blockchain.info/ticker')
	usd_rate = ticker.json()['USD']['last']
	return usd_rate * btc_amount

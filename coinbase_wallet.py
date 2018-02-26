


# Author:		Andreas Slovacek
# Created Date:		23 Feb 2018
# Purpose:		
#	1		Connect to the wallet
#	2		Get my balance
#	3		Make a trade		
#############################################################################
# References:
#	(1) Intro: https://developers.coinbase.com/docs/wallet/guides/bitcoin-wallet
#############################################################################

import json
import os
from coinbase.wallet.client import Client



# Class to implement the basic functions listed on (1)
# I:		_getApiCreds_ Load the credentials from a file
# II:		_authenticate_ Authenticate and create a client
# III:		_getAccounts_ Check account details 
class cb:

	# Authenticate according to (1)
	def authenticate(self, key, secret):
		self.client = Client(key,secret)




	# Get accounts associated with the key:secret
	def getAccounts(self):
		self.accounts = self.client.get_accounts()
		for account in self.accounts.data:
		  balance = account.balance
		  print("%s: %s %s" % (account.name, balance.amount, balance.currency))
		  print ( account.get_transactions() )




	# Get auth credits from file
	def getApiCreds(self):
		with open('creds.json', 'r') as f:
			datas = json.loads( f.read() )
		self.api_key=datas['key']
		self.api_secret=datas['secret']




	# Get accounts associated with the key:secret
	def getPrimaryAccounts(self):
		self.primaryAccount = primaryAccount = self.client.get_primary_account() 
		print("%s: %s %s" % ( primaryAccount.name, primaryAccount.balance.amount, primaryAccount.balance.currency ) )




	# Check market mismatch on prices
	def checkMarket(self):
		currency_pair = 'BTC-USD'
		buyP = self.client.get_buy_price(currency_pair = currency_pair ).amount
		sellP = self.client.get_sell_price(currency_pair = currency_pair ).amount
		if buyP > sellP :
			print("BUYERS PAYING %s above asking!\n" % ( str(buyP - sellP)  )
		elif buyP < sellP:
			print("SELLERS ASKING %s above buy!\n" % ( str(sellP - buyP) ) )
		# end else-if
		else:
			print("The market is at parity...: BUY %s == SELL %s"  % (buyP, sellP) )
		# end else




	# Get the real-time price of BTC
	def rt_price(self):
		price = self.client.get_spot_price(currency=self.currency_code)
		return price.amount




	# run a command for a little while
	def run(self):
		count = 10
		while( count != 0 ):
			self.checkMarket()
			count = count - 1
			time.sleep(5)






	# Setup credits and self vars
	def setup(self):
		self.getApiCreds()
		self.authenticate( self.api_key, self.api_secret)
		self.primaryAccount = self.client.get_primary_account()
		self.currency_code = 'USD'




	def __init__(self):
		self.setup()
		print("Current price in %s: %s" % ( self.currency_code, self.rt_price()  ))
		#print("Payment methods: %s" % ( self.client.get_payment_methods() ) )
		self.checkMarket()
		print("End of class")

x = cb()

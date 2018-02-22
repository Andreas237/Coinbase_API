


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
	
 
	

	
	
	
	def __init__(self):
		self.getApiCreds()
		self.authenticate( self.api_key, self.api_secret)
		self.getAccounts()
		print("End of class")

x = cb()
json.dumps("creds.json")

from web3 import Web3
import hidden_details as hidden_details
import contracts.catrinas_contract as catrinas_contract
import requests, json


#############################################################
wallet = hidden_details.user_wallet
#############################################################

w3_poly = Web3(Web3.HTTPProvider(hidden_details.poly_mainnet))
wallet = hidden_details.user_wallet

balance_of = catrinas_contract.balance_of(w3_poly, wallet)

print(f"Balance({wallet}): {balance_of}")

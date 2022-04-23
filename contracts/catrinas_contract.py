from web3 import Web3
import contracts.catrinas_abi as catrinas_abi
import requests, datetime

contract_address = "0xDc87dC7312662AdA8b2996c5258dd8DF1aB5e366"

def balance_of(w3, wallet):
    contract = w3.eth.contract(address=contract_address, abi=catrinas_abi.get_abi())
    balanceOf = contract.functions.balanceOf(wallet).call()
    return balanceOf

def max_supply(w3):
    contract = w3.eth.contract(address=contract_address, abi=catrinas_abi.get_abi())
    maxSupply = contract.functions.maxSupply().call()
    return maxSupply
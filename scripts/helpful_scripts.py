from brownie import MockV3Aggregator, accounts, network, config
from web3 import Web3
import time


FORKER_LOCAL_ENVIROMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS or network.show_active() in FORKER_LOCAL_ENVIROMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        mock = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks Deployed!")

def get_network_address():
    if(network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS):
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
        return price_feed_address
    else:
        deploy_mocks()
        time.sleep(1)
        price_feed_address =  MockV3Aggregator[-1].address
        return price_feed_address





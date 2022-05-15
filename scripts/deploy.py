from brownie import accounts, network, config, FundMe
from web3 import Web3
from scripts.helpful_scripts import get_account, get_network_address
import time


def deploy_fund_me():
    account = get_account()
    fund_me =  FundMe.deploy(
        get_network_address(),
        {"from": account}, 
        publish_source=config["networks"][network.show_active()].get("verify")
    )
    print(f"Contract deployed to {fund_me.address}")
    time.sleep(1)
    return fund_me

def main():
    deploy_fund_me()


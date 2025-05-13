# main.py
from web3 import Web3

INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.isConnected():
    print("Connection failed.")
    exit()

if not w3.ens:
    w3.ens = Web3.ens.ENS.fromWeb3(w3)

name = input("🔍 Enter ENS name (e.g., vitalik.eth): ")

try:
    address = w3.ens.address(name)
    if address:
        print(f"✅ {name} resolves to {address}")
    else:
        print("❌ ENS name not found.")
except Exception as e:
    print("Error:", e)

# Importing Web3 library
from web3 import Web3

# Place your infura API key
Infura_Connection = "https://mainnet.infura.io/v3/INFURA_KEY"

# Producing the connection to the blockchain
web3 = Web3(Web3.HTTPProvider(Infura_Connection))

# Checking connection status
print(web3.isConnected())

# Displaying block number
print(web3.eth.blockNumber)

# Input account key here
myBalance = web3.eth.getBalance("YOUR_ACCOUNT")

# Converting Wei to Ether cryptocurrency
print(web3.fromWei(myBalance, "ether"))


#The sha256 function will give us the ability to compute hashes 
from hashlib import sha256
import json
import time

class Chain:
    '''#A blockchain is a ledger of “blocks” and blocks are a collection of transactions. Each block in the blockchain is linked to its predecessor'''
    def __init__(self):
        #blockchain is the actual list of our blocks and pending is the list of transactions that are yet to be added
        self.blockchain = []
        self.pending = []
        self.add_block(prevhash="Genesis", proof=123)

    # define a function
    def add_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount}
        self.pending.append(transaction)    
    
    def compute_hash(self, block):
        json_block = json.dumps(block, sort_keys=True).encode()
        curhash = sha256(json_block).hexdigest()
        return curhash

    def add_block(self, proof, prevhash=None):
        block = {
            "index": len(self.blockchain),
            "timestamp": time.time(),
            "transactions": self.pending,
            "proof": proof,
            "prevhash": prevhash or self.compute_hash(self.blockchain[-1])}
        self.pending = []
        self.blockchain.append(block)

chain = Chain()

t1 = chain.add_transaction("Vitalik", "Satoshi", 100)
t2 = chain.add_transaction("Satoshi", "Alice", 10)
t3 = chain.add_transaction("Alice", "Charlie", 34)
                           
chain.add_block(12345)
t4 = chain.add_transaction("Bob", "Eve", 500)
t4 = chain.add_transaction("Dennis", "Brian", 300)
t6 = chain.add_transaction("Ken", "Doug", 88000)

chain.add_block(6789)
print(chain.blockchain)
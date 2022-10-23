import sgx
import sys
import time
import user
import merkle
import random
import pickle
import hashlib
import datetime
import transaction


class Blockchain:
    # this is my blockchain
    def __init__(self):
        # define chain as a list essentially it's a list of blocks, in form of json objects, initialize with empty list
        # later I'll write a create block function to create a block and add it to this chain appropriately
        # I'll also have seperate functionality to create a genisis block
        self.chain = []
        # create_block has two parameters, hsh ie: hash of current block, prev_hsh ie: hash of previous block
        # call it once when you create the blockchain, while creating the blockchain, the 1st block is genesis block
        # hash of 1st block in not starting with 4 zeros
        # after you mine a block you'll get a nonce, you call create_block fucntion after you mine
        self.add_block(self.create_block(prev_hsh='0'))
        self._timedict = {}

    def create_block(self, prev_hsh, transactions=None):
        # what this function does is:
        # it structures a block, basically take block number ie: index and prev_hsh, and nonce and timestamp and data
        # then add this block to the chain, append.
        m = merkle.MerkleTree(transactions)
        block = {
            'block_number': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'prev_hsh': prev_hsh,  # add data to this block
            'transactions': transactions,
            'merkleroot': m.get_tree()[0],
            'merkletree': m.get_tree()[1]
        }
        return block

    def add_block(self, block):
        self.chain.append(block)

    def get_prev_block(self):
        # [-1] returns last iten of the list
        return self.chain[-1]

    # This function implements the proof of elapsed time consensus mechanism. It assigns a random timer to each user
    # node in the network and every node becomes inactive till the timer of some node expires. The moment a timer of
    # any node is elapsed, that node becomes the next miner.
    def poet(self, transactions=None):
        miners = [x[0] for x in user.get_all_userids()]
        miner = ""
        minimum = sys.maxsize
        for i in range(0, len(miners)):
            k = random.randint(500, 20000)
            if minimum > k:
                minimum = k
                miner = miners[i]
            self._timedict[miners[i]] = k
        secs = minimum // 100
        print('SLEEP : ', secs)
        print()
        time.sleep(secs)
        for i in range(0, len(miners)):
            self._timedict[i] = 0
        certificate = sgx.get_certificate(minimum, miner)
        new_block = self.create_block(self.hashblock(self.get_prev_block()), transactions)
        return (new_block, certificate)

    # seperate hash function takes a block and returns hash of it
    def hashblock(self, block):
        # make dict object into string in order to input it to the sha256
        # Jason.dumps() : converts a python object Into Json string. because I'm storing all blocks (entire blockchain) as a jason file
        encoded_block = pickle.dumps(block)
        return hashlib.sha256(encoded_block).hexdigest()

    # check whether each block is valid by taking nonce of previous block and nonce of current block
    # and the prev_hsh feild in each block is actually equal to the hash of previous block
    def validity_of_chain(self, chain):
        prev_block = chain[0]
        block_number = 1
        n = len(chain)
        while block_number < n:
            curr_block = chain[block_number]
            if curr_block['prev_hash'] != self.hashblock(prev_block):
                return False
            prev_block = curr_block
            block_number = block_number + 1
        return True

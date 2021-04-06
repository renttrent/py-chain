from datetime import datetime
import json
from block import Block
from tx import Tx


class Chain:
    def __init__(self, blocks=[]):
        self.chain = blocks
        self.lastindex = - 1
        self.difficulty = 4

        if self.chain == []:
            self.createGenesis()
        self.lastindex = self.chain[-1].index

    def createGenesis(self):
        genesis = Block(str(datetime.now()), Tx('', '', 1.0, 'Genesis'), '')
        self.addBlock(genesis)
        self.lastindex = genesis.index

    def addBlock(self, block):
        block.index = self.lastindex = self.lastindex + 1

        if self.verifyBlock(block):
            self.chain.append(block)

    def verifyBlock(self, block):
        newhash = block.hashfunc
        while block.hash[:self.difficulty] != '0' * self.difficulty:
            block.nonce += 1
            newhash.update(str(block.nonce).encode())
            block.hash = newhash.hexdigest()
        block.hash = newhash.hexdigest()
        return True

    def print(self):
        for block in self.chain:
            print(block)

    def getJSON(self):
        rv = {}
        i = 0
        for block in self.chain:
            rv[f'Block {i}'] = json.loads(block.getJSON())
            i += 1

        return rv

    def writeJSON(self):
        with open('file.json', 'w') as file:
            json.dump(self.getJSON(), file, indent=4)

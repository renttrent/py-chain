from hashlib import sha256
from datetime import datetime
import json


class Tx:
    def __init__(self, fromAddr, toAddr, amount, data):
        self.fromAddr = fromAddr
        self.toAddr = toAddr
        self.amount = amount
        self.data = data

    def __str__(self):
        pass


class Block:
    def __init__(self, timestamp, txs, prevHash):
        self.index = -1
        self.timestamp = timestamp
        self.txs = txs
        self.merkleroot = self.calcMerkle()
        self.prevHash = prevHash
        self.hashfunc = self.getHashFunc()
        self.hash = ''
        self.nonce = 0

        self.map = {
            'timestamp': self.timestamp,
            'txs': self.txs,
            'merkleroot': self.merkleroot,
            'prevHash': self.prevHash,
            'hash': self.hash,
            'nonce': self.nonce
        }

    def getHashFunc(self):
        hash = sha256()
        hash.update(self.timestamp.encode())
        hash.update(self.merkleroot.encode())
        hash.update(self.prevHash.encode())
        return hash

    def calcMerkle(self):
        root = sha256()
        for tx in self.txs:
            root.update(tx.encode())
        return root.hexdigest()

    def updateMap(self):
        self.map = {
            'timestamp': self.timestamp,
            'txs': self.txs,
            'merkleroot': self.merkleroot,
            'prevHash': self.prevHash,
            'hash': self.hash,
            'nonce': self.nonce
        }

    def getJSON(self):
        return json.dumps(self.map)

    def __str__(self):
        rv = ''
        rv += f'Block {self.index} -----------------------------------------------------------------------\n'
        for key in self.map:
            rv += f'\t{key} : {self.map[key]}\n'
        return rv


class Chain:
    def __init__(self, blocks=[]):
        self.chain = blocks
        self.lastindex = - 1
        self.difficulty = 4

        if self.chain == []:
            self.createGenesis()
        self.lastindex = self.chain[-1].index

    def createGenesis(self):
        genesis = Block(str(datetime.now()), ['Genesis'], '')
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
        block.updateMap()
        return True

    def print(self):
        for block in self.chain:
            print(block)


chain = Chain()
chain.addBlock(
    Block(str(datetime.now()), ['tx1', 'tx2', 'tx3'], chain.chain[-1].hash))
chain.addBlock(
    Block(str(datetime.now()), ['tx4', 'tx5', 'tx6'], chain.chain[-1].hash))
chain.print()

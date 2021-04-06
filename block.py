from hashlib import sha256
import json


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

    def getHashFunc(self):
        hash = sha256()
        hash.update(self.timestamp.encode())
        hash.update(self.merkleroot.encode())
        hash.update(self.prevHash.encode())
        return hash

    def calcMerkle(self):
        root = sha256()
        if isinstance(self.txs, list):
            for tx in self.txs:
                root.update(tx.txHash.encode())
        else:
            root.update(self.txs.txHash.encode())
        return root.hexdigest()

    def getJSON(self):
        temp = {
            'timestamp': self.timestamp,
            'txs': json.loads(self.txs.getJSON()),
            'merkleroot': self.merkleroot,
            'prevHash': self.prevHash,
            'hash': self.hash,
            'nonce': self.nonce
        }
        return json.dumps(temp, indent=4)

    def __str__(self):
        temp = json.loads(self.getJSON())
        rv = ''
        rv += f'Block {self.index} -----------------------------------------------------------------------\n'
        for key in temp:
            rv += f'\t{key} : {temp[key]}\n'
        return rv

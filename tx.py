from hashlib import sha256
import json


class Tx:
    def __init__(self, fromAddr, toAddr, amount, data):
        self.fromAddr = fromAddr
        self.toAddr = toAddr
        self.amount = amount
        self.data = data
        self.txHash = self.calcHash()

    def calcHash(self):
        hash = sha256()
        hash.update(self.fromAddr.encode())
        hash.update(self.toAddr.encode())
        hash.update(str(self.amount).encode())
        hash.update(self.data.encode())
        return hash.hexdigest()

    def getJSON(self):
        temp = {
            'fromAddr': self.fromAddr,
            'toAddr': self.toAddr,
            'amount': self.amount,
            'data': self.data,
            'hash': self.txHash
        }

        return json.dumps(temp, indent=4)

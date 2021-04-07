from hashlib import sha256


class MerkleTree:
    def __init__(self, data=['1', '2', '3', '4', '5', '6']):
        self.data = data
        self.length = len(self.data)
        self.right = sha256()
        self.left = sha256()

    def getMerkleRoot(self, index, hashFunc=sha256(), stack=[]):
        if index >= self.length:
            return hashFunc.hexdigest()
        else:
            temp = sha256()
            temp.update(self.data[index].encode())
            temp.update(self.data[index+1].encode())
            hashFunc.update(temp.hexdigest().encode())
            return self.getMerkleRoot(index + 2, hashFunc)


m = MerkleTree()
print(m.getMerkleRoot(index=0))

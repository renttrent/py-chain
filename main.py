from time import time
from block import Block
from chain import Chain
from tx import Tx

import argparse


parser = argparse.ArgumentParser(description='Add some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='interger list')
parser.add_argument('--sum', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.sum(args.integers))


if __name__ == '__main__':
    chain = Chain()
    chain.addBlock(
        Block(str(time()), Tx('addr1', 'addr2', 14.2245, 'Hello there'), chain.chain[-1].hash))
    chain.addBlock(
        Block(str(time()), Tx('addr1', 'addr2', 42.22, 'Hey there you'), chain.chain[-1].hash))
    chain.print()
    chain.writeJSON()

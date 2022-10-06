#python module to implement a common interface to many different secure hash and message digest algorithms
import hashlib

# function to generate hash
def hashGenerator(data):
    # data.encode() - converts the string into bytes
    result = hashlib.sha256(data.encode())
    # hexdigest() - converts the encoded data in hexadecimal
    return result.hexdigest()

#to create a block in the blockchain
class Block:
    #parametrised constructor
    #passing the value data the block will contain, hash of the block, and hash of the previous block
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash

#to create the blockchain
class Blockchain:
    #to create the genesis block(first block of the blockchain)
    def __init__(self):
        hashLast=hashGenerator('Dogra')
        hashStart=hashGenerator('Kanika')

        genesis=Block('some_data',hashStart,hashLast)
        self.chain = [genesis]

    def add_block(self,data):
        #prev_hash will contain the hash of last block that is currently present in the chain
        prev_hash=self.chain[-1].hash
        #the current block hash will be the concatenation of data and the previous hash to make it unique
        hash=hashGenerator(data+prev_hash)
        block = Block(data,hash,prev_hash)
        self.chain.append(block)


#bc is a Blockchain object
bc = Blockchain()
bc.add_block('1')
bc.add_block('2')
bc.add_block('3')


#printing the blockchain in a dictonary form
for block in bc.chain:
    print(block.__dict__)


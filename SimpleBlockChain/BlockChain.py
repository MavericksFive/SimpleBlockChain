from MiningScript import mine
from Block import Block
import datetime

#Test 

if __name__ == '__main__':

	block_chain = [Block.create_genesis_block()]
	print("Block #%a has been created." %(0))
	print("Block #%a hash : %s" %(0,mine(block_chain[0],3)))

	num_blocks_to_add = 10

	for i in range(1, num_blocks_to_add + 1):
		block_chain.append(Block(i,"DATA !",block_chain[-1].hash, datetime.datetime.now()))
		block_chain[i].set_hash(mine(block_chain[i],3))
		print("Block #%a has been created." %i)
		print("Block #%a hash : %s" %(i,block_chain[i].hash))


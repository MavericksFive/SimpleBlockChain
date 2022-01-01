from hashlib import sha256
from Block import Block
import datetime

#Random MAX_Nonce

MAX_Nonce = 1000000000

#Cryptography Method 

def SHA256(text) : 
	return sha256(text.encode("ascii")).hexdigest()


#Function for Mining (Having an access to validate the current Block and being reward)
#prefix_zeros variable is the number of zero required in the new hash function of the current Block mined

def mine(Block, prefix_zeros):

	prefix_str = '0'*prefix_zeros

	#Try different nonce until the hash function has the prefix_str

	for nonce in range(MAX_Nonce):
		
		Block.add_Nonce(nonce)
		new_hash = Block.get_hash()
		if new_hash.startswith(prefix_str):
			print('Successfully mined Block with nonce value : ' + str(nonce))
			return(new_hash)
	raise BaseExecption("Couldn't find correct solution after trying" + str(MAX_Nonce) + "times")
		


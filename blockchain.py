import time
import hashlib
# from api.schema.block import BlockSchema
from time import time


class Transaction:
    def __init__(self, sender, recipient, amount):
        """
        Creates a new transaction

        :param sender: <str> sender account
        :param recipient: <str> recipient account
        :param amount: <float> amount to be transferred
        """
        self.sender = sender
        self.recipient = recipient
        self.timestamp = time.time()
        self.amount = amount

    def validate(self):
        """
        Checks if a transaction is valid

        :return: <bool> True if it is valid, False if not.
        """

        # Prevent stealing by creating negative transactions
        if self.amount < 0:
            return False

        return True


class Block:
    def __init__(self, index, transactions, nonce, previous_hash):
        """
        Constructs a new block

        :param index:
        :param transactions:
        :param previous_hash:
        """
        self.index = index
        self.timestamp = time()
        self.transactions = transactions
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def serialize(self, ignore=None):
        """
        Serializes a block into a string

        :return:
        """
        if ignore is None:
            ignore = []
        block_params = {x: self.__dict__[x] for x in self.__dict__ if x not in ignore}

        return BlockSchema().dumps(block_params)

    def hash_block(self):
        """
        Calculates the hash of the block

        :return:
        """
        sha = hashlib.sha256()
        sha.update(self.serialize(['hash']).encode('utf-8'))
        return sha.hexdigest()


# https://livecodestream.dev/post/from-zero-to-blockchain-in-python-part-1/
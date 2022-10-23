import pickle
import hashlib
from collections import OrderedDict

# Assign values to LEFT, RIGHT, UNDEFINED from a tuple
LEFT, RIGHT, UNDEFINED = (0, 1, 2)
# Create empty object
_empty = object()

# Code for concatenating left and right hashes
def _concatenate(left, right):
    if (left is _empty) or (right is _empty):
        if (right is _empty):
            return left.hash 
        else:
            return right.hash
    # x + y or y + x
    if left.child_type == RIGHT:
        return hashlib.sha256(pickle.dumps(right.hash + left.hash)).hexdigest()
    elif right.child_type == LEFT:
        return hashlib.sha256(pickle.dumps(right.hash + left.hash)).hexdigest()
    return hashlib.sha256(pickle.dumps(left.hash + right.hash)).hexdigest()    

class MerkleNode():
    __slots__ = ('hash', 'type', 'left', 'right', 'parent')

    def __init__(self, hash, left = None, right = None, parent = None):
        self.hash = hash
        self.left = left
        self.right = right 
        if left and (left is not _empty):
            left.parent = self
        if right and (right is not _empty):
            right.parent = self
        self.parent = parent

    # Function to return the sibling as property object
    @property
    def sibling(self):
        parent = self.parent
        if parent is None:
            return None
        if parent.left is self:
            return parent.right
        elif parent.right is self:
            return parent.left
        return None

    # Function to determine the child type; 0 for LEFT, 1 for RIGHT, 2 for UNDEFINED as property object
    @property
    def child_type(self):
        parent = self.parent
        if parent is None:
            return UNDEFINED
        return LEFT if (parent.left is self) else RIGHT

    # Function to combine left and right nodes and return as class method
    @classmethod
    def combine_node(cls, left, right):
        return cls(_concatenate(left, right), left, right)

# Code to check the verification if the hash of transactions and merkle root are the same or not
def verify_proof(MerkleRoot, transaction, proof):
    transaction = hashlib.sha256(pickle.dumps(transaction)).hexdigest()
    for i in range(len(proof)):
        node = proof[i][0]
        child_type = proof[i][1]
        if child_type == 0:
            transaction = hashlib.sha256(pickle.dumps(node + transaction)).hexdigest()
        elif child_type == 1:
            transaction = hashlib.sha256(pickle.dumps(transaction + node)).hexdigest()
    return (transaction == MerkleRoot)

class MerkleTree():
    def __init__(self, transactions = None):
        #Convert NoneType to empty list and build tree
        transactions = transactions or []
        self._tree(transactions)

    def get_tree(self):
        if self._MerkleRoot is None:
            return (None, self._treeobj)
        else:
            return (self._MerkleRoot.hash, self._treeobj)
    
    def _tree(self, transactions):
        self._MerkleRoot = None
        leaf_nodes = [MerkleNode(hashlib.sha256(pickle.dumps(x)).hexdigest()) for x in transactions]
        nodes = list(leaf_nodes)
        while len(leaf_nodes) > 1:
            if len(leaf_nodes) % 2 != 0:
                leaf_nodes.append(_empty)
            i = iter(leaf_nodes)
            l = list(zip(i, i))
            leaf_nodes = [MerkleNode.combine_node(left, right) for left, right in l]
        treeobj = OrderedDict()
        if len(nodes) > 0:
            for node in nodes:
                treeobj[node.hash] = node
        if len(leaf_nodes) == 0:
            self._MerkleRoot = None
        else:
            self._MerkleRoot = leaf_nodes[0]
        self._treeobj = treeobj

    # Code to check the proof of membership of a node
    def proof_of_membership(self, transaction):
        treeobj = self._treeobj
        t = treeobj.get(hashlib.sha256(pickle.dumps(transaction)).hexdigest())
        if t is None:
            return []
        MerkleRoot = self._MerkleRoot
        proof = []
        while t is not MerkleRoot:
            sibling = t.sibling
            if sibling is not _empty:
                proof.append((sibling.hash, sibling.child_type))
            t = t.parent
        return proof

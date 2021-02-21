#!/usr/bin/python3

import hashlib

class HashUtil:
    def __init__(self):
        self.m = hashlib.md5()

    def add_int(self,val):
        self.m.update(str(val).encode('ASCII'))

    def add_str(self,val):
        self.m.update(val.encode('ASCII'))

    def get_hash(self):
        return self.m.hexdigest()

class MerkleTree:
    def __init__(self, x):
        self.hashes = {}
        self.build(x)

    def contains(self, H):
        return H in self.hashes

    def build(self, x):
        h = HashUtil()

        if not x.left and not x.right:
            h.add_int(x.val)
            x.hash = h.get_hash()
            self.hashes[x.hash]=1
            return x.hash

        h.add_int(x.val)

        if x.left:
            h.add_str("L"+self.build(x.left))

        if x.right:
            h.add_str("R"+self.build(x.right))

        x.hash = h.get_hash()
        self.hashes[x.hash]=1
        return x.hash

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        M_s = MerkleTree(s)
        M_t = MerkleTree(t)

        return M_s.contains(t.hash)

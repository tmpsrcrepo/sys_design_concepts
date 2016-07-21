"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""
from collections import OrderedDict
class MiniCassandra:
    def __init__(self):
        # initialize your data structure here.
        #each shard = {column_key:column_value} (sorted)
        self.shards = {}

    # @param {string} raw_key a string
    # @param {int} column_key an integer
    # @param {string} column_value a string
    # @return nothing
        
    def insert(self, raw_key, column_key, column_value):
        # Write your code here
        #hash_key = hash(raw_key)
        
        if raw_key not in self.shards:
            self.shards[raw_key] = {}#OrderedDict()
            #self.shards
        self.shards[raw_key][column_key] = column_value
        

    # @param {string} raw_key a string
    # @param {int} column_start an integer
    # @param {int} column_end an integer
    # @return {Column[]} a list of Columns
    def query(self, raw_key, column_start, column_end):
        # Write your code here
        res = []
        if raw_key not in self.shards:
            return res
        else:
            #sort the dictionary -> the values in the column
            #self.shards[raw_key] = OrderedDict(sorted(self.shards[raw_key].items(), key=lambda t: t[0]))
            for k,v in sorted(self.shards[raw_key].items(), key=lambda t: t[0]):
                if k>=column_start and k<=column_end:
                    res.append(Column(k,v))
            return res

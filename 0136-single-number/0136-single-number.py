class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # STEP ONE: define a hashtable
        
        hash_table = {}
        
        
        # STEP TWO: loop through the elements
        for i in nums:
            try:
                # STEP THREE: try to pop out the element in the Hash-table
                hash_table.pop(i)
                # print(hash_table)
                
            except:
                # if there is no value in the Hash-table to create a key, value pair.
                hash_table[i] =1 
                # print(hash_table)
                
          # STEP FOUR:  Pop  the item off the hash-table but specify position zero so as it removes the first item inside the 
          # the hash-table.
        print(hash_table)
        return hash_table.popitem()[0]
                
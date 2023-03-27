# STEP ONE: create a Union class
class UnionFind:
    # Create the tree
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1] *n   # size of the trees/ data sets
    
    # create method to find the root within the data structure/ tree
    def find(self,x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    # Method to perform the union itself on the two trees
    
    def union(self,x1,x2):
        # finding the two pairs within the tree
        p1,p2 = self.find(x1),self.find(x2)
        # if the pairs are the same
        if p1 == p2:
            return False
        # if the pairs are NOT the same.
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # STEP TWO: create UnionFind with the length of the account
        uf = UnionFind(len(accounts))
        
        # STEP THREE: Map each email to the index of each account
        emailToAcc = {}
        
        # Iterate through each account: i is for index, a is for Account
        for i,a in enumerate(accounts):
            for e in a[1:]:
                # check if the email exists in emailToAcc
                if e in emailToAcc:
                    # merge the two accounts together
                    uf.union(i, emailToAcc[e])
                    
                    
                else:
                    emailToAcc[e] = i
                    
        # grouping the emails together            
        emailGroup = defaultdict(list)  # take each index of the account and map to list of emails
        for e,i in emailToAcc.items():
            # find the leader of the account 
            leader  = uf.find(i)
            emailGroup[leader].append(e)
            
        res = []
        for i, emails in emailGroup.items():
            name =  accounts[i][0]
            res.append([name] + sorted( emailGroup[i])) # array concantenation
            
        return res
           
                    
            
        
       
        
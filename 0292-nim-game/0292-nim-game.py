class Solution(object):
    def canWinNim(self, n):
        # If Player one goes first AND the n is a multiple of four.
        if(n % 4 == 0):
            return False
        # if the stones are NOT multiples of four and player one goes first. 
        return True 
        
        """
        Plan of Attack
        1) Understand the problem and the constraints(DONE)
        2) If n is a multiple of four, the first player WILL loose.
        2A) For example, four stones, and player one takes three, player two takes one and looses. 
        The same holds true for six and eight: P1 takes three stones, P2 takes three for six and P1 takes four and P2 takes four.
        
        3A) CONTRAST, if the stones aren't multiples of four, 1, 3, 5 and 9 this isn't the case. 
        3B) If say five stones and Player one takes three, then player two will take two and they win.
        3C) BUT if Player one takes one stone and Player two takes one stone there's three stones left which means Player one can win.
        
        NOTE this works because we are assuming both you and your friend are playing OPTIMALLY which means you're playing optimally. 
        
        
        """
        
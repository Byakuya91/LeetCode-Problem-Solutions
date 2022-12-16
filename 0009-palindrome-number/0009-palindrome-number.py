class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
      #While loop potentially needs to be utilized 
       # Base conditions to used if the number is negative 
        if x<0:
            return False
        # store the number inside of a variable to be able to modify it.
        number = x
        # store the reverse of the number
        reverse_num = 0
        
        # While loop to check the number
        while number:
            # Reverseing the number by dividing by 10 until it hits zero
            # After the loop check if the output is greater than the range (−231, 231 − 1).
            # At last, return the output with the correct sign (positive or negative).
            reverse_num = reverse_num * 10 + number % 10
            number //=10
         # checking to see if reverse_num equals the original x value   
        return x == reverse_num
class Solution(object):
    def characterReplacement(self, s, k):
        
        # PLAN OF ATTACK(POA)
        # 1)CONCEPTUAL EXPLANATION: 
        # Go through the string and replace the characters that are less frequent.
        # This can be accomplished through a hashmap/ dictionary where we get a total count of each character
        #  This leads to taking the window length of the substring and subtracting it from the most frequent char in
        # the HashMap.  
        # That result equals how many possible replacements can be made. if it is less than or equal to K: the number of
        #  POSSIBLE replacements then it works.
        # The problem is only concerned with returning the total number of replacements for each char,
        # EX: "ABAB" equals 4. That means you can replace two "As" with two "Bs" and vice versa
        
        # 2) BRUTE FORCE METHOD
        # update the hashmap with each of the counts for each char w
        # This can be done with a sliding window technique through a left and right pointer. 
        # the pointers will allow the hashmap to be incremented with the respect characters
        # The edge case will happen if the number of replacements(through a bigger window size) exceeds that of the 
        # number of POSSIBLE replacements. 
        # Thus one needs to reduce the window size in order to meet the critera.
        # That can be accomplished by popping the values off the substring which will affect the count of the Hashmap
        
        # 3) A MORE OPTIMIZED SOLUTION
        # There is a way to do this much more easily
        # declare a variable that contains the max frequency of each char and update that when the max freq
        # inside the hashMap changes. 
        # This creates another problem. When the window shifts the count map is updated.
        # You need to rescan the entire Hashmap to find the new most frequent char
        #  But you don't need to do this because this won't change the number of Possible replacemnets.
        #  Remember, K is constant and it needs to be less than OR equal to.  
        # We know at one point that the max frequency was at a specific point so it doesn't need to change 
        # WHEN decirmented. This is NOT the case when frequencies of chars is INCREMENTED.
        
        
        
        # STEP ONE: Create a dictionary/ Hashmap and substring result
        char_count = {}
        
        sub_Str_result = 0
        
        # STEP TWO: Create a left  pointer. The right pointer will traverse the string at each position
        l = 0
        
        # BONUS STEP: create a max_freq 
        max_freq = 0
        
        # STEP THREE: For loop
        
        for r in range(len(s)):
            # increment the count for the right pointer
            char_count[s[r]] = 1 + char_count.get(s[r],0)
            # update the max_freq count 
            max_freq = max( max_freq, char_count[s[r]])
            
            # check ig the current window is valid. note (r - l + 1) shifts the window with the right and left pointers.
            while (r - l + 1 ) - max_freq > k:
                # decrement the count at the left position
                char_count[s[l]]-= 1
                # increment the left pointer
                l+=1
            
            # update the sub_Str_result
            sub_Str_result = max(sub_Str_result, r - l + 1)
        # return sub_Str_result
        return sub_Str_result
        
        
        
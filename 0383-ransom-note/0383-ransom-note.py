class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # OPTIMIZED SOLUTION
        
        # STEP ONE: create a dictionary for the magazine
        m_dic = {}
        
        # STEP TWO: loop through the magazine
        for char in magazine:
            # add char to the m_dic
            if char not in m_dic:
                m_dic[char] =1
             # existing char 
            else:
                m_dic[char]+=1
        # print(m_dic)
        
        # STEP THREE: loop through ransomNote
        for  char in ransomNote:
            # checking if the char in m_dic is 0 OR the char is NOT in m_dic
            if char not in m_dic or m_dic[char] == 0:
                return False
            else:
                m_dic[char]-=1
        return True 
            
                
        
        
        # OLD SOLUTION 
#        #STEP ONE create two dictionaries for ransomNote and Magazine
#         note_dic = {}
#         mg_dic =  {}
        
#        # STEP TWO: add chars from ransomNote and magazine into dictionaries
        
#         for r_char in ransomNote:
#             # new char to the dictionary
#             if r_char not in note_dic:
#                 note_dic[r_char] = 1
#             else:
#                 note_dic[r_char]+=1
                
#         for m_char in magazine:
#             # new char to the dic
#             if m_char not in mg_dic:
#                 mg_dic[m_char] =1 
#             else:
#                 mg_dic[m_char]+=1
                
#        # STEP THREE: iterate through the ransomNote
    
#         for char in ransomNote:
            
#             # STEP FOUR: check for the char in mg_dic or mg_dic is less than note_dic. Ret
#             if char not in mg_dic or mg_dic[char] < note_dic[char]:
#                 return False
#             # if the values exist. 
#             return True 
        
        
        
        
        

        